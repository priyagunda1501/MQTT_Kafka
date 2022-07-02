# mqtt_kafka
MQTT, IOT, Kafka

# On Edge Device 

1. install python,pip3 
2. Install the Python Paho client
	$ pip install paho-mqtt
3. update config.py file with mqtt host and port 
4. run mqtt_producer.py script
	$ python3 mqtt_producer.py

# On Kafka server(Mac):

1. install confluent kafka, refer: https://docs.confluent.io/platform/current/kafka-mqtt/intro.html
2. start zooKeeper and kafka using: 
	$ confluent local services kafka start
3. update mqtt-proxy configuration file at etc/confluent-kafka-mqtt/kafka-mqtt-dev.properties, add required topics list to topic.regex.list filed
4. start mqtt-proxy-server: 
	$ kafka-mqtt-start etc/confluent-kafka-mqtt/kafka-mqtt-dev.properties
5. if mqtt-proxy-server stops with the error: java.net.BindException: Address already in use; then change the mqtt port.no to 1881
