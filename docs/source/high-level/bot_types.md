# Bot Types
## Linemen
### Description
- Linemen are the most basic in terms of functionality. 
- Their primary purpose is to initiate physical contact with opposing bots. 
- They have no unique features and their only controllable aspect is basic movement.
	- All other robots with the exception of the [Quarterback v3](bot_types.md#Quarterback%20v3) Turret have a superset of the controls listed below.

### Current Linemen
- `i++`
- `sqrt(-1)`
- `pi`
- `rho`
- `2.72`
- `:)`
- `>=`

### Lineman Controls

| Stick        | Action                               |
| ------------ | ------------------------------------ |
| Left Y-Axis  | Forward/Backward Movement (X/Y Axes) |
| Right X-Axis | Turning/Rotational Movement (Z Axis) |

| Button      | Action                        |
| ----------- | ----------------------------- |
| PlayStation | Turn on Controller            |
| Touchpad    | Emergency Stop                |
| Options     | Change LEDs (Offense/Defense) |
| Share       | Set LEDs to Disco             |
| R1          | Enter Boost Mode              |
| L1          | Enter Slow Mode               |

## Receivers
### Description
- Receivers are similar in function to linemen, but also have nets mounted to their tops. 
- Their primary purpose is to catch footballs thrown by the quarterback using the aforementioned nets.
- Like the linemen, these bots only have basic movement controls.

### Current Receivers
- `32.2`
- `9.8`

## Runningback
### Description
- The runningback is smaller and faster than the other robots.
	- It uses [VEX Falcon 500 motors](../hardware/falcons)
- Its primary purpose is to quickly carry the football along the ground (i.e., to *run*). 
- Like the linemen and receivers, the runningback only has basic movement controls.
	- There is one exception: the right trigger (R2) can be used to calibrate the falcon motors.

### Current Runningback
- `c`

## Center
### Description
- The "old" center features a large claw that can pick up objects off the ground directly in front of the bot, and deposit those objects behind the it. 
- The center's primary purpose is pick up the football from the ground and pass it to the quarterback to initiate a play. 
- In addition to the basic movement controls, the driver is also able to control the arm and the claw of the claw device.

### Applicable Robots
- `phi`

### Center Controls

| Button     | Action     |
| ---------- | ---------- |
| Triangle   | Raise Arm  |
| Cross      | Lower Arm  |
| Circle     | Hold Arm   |
| D-Pad Up   | Open Claw  |
| D-Pad Down | Close Claw |

## Mecanum Center
### Description
- The "new" mecanum center features mecanum wheels for movement and a conveyor belt with flywheels for collecting the ball from the ground. 
- Its primary purpose, similar to the "old" center, is to pick up the football using the flywheels and use the conveyor belt to hand it off to the quarterback. 
- In addition to the basic movement controls, the driver is also able to control the conveyor belt and flywheels.

### Current Center
- `y=x`

### Mecanum Center Controls

| Stick        | Action                       |
| ------------ | ---------------------------- |
| Left Y-Axis  | Forward/backward movement    |
| Left X-Axis  | Strafing/horizontal movement |
| Right X-Axis | Turning/rotational movement  |


| Button   | Action               |
| -------- | -------------------- |
| Square   | Toggle Conveyor      |
| Circle   | Toggle Flywheels     |
| Triangle | Raise Flywheel Speed |
| Cross    | Lower Flywheel Speed |

## Quarterback v2
### Description
- The "old" quarterback features a conveyor belt and flywheels that can launch the football.
	- It also has linear actuators that can adjust the launch angle.
- Its primary purpose is to throw the football using the flywheels.
- In addition to the basic movement controls, the driver is also able to control the conveyor belt, flywheels, and linear actuators.

### Applicable Bots
- `infinity`

### Quarterback v2 Controls

| Button     | Action                  |
| ---------- | ----------------------- |
| Square     | Toggle Conveyor         |
| Circle     | Toggle Flywheels        |
| Triangle   | Increase Flywheel Speed |
| Cross      | Decrease Flywheel Speed |
| D-Pad Up   | Raise Launch Angle      |
| D-Pad Down | Lower Launch Angle      |

## Quarterback v3
### Description
- The "new" quarterback is functionally two robots attached to the same chassis.
	- The "base" is functionally identical to a lineman and is controlled the same way.
	- The "turret" features a tiltable launch assembly consisting of flywheels and a "gripper" or "cradle" to hold the ball.
- Its primary purpose is to throw the football using the flywheels.
- For the turret, the driver is also able to:
	- control flywheel speed
	- switch between manual and automatic targeting
		- in manual mode, aim the turret
		- in automatic mode, switch between receivers
	- launch the football
	- run a variety of macros

### Quarterback v3 Turret Controls

| Stick        | Action                                 | Function           |
| ------------ | -------------------------------------- | ------------------ |
| Left Y-Axis  | Absolute Analog Flywheel Speed Control | `setFlywheelSpeed` |
| Right X-Axis | Aim Turret (Left = CCW, Right = CW)    | `moveTurret`       |

| Button             | Action                                                          | Function                     |
| ------------------ | --------------------------------------------------------------- | ---------------------------- |
| D-Pad Up           | Increase Flywheel Speed                                         | `adjustFlywheelSpeedStage`   |
| D-Pad Down         | Decrease Flywheel Speed                                         | `adjustFlywheelSpeedStage`   |
| Triangle           | Intake Ball from [Mecanum Center](bot_types.md#Mecanum%20Center) | `loadFromCenter`             |
| Cross              | Handoff to [Runningback](bot_types.md#Runningback)                                     | `handoff`                    |
| Square             | Toggle Power to Flywheels/Turret                                | `setEnabled`                 |
| Circle             | Startup and Zero Turret                                         | `reset`, `zeroTurret`        |
| Touchpad           | Emergency Stop Turret                                           | `emergencyStop`              |
| Options            | Toggle Auto/Manual Targeting                                    | `switchMode`                 |
| Right Button (R1)  | Target Receiver 2                                               | `switchTarget`, `switchMode` |
| Right Trigger (R2) | Launch (cradle forward)                                         | `moveCradle`                 |
| Left Button (L1)   | Target Receiver 1                                               | `switchTarget`, `switchMode` |

## Kicker
### Description
- The kicker features a large paddle connected to a motor. 
- Its primary purpose is to use the paddle to propel the football forward and upward by "kicking" it. 
- In addition to the basic movement controls, the driver can also control the motor which is linked to the paddle.

### Current Kicker
- `theta`

### Kicker Controls

| Button   | Action                   |
| -------- | ------------------------ |
| Triangle | Turn Kicker Arm Forward  |
| Cross    | Turn Kicker Arm Backward |
