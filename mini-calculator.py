import sys

def calculate(first_number, operation, second_number):
    """Функция, принимающая три значения: первое число, операцию и второе число. Она определяет, какую операцию нужно сделать и выполняет ее."""
    try:
        if operation == "плюс":
            if (determinator_of_number(first_number)) + determinator_of_number(second_number) < 0:
                return "минус " + undo_helper_of_determinator((determinator_of_number(first_number)) + determinator_of_number(second_number))
            else:
                return undo_helper_of_determinator((determinator_of_number(first_number)) + determinator_of_number(second_number))
        elif operation == "минус":
            if (determinator_of_number(first_number)) - determinator_of_number(second_number) < 0:
                return "минус " + undo_helper_of_determinator(abs((determinator_of_number(first_number)) - determinator_of_number(second_number)))
            else:
                return undo_helper_of_determinator((determinator_of_number(first_number)) - determinator_of_number(second_number))
        elif operation == "разделить":
            if (determinator_of_number(first_number)) / determinator_of_number(second_number) < 0:
                return "минус " + undo_helper_of_determinator(abs((determinator_of_number(first_number)) / determinator_of_number(second_number)))
            else:
                return undo_helper_of_determinator((determinator_of_number(first_number)) / determinator_of_number(second_number))
        elif operation == "умножить":
            if (determinator_of_number(first_number)) * (determinator_of_number(second_number)) < 0:
                return "минус " + undo_helper_of_determinator(abs((determinator_of_number(first_number)) * (determinator_of_number(second_number))))
            else:
                return undo_helper_of_determinator((determinator_of_number(first_number)) * (determinator_of_number(second_number)))
        else:
            if (determinator_of_number(first_number)) % (determinator_of_number(second_number)) < 0:
                return "минус " + undo_helper_of_determinator(abs((determinator_of_number(first_number)) % (determinator_of_number(second_number))))
            else:
                return undo_helper_of_determinator((determinator_of_number(first_number)) % (determinator_of_number(second_number)))
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
    return list(set(filter(None, [numbers_from_0_to_9.get(from_list_to_string(listt)),
                              numbers_used_in_thousands.get(from_list_to_string(listt)),
                              numbers_from_10_to_19.get(from_list_to_string(listt)),
                              numbers_mod10_equal_zero.get(from_list_to_string(listt)),
                              numbers_mod100_equal_zero.get(from_list_to_string(listt))])))


def determinator_of_operation(list):
    """Функция для определения операции, и возврата ее."""
    for word in list:
        if word in operations:
            operation = word
            break
    return operation

def decimal_part_determinator(list):
    tenth = ["десятых", "десятая", "десятые"]
    hundr = ["сотых", "сотая", "сотые"]
    thous = ["тысячных", "тысячная", "тысячные"]
    while True:
        for element in tenth:
            for elem in list:
                if element == elem:
                    list.remove(elem)
                    return determinator_of_number(list) / 10
        for element in hundr:
            for elem in list:
                if element == elem:
                    list.remove(elem)
                    return determinator_of_number(list) / 100
        for element in thous:
            for elem in list:
                if element == elem:
                    list.remove(elem)
                    return determinator_of_number(list) / 1000
        print("Неверное задана десятичная часть!")
        sys.exit(0)

