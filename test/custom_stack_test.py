from src.custom_stack_class import *

import pytest


# Teste para __init__
def test_init():
    stack = CustomStack(4)
    assert stack.limit == 4
    assert stack.elements == []
    assert stack.size() == 0
    assert stack.is_empty() == True


def test_size():
    stack = CustomStack(10)
    assert stack.size() == 0  # pilha sem elementos
    stack.push(1)   #adiciona 1 elemento
    assert stack.size() == 1  #verifica se tem apenas 1
    stack.push(2) #adiciona 1 elemento
    assert stack.size() == 2  # verifica se tem 2 items
    stack.pop() #tira 1 elemento
    assert stack.size() == 1  # verifica se foi removido


def test_is_empty():
    stack = CustomStack(5)
    assert stack.is_empty() == True  # verifica se está vazia
    stack.push(42) #adiciona 1 elemento
    assert stack.is_empty() == False  # verifica se diz q não está vazia
    stack.pop() #retira o elemento de teste
    assert stack.is_empty() == True  #verifica se diz q está vazia


def test_push():
    stack = CustomStack(2)
    stack.push(1.0) #adiciona um item float
    assert stack.size() == 1 #verifica se o tamanho ainda é 1
    assert stack.top() == 1.0 #verifica se o primeiro elemento é o 1.0
    stack.push(2.0) #adiciona um item float
    assert stack.size() == 2 #verifica se o tamanho ainda é 2
    assert stack.top() == 2.0 #verifica se o primeiro elemento é o 2.0
    assert stack.is_empty() == False # verifica se diz q não está vazia


def test_push_full_stack():
    stack = CustomStack(1)
    stack.push(1) #adiciona 1 elemento
    with pytest.raises(StackFullException): #usa o pytest para verificar, se quando adicionar outro elemento ele da uma exceção
        stack.push(2)  #


def test_pop():
    stack = CustomStack(3)
    stack.push(5.0)
    stack.push(10.0) #adiciona 2 itens
    popped_value = stack.pop() #tenta retirar um item da pilha
    assert popped_value == 10.0  # verifica se o elemento retirado, foi o ultimo da pilha
    assert stack.size() == 1 # verifica se o tamanho está certo, len antigo -1
    assert stack.top() == 5.0 #verifica se o elemento no topo da lista é o 5.0
    assert stack.is_empty() == False #verifica se diz q a pilha não está vazia


def test_pop_empty_stack():
    stack = CustomStack(3)
    with pytest.raises(StackEmptyException): #tenta fazer um pop na lista vazia, e usa o pytest para verificar a exceção
        stack.pop()  


def test_top():
    stack = CustomStack(3) 
    stack.push(7) 
    stack.push(14) 
    assert stack.top() == 14  # Verifica se o ultimo elemento é o ultimo que foi adicionado
    assert stack.size() == 2  # verifica se o tamanho está correto
    stack.pop() #remove o item de cima
    assert stack.top() == 7  #verifica se o novo item do topo é o primeiro adicionado


def test_top_empty_stack():
    stack = CustomStack(3)
    with pytest.raises(StackEmptyException): #tenta pegar o item do topo em uma lista vazia
        stack.top()  # Deve levantar exceção