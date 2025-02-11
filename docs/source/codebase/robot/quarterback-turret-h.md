# `QuarterbackTurret.h`

## Includes

- `Robot/Robot.h`
- `Robot/MotorControl.h`
- `ps5Controller.h`
- `Utilities/Debouncer.h`
- `Adafruit_LIS3MDL.h`
- `HardwareSerial.h`
- `ADXL335.h`

## Enums

| Enum | Definitions|
| :--: | :---------: |
|`TurretMode`| `Manual, Automatic` |
|`TurretUnits` |`Degrees, Counts`|
|`AssemblyAngle`|`Straight, Angled`|
|`CradleState`|`Forward, Back`|
|`TargetReciever`| `Reciever_1, Reciever_2`|
|`FlywheelSpeed`|`Slow_inwards`, `Stopped`,`Slow_outwards`, `Lvl1_outwards`, `Lvl2_outwards`, `lvl3_outwards`, `maximum`|

### _Combine Specific_
| Enum | Definitions |
| :--: | :---------- |
| `CombinePosition` | `CombineLeft`, `CombineStraight`, `CombineRight` |

## Defined Variables

### Turret Setup
- `QB_TURRET_NUM_SPEEDS`
  - 7

- `FlywheelSpeeds`
  - _Accepts `QB_TURRET_SPEEDS` as the array length_
  - -0.1, 0, 0.1, 0.3, 0.5, 0.7, 1.0
  
### Debounce & Miscellaneous Delay Constants

- `QB_BASE_DEBOUNCE_DELAY`
  - `50 (LONG)`
- `QB_CRADLE_TRAVEL_DELAY`
  - `750 (LONG)`
- `QB_CIRCLE_HOLD_DELAY`
  - `750 (LONG)`
- `QB_CROSS_HOLD_DELAY`
  - `200 (LONG)`
- `QB_CROSS_HOLD_DELAY`
  - `200 (LONG)`
- `QB_TURRET_INTERPOLATION_DELAY`
  - `5L (LONG)`
- `QB_TURRET_THRESHOLD`
  - `35`
- `QB_TURRET_STICK_SCALE_FACTOR`
  - `0.25`

### Speed Constants
- `QB_MIN_PWM_VALUE`
  - `0.08`
- `QB_HOME_PCT`
  - `0.125`
- `QB_HANDOFF`
  - `0.3`
- `QB_HOME_MAG `
  -`0.1`

### Turret Angle Calculation Constants
- `QB_COUNTS_PER_ENCODER_REV`
  - _Number of ticks per encoder revolution_
  - 1000
- `QB_COUNTS_PER_TURRET_REV`
  - _The ratio is 27:1 for the falcon to turret, and the ratio is 5:1 for the falcon to the encoder (for a 12t driving sprocket on 60t gear)_
  - _Encoder spins 5.4 times (or 27/5) for every turret revolution equates for 5400 ticks per rev_
  - 5400
- `QB_COUNTS_PER_TURRET_DEGREE`
  - _15 ticks per degree (5400 / 360)_
  - 15
- `QB_TURRET_SLOP_COUNTS`
  - _Due to the high levels of backlash between the input and output, there are 540 ticks used in the encoder to add a delay before the turret actually starts to move. This prevents problems when switching directions._
  - 540

### Turret Homing Constants
- `QB_TURRET_STOP_LOOP_DELAY_MS`
  - _*ASSUMED to be a delay (measured in milliseconds) between iterations of the turret's move loop_
  - 10
- `QB_TURRET_STOP_THRESHOLD_MS`
  - _MUST be a multiple of `QB_TURRET_STOP_LOOP_DELAY_MS`_
  - 500
- `QB_TURRET_HOME_STOP_FACTOR`
  - _A correction constant for homing,_
    - _*ASSUMED to be multiplied into the stop counts in the final homing algorithm_
  - 0.5
- `QB_TURRET_MANUAL_CONTROL_FACTOR`
  - _Higher values equate to less sensitivity during manual control (Basically dividing the clock of the loop)_
  - 4
  
### Turret PID Controller Constants
- `QB_TURRET_PID_THRESHOLD`
  - _The acceptable error in the position control (in degrees) that will zero the error constants / build up_
  - 3
- `QB_TURRET_PID_MIN_DELTA_T`
  - _*ASSUMED to be a failsafe, if the PID error values are not updated fast enough, such as if the controller hangs for half a second, the PWM values will be massive compared to what they should be_
  - 5
- `QB_TURRET_PID_MAX_DELTA_T`
  - _The maximum time between updates_
- `QB_TURRET_PID_BAD_DELTA_T`
  - _*ASSUMED to be the maximum time before the turret needs to be zeroed out_
  - 250
