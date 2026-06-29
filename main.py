from collections import Counter
import ipaddress
import logging

# Configuration
LOG_FILE = "sample.log"
REPORT_FILE = "threat_report.txt"
THRESHOLD = 3

# Logging Setup
logging.basicConfig(
    filename="hunt_log.txt",
    level=logging.INFO,
    format="%(asctime)s - %(message)s"
)

logging.info("Threat hunting started.")

try:
    failed_ips = []

    # Read Log File
    with open(LOG_FILE, "r") as file:
        for line in file:
            parts = line.strip().split()

            if len(parts) >= 4:
                ip = parts[2]
                event = parts[3]

                # Validate IP Address
                try:
                    ipaddress.ip_address(ip)
                except ValueError:
                    logging.warning(f"Invalid IP skipped: {ip}")
                    continue

                if event == "LOGIN_FAILED":
                    failed_ips.append(ip)

    # Count Failed Attempts
    ip_counts = Counter(failed_ips)

    # Generate Report
    report_lines = []
    report_lines.append("=" * 55)
    report_lines.append("THREAT HUNTING REPORT")
    report_lines.append("=" * 55)
    report_lines.append("")
    report_lines.append(
        f"{'IP Address':<18}{'Attempts':<12}{'Severity'}"
    )
    report_lines.append("-" * 55)

    suspicious_count = 0

    for ip, count in ip_counts.items():

        if count > THRESHOLD:

            suspicious_count += 1

            # Severity Classification
            if count <= 3:
                severity = "LOW"
            elif count <= 6:
                severity = "MEDIUM"
            elif count <= 10:
                severity = "HIGH"
            else:
                severity = "CRITICAL"

            report_lines.append(
                f"{ip:<18}{count:<12}{severity}"
            )

    report_lines.append("")
    report_lines.append(
        f"Total Suspicious IPs: {suspicious_count}"
    )

    # Display Report
    print("\n".join(report_lines))

    # Save Report
    with open(REPORT_FILE, "w") as report:
        report.write("\n".join(report_lines))

    logging.info("Threat report generated successfully.")

except FileNotFoundError:
    print(f"ERROR: '{LOG_FILE}' not found.")
    logging.error(f"{LOG_FILE} not found.")

except Exception as e:
    print(f"ERROR: {e}")
    logging.error(str(e))

logging.info("Threat hunting completed.")