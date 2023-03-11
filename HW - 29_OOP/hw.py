# Общий класс студент
class Student:
    def __init__(self, name):
        self.name = name
        self.notebook = self.Notebook()

    # Информация о студенте и ноутбуке (берёт из class Notebook)
    def print_info(self):
        print(self.name, end=' ')
        self.notebook.print_info()

    class Notebook:
        def __init__(self):
            self.model = 'LG'
            self.cpu = 'I5'
            self.ozu = '16GB'

        def print_info(self):
            print(f' => Модель : {self.model}, Процессор : {self.cpu}, Оперативная память : {self.ozu}')


result = Student('Ярослав')
result.print_info()

result2 = Student('Игнат')
result2.print_info()
