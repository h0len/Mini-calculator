import sys

def calculate(first_number, operationn, second_number):
    """Функция, принимающая три значения: первое число, операцию и второе число. Она определяет, какую операцию нужно сделать и выполняет ее."""
    try:
        if operationn == "плюс":
            return undo_helper_of_determinator((determinator_of_number(first_number)) + determinator_of_number(second_number))
        elif operationn == "минус":
            return undo_helper_of_determinator((determinator_of_number(first_number)) - determinator_of_number(second_number))
        elif operationn == "разделить":
            print(first_number, second_number, determinator_of_number(first_number), determinator_of_number(second_number), (determinator_of_number(first_number)) / determinator_of_number(second_number))
            return undo_helper_of_determinator((determinator_of_number(first_number)) / determinator_of_number(second_number))
        else:
            return undo_helper_of_determinator((determinator_of_number(first_number)) * determinator_of_number(second_number))
    except TypeError:
        print("Изначально были неправильно введены значения!")
        sys.exit(0)

def from_list_to_string(list):
    """Функция для перевода списка в строку."""
    string_ = ""
    for element in list:
        string_ += element
    return string_

def from_list_to_integer(list):
    """Функция для перевода списка в целочисленный формат."""
    for element in list:
        return int(element)

def helper_of_determinator(listt):
    """Функция для составления списка из одного элемента. В данной программе, она возвращает число(первое или второе), которое было введено пользователем."""
    return list(filter(None, [numbers_from_0_to_9.get(from_list_to_string(listt)),
                              numbers_from_10_to_19.get(from_list_to_string(listt)),
                              numbers_mod10_equal_zero.get(from_list_to_string(listt))]))

def determinator_of_operation(list):
    """Функция для определения операции, и возврата ее."""
    for word in list:
        if word in operations:
            operation = word
            break
    return operation

def determinator_of_number(number):     #Принимает список
    """Функция для перевода числа из списка в целочисленный формат."""
    if len(number) == 1:
        if number[0] == "ноль":
            return 0
        else:
            return (from_list_to_integer(helper_of_determinator(number)))
    else:
        if "минус" in number:
            number.remove("минус")
            if len(number) == 2:
                number_split_first_part, number_split_second_part = [str(word) for word in number]
                return (-from_list_to_integer(helper_of_determinator(number_split_first_part)) - from_list_to_integer(helper_of_determinator(number_split_second_part)))
            else:
                number_split_first_part = [str(word) for word in number]
                return (-from_list_to_integer(helper_of_determinator(number_split_first_part)))
        else:
            number_split_first_part, number_split_second_part = [str(word) for word in number]
            return (from_list_to_integer(helper_of_determinator(number_split_first_part)) + from_list_to_integer(helper_of_determinator(number_split_second_part)))

def get_key_by_value(dictionary, value):
    """Функция для получения ключа по значению в словаре."""
    for key, v in dictionary.items():
        if v == value:
            return key
    return None

