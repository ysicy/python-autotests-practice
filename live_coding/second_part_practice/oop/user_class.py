import json

from faker import Faker

class User:
    def __init__(self, id, name, email, age):
        self.id = id
        self.name = name
        self.email = email
        self.age = age

    @classmethod
    def generate_random(cls):
        """Генерим пользователя со случайными данными"""
        faker = Faker()
        return cls(
            id = faker.random_int(1, 100),
            name = faker.first_name(),
            email = faker.email(),
            age = faker.random_int(18,65))


    def validate_structure(self):
        messages = []

        if self.age <= 0:
            messages.append(f"Invalid age, {self.age}")

        if '@' not in self.email:
            messages.append(f"Invalid email, {self.email}")

        if "." not in self.email:
            messages.append(f"Invalid email, {self.email}")

        if self.name.islower():
            messages.append(f"Invalid name, {self.name}")

        is_validate = len(messages) == 0
        return is_validate, messages

    def to_dict(self):
        """Convert to Dictionaries"""
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email,
            'age': self.age,
        }

    def to_json(self):
        """Convert to Json"""
        return json.dumps(self.to_dict(), indent=4)


random_user = User.generate_random()
print(random_user.to_dict())

user = User(0, "AlexTester", "alextest@mail.su", -18)
is_valid, messages = user.validate_structure()
print(f"Valid: {is_valid}, Messages: {messages}")
print(user.to_json())

user2 = User(4,"alex","a@emailru",-3)
is_valid, messages = user2.validate_structure()
print(f"Valid: {is_valid}, Messages: {messages}")


