
def check_configurations(file_content):
    if '"*"' in file_content:
        return ["Overly permissive CORS configuration found."]
    return []
