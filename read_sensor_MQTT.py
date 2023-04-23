import paho.mqtt.client as mqtt
import time as strftime

from w1thermsensor import W1ThermSensor
#Establish mqtt connection
topic = "sensor_data"
client = mqtt.Client()
client.connect('34.125.211.55',1883,60)

#Read and publish sensor information
for sensor in W1ThermSensor.get_available_sensors():
    ID = sensor.id
    temperature = sensor.get_temperature()
    Time = strftime("%d/%m/%y at %I:%M%p")
    payload["ID"]=ID
    payload["temperature"]=temperature
    payload["Time"]=Time
    (rc,mid)=client.publish(topic,payload);
    
    
client.disconnect()

