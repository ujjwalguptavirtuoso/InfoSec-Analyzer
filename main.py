
from scanners import code_vulnerability_scanner, configuration_checker, secrets_detector
from report import report_generator
from utils import file_operations

def main(file_path):
    file_content = file_operations.read_file(file_path)
    
    vulnerabilities = code_vulnerability_scanner.scan_for_vulnerabilities(file_content)
    misconfigs = configuration_checker.check_configurations(file_content)
    secrets = secrets_detector.detect_secrets(file_content)
    
    report = report_generator.generate_report(vulnerabilities, misconfigs, secrets)
    print(report)

if __name__ == "__main__":
    main("patterns.txt")
