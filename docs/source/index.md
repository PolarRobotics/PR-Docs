% PR-Docs documentation master file, created by
% sphinx-quickstart on Mon Sep 11 20:08:43 2023.
% You can adapt this file completely to your liking, but it should at least
% contain the root `toctree` directive.

# Welcome to the Polar Robotics documentation!

```{toctree}
---
caption: Meta-Documentation
maxdepth: 2
---
metadocs/programming_style_guide
metadocs/documentation_style_guide
metadocs/sphinx
```

```{toctree}
---
caption: High-Level Robot Documentation
maxdepth: 2
---
high-level/bot_types
```

```{toctree}
---
caption: Hardware Documentation
maxdepth: 1
---
hardware/encoders
hardware/esp32
hardware/falcons
hardware/sabertooth_2x25
hardware/sabertooth_2x32
hardware/tackle_sensor_rev3
hardware/tackle_sensor_rev4
hardware/uart
hardware/wiring
```

```{toctree}
---
caption: Data Acquisition
maxdepth: 1
---
data-aq/filezilla.md
data-aq/raspberry_pi_ssh.md
data-aq/router_setup.md
data-aq/serial_printing.md
data-aq/standalone_serial_monitor.md
```

# Indices and tables

- {ref}`genindex`
- {ref}`modindex`
- {ref}`search`
