# Threat Hunting Script (v2)

A lightweight Python tool that scans log files for brute-force login attempts and generates a severity-ranked threat report.

## Features
- Parses log entries and validates IP addresses
- Detects `LOGIN_FAILED` events and counts attempts per IP
- Flags IPs exceeding a configurable threshold as suspicious
- Classifies severity: LOW / MEDIUM / HIGH / CRITICAL
- Outputs a formatted report to console and `threat_report.txt`
- Logs execution details to `hunt_log.txt`

## Requirements
- Python 3.8+
- No external dependencies (uses built-in `collections`, `ipaddress`, `logging`)

## Usage
1. Place your log file as `sample.log` in the project directory (format: `date time ip event`).
2. Run:
   ```bash
   python main.py
   ```
3. View results in the console or `threat_report.txt`.

## Log Format Example
```
2026-06-20 10:01:00 192.168.1.10 LOGIN_FAILED
```

## Configuration
Edit these variables at the top of `main.py`:
| Variable | Description | Default |
|---|---|---|
| `LOG_FILE` | Input log file path | `sample.log` |
| `REPORT_FILE` | Output report path | `threat_report.txt` |
| `THRESHOLD` | Failed attempts before flagging | `3` |

## Output Files
- `threat_report.txt` — generated threat summary
- `hunt_log.txt` — run/execution log

## License
For educational and personal security research use.