def undo_helper_of_determinator_for_integers_until_1000(integer):
    if integer == 0:
        return "ноль"
    if 1 <= integer < 20:
        return " ".join(list(filter(None, [get_key_by_value(numbers_from_0_to_9, integer), get_key_by_value(numbers_from_10_to_19, integer)])))
    if 20 <= integer < 100:
        return " ".join(list(filter(None, [get_key_by_value(numbers_mod10_equal_zero, (integer - (integer % 10))), get_key_by_value(numbers_from_0_to_9, (integer % 10))])))
    if 100 <= integer < 1000:
        return " ".join(list(filter(None, [get_key_by_value(numbers_mod100_equal_zero, integer - (integer % 100)), get_key_by_value(numbers_mod10_equal_zero, ((integer - ((integer // 100) * 100) - integer % 10))), get_key_by_value(numbers_from_0_to_9, (integer % 10))])))

def undo_helper_of_determinator(integer_or_float):
    """Функция для перевода числа из целочисленного формата в текстовый."""
    result = ""
    if int(integer_or_float) != (integer_or_float):
        str_integer_or_float = str(integer_or_float)
        integer_part, decimal_part = str_integer_or_float.split('.')
        integer_part = int(integer_part)
        if integer_part == 0:
            result += "ноль"
        elif 1 <= integer_part < 20:
            result +=  " ".join(list(filter(None, [get_key_by_value(numbers_from_0_to_9, integer_part),
                                               get_key_by_value(numbers_from_10_to_19, integer_part)])))
        elif 20 <= integer_part < 100:
            result += " ".join(list(filter(None, [get_key_by_value(numbers_mod10_equal_zero, (integer_part - (integer_part % 10))),
                                               get_key_by_value(numbers_from_0_to_9, integer_part % 10)])))
        elif 100 <= integer_part < 1000:
            result += " ".join(list(filter(None, [get_key_by_value(numbers_mod100_equal_zero, integer_part // 100),
                                               get_key_by_value(numbers_mod10_equal_zero, (integer_part - ((integer_part // 100) * 100) - (integer_part % 10))),
                                               get_key_by_value(numbers_from_0_to_9, (integer_part % 10))])))
        if len(decimal_part) <= 3:
            decimal_part = decimal_part.ljust(3, '0')
            if len(decimal_part) == 1 or decimal_part[1:] == "00":
                result += f" и {undo_helper_of_determinator_for_integers_until_1000(int(decimal_part[0]))} десятая(ых)"
            elif len(decimal_part) == 2 or decimal_part[2] == "0":
                result += f" и {undo_helper_of_determinator_for_integers_until_1000(int(decimal_part[:2]))} сотая(ых)"
            else:
                result += f" и {undo_helper_of_determinator_for_integers_until_1000(int(decimal_part))} тысячная(ых)"
        else:
            decimal_part = decimal_part[:3]
            result += f" и {undo_helper_of_determinator_for_integers_until_1000(int(decimal_part))} тысячная(ых)"
        return result
    else:
        return undo_helper_of_determinator_for_integers_until_1000(integer_or_float)

#Как вообще задавать число?
numbers_from_0_to_9 = {"ноль":0, "один":1, "два":2,
                        "три":3, "четыре":4, "пять":5,
                        "шесть":6, "семь":7, "восемь":8,
                        "девять":9}

numbers_from_10_to_19 = {"десять":10, "одиннадцать":11, "двенадцать":12,
                         "тринадцать":13,"четырнадцать":14, "пятнадцать":15,
                         "шестнадцать":16,"семнадцать":17, "восемнадцать":18,
                         "девятнадцать":19}

numbers_mod10_equal_zero = {"двадцать":20, "тридцать":30, "сорок":40,
                            "пятьдесят":50,"шестьдесят":60, "семьдесят":70,
                            "восемьдесят":80, "девяносто":90}

numbers_used_in_float = {"ноль":0, "одна":1, "две":2, "три":3,
                         "четыре":4, "пять":5, "шесть":6,
                         "семь":7, "восемь":8, "девять":9}

numbers_mod100_equal_zero = {"сто":100, "двести":200, "триста":300,
                             "четыреста":400, "пятьсот":500, "шестьсот":600,
                             "семьсот":700, "восемьсот":800, "девятьсот":900}

operations = ["плюс", "минус", "умножить", "разделить"]

print("Добро пожаловать в калькулятор! Введите выражение в формате: {первое число} {операция} {второе число}\nПример: \"двадцать три минус девятнадцать\"")
flag = False
while flag == False:
    expression = input().lower()
    words = list(filter(None, expression.split(" ")))
    if (words.count("плюс") + words.count("минус") + words.count("умножить") + words.count("разделить") == 1):
        operation = determinator_of_operation(words)
        index_of_operation = words.index(operation)
        first_num = words[:index_of_operation]
        second_num = words[(index_of_operation + 1):]
        if ((2 <= len(first_num) + len(second_num) <= 4) and (operation is not None) and (len(first_num) != 0) and (len(second_num) != 0)):
            flag = True
            if ((operation == "разделить") and (from_list_to_string(second_num) == "ноль")):
                flag = False
                print("Делить на ноль нельзя! Введите запрос корректно: ")
    elif (words.count("плюс") + words.count("минус") + words.count("умножить") + words.count("разделить") == 2) and (words.count("минус") > 0):
        operation = determinator_of_operation(words)
        index_of_operation = words.index(operation)
        first_num = words[:index_of_operation]
        second_num = words[(index_of_operation + 1):]
        if ((3 <= len(first_num) + len(second_num) <= 5) and (operation is not None) and (len(first_num) != 0) and (len(second_num) != 0)):
            flag = True
            if ((operation == "разделить") and (from_list_to_string(second_num) == "ноль")):
                flag = False
                print("Делить на ноль нельзя! Введите запрос корректно: ")
    else:
        print("Неправильный формат ввода! Введите еще раз: ")

print(f"Ваш результат: {calculate(first_num, operation, second_num)}")

#ДОП ЗАДАНИЯ - 5, 1(пока что нет)
