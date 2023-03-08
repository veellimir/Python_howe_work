# Изменил имя владельца и проценты

class Account:
    # статические методы
    rate_usd = 0.013
    rate_eur = 0.011
    suffix = 'RUB'
    suffix_usd = 'USD'
    suffix_eur = 'EUR'

    def __init__(self, surname, num, percent, value=0):
        self.__surname = surname
        self.num = num
        self.__percent = percent
        self.value = value
        print(f'Счёт #{self.num} принадлежащий {self.__surname} был открыт.')
        print('*' * 50)

    def __del__(self):
        print('*' * 50)
        print(f'Счёт #{self.num} принадлежащий {self.__surname} был закрыт.')

    # Изминение данных через декоратор
    @property
    def surname(self):
        return self.__surname

    @surname.setter
    def surname(self, surname):
        self.__surname = surname

    # Изменение данных через get и set
    def get_percent(self):
        return self.__percent

    def set_percent(self, percent):
        self.__percent = percent

    @staticmethod
    def convert(value, rate):
        return value * rate

    # ЕСЛИ КУРС БУДЕТ МЕНЯТСЯ
    @classmethod
    def set_rate_usd(cls, rate):
        cls.rate_usd = rate

    # ЕСЛИ КУРС БУДЕТ МЕНЯТСЯ
    @classmethod
    def set_rate_eur(cls, rate):
        cls.rate_eur = rate

    # Метод рубль
    def print_balance(self):
        print(f'Текущий баланс {self.value} {Account.suffix}')

    def convert_to_usd(self):
        usd_val = Account.convert(self.value, Account.rate_usd)
        print(f'Состояние счёта: {usd_val} {Account.suffix_usd}')

    def convert_to_eur(self):
        usd_eur = Account.convert(self.value, Account.rate_eur)
        print(f'Состояние счёта: {usd_eur} {Account.suffix_eur}')

    # начисление процентов
    def add_percent(self):
        self.value += self.value * self.__percent
        print(f'Проценты были начисленны {self.__percent}')
        self.print_balance()

    # Снятие денег с счёта
    def withdraw_money(self, val):
        if val > self.value:
            print(f"У вас нет {val} {Account.suffix}")
        else:
            self.value -= val
            print(f'{val} {Account.suffix} Было снято')
        self.print_balance()

    # добавить деньги на счёт
    def add_money(self, val):
        self.value += val
        print(f'Сумма {val} {Account.suffix} была добавленна')
        self.print_balance()


    # метод онфо о счёте
    def print_inf(self):
        print('Инфор о счёте :')
        print(f'#{self.num}')
        print(f'Владелец:{self.__surname}')
        self.print_balance()
        print(f'Проценты: {self.__percent:.0%}')
        print('-' * 20)

acc = Account(num='8954155224', surname='Долгих', percent=0.03, value=1000)
acc.print_balance()
acc.print_inf()

acc.convert_to_usd()
acc.convert_to_eur()
print()

# новый курс
Account.set_rate_usd(2)
acc.convert_to_usd()
Account.set_rate_eur(3)
acc.convert_to_eur()
print()

# смена владельца счёта
acc.surname = 'Васильев'
acc.print_inf()

# Смена значение процентов
acc.set_percent(0.08)
acc.print_inf()

# начисление процентов
acc.add_percent()
print()

# Снятие денег с счёта
acc.withdraw_money(100)
print()
acc.withdraw_money(1000)
print()
# добавить деньги на счёт
acc.add_money(5000)
acc.withdraw_money(1000)