def determinator_of_number(number):
    """Функция для перевода числа из списка в целочисленный формат."""
    if len(number) == 1:
        if number[0] == "ноль":
            return 0
        else:
            return (from_list_to_integer(helper_of_determinator(number)))
    else:
        if "минус" in number:
            if "и" in number:
                number_first_part, number_second_part = number[1:number.index("и")], number[number.index("и") + 1:]
                number_second_part_int = -decimal_part_determinator(number_second_part)
                if number_first_part == 1:
                    number_first_part_int = -from_list_to_integer(helper_of_determinator(number_first_part))
                    return number_first_part_int + number_second_part_int
                else:
                    number_first_first_part = number_first_part[0]
                    number_first_second_part = number_first_part[1]
                    number_first_first_part_int = -from_list_to_integer(helper_of_determinator(number_first_first_part))
                    number_first_second_part_int = -from_list_to_integer(
                        helper_of_determinator(number_first_second_part))
                    return number_first_first_part_int + number_first_second_part_int + number_second_part_int
            else:
                if len(number[1:]) == 2:
                    number_split_first_part, number_split_second_part = [str(word) for word in number[1:]]
                    return (-from_list_to_integer(helper_of_determinator(number_split_first_part)) - from_list_to_integer(helper_of_determinator(number_split_second_part)))
                else:
                    number_split_first_part = [str(word) for word in number[1:]]
                    return (-from_list_to_integer(helper_of_determinator(number_split_first_part)))
        else:
            if "и" in number:
                number_first_part, number_second_part = number[:number.index("и")], number[number.index("и") + 1:]
                number_second_part_int = decimal_part_determinator(number_second_part)
                if number_first_part == 1:
                    number_first_part_int = from_list_to_integer(helper_of_determinator(number_first_part))
                    return number_first_part_int + number_second_part_int
                else:
                    number_first_first_part = number_first_part[0]
                    number_first_second_part = number_first_part[1]
                    number_first_first_part_int = (from_list_to_integer(helper_of_determinator(number_first_first_part)))
                    number_first_second_part_int = from_list_to_integer(helper_of_determinator(number_first_second_part))
                    return number_first_first_part_int + number_first_second_part_int + number_second_part_int
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
    """Функция для перевода чисел из целочисленного формата в текстовый."""
    if integer == 0:
        return "ноль"
    if 1 <= integer < 20:
        return " ".join(list(filter(None, [get_key_by_value(numbers_from_0_to_9, integer), get_key_by_value(numbers_from_10_to_19, integer)])))
    if 20 <= integer < 100:
        if integer % 10 == 0:
            return " ".join(list(filter(None, [get_key_by_value(numbers_mod10_equal_zero, (integer - (integer % 10)))])))
        else:
            return " ".join(list(filter(None, [get_key_by_value(numbers_mod10_equal_zero, (integer - (integer % 10))), get_key_by_value(numbers_from_0_to_9, (integer % 10))])))
    if 100 <= integer < 1000:
        if len(list(filter(None, [get_key_by_value(numbers_mod100_equal_zero, int(str(integer)[0])), get_key_by_value(numbers_mod10_equal_zero, ((integer % 100) - (integer % 10))), get_key_by_value(numbers_from_0_to_9, int(str(integer)[2]))]))) > 1 and (integer % 10 == 0):
            return " ".join(list(filter(None, [get_key_by_value(numbers_mod100_equal_zero, int(str(integer)[0])), get_key_by_value(numbers_mod10_equal_zero, (integer % 100) - (integer % 10))])))
        else:
            return " ".join(list(filter(None, [get_key_by_value(numbers_mod100_equal_zero, int(str(integer)[0])), get_key_by_value(numbers_mod10_equal_zero, (integer % 100) - (integer % 10)), get_key_by_value(numbers_from_0_to_9, (integer % 10))])))
    if 1000 <= integer < 10000:
        if (len(list(filter(None, [get_key_by_value(numbers_used_in_thousands, int(str(integer)[0])), get_key_by_value(numbers_mod100_equal_zero, int(str(integer)[1])), get_key_by_value(numbers_mod10_equal_zero, int(str(integer)[1:]) - integer % 10 - int(str(integer)[1]) * 100), get_key_by_value(numbers_from_0_to_9, int(str(integer)[3]))]))) > 1) and (integer % 10 == 0):
            return " ".join(list(filter(None, [get_key_by_value(numbers_to_thousands, int(str(integer)[0])), get_key_by_value(numbers_mod100_equal_zero, int(str(integer)[1])), get_key_by_value(numbers_mod10_equal_zero, int(str(integer)[1:]) - integer % 10 - int(str(integer)[1]) * 100)])))
        else:
            return " ".join(list(filter(None, [get_key_by_value(numbers_to_thousands, int(str(integer)[0])), get_key_by_value(numbers_mod100_equal_zero, int(str(integer)[1])), get_key_by_value(numbers_mod10_equal_zero, int(str(integer)[1:]) - integer % 10 - int(str(integer)[1]) * 100), get_key_by_value(numbers_from_0_to_9, int(str(integer)[3]))])))

def undo_helper_of_determinator(integer_or_float):
    """Функция для определения формата числа, перевода его в текстовый, если это число с плавающей запятой, и вызов функции для перевода его в текстовый, если это целочисленный формат."""
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
            if integer_part % 10 == 0:
                result += " ".join(list(filter(None, [get_key_by_value(numbers_mod10_equal_zero, (integer_part - (integer_part % 10)))])))
            else:
                result += " ".join(list(filter(None, [get_key_by_value(numbers_mod10_equal_zero, (integer_part - (integer_part % 10))),
                                                      get_key_by_value(numbers_from_0_to_9, integer_part % 10)])))
        elif 100 <= integer_part < 1000:
            if integer_part % 10 == 0:
                result += " ".join(list(filter(None, [get_key_by_value(numbers_mod100_equal_zero, int(str(integer_part)[0])),
                                                      get_key_by_value(numbers_mod10_equal_zero, ((integer_part % 100) - (integer_part % 10)))])))
            else:
                result += " ".join(list(filter(None, [get_key_by_value(numbers_mod100_equal_zero, int(str(integer_part)[0])),
                                                      get_key_by_value(numbers_mod10_equal_zero, ((integer_part % 100) - (integer_part % 10))),
                                                      get_key_by_value(numbers_from_0_to_9, (integer_part % 10))])))
        elif 1000 <= integer_part < 10000:
                if (len(list(filter(None, [get_key_by_value(numbers_used_in_thousands, int(str(integer_part)[0])), get_key_by_value(numbers_mod100_equal_zero, int(str(integer_part)[1])), get_key_by_value(numbers_mod10_equal_zero, int(str(integer_part)[1:]) - integer_part % 10), get_key_by_value(numbers_from_0_to_9, int(str(integer_part)[3]))]))) > 1) and (integer_part % 10 == 0):
                    result +=  " ".join(list(filter(None, [get_key_by_value(numbers_to_thousands, int(str(integer_part)[0])),
                                                           get_key_by_value(numbers_mod100_equal_zero, int(str(integer_part)[1])),
                                                           get_key_by_value(numbers_mod10_equal_zero, int(str(integer_part)[1:]) - integer_part % 10 - int(str(integer_part)[1]) * 100)])))
                else:
                    result += " ".join(list(filter(None, [get_key_by_value(numbers_to_thousands, int(str(integer_part)[0])),
                                                          get_key_by_value(numbers_mod100_equal_zero, int(str(integer_part[1]))),
                                                          get_key_by_value(numbers_mod10_equal_zero, int(str(integer_part)[1:]) - integer_part % 10 - int(str(integer_part)[1]) * 100),
                                                          get_key_by_value(numbers_from_0_to_9,int(str(integer_part)[3]))])))
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

