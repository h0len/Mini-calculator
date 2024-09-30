import sys

def calculate(first_number, operationn, second_number):
    """Функция, принимающая три значения: первое число, операцию и второе число. Она определяет, какую операцию нужно сделать и выполняет ее."""
    try:
        if operationn == "плюс":
            return undo_helper_of_determinator((determinator_of_number(first_number)) + determinator_of_number(second_number))
        elif operationn == "минус":
            return undo_helper_of_determinator((determinator_of_number(first_number)) - determinator_of_number(second_number))
        #ДЕЛИТЬ НЕ РАБОТАЕТ
        elif operationn == "разделить":
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
        if from_list_to_integer(helper_of_determinator(number)) == 100:
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

def undo_helper_of_determinator(integer):
    """Функция для перевода числа из целочисленного формата в текстовый."""
    if 1 <= integer < 20:
        return " ".join(list(filter(None, [get_key_by_value(numbers_from_0_to_9, integer),
                                  get_key_by_value(numbers_from_10_to_19, integer)])))
    else:
        return " ".join(list(filter(None, [get_key_by_value(numbers_mod10_equal_zero, (integer - (integer % 10))),
                                  get_key_by_value(numbers_from_0_to_9, integer % 10),])))

#Как вообще задавать число?
numbers_from_0_to_9 = {"ноль":100, "один":1, "два":2,
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

numbers_used_in_float = {"одна":1, "две":2, "три":3,
                         "четыре":4, "пять":5, "шесть":6,
                         "семь":7, "восемь":8, "девять":9}          #При делении нужно

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
