# Вложенные условия
print("=== Вложенные условия ===")

# Анализ домашнего задания - отличник
student_name = "Анна"
subject = "Математика"
score = 5
submission_time = "вовремя"

print(f"Домашнее задание: {student_name}")
print(f"Предмет: {subject}")
print(f"Оценка: {score}")
print(f"Время сдачи: {submission_time}")

if score >= 4:
    print("✅ Задание выполнено хорошо")

    if score == 5:
        print("  🌟 Отличная работа!")
        if submission_time == "вовремя":
            print("    🎯 Сдано в срок - молодец!")
        else:
            print("    ⏰ Сдано с опозданием, но качество отличное")
    else:
        print("  👍 Хорошая работа!")
        if submission_time == "вовремя":
            print("    ✅ Сдано в срок")
        else:
            print("    ⚠️ Сдано с опозданием")

elif score >= 3:
    print("⚠️ Задание выполнено удовлетворительно")
elif score >= 2:
    print("❌ Задание выполнено плохо")
else:
    print("💥 Задание не выполнено")