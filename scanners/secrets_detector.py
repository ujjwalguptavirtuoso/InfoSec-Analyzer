
import re

def detect_secrets(file_content):
    pattern = r"[A-Za-z0-9]{32}" 
    return re.findall(pattern, file_content)
