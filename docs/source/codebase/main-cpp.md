# `main.cpp`
## Description
- This file acts as a central platform for all of the robots' functionality.
- The `setup()` function initializes several aspects of the robot, including the ESP32 pins, the robot and drive objects, and the LED lights.
- The `loop()` function repeatedly reads inputs from the PS5 controller and issues corresponding instructions to the robot.
- The function `onConnection()` prints a message when a controller is connected to the robot.
- The function `onDisconnect()` prints a message when a previously connected controller disconnects from the robot.

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
- `Robot/QuarterbackBase.h`
- `Robot/QuarterbackTurret.h`
- `Drive/Drive.h`
- `Drive/DriveMecanum.h`