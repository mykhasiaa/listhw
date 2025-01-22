filmy = ["film nomer 1", "фільм номер 2"]

# варіанти
print("Список фільмів")
print("1. Додати фільм")
print("2. Переглянути список фільмів")
print("3. Видалити фільм")

# додати
choice = input("Оберіть варіант: ")
if choice == '1':
    add = input("Який фільм ви хочете додати до списку?\n")
    filmy.append(add)
    print(f"Фільм {add} додано до списку!")
    print(f"Оновлений список: {filmy}")

# переглянути
elif choice == '2':
    print(f"Список фільмів: {filmy}")

# видалити
elif choice == '3':
    delete = input("Який фільм ви хочете видалити зі списку?\n")
    filmy.remove(delete)
    print(f"Фільм {delete} видалено зі списку!")
    print(f"Оновлений список: {filmy}")

# ну йой
else:
    print("Я б тут цикл додала, але сорі, наступного разу")