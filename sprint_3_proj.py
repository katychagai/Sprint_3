import datetime

class OnlineSalesRegisterCollector:
    def __init__(self):
        self.__name_items = []
        self.__number_items = 0
        self.__item_price = {'чипсы': 50, 'кола': 100, 'печенье': 45, 'молоко': 55, 'кефир': 70}
        self.__tax_rate = {'чипсы': 20, 'кола': 20, 'печенье': 20, 'молоко': 10, 'кефир': 10}

    @property
    def name_items(self):
        return self.__name_items
    
    @property
    def number_items(self):
        return self.__number_items

    def add_item_to_cheque(self, name):
        try:
            if len(name) == 0 or len(name) > 40:
                raise ValueError('Нельзя добавить товар, если в его названии нет символов или их больше 40')
            
            if name not in self.__item_price:
                raise NameError('Позиция отсутствует в товарном справочнике')
            
            self.__name_items.append(name)
            self.__number_items += 1

            print(f"Товар '{name}' успешно добавлен в чек")
        except (ValueError, NameError) as e:
            print(f"Ошибка при добавлении товара: {e}")

    def delete_item_from_check(self, name):
        try:
            if name not in self.__name_items:
                raise NameError('Позиция отсутствует в чеке')
            
            self.__name_items.remove(name)
            self.__number_items -= 1

            print(f"Товар '{name}' успешно удален из чека")
        except NameError as e:
            print(f"Ошибка при удалении товара: {e}")

    def check_amount(self):
        total = 0

        for item in self.__name_items:
            total += self.__item_price[item]
        
        if self.__number_items > 10:
            total *= 0.9  
        
        return total
        
    def twenty_percent_tax_calculation(self):
        twenty_percent_tax = []
        total = []

        for item in self.__name_items:
            if self.__tax_rate[item] == 20:
                twenty_percent_tax.append(item)
                total.append(self.__item_price[item])

        sum_total = sum(total)
        
        if self.__number_items > 10:
            sum_total *= 0.9

        return sum_total * 0.2
        
    def ten_percent_tax_calculation(self):
        ten_percent_tax = []
        total = []

        for item in self.__name_items:
            if self.__tax_rate[item] == 10:
                ten_percent_tax.append(item)
                total.append(self.__item_price[item])

        sum_total = sum(total)

        if self.__number_items > 10:
            sum_total *= 0.9
        
        return sum_total * 0.1
        
    def total_tax(self):
        nds = self.twenty_percent_tax_calculation() + self.ten_percent_tax_calculation()

        return nds
        
    @staticmethod
    def get_telephone_number(telephone_number):
        try:
            if not isinstance(telephone_number, int):
                raise ValueError('Необходимо ввести цифры')

            if len(str(telephone_number)) > 10:
                raise ValueError('Необходимо ввести 10 цифр после "+7"')
            
            return f"+7{telephone_number}"
        except ValueError as e:
            return (f"Ошибка в номере телефона: {e}")

    @staticmethod
    def get_date_and_time():
        now = datetime.datetime.now()
        date_and_time = []
        date = [
            ['часы', lambda x: x.hour], 
            ['минуты', lambda x: x.minute], 
            ['день', lambda x: x.day],
            ['месяц', lambda x: x.month],
            ['год', lambda x: x.year] 
            ]
        
        for name, func in date:
            date_and_time.append(f'{name}: {func(now)}')

        return date_and_time

register = OnlineSalesRegisterCollector()
register.add_item_to_cheque('кола')
register.add_item_to_cheque('мороженко')
register.add_item_to_cheque('молоко')
register.add_item_to_cheque('кефир')
register.add_item_to_cheque('очень длинное название товара которого нет в справочнике')
print("Чек:", register.name_items)
register.delete_item_from_check('Молоко')
register.delete_item_from_check('молоко')
print("Чек:", register.name_items)
print("Сумма чека:", register.check_amount())
print("НДС 20%:", register.twenty_percent_tax_calculation())
print("НДС 10%:", register.ten_percent_tax_calculation())
print("Общий НДС:", register.total_tax())
  
print(f'Телефон: {register.get_telephone_number(9087689790)}')
print(f'Телефон: {register.get_telephone_number('9087689790')}')
print(f'Телефон: {register.get_telephone_number(908768979)}')
print(f'Телефон: {register.get_telephone_number(90876897901)}')

print(f'Дата: {register.get_date_and_time()}')