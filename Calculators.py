import datetime as dt


class Calculator:
    def __init__(self, limit):
        self.limit = limit
        self.records = []

    def add_record(self, rec):
        self.records.append(rec)

    def get_today_stats(self):
        today_counter = 0
        for rec in self.records:
            if rec.date == dt.datetime.now().date():
                today_counter += rec.amount
        return today_counter

    def get_week_stats(self):
        week_counter = 0
        today_date = dt.datetime.now().date()
        week_range = today_date - dt.timedelta(7)
        for rec in self.records:
            if week_range <= rec.date <= today_date:
                week_counter += rec.amount
        return week_counter


class Record:
    def __init__(self, amount, comment, date=''):
        self.amount = amount
        self.comment = comment
        if date == '':
            self.date = dt.datetime.now().date()
        else:
            self.date = dt.datetime.strptime(date, '%d.%m.%Y').date()


class CashCalculator(Calculator):
    EURO_rate = 90.00
    DOLLAR_rate = 80.00

    def __init__(self, limit):
        super().__init__(limit)

    def get_today_cash_remained(self, currency):
        currencies = ['rub', 'usd', 'eur']
        today_counter = self.get_today_stats()
        diff = abs(self.limit - today_counter)
        if currency in currencies:
            if today_counter < self.limit:
                if currency == 'rub':
                    return f'На сегодня осталось {diff} {currency}'
                elif currency == 'usd':
                    diff = round(diff/self.DOLLAR_rate, 2)
                    return f'На сегодня осталось {diff} {currency}'
                elif currency == 'eur':
                    diff = round(diff / self.EURO_rate, 2)
                    return f'На сегодня осталось {diff} {currency}'
            elif today_counter == self.limit:
                return "Денег нет, держись"
            else:
                if currency == 'rub':
                    return f'Денег нет, держись: твой долг - {diff} {currency}'
                elif currency == 'usd':
                    diff = round(diff/self.DOLLAR_rate, 2)
                    return f'Денег нет, держись: твой долг - {diff} {currency}'
                elif currency == 'eur':
                    diff = round(diff / self.EURO_rate, 2)
                    return f'Денег нет, держись: твой долг - {diff} {currency}'
        else:
            return f'Валюта "{currency}" не принимается'


class CaloriesCalculator(Calculator):
    def __init__(self, limit):
        super().__init__(limit)

    def get_calories_remained(self):
        today_counter = self.get_today_stats()
        diff = abs(self.limit - today_counter)
        if today_counter < self.limit:
            return f'Сегодня можно съесть что-нибудь ещё, но с общей калорийностью не более {diff} кКал'
        else:
            return "Хватит есть!"


# cal_calc = CaloriesCalculator(1000)
# r4 = Record(amount=0, comment="Кусок тортика. И ещё один.")
# r5 = Record(amount=2999, comment="Йогурт.")
# r6 = Record(amount=0, comment="Баночка чипсов.", date="24.02.2019")
# cal_calc.add_record(r4)
# cal_calc.add_record(r5)
# cal_calc.add_record(r6)
#
#
# cash_calculator = CashCalculator(1000)
# cash_calculator.add_record(Record(amount=999, comment="кофе"))
# cash_calculator.add_record(Record(amount=0, comment="Серёге за обед"))
# cash_calculator.add_record(Record(amount=3000, comment="бар в Танин др", date="10.10.2020"))
#
# print(cal_calc.get_today_stats())
# print(cash_calculator.get_today_stats())
# print(cal_calc.get_calories_remained())
# print(cash_calculator.get_today_cash_remained("eur"))
#
# print(cash_calculator.get_week_stats())
# print(cal_calc.get_week_stats())