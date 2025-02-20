# `Drive.h`
## Description
- This file defines the following constants:
    | Constant                  | Value    |
    |---------------------------|----------|
    | NUM_MOTORS                | 2        |
    | ACCELERATION_RATE         | 0.00375f |
    | RB_ACCELERATION_RATE      | 0.0015f  |
    | BRAKE_PERCENTAGE          | 0.9      |
    | TIME_INCREMENT            | 5        |
    | NORMAL_TURN_CONSTANT      | 0.05     |
    | TANK_MODE_PCT             | 0.75     |
    | RB_TANK_MODE_PCT          | 0.5      |
    | DRIFT_MODE_PCT            | 0.8      |
    | STICK_DEADZONE            | 0.075    |
    | THRESHOLD                 | 0.00001  |
    | FALCON_CALIBRATION_FACTOR | 1.0f     | 
    | MOTOR_ZERO_OFFSET         | 0.05f    | 
    | SMALL_12V_BOOST_PCT       | 0.15f    |
    | SMALL_12V_NORMAL_PCT      | 0.1f     |
    | SMALL_12V_SLOW_PCT        | 0.05f    |
    | BRAKE_BUTTON_PCT          | 0        |
- Next, an array containing the BNS values for each motor type is created.
- Finally, this file creates the Drive class, featuring relevant variable declarations and function prototypes. More information about these functions can be found in the documentation for Drive.cpp.
## Included Headers
- `Arduino.h`
- `Robot/MotorControl.h`
- `PolarRobotics.h`