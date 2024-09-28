class User:                                 # создаём класс User
    def __init__(self, user_id, name):      # инициализация объекта с атрибутами (user_id, name)
        self._user_id = user_id             # Защищенный атрибут ID пользователя
        self._name = name                   # Защищенный атрибут имени пользователя
        self._access_level = 'user'         # Уровень доступа по умолчанию для обычного сотрудника

    def get_user_id(self):                  # Метод для получения ID пользователя.
        return self._user_id

    def set_user_id(self, user_id):         # Метод для изменения ID пользователя.
        self._user_id = user_id

    def get_name(self):                     # Метод для получения имени пользователя.
        return self._name

    def set_name(self, name):               # Метод для изменения имени пользователя.
        self._name = name

    def get_access_level(self):             # Метод для получения уровня доступа пользователя.
        return self._access_level

    def set_access_level(self, access_level): # Метод для изменения уровня доступа пользователя.
        self._access_level = access_level


class Admin(User):                           # создаём дочерний класс Admin
    def __init__(self, user_id, name):       # правильно используем конструктор
        super().__init__(user_id, name)      # Наследуем конструктор из класса User
        self._access_level = 'admin'         # Уровень доступа для администратора

    def add_user(self, user_list, user):     # Метод для добавления нового пользователя в список
        if isinstance(user, User):
            user_list.append(user)
            print(f"Пользователь {user.get_name()} добавлен в систему.")
        else:
            print("Невозможно добавить объект, так как он не является экземпляром класса User.")

    def remove_user(self, user_list, user_id):  # Метод для удаления пользователя из списка по его ID
        for user in user_list:
            if user.get_user_id() == user_id:
                user_list.remove(user)
                print(f"Пользователь с ID {user_id} удален из системы.")
                return
        print(f"Ошибка: Пользователь с ID {user_id} не найден.")


# Пример использования системы управления учетными записями пользователей:

user_list = []                                    # Создаем список пользователей

user1 = User(1, "Сергей Иванов")     # Создаем пользователя 1
user2 = User(2, "Александр Петров")  # Создаем пользователя 2
user3 = User(3, "Василий Литвинов")  # Создаем пользователя 3
user4 = User(4, "Кирил Орда")        # Создаем пользователя 4

admin = Admin(0, "Валерий Попов")    # Создаем администратора

admin.add_user(user_list, user1)                  # Администратор добавляет пользователя 1 в систему
admin.add_user(user_list, user2)                  # Администратор добавляет пользователя 2 в систему
admin.add_user(user_list, user3)                  # Администратор добавляет пользователя 3 в систему
admin.add_user(user_list, user4)                  # Администратор добавляет пользователя 4 в систему

# Пример использования методов для получения и изменения атрибутов пользователей
print("\nИзменение данных пользователя:")

user1.set_user_id(10)                             # Изменение ID пользователя 1
user1.set_name("Сергей Иванович")                 # Изменение имени пользователя 1
user1.set_access_level("manager")                 # Изменение уровня доступа пользователя 1

# Проверяем изменения
print(f"Изменен ID: {user1.get_user_id()}")
print(f"Изменено имя: {user1.get_name()}")
print(f"Изменен уровень доступа: {user1.get_access_level()}")

admin.remove_user(user_list, 1)                   # Администратор пытается удалить пользователя с ID 1
admin.remove_user(user_list, 10)                  # Администратор удаляет пользователя с новым ID

print("\nТекущий список пользователей:")                 # Проверяем состояние списка пользователей
for user in user_list:
    print(f"ID: {user.get_user_id()}, Имя: {user.get_name()}, Уровень доступа: {user.get_access_level()}")