- `QB_NORTH_OFFSET`
  - _Deals with the problems of zeroing the turret but then holding a set angle afterwards_
  - _NOTE: May be obsolete now_
  - 0
- `QB_AUTO_ENABLED`
  - _Enables or disables Auto Mode. Used for testing_
  - False

### UART Communication Pins
| Pin | Name | Value |
| :-: | :--: | :---: |
| `RX2` | Reciever Pin | 16 |
| `TX2` | Transmitter Pin | 17 |


## Classes
### QuarterbackTurret

**Private**

As is the case for most of these variables, they are *initiated* in a `.h` file, and *instanciated* in the corresponding `.cpp` file.

**MotorControl Instances**
* *Taken from the MotorControl file*
- `cradleActuator`
- `turretMotor`
- `assemblyMotor`
- `flywheelLeftMotor`
- `flywheelRightMotor`

**Pin declartion**
- `turretEncoderPinA`
  - Type: unsigned 8-bit integer
  - Value: defined in `QuarterbackTurret.cpp`
  - Modifyable: NO

- `turretEncoderPinB`
  - Type: unsigned 8-bit integer
  - Value: defined in `QuarterbackTurret.cpp`
  - Modifyable: NO

- `turretLaserPin`
  - Type: unsigned 8-bit integer
  - Value: defined in `QuarterbackTurret.cpp`
  - Modifyable: YES

**Joystick Inputs**
- `stickTurret`
  - Type: float
  - Value: defined in `QuarterbackTurret.cpp`
  - Modifyable: YES
  - *Write purpose found in .h when documenting .cpp*
- `stickFlywheel`
  - Type: float
  - Value: defined in `QuarterbackTurret.cpp`
  - Modifyable: YES
  - *same as above*

**Autonomous Targeting**
* *From the enums earlier in this doc*
- `mode`
  - Enum: `TurretMode`
  - Value: `Manual`, `Automatic`
  - Modifyable: YES
- `target`
  - Enum: ``TargetReciever`
  - Value: `Reciever_1`, `Reciever_2`
  - Modifyable: YES
- `combinePosition`
  - Enum: `CombinePosition`
  - Value: `CombineLeft`, `CombineStraight`, `CombineRight`
  - Modifyable: YES
  - 

**Setup & Status variables**
* *The definitions for these items will be included in the .cpp file for convenience sake*
- `enabled`
  - Type: boolean
  - Value: True or False
  - Modifyable: YES
- `initialized`
  - Type: boolean
  - Value: True or False
  - Modifyable: YES
- `runningMacro`
  - Type: boolean
  - Value: True or False
  - Modifyable: YES

**Assembly Movement**
* *The definitions for these items will be included in the .cpp file for convenience*
* *Again, these are enums, not variables*
- `currentAssemblyAngle`
  - Enum: `AssemblyAngle`
  - Value: `Straight`,`Angle`
  - Modifyable: YES
- `targetAssemblyAngle`
  - Enum: `AssemblyAngle`
  - Value: `Straight`, `Angle`
  - Modifyable: YES
- `assemblyMoving`
  - Type: boolean
  - Value: True or False
  - Modifyable: YES
- `assemblyTriggerToggled`
  - Type: boolean
  - Value: True or False
  - Modifyable: YES
- `assemblyStartTime`
  - Type: unsigned 8-bit integer
  - Value: Defined in `QuarterbackTurret.cpp`
  - Modifyable: YES
  
**Ball Cradle State Variables**
* *Again, some of these are enums, the ones that have enums are denoted*
- `currentCradleState`
  - Enum: `CradleState`
  - Value: `Forward`, `Back`
  - Modifyable: YES
- `targetCradleState`
  - Enum: `CradleState`
  - Value: `Forward`, `Back`
  - Modifyable: YES
- `cradleMoving`
  - Type: boolean
  - Value: True or False
  - Modifyable: YES
- `cradleStartTime`
  - Type: unsigned 32-bit integer
  - Value: defined in QuarterbackTurret.cpp
  - Modifyable: YES

**Flywheel State Variables**
- `currentFlywheelStage`
  - Enum: `FlywheelSpeed`
  - Value: Defined in QuarterbackTurret.cpp
  - Modifyable: YES
- `targetFlywheelStage`
  - Enum: `FlywheelSpeed`
  - Value: Defined in QuarterbackTurret.cpp
  - Modifyable: YES
- `currentFlywheelSpeed`
  - Type: `float`
  - Value: Defined in QuarterbackTurret.cpp
  - Modifyble: YES
- `flywheelManualOverride`
  - Type: boolean
  - Value: True or False
  - Modifyable: YES

**Turret State Variables**
- `currentTurretSpeed`
  - Type: float
  - Value: Defined in QuarterbackTurret.cpp
  - Modifyable: YES
- `targetTurretSpeed`
  - Type: float
  - 

