
def generate_report(vulnerabilities, misconfigs, secrets):
    report = "InfoSec-Analyzer Report\n"
    report += "="*50 + "\n"
    report += "Vulnerabilities:\n" + "\n".join(vulnerabilities) + "\n"
    report += "Misconfigurations:\n" + "\n".join(misconfigs) + "\n"
    report += "Secrets Detected:\n" + "\n".join(secrets) + "\n"
    return report
