from calculadora import adicao
from calculadora import subtracao
from calculadora import multiplicacao
from calculadora import divisao


def teste_soma():
    assert adicao(4, 6) == 10


def teste_sub():
    assert subtracao(6, 5) == 1


def teste_mult():
    assert multiplicacao(4, 5) == 20


def teste_div():
    assert divisao(10, 5) == 2
