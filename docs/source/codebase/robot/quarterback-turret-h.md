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
        | Constant             | Value |
        |----------------------|-------|
        | QB_BASE_DEBOUNCE_DELAY        |  |
        | QB_ASSEMBLY_TILT_DELAY        |  |
        | QB_CRADLE_TRAVEL_DELAY        |  |
        | QB_CIRCLE_HOLD_DELAY          |  |
        | QB_TRIANGLE_HOLD_DELAY        |  |
        | QB_CROSS_HOLD_DELAY           |  |
        | QB_TURRET_INTERPOLATION_DELAY |  |
        | QB_TURRET_THRESHOLD           |  |
        | QB_TURRET_STICK_SCALE_FACTOR  |  |
    - Speed Constants:
    - Turret Angle Calculation Constants:
    - Turret Homing Constants:
    - Turret PID Controller Constants:
    - UART Communication Pins:
        
        
- In addition, this file creates the Quarterback class, featuring relevant variable declarations and function prototypes. More information about these functions can be found in the documentation for Quarterback.cpp.
## Included Headers
- `Robot/Robot.h`
- `Robot/MotorControl.h`
- `ps5Controller.h`
- `Utilities/Debouncer.h`
- `Adafruit_LIS3MDL.h`
- `HardwareSerial.h`