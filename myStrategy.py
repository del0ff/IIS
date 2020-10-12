class Сelsius:
    def temp(self, value):
        return f'{value} °C'

class Fahrenheit:
    def temp(self, value):
        return f'{value} °F'


class Temperature:
    def set_strategy(self, strategy):
        self.strategy = strategy
    def temperature(self, value):
        print('Strategy', self.strategy.temp(value))


temp = Temperature()

value = int(input('Введите значение температуры: '))

strategy = input('Введите единицу измерения (c, f):')

if strategy == 'c':
    temp.set_strategy(Сelsius())
elif strategy == 'f':
    temp.set_strategy(Fahrenheit())


temp.temperature(value)
