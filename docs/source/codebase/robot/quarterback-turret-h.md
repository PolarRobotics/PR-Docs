# `QuarterbackTurret.h`
## Description
- This file defines the following enums:
    | Enum            | States                     |
    |-----------------|----------------------------|
    | TurretMode      | manual, automatic, combine |
    | TurretUnits     | degrees, counts            |
    | AssemblyAngle   | straight, angled, unknownAngle                                   |
    | CradleState     | forward, back              |
    | TargetReceiver  | receiver_1, receiver_2     |
    | CombinePosition | combineLeft, combineStraight, combineRight                  |
    | FlywheelSpeed   | slow_inwards, stopped, slow_outwards, lvl1_outwards, lvl2_outwards, lvl3_outwards, maximum                         |
- This file also defines the following constants:
    - Turret Speed Constants:
        | Constant             | Value |
        |----------------------|-------|
        | QB_TURRET_NUM_SPEEDS | 7     |
        | flywheelSpeeds       | {-0.1, 0, 0.1, 0.215, 0.31, 0.3875, 1.0}        |
    - Debounce and Delay Constants:
        | Constant                      | Value |
        |-------------------------------|-------|
        | QB_BASE_DEBOUNCE_DELAY        | 50L   |
        | QB_ASSEMBLY_TILT_DELAY        | 200L  |
        | QB_CRADLE_TRAVEL_DELAY        | 750L  |
        | QB_CIRCLE_HOLD_DELAY          | 750L  |
        | QB_TRIANGLE_HOLD_DELAY        | 200L  |
        | QB_CROSS_HOLD_DELAY           | 200L  |
        | QB_TURRET_INTERPOLATION_DELAY | 5L    |
        | QB_TURRET_THRESHOLD           | 35    |
        | QB_TURRET_STICK_SCALE_FACTOR  | 0.15  |
    - Speed Constants:
        | Constant         | Value |
        |------------------|-------|
        | QB_MIN_PWM_VALUE | 0.1   |
        | QB_HOME_PCT      | 0.125 |
        | QB_HANDOFF       | 0.3   |
        | QB_HOME_MAG      | 0.1   |
        | QB_ASM_SPEED     | 0.3   |
    - Turret Angle Calculation Constants:
        | Constant                    | Value  |
        |-----------------------------|--------|
        | QB_COUNTS_PER_ENCODER_REV   | 1250   |
        | QB_COUNTS_PER_TURRET_REV    | 10556  |
        | QB_COUNTS_PER_TURRET_DEGREE | 29.321 |
        | QB_TURRET_SLOP_COUNTS       | 540    |
    - Turret Homing Constants:
        | Constant                        | Value |
        |---------------------------------|-------|
        | QB_TURRET_STOP_LOOP_DELAY_MS    | 10    |
        | QB_TURRET_STOP_THRESHOLD_MS     | 500   |
        | QB_TURRET_HOME_STOP_FACTOR      | 0     |
        | QB_TURRET_MANUAL_CONTROL_FACTOR | 4     |
    - Turret PID Controller Constants:
        | Constant                  | Value |
        |---------------------------|-------|
        | QB_TURRET_PID_THRESHOLD   | 3     |
        | QB_TURRET_PID_MIN_DELTA_T | 5     |
        | QB_TURRET_PID_MAX_DELTA_T | 25    |
        | QB_TURRET_PID_BAD_DELTA_T | 250   |
        | QB_NORTH_OFFSET           | 0     |
        | QB_AUTO_ENABLED           | false |
    - UART Communication Pins:
        | Constant | Value | Notes           |
        |----------|-------|-----------------|
        | RX2      | 16    | Reciever Pin    |
        | TX2      | 17    | Transmitter Pin |
- In addition, this file creates the QuarterbackTurret class, featuring relevant variable declarations and function prototypes. More information about these functions can be found in the documentation for QuarterbackTurret.cpp.
## Included Headers
- `Robot/Robot.h`
- `Robot/MotorControl.h`
- `ps5Controller.h`
- `Utilities/Debouncer.h`
- `Adafruit_LIS3MDL.h`
- `HardwareSerial.h`