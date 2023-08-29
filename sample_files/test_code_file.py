
import os
import requests
from math import sqrt

API_KEY = "ABC123DEFG456XYZ"  # Hardcoded API key

def compute_root(x):
    return sqrt(x)

def get_data():
    data = {
        "id": "XYZ789",
        "value": 12345
    }
    return data

def unsafe_eval(input_str):
    return eval(input_str)  # Unsafe use of eval

def fetch_data_from_api(endpoint):
    headers = {
        "Authorization": "Bearer " + API_KEY  # Using the hardcoded API key
    }
    response = requests.get(endpoint, headers=headers)
    return response.json()

configurations = {
    "CORS": "*",  # Overly permissive CORS configuration
    "DEBUG": True,
    "API_ENDPOINT": "https://api.endpoint.com",
    "SECRET": "hjYU78jkKLO90pl"  # Another hardcoded secret
}

class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password  # Storing password in plain text

    def authenticate(self):
        # Placeholder for authentication logic
        pass

def compute_factorial(n):
    if n == 0:
        return 1
    else:
        return n * compute_factorial(n-1)

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def apply_discount(self, percentage):
        self.price = self.price * (1 - (percentage/100))

def fetch_user_data(user_id):
    # Placeholder for a function that fetches user data
    pass

def reset_user_password(user):
    # Placeholder for password reset logic
    pass

class Admin(User):
    def __init__(self, username, password, privileges):
        super().__init__(username, password)
        self.privileges = privileges

def main():
    user_input = input("Enter a value to compute the square root: ")
    print(unsafe_eval(user_input))  # Vulnerable to code injection

if __name__ == "__main__":
    main()

