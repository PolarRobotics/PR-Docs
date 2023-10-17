# Bot Types
## Controls Summary
| Stick        | Action                      |
| ------------ | --------------------------- |
| Left Y-Axis  | Forward/backward movement   | 
| Right X-Axis | Turning/rotational movement |


| Button | Action           |
| ------ | ---------------- |
| R1     | Enter Boost Mode |
| L1     | Enter Slow Mode  |

## Linemen
### Description
- Linemen are the most basic in terms of functionality. Their primary purpose is to initiate physical contact with opposing bots. They have no unique features and their only controllable aspect is basic movement.

- Current Linemen:
    - `i++`
    - `sqrt(-1)`
    - `pi`
    - `rho`
    - `2.72`
    - `:)`
    - `>=`

## Receivers
### Description
- Receivers are similar in function to linemen, but also have nets mounted to their tops. Their primary purpose is to catch footballs thrown by the quarterback using the aforementioned nets. Like the linemen, these bots only have the basic movement controls.

- Current Receivers:
    - `32.2`
    - `9.8`

## Runningback
### Description
- The runningback is smaller and faster than the other robots. Its primary purpose is to quickly carry the football along the ground (i.e., to *run*). Like the linemen and receivers, the runningback has only the basic movement controls.

- Current Runningback:
    - `c`

## Center
### Description
- The "old" center features a large claw that can pick up objects off the ground directly in front of the bot, and deposit those objects behind the it. The center's primary purpose is pick up the football from the ground and pass it to the quarterback to initiate a play. In addition to the basic movement controls, the driver is also able to control the arm and the claw of the claw device.

- Current Bots:
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
- The "new" mecanum center features mecanum wheels for movement and a conveyor belt with flywheels for picking up objects from the ground. Its primary purpose, similar to the "old" center, is to pick up the football using the flywheels and use the conveyor belt to hand it off to the quarterback. In addition to the basic movement controls, the driver is also able to control the conveyor belt and flywheels.

- Current Mecanum Center:
	- (under construction)

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

## Quarterback
### Description
- The quarterback features a conveyor belt and flywheels that can propel objects held by the bot. Their primary purpose is to throw the football via flywheel propulsion. In addition to the basic movement controls, the driver is also able to control the conveyer belt and flywheels.

- Current Bots:
    - `infinity`

### Quarterback Controls

| Button     | Action               |
| ---------- | -------------------- |
| Square     | Toggle Conveyor      |
| Circle     | Toggle Flywheels     |
| Triangle   | Raise Flywheel Speed |
| Cross      | Lower Flywheel Speed |
| D-Pad Up   | Raise Launch Angle   |
| D-Pad Down | Lower Launch Angle   |

## Kicker
### Description
- This bot type features a large paddle connected to a motor. Their primary purpose is to use the paddle to propel the football forward and upward by smacking it. In addition to the basic movement controls, the driver can also control the motor, therefore also indirectly controlling the paddle.

- Current Bots:
    - `theta`

### Kicker Controls

| Button   | Action                     |
| -------- | -------------------------- |
| Triangle | Turn Kicker Motor Forward  | 
| Cross    | Turn Kicker Motor Backward |