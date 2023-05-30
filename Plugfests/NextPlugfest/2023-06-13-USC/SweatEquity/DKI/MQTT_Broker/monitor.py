import fire
import os
import paho.mqtt.client as mqtt

"""
Monitor all traffic published on MQTT broker with topics beginning with "oc2/"

Broker address: environment variable CAVBROKER - url:port
Authentication: environment variable CAVUSER - username,password
"""
BROKER, BROKER_PORT = os.getenv('CAVBROKER').rsplit(':')
USERNAME, PASSWORD = os.getenv('CAVUSER').split(',')

TOPIC_C_ALL = 'oc2/cmd/all'
TOPIC_C_SBOM = 'oc2/cmd/ap/sbom'
TOPIC_C_01 = 'oc2/cmd/device/c01'
TOPIC_P_ALL = 'oc2/rsp'
TOPIC_P = 'oc2/rsp/p01'


def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    client.subscribe([('$SYS/#', 0), ('oc2/#', 0)])


def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))


def main(cmd: str = '', broker: str = BROKER, port: int = int(BROKER_PORT)):
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
