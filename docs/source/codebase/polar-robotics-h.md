# `PolarRobotics.h`
## Description
% this description needs to be revised into a table that states what exactly the pin numbers are, or better yet, link to the google sheet
- This file primarily contains various global pin declarations. 
	- The first four pins declared are for connecting to the motors. 
		- In a four wheel configuration, each pin connects to one of a robot's four wheels. 
		- In a two wheel configuration, one pin connects the the left drive, one pin connects to the right drive, and the other two pins are unused. 
	- The next four pins declared are reserved for special bots. 
		- These pins connect to various features that are exclusive to special bots, such as conveyor belts and flywheels. 
	- The ninth pin declared connects to the LED lights on the outside of a robot. 
	- Lastly, the tenth pin declared appears to connect to a robot's tackle sensor, which detects when a robot has been hit.
	- The full pin spreadsheet can be found [here](https://docs.google.com/spreadsheets/d/17pdff4T_3GTAkoctwm2IMg07Znoo-iJkyDGN5CqXq3w/edit?gid=0#gid=0).
- This file also contains a global `enum` variable named `BOT_STATE`. 
	- This variable contains six different enumerations reflecting different states of a robot, which is used to determine the color of the robot's LED lighting. 
		- The first state, `PAIRING`, indicates that the robot is currently attempting to pair with a controller. 
		- The second state, `CONNECTED`, indicates that the robot has successfully connected to a controller. 
		- The third state, `DISCONNECTED`, indicates that the robot has become disconnected from a controller that it was previously connected to. 
		- The fourth state, `OFFENSE`, indicates that the robot is in an offensive position. 
		- The fifth state, `DEFENSE`, indicates that the robot is in a defensive position. 
		- The last state, `TACKLED`, indicates that the robot has been hit by another robot, triggering the CRFC [tackle sensor](../hardware/tackle-sensor-rev4.md).

## Included Headers
- `Arduino.h`
- `Utilities/BotTypes.h`
- `Utilities/MotorTypes.h`