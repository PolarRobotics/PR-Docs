# `Drive.cpp`
## Description
- This file, which contains the functions of the Drive class, controls several parameters related to the driving of the robots. The purpose of this code is to ensure that the robots respond appropriately to controller input. Based on stick inputs from a controller, this code will alter the speed of a robot's motors. The code also incorporates ramping to ensure that the robots don't lose control due to the motors starting up too quickly.
- This code is intended to be used with robots featuring the standard lineman configuration, with the back left wheel connected to a left motor, the back right wheel connected to a right motor, and the front wheel(s) not connected to any motor.
- The function "Drive" acts as a constructor for the Drive class, establishing the robot's type, motor type, gear ratio, wheel base, minimum and maximum turning radius, and whether or not it has encoders. In addition, it also sets baseline motor power levels and additional turning parameters for the mecanum center.
- The function "setupMotors" calls setup functions for the two motors, passing motorType, hasEncoders, and gearRatio. If a robot has encoders, an alterate version will be called that also passes the encoder pins.
- The function "setMotorType" sets the type of motors present within the robot.
- The function "setStickPwr" normalizes the stick values passed in to values between -1 and 1 before setting them to stickForwarddRev and stickTurn, essentially preprocessing the stick input values before they are applied.
- The function "getForwardPower" returns the value of stickForwardRev.
- The function "getTurnPower" returns the value of stickTurn.
- The function "setSpeedScalar" sets the internal speed variable based on the bns input passed into the function. The bns represents the drive mode of the robot, which can be either Boost, Normal, or Slow. The scalar my also be set to 0 if the requested power is greater than 1 as a safety measure.
- The function "setSpeedValue" constrains the speed percentage to a value between -1 and 1.
- The function "getSpeedScalar" returns the value of this->speedScalar.
- The function "generateMotionValues" changes the power of the motors based on the status of the forward power and turning control sticks.
- The function "calcTurning" helps to calculate the motor power needed to achieve turning.
- The function "emergencyStop" directly sets the power of both motors to zero, stopping the robot's movement.
- The function "printSetup" print information about the robot to the console, which includes the motor type, gear ration, minimum R and RPM, maximum R and RPM, turn sensitivity mode, and whether or not the robot has encoders.
- The function "update" updates the motors following the setting of motor values in other functions. In addition, this function also where ramping is implemented for the motors. 
- The function "getMotorWifiValue" returns a value based on the motor requested in the function.
## Included Headers
- `Arduino.h`
- `Drive/Drive.h`
- `Robot/MotorControl.h`