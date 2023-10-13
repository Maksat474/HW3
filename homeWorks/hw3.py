# Задание №1
class Bank:
    def __init__(self, name, balance):
        self._name = name
        self._balance = balance

    def moneyX(self):
        amount = float(input("Введите сумму для добавления на счет: "))
        self._balance += amount

    def kill(self):
        self._balance = 0

    def _jackpot(self):
        self._balance *= 10

    def transfer_balance(self, another_bank):
        if isinstance(another_bank, Bank):
            self._balance += another_bank._balance
            another_bank._balance = 0
        else:
            print("Ошибка!!!")

bank1 = Bank("Максат", 100)
bank2 = Bank("Сыймык", 200)

print(f"{bank1._name} баланс: {bank1._balance}")
print(f"{bank2._name} баланс: {bank2._balance}")

bank1.transfer_balance(bank2)

print(f"{bank1._name} баланс: {bank1._balance}")
print(f"{bank2._name} баланс: {bank2._balance}")


# Задание №2
class Calculator:
    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        return self.value + other.value

    def __sub__(self, other):
        return self.value - other.value

    def __mul__(self, other):
        return self.value * other.value

    def __truediv__(self, other):
        if other.value != 0:
            return self.value / other.value
        else:
            return "Деление на ноль невозможно"

num1 = Calculator(44)
num2 = Calculator(4)

print(f"Сложение: {num1 + num2}")
print(f"Вычитание: {num1 - num2}")
print(f"Умножение: {num1 * num2}")
print(f"Деление: {num1 / num2}")