# utils/registration_data.py
from faker import Faker

faker = Faker()

def generate_data():
    return {
        "first_name": "John",
        "last_name": "Doe",
        "street": "123 Maple Street",
        "city": "Springfield",
        "state": "IL",
        "zip": "62704",
        "phone": "555-123-4567",
        "ssn": "123-45-6789",
        "username": faker.user_name(),
        "password": "Test@1234"
    }