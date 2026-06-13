import requests


API_URL = "https://my.api.mockaroo.com/ironclad-soc-case-artifacts"
API_KEY = "cf7bbbd0"


class Artifact:
    def __init__(self, artifact_id, case_id, artifact_type, value, severity, source):
        self.artifact_id = artifact_id
        self.case_id = case_id
        self.artifact_type = artifact_type
        self.value = value
        self.severity = severity
        self.source = source

    def display(self):
        return f"{self.artifact_type}: {self.value} | Severity: {self.severity} | Source: {self.source}"


class SOCCase:
    def __init__(self, case_id):
        self.case_id = case_id
        self.artifacts = []

    def add_artifact(self, artifact):
        self.artifacts.append(artifact)

    def determine_severity(self):
        severities = [artifact.severity.lower() for artifact in self.artifacts]

        if "critical" in severities:
            return "CRITICAL"
        elif "high" in severities:
            return "HIGH"
        elif "medium" in severities:
            return "MEDIUM"
        elif "low" in severities:
            return "LOW"
        else:
            return "INFORMATIONAL"

    def generate_report(self):
        print("=" * 50)
        print(f"SOC Case Report: {self.case_id}")
        print(f"Case Severity: {self.determine_severity()}")
        print("-" * 50)

        for artifact in self.artifacts:
            print(artifact.display())

        print("=" * 50)
        print()


def fetch_api_data():
    response = requests.get(API_URL, params={"key": API_KEY})

    if response.status_code == 200:
        return response.json()
    else:
        print("Failed to retrieve API data.")
        print(f"Status Code: {response.status_code}")
        return []


def main():

    print("Pulling SOC case artifact data from API...\n")

    data = fetch_api_data()

    cases = {}

    for item in data:

        artifact_id = item.get("ip", item.get("domain", item.get("file_hash", "Unknown")))
        case_id = item.get("case_id", "Unknown")
        artifact_type = item.get("indicator_type", "Unknown")
        value = item.get("ip", item.get("domain", item.get("file_hash", "Unknown")))
        severity = "Medium"
        source = item.get("comment", "Unknown")

        artifact = Artifact(
            artifact_id,
            case_id,
            artifact_type,
            value,
            severity,
            source
        )

        if case_id not in cases:
            cases[case_id] = SOCCase(case_id)

        cases[case_id].add_artifact(artifact)

    for case in cases.values():
        case.generate_report()


if __name__ == "__main__":
    main()