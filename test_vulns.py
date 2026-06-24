from vulnerability_source import VulnerabilitySource

API_URL = "https://my.api.mockaroo.com/ironclad/vulns/findings.json"

HEADERS = {
    "X-API-Key": "cf7bbbd0"
}

source = VulnerabilitySource(
    API_URL,
    HEADERS
)

vulns = source.fetch_vulns()

print("Total Vulnerabilities:", len(vulns))

first = vulns[0]

print("Title:", first.title)
print("Severity:", first.severity)
print("CVSS:", first.cvss_score)
print("Hostname:", first.asset_hostname)

print(first)