#минус число операция минус число, числа двузначные

#Как вообще задавать число?
numbers_from_0_to_9 = {"ноль": 0,"один": 1, "два": 2,
                        "три": 3, "четыре": 4, "пять": 5,
                        "шесть": 6, "семь": 7, "восемь": 8,
                        "девять": 9}

numbers_from_10_to_19 = {"десять": 10, "одиннадцать": 11, "двенадцать": 12,
                         "тринадцать": 13,"четырнадцать": 14, "пятнадцать": 15,
                         "шестнадцать": 16,"семнадцать": 17, "восемнадцать": 18,
                         "девятнадцать": 19}

numbers_mod10_equal_zero = {"двадцать": 20, "тридцать": 30, "сорок": 40,
                            "пятьдесят": 50,"шестьдесят": 60, "семьдесят": 70,
                            "восемьдесят": 80, "девяносто": 90}

numbers_used_in_thousands = {"ноль": 0, "одна": 1, "две": 2, "три": 3,
                         "четыре": 4, "пять": 5, "шесть": 6,
                         "семь": 7, "восемь": 8, "девять": 9}

numbers_mod100_equal_zero = {"сто": 1, "двести": 2, "триста": 3,
                             "четыреста": 4, "пятьсот": 5, "шестьсот": 6,
                             "семьсот": 7, "восемьсот": 8, "девятьсот": 9}

numbers_to_thousands = {"одна тысяча": 1, "две тысячи": 2, "три тысячи": 3,
                        "четыре тысячи": 4, "пять тысяч": 5, "шесть тысяч": 6,
                        "семь тысяч": 7, "восемь тысяч": 8, "девять тысяч": 9}

operations = ["плюс", "минус", "умножить", "разделить", "остаток"]

print("Добро пожаловать в калькулятор! Введите выражение в формате: {первое число} {операция} {второе число}\nПример: \"двадцать три минус девятнадцать\"")
flag = False
while flag == False:
    expression = input().lower()
    words = list(filter(None, expression.split(" ")))
    if (words.count("плюс") + words.count("минус") + words.count("умножить") + words.count("разделить") + words.count("остаток")== 1):
        operation = determinator_of_operation(words)
        index_of_operation = words.index(operation)
        first_num = words[:index_of_operation]
        second_num = words[(index_of_operation + 1):]
        if ((2 <= len(first_num) + len(second_num) <= 14) and (operation is not None) and (0 < len(first_num) < 8) and (0 < len(second_num) < 8)):
            flag = True
            if ((operation == "разделить" or operation == "остаток") and (from_list_to_string(second_num) == "ноль")):
                flag = False
                print("Делить на ноль нельзя! Введите запрос корректно: ")
        else:
            print("Неправильный формат ввода! Введите еще раз: ")
    elif (words.count("плюс") + words.count("минус") + words.count("умножить") + words.count("разделить") + words.count("остаток") >= 2) and (words.count("минус") > 0):
        if words.index("минус") == 0:
            operation = determinator_of_operation(words[1:])
            index_of_operation = words[1:].index(operation) + 1
            first_num = words[:index_of_operation]
            second_num = words[(index_of_operation + 1):]
        else:
            operation = determinator_of_operation(words)
            index_of_operation = words.index(operation)
            first_num = words[:index_of_operation]
            second_num = words[(index_of_operation + 1):]
        if (3 <= len(first_num) + len(second_num) <= 16) and (operation is not None) and (0 < len(first_num) < 9) and (0 < len(second_num) < 9):
            flag = True
            if (operation == "разделить" or operation == "остаток") and (from_list_to_string(second_num) == "ноль"):
                flag = False
                print("Делить на ноль нельзя! Введите запрос корректно: ")
        else:
            print("Неправильный формат ввода! Введите еще раз: ")
    else:
        print("Неправильный формат ввода! Введите еще раз: ")

print(f"Ваш результат: {calculate(first_num, operation, second_num)}")

#ДОП ЗАДАНИЯ - 5, 1(пока что нет)
