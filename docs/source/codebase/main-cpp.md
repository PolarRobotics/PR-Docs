# `main.cpp`
## Description
- This file acts as a central platform for all of the robots' functionality.
- The setup function initializes several aspects of the robots, including the ESP32 pins, the robot type, the drive type, and the LED lights.
- The loop function helps to issue various instructions to the robot based on controller input.
- The function "onConnection" prints a message when the robot and a controller connect.
- The function "onDisconnect" prints a message when the robot and a controller disconnect.
## Included Headers
- `Arduino.h`
- `ps5Controller.h`
- `PolarRobotics.h`
- `Pairing/pairing.h`
- `Utilities/ConfigManager.h`
- `Robot/Lights.h`
- `Robot/Robot.h`
- `Robot/Lineman.h`
- `Robot/Center.h`
- `Robot/MecanumCenter.h`
- `Robot/Kicker.h`
- `Robot/Quarterback.h`
- `Drive/Drive.h`
- `Drive/DriveMecanum.h`
- `Drive/DriveQuick.h`