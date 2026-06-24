import requests

VULN_API_URL = "https://my.api.mockaroo.com/ironclad/vulns/findings.json"
API_KEY = "cf7bbbd0"

headers = {
    "X-API-Key": API_KEY
}

response = requests.get(VULN_API_URL, headers=headers)
print("Status Code:", response.status_code)

data = response.json()

print("Total vulnerabilities:", len(data))
print("\nJSON Fields Discovered:")
for field in data[0].keys():
    print("-", field)

print("\nFirst Vulnerability Record:")
print(data[0])
print("\nSample Vulnerability Summary")

print("Title:", data[0]["vuln_title"])
print("CVE:", data[0]["cve_id"])
print("CVSS Score:", data[0]["cvss_score"])
print("Status:", data[0]["status"])
print("Recommended Fix:", data[0]["recommended_fix"])
high_count = 0

for vuln in data:
    if float(vuln["cvss_score"]) >= 7.0:
        high_count += 1

print("\nHigh Risk Vulnerabilities:", high_count)