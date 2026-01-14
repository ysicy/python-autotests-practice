from faker import Faker

# Устанавливаем seed для воспроизводимости
Faker.seed(42)

# Простая инициализация (английский по умолчанию)
fake = Faker()

# С локализацией (русские данные)
fake_ru = Faker('ru_RU')


# С несколькими провайдерами
fake = Faker()

fake.add_provider('faker.providers.person.ru_RU')
fake.add_provider('faker.providers.address.ru_RU')


def generate_test_users(count=10):
    """Генерация тестовых пользователей для системы"""
    users = []
    for i in range(count):
        user = {
            "id": i + 1, # Уникальный идентификатор, начинается с 1
            "personal_info": {
                "name": fake_ru.name(), # Случайное ФИО на русском
                "birth_date": fake_ru.date_of_birth().isoformat(), # Дата рождения в формате ISO
                "gender": fake_ru.random_element(["M", "F"]), # Пол (М/Ж)
                "documents": {
                    "passport": fake_ru.passport_number(), # Номер паспорта
                    "snils": fake_ru.snils() # Номер СНИЛС
                }
            },
            "contact_info": {
                "email": fake_ru.email(), # Электронная почта
                "phone": fake_ru.phone_number(), # Номер телефона
                "address": fake_ru.address() # Адрес
            },
            "work_info": {
                "company": fake_ru.company(), # Название компании
                "position": fake_ru.job(), # Должность
                "salary": fake_ru.random_int(30000, 200000) # Зарплата от 30к до 200к
            },
            "system_info": {
                "registration_date": fake_ru.date_this_year().isoformat(), # Дата регистрации
                "last_login": fake_ru.date_time_this_month().isoformat(), # Последний вход
                "is_active": fake_ru.boolean(chance_of_getting_true=80) # 80% активных пользователей
            }
        }
        users.append(user)
    return users

# Вывод результата
test_users = generate_test_users(5)
for user in test_users:
    print(f"   {user['personal_info']['name']}")
    print(f"   {user['contact_info']['email']}")
    print(f"   {user['work_info']['position']}")
    print("---")