import fire
import json
import os
import paho.mqtt.client as mqtt

"""
Receive an OpenC2 command and return a response to producer via MQTT Broker

Broker address: environment variable CAVBROKER - url:port
Authentication: environment variable CAVUSER - username,password
Command received on topic TOPIC_ME
"""
BROKER, BROKER_PORT = os.getenv('CAVBROKER').rsplit(':')
USERNAME, PASSWORD = os.getenv('CAVUSER').split(',')
TOPIC_ME = 'oc2/cmd/device/c01'         # This consumer device's individual topic


def make_oc2_response(cmd: dict) -> dict:
    return {
        'headers': {
            'request_id': cmd['headers']['request_id'],
            'from': TOPIC_ME,
            'to': [cmd['headers']['from']]
        },
        'body': {
            'openc2': {
                'response': {
                    'status': 200,
                    'status_text': "Got it, boss",
                    'results': {
                        'enc': {
                            'encabulator_flux': 395
                        }
                    }
                }
            }
        }
    }


def on_connect(client, userdata, flags, rc):
    print(f'Connected with result code {rc}, Subscribing to {TOPIC_ME}')
    client.subscribe(TOPIC_ME)


# Receive a command, process it, and return response to the producer
def on_message(client, userdata, msg):
    cmd = json.loads(msg.payload)
    if TOPIC_ME in cmd['headers']['to']:
        rsp = make_oc2_response(cmd)
        client.publish(producer := cmd['headers']['from'], json.dumps(rsp), qos=0, retain=False)
        print(f'Received {msg.topic}: {cmd}\nSent to {producer}: {json.dumps(rsp)}')
    else:
        print(f'Received {msg.topic}: not mine - ignored')


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
