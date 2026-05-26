# Ros2-GPS-Project
A simple Publisher and Subscriber Node in Python using ROS2 on Ubuntu. 

In this final technical task, I created a ROS 2 publisher and subscriber system that sends simulated GPS signal data. The project generates initial arbitrary values for latitude and longitude, then applies a random variation between -0.01 and 0.01 to simulate the movement of a simple robotic system. This data is published as string messages on the /gps_data topic. The subscriber node listens to this topic and receives the published messages in real time, printing the data to the terminal. This demonstrates successful communication between two ROS 2 nodes through a shared topic.

This type of data communication is a fundamental concept in robotics systems used for navigation and coordination. Robots such as drones and autonomous vehicles rely on similar sensor-based communication to determine their position and plan movement paths in an environment. By simulating GPS data, this fun mini-project demonstrates how sensor information can be shared between nodes in a ROS 2 system to support real-time decision-making.


