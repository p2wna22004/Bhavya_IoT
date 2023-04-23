import paho.mqtt.client as paho
#pip3 install paho-mqtt
global mqttclient;
global broker;
global port;

#Import pymysql module library
import pymysql
#Create a connection to MySQL Database 
conn =pymysql.connect(database="mysql",user="bhavya",password="password1",host="localhost")
#Create a MySQL Cursor to that executes the SQLs
cur=conn.cursor()

broker = "0.0.0.0";
port = 1883;

client_uniq = "34.125.6.224"

mqttclient = paho.Client(client_uniq, True) 

def test(client, userdata, message):
  print("client:"+ str(client))
  print("userdata:"+ userdata)
  print("message:"+ message.payload)

def _on_message(client, userdata, msg):
# print("Received: Topic: %s Body: %s", msg.topic, msg.payload)
print(msg.topic+" "+str(msg.payload))
 
#Subscribed Topics 
def _on_connect(mqttclient, userdata, flags, rc):
# print("New Client: "+str(mqttclient)+ " connected")
# print(rc)
mqttclient.subscribe("sensor_data", qos=0) 
  
mqttclient.message_callback_add("sensor_data/test", test)

mqttclient.connect(broker, port, keepalive=1, bind_address="")
  


#Execute the SQL to write data to the database
cur.execute("INSERT INTO <tablename>(ID, Time, temperature)VALUES(%(ID)s,%(Time)s,%(temperature)s);",msg.payload)

mqttclient.on_connect = _on_connect

mqttclient.loop_forever()

#Close the cursor
cur.close()
#Commit the data to the database
conn.commit()
#Close the connection to the database
conn.close()





