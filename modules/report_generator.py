import json

def generate_report(vulnerabilities):
    with open('report.json', 'w') as file:
        json.dump(vulnerabilities, file, indent=4)
    print("Report saved as report.json")
