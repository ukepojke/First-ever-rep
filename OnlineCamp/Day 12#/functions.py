#3
def reccur(num: int):
    if num % 2 != 0:
        print(num)
    reccur(num+1)

#4
def set_number(hi):
    print(hi)
    hi.pop()
    if hi == set():
        return
    set_number(hi)

#5
def not_same(func):
    def inner():
        hello = func()
        return list(set(hello))
    return inner


@not_same
def random_num():
    from random import randint
    numbers = []
    for i in range(100):
        numbers.append(randint(10,50))
    return numbers



#6
def shiff(func):       #Декоратор шифровщик.
    def inner():
        lol = func()
        hi = []
        for i in lol[0]:  # Возвращает логин с первой функции как ord()
            hi.append(ord(i))
        for i in lol[1]:
            hi.append(ord(i)) # Возвращает пароль с второй функции как ord()
        return hi
    return inner


@shiff
def log_pass():         #
    log = input("Write you're login - ")
    pas = input("Write you're password - ")
    return log,pas
