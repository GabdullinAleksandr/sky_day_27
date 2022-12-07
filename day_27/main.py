class Bottle:
    def __init__(self, color, volume):
        self.volume = volume
        self.color = color


# bottle_1 = Bottle('Красная', 0.7)
# bottle_2 = Bottle('Белая', 0.3)
# bottle_3 = Bottle('Черная', 1.0)


class Bottle_fill(Bottle):
    def __init__(self, color, volume):
        super().__init__(color, volume)
        self.contains = 0

    def get_content(self):
        return self.contains

    def fill(self, value):
        self.contains = value


# bottle_1 = Bottle_fill('Красная', 0.7)
# bottle_2 = Bottle_fill('Синяя', 0.5)
# print(bottle_1.color, bottle_1.get_content())
# bottle_1.fill(100)
# print(bottle_1.color, bottle_1.get_content())
#
# print(bottle_2.color, bottle_2.get_content())
# bottle_2.fill(500)
# print(bottle_2.color, bottle_2.get_content())


class Todolist:
    def __init__(self):
        self.tasks = []

    def add_task(self, *args):
        [self.tasks.append(i) for i in args]


# todo_list = Todolist()
# todo_list.add_task('Купить лампочку', 'Поменять лампочку', 'Выкинуть лампочку')
# print("\n".join(todo_list.tasks))


class DataBase:
    object_reference = 0

    def __new__(cls, *args, **kwargs):
        if DataBase.object_reference == 0:
            return super().__new__(cls)
        else:
            return DataBase.object_reference

    def __init__(self, user, psw, port):
        self.user = user
        self.psw = psw
        self.port = port
        DataBase.object_reference = self

    def connect(self):
        print(f"соединение с БД: {self.user}, {self.psw}, {self.port}")

    def close(self):
        print("закрытие соединения с БД")

    def read(self):
        return "данные из БД"

    def write(self, data):
        print(f"запись в БД {data}")


# db = DataBase('root', '1234', 80)
# db2 = DataBase('root2', '5678', 40)
# print(db is db2)
