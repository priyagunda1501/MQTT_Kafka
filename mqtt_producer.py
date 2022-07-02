import paho.mqtt.client as mqtt
import logging
import time

import config

logger = logging.getLogger(__name__)


clientId = "telemetry-data"
topic = "raspberrypi"
device_name = "My Python MQTT device"

# on connect
def on_connect(client, userdata, flags, rc):
        print("point connect rc:",rc)
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code %d\n", rc)


def connect_mqtt():
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code %d\n", rc)

    client = mqtt.Client(clientId)
    client.on_connect = on_connect
    client.connect(config.MQTT_HOST,config.MQTT_PORT,60)
    return client


# publish a message
def publish(client):
    msg_count = 0
    while msg_count < 11:
        time.sleep(1)
        msg = "messages: {msg_count}".format(msg_count=msg_count)
        result = client.publish(topic, msg)
        # result: [0, 1]
        status = result[0]
        if status == 0:
            print("Send `{msg}` to topic `{topic}`".format(msg=msg,topic=topic))
        else:
            print("Failed to send message to topic {topic}".format(topic=topic))
        msg_count += 1

def run():
    # connect to mqtt
    client = connect_mqtt()
    # publish a message
    publish(client)


if __name__ == '__main__':
    run()
