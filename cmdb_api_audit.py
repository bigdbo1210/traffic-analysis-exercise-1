import requests
from datetime import datetime

API_URL = "https://my.api.mockaroo.com/ironclad/cmdb.json"
API_KEY = "cf7bbbd0"


class Asset:
    def __init__(self, raw):
        self.asset_id = raw.get("asset_id")
        self.hostname = raw.get("hostname", "unknown")
        self.asset_type = raw.get("asset_type", "unknown")
        self.os = raw.get("os", "unknown")
        self.environment = raw.get("environment", "unknown")
        self.owner_team = raw.get("owner_team", "unknown")
        self.internet_exposed = bool(raw.get("internet_exposed", False))
        self.criticality = raw.get("criticality", "low")
        self.last_seen = raw.get("last_seen", "unknown")

    def risk_level(self):
        crit_high = str(self.criticality).lower() == "high"

        if self.internet_exposed and crit_high:
            return "HIGH"
        elif self.internet_exposed or crit_high:
            return "MEDIUM"
        else:
            return "LOW"

    def days_since_seen(self):
        try:
            seen_date = datetime.strptime(self.last_seen, "%m/%d/%Y")
            return (datetime.now() - seen_date).days
        except:
            return None

    def __str__(self):
        return (
            f"{self.hostname} | "
            f"type={self.asset_type} | "
            f"os={self.os} | "
            f"env={self.environment} | "
            f"owner={self.owner_team} | "
            f"risk={self.risk_level()}"
        )


try:
    response = requests.get(
        API_URL,
        headers={"X-API-Key": API_KEY},
        timeout=10
    )

    print("Status code:", response.status_code)

    if response.status_code != 200:
        print("Request failed.")
        raise SystemExit

    data = response.json()

except requests.exceptions.Timeout:
    print("Request timed out.")
    raise SystemExit

except requests.exceptions.ConnectionError:
    print("Connection error.")
    raise SystemExit

except Exception as e:
    print("Error:", e)
    raise SystemExit


print("Number of assets:", len(data))

assets = [Asset(record) for record in data]


env_counts = {}

for asset in assets:
    env_counts[asset.environment] = env_counts.get(asset.environment, 0) + 1


risk_counts = {
    "HIGH": 0,
    "MEDIUM": 0,
    "LOW": 0
}

for asset in assets:
    risk_counts[asset.risk_level()] += 1


exposed_assets = [
    asset for asset in assets
    if asset.internet_exposed
]


high_priority_review = [
    asset for asset in assets
    if asset.environment.lower() == "prod"
    and (
        asset.internet_exposed
        or asset.criticality.lower() == "high"
    )
]


team_high_risk = {}

for asset in assets:
    if asset.risk_level() == "HIGH":
        team_high_risk[asset.owner_team] = (
            team_high_risk.get(asset.owner_team, 0) + 1
        )

top_teams = sorted(
    team_high_risk.items(),
    key=lambda x: x[1],
    reverse=True
)[:3]


stale_assets = []

for asset in assets:
    days = asset.days_since_seen()

    if days is not None and days >= 30:
        stale_assets.append((asset, days))


print("\n=== Assets by Environment ===")

for env, count in env_counts.items():
    print(f"{env}: {count}")


print("\n=== Assets by Risk Level ===")

for level, count in risk_counts.items():
    print(f"{level}: {count}")


print("\n=== High Priority Review ===")

for asset in high_priority_review:
    print(asset)


print("\n=== Top 3 Teams with HIGH Risk Assets ===")

for team, count in top_teams:
    print(f"{team}: {count}")


with open("cmdb_summary.txt", "w") as out:

    out.write("Ironclad CMDB API Audit Report\n")
    out.write("================================\n\n")

    out.write(f"Total Assets: {len(assets)}\n\n")

    out.write("Assets by Environment:\n")

    for env, count in env_counts.items():
        out.write(f"- {env}: {count}\n")

    out.write("\nAssets by Risk Level:\n")

    for level, count in risk_counts.items():
        out.write(f"- {level}: {count}\n")

    out.write("\nHigh Priority Review:\n")

    for asset in high_priority_review:
        out.write(f"- {asset}\n")

    out.write("\nTop 3 Teams with HIGH Risk Assets:\n")

    for team, count in top_teams:
        out.write(f"- {team}: {count}\n")

    out.write("\nAssets Not Seen in 30+ Days:\n")

    for asset, days in stale_assets:
        out.write(
            f"- {asset.hostname} | "
            f"{days} days since seen\n"
        )

print("\nWrote report to cmdb_summary.txt")