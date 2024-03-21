#include <ros.h>
#include <geometry_msgs/Twist.h>
#include <SoftwareSerial.h>
#include <HCSR04.h>

HCSR04 hcl(1, 2);   //Left Sensor
HCSR04 hcc(7, 8);   //Center Sensor
HCSR04 hcr(12, 13); //Right Sensor

ros::NodeHandle  ultra;

geometry_msgs::Twist dis_data;
geometry_msgs::Twist motor_data;
ros::Publisher ultra_data("ultrasound", &dis_data);



void cal_data(const geometry_msgs::Twist& sub_data)
{
  motor_data = sub_data;
  analogWrite(5, motor_data.linear.x);
  analogWrite(6, motor_data.linear.y);
  digitalWrite(3, motor_data.linear.z);
  digitalWrite(4, motor_data.linear.z);  
}

ros::Subscriber<geometry_msgs::Twist> mod_data("mybot", &cal_data);

void setup() {
  
  ultra.initNode();
  ultra.advertise(ultra_data);
  ultra.subscribe(mod_data);
  pinMode(5, OUTPUT); //Motor Driver-1 Speed Left
  pinMode(3, OUTPUT); //Motor Driver-1 Direction Left
  pinMode(6, OUTPUT); //Motor Driver-2 Speed Riight
  pinMode(4, OUTPUT); //Motor Driver-2 Direction Right
  
}

void loop() {

  dis_data.linear.x = hcl.dist();
  dis_data.linear.y = hcc.dist();
  dis_data.linear.z = hcr.dist();
  ultra_data.publish(&dis_data);
  ultra.spinOnce();
  delay(100);
  
}
