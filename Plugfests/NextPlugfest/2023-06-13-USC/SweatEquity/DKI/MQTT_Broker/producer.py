import fire
import json
import os
import paho.mqtt.client as mqtt
import time
from base64 import b16encode

"""
Publish an OpenC2 command to MQTT Broker using consumer's TOPIC_C01

Broker address: environment variable CAVBROKER - url:port
Authentication: environment variable CAVUSER - username,password
Command is a JSON string passed via CLI, or defaults to COMMAND_01
"""

BROKER, BROKER_PORT = os.getenv('CAVBROKER').rsplit(':')
USERNAME, PASSWORD = os.getenv('CAVUSER').split(',')
TOPIC_P = 'oc2/rsp/p01'                 # This producer's topic
TOPIC_C01 = 'oc2/cmd/device/c01'        # OpenC2 consumer's topic

COMMAND_01 = json.dumps({
    "headers": {
        "request_id": b16encode(int(time.time()*1000).to_bytes(8, byteorder='big')[4:8]).decode(),
        "from": TOPIC_P,
        "to": [TOPIC_C01]
    },
    'body': {
        'openc2': {
            'request': {
                'action': 'query',
                'target': {'enc': ['flux']}
            }
        }
    }
})


def on_connect(client, userdata, flags, rc):
    print(f'Connected with result code {rc}')
    client.subscribe(TOPIC_P, 0)
    client.publish(TOPIC_C01, userdata, qos=0, retain=False)
    print(f'Command to {TOPIC_C01}: {userdata}')


# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    resp = json.loads(msg.payload.decode())
    print(f'Response to {msg.topic}: {resp}')


def main(cmd: str = COMMAND_01, broker: str = BROKER, port: int = int(BROKER_PORT)):
    client = mqtt.Client(userdata=cmd)
    client.on_connect = on_connect
    client.on_message = on_message

    client.tls_set()
    client.username_pw_set(USERNAME.strip(), PASSWORD.strip())
    client.connect(broker, port, 60)
    print(f'Connected to {broker}:{port}')
    client.loop_start()
    time.sleep(1)


if __name__ == '__main__':
    fire.Fire(main)
