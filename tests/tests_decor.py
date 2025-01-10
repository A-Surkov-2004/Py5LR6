from src.decor import *


def test1():
    # given
    simple = ConcreteComponent()
    decorator1 = ConcreteDecoratorA(simple)

    # when
    ans = client_code(decorator1)

    # then
    assert ans[1]['KZT']['name'] == 'Тенге'  # проверка кооректности работы json


def test2():
    # given
    simple = ConcreteComponent()
    decorator1 = ConcreteDecoratorA(simple)
    decorator2 = ConcreteDecoratorB(simple)

    # when
    ans1 = client_code(decorator1)
    ans2 = client_code(decorator2)

    assert ans2.split('\r\n')[2].split(',')[2] == str(ans1[1]['KZT']['value'])  # Тенеге csv = Тенге json


def test3():
    # given
    simple = ConcreteComponent()
    decorator1 = ConcreteDecoratorA(simple)
    decorator2 = ConcreteDecoratorB(decorator1)
    dec3 = ConcreteDecoratorA(decorator2)

    # when
    ans1 = client_code(decorator1)
    ans2 = client_code(dec3)

    # then
    assert ans1 == ans2  # Raw to json == Raw to json to csv to json



test1()
test2()
test3()
