import fire
import json
import os
import paho.mqtt.client as mqtt

"""
Receive an OpenC2 command and return a response via MQTT Broker

Command received on topic TOPIC_ME
Response returned to producer on topic TOPIC_P
Broker address: environment variable CAVBROKER - url:port
Authentication: environment variable CAVUSER - username,password
"""
BROKER, BROKER_PORT = os.getenv('CAVBROKER').rsplit(':')
USERNAME, PASSWORD = os.getenv('CAVUSER').split(',')
TOPIC_ME = 'oc2/cmd/device/c01'         # This consumer device's individual topic
TOPIC_P = 'oc2/rsp/p01'                 # Producer's topic (not included in received data, need Message struct 'from')
RESP = json.dumps({
    'status': 200,
    'status_text': "Got it, boss",
    'results': {
        'ap': {
            'encabulator_flux': 395
        }
    }
})


def on_connect(client, userdata, flags, rc):
    print(f'Connected with result code {rc}')
    client.subscribe(TOPIC_ME)


# Receive a command, process it, and return response to the producer
def on_message(client, userdata, msg):
    cmd = msg.payload.decode()
    client.publish(TOPIC_P, RESP, qos=0, retain=False)
    print(f'Received {msg.topic}: {cmd}\nSent {RESP} to {TOPIC_P}')


def main(broker: str = BROKER, port: int = int(BROKER_PORT)):
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message

    client.tls_set()
    client.username_pw_set(USERNAME, PASSWORD)
    client.connect(broker, port, 60)
    print(f'Connected to {broker}:{port}')
    client.loop_forever()


if __name__ == '__main__':
    fire.Fire(main)
