# README.md (Version 2)

````md
# Threat Hunting Script

A Python-based threat hunting utility that analyzes log files to identify suspicious activities and potential Indicators of Compromise (IoCs). The tool helps security students understand log analysis, brute-force detection, and basic security monitoring techniques.

## Features

### Version 1 Features

- Read and analyze log files
- Detect failed login events
- Count failed login attempts per IP address
- Identify suspicious IP addresses
- Generate a console-based threat report

### Version 2 Features

- IP Address Validation
- Threat Severity Classification
- Enhanced Threat Reports
- Export Reports to TXT File
- Activity Logging
- Improved Error Handling
- Better Output Formatting
- Suspicious Activity Summary

## Technologies Used

- Python 3
- Visual Studio Code (Recommended)
- Built-in `collections` module
- Built-in `ipaddress` module
- Built-in `logging` module

## Requirements

### Software Requirements

- Python 3.8 or later
- Visual Studio Code (optional but recommended)

### Python Libraries

No external libraries are required.

This project uses Python's built-in modules:

```python
from collections import Counter
import ipaddress
import logging
```
