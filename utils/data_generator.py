from faker import Faker

fake = Faker()

def generate_signup_user():
    return {
        "name": fake.first_name(),
        "email": fake.email(),
        "password": "TestPassword123!",
        "first_name": fake.first_name(),
        "last_name": fake.last_name(),
        "company": fake.company(),
        "address1": fake.street_address(),
        "address2": fake.secondary_address(),
        "country": "Canada",
        "state": fake.state(),
        "city": fake.city(),
        "zip_code": fake.postcode(),
        "mobile_number": fake.phone_number()
    }