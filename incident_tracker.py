from enum import Enum


class AlertType(Enum):
    LOGIN_FAILURE = "login_failure"
    LOGIN_SUCCESS = "login_success"
    FILE_HASH_DETECTED = "file_hash_detected"
    DNS_QUERY = "dns_query"
    PORT_SCAN = "port_scan"


class Alert:
    def __init__(self, date, alert_type, asset, indicator):
        self.date = date
        self.alert_type = alert_type
        self.asset = asset
        self.indicator = indicator
        self.classification = "Unknown"
        self.escalated = False

    def classify_indicator(self):
        if self.indicator.startswith(("10.", "192.168.")):
            self.classification = "Internal"
        elif self.indicator.count(".") == 3:
            self.classification = "External"
        else:
            self.classification = "Domain/Hash"

    def severity(self):
        if self.alert_type == AlertType.FILE_HASH_DETECTED:
            return "HIGH"
        elif self.alert_type == AlertType.PORT_SCAN:
            return "MEDIUM"
        elif self.alert_type == AlertType.LOGIN_FAILURE:
            return "MEDIUM"
        else:
            return "LOW"

    def escalate(self):
        if self.severity() == "HIGH":
            self.escalated = True

    def __str__(self):
        return (
            f"{self.date} | "
            f"{self.alert_type.value} | "
            f"{self.asset} | "
            f"{self.indicator} | "
            f"{self.classification} | "
            f"Severity: {self.severity()} | "
            f"Escalated: {self.escalated}"
        )


alerts = []

with open("alerts.txt", "r") as file:
    lines = file.readlines()

print(f"Loaded {len(lines)} alerts.\n")

for line in lines:
    parts = line.strip().split(",")

    date = parts[0]
    alert_type = AlertType(parts[1])
    asset = parts[2]
    indicator = parts[3]

    alert = Alert(date, alert_type, asset, indicator)

    alert.classify_indicator()

    alert.escalate()

    alerts.append(alert)

print("===== Incident Triage Summary =====\n")

for alert in alerts:
    print(alert)

with open("incident_summary.txt", "w") as report:
    report.write("===== Incident Triage Summary =====\n\n")

    for alert in alerts:
        report.write(str(alert) + "\n")

print("\nSummary report saved to incident_summary.txt")