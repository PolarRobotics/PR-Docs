describe the different components and subsystems of the robot here (from a practical perspective), including the two types of batteries and the ESP LEDs.

# Robot Components and Subsystems
## Overview
- Broadly speaking, all robots we use have at least these key electrical components:
  1. ESP32 Microcontroller
  2. "ESP Battery" (18650 Lithium Cell 7.7V Battery Pack)
  3. Main Power Battery (usually a Kobalt 24V Drill Battery)
  4. Sabertooth Motor Controller
  5. Drive Motors (usually AmpFlow)
  6. Main Power Switch
- Some robots have additional sensors or actuators which are programmed via specialized subclasses of the base `Robot` class.
  - Notable examples include the Quarterback V3 or the Center V2.