import sys

def calculate(first_num, operation, second_num):
    """Функция, принимающая три значения: первое число, операцию и второе число. Она делает определяет, какую операцию нужно сделать и выполняет ее."""
    try:
        if operation == "плюс":
            return determinator_of_number(first_num) + determinator_of_number(second_num)
        elif operation == "минус":
            return determinator_of_number(first_num) - determinator_of_number(second_num)
        else:
            return determinator_of_number(first_num) * determinator_of_number(second_num)
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
    """Функция для перевода списка в целочисленные формат."""
    for element in list:
        return int(element)

def helper_of_determinator(listt):
    """Функция для составления списка из одного элемента. В данной программе, она возвращает число(первое или второе), которое было введено пользователем."""
    return list(filter(None, [numbers_from_0_to_9.get(from_list_to_string(listt)), numbers_from_10_to_19.get(from_list_to_string(listt)), numbers_mod10_equal_zero.get(from_list_to_string(listt))]))

def determinator_of_operation(list):
    """Функция для определения операции, и возврата ее."""
    for word in list:
        if word in operations:
            operation = word
    return operation

def determinator_of_number(number):     #Принимает список
    """Функция для перевода числа из списка в целочисленный формат."""
    if len(number) == 1:
        return (from_list_to_integer(helper_of_determinator(number)))
    else:
        number_split_first_part, number_split_second_part = [str(word) for word in number]
        return (from_list_to_integer(helper_of_determinator(number_split_first_part)) + from_list_to_integer(helper_of_determinator(number_split_second_part)))



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

operations = ["плюс", "минус", "умножить"]

print("Добро пожаловать в калькулятор! Введите выражение в формате: {первое число} {операция} {второе число}\nПример: \"двадцать три минус девятнадцать\"")
flag = False
while flag == False:
    exspression = input().lower()
    words = list(filter(None, exspression.split(" ")))
    if (words.count("плюс") + words.count("минус") + words.count("умножить") == 1):
        operation = determinator_of_operation(words)
        index_of_operation = words.index(operation)
        first_num = words[:index_of_operation]
        second_num = words[(index_of_operation + 1):]
        if ((2 <= len(first_num) + len(second_num) <= 4) and (operation is not None)):
            flag = True
    else:
        print("Неправильный формат ввода! Введите еще раз: ")

print(f"Ваш результат: {calculate(first_num, operation, second_num)}")
