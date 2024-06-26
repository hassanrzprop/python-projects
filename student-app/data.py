import random
from faker import Faker

fake = Faker()

students = []

for i in range(1, 6):
    student = {
        'id': f"{i}",
        'name': fake.name(),
        'email': fake.email(),
        'roll_no': random.randint(1, 100),
        'class': random.choice(['10th', '11th', '12th'])
    }
    students.append(student)