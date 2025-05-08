import pytest
import random
from src.custom_stack_class import CustomStack
from src.NumberAscOrder import NumberAscOrder

def test_sort_six_numeros():
    stack = CustomStack(6)
    
    # Gerar 6 números aleatórios únicos entre 1 e 60 (Mega Sena)
    numeros = random.sample(range(1, 99), 6)
    
    # Adicionar números à pilha
    for x in numeros:
        stack.push(x)
    
    # cria 2 variaveis, uma para os valores vindos do NumberAsc e outro feito localmente para comparar
    sorter = NumberAscOrder()
    result = sorter.sort(stack)
    
    # compara os dois valores para ver se está correto
    assert result == sorted(numeros)
    
    #testando o tamano
    assert len(result) == 6
    
    #verifica se está vazio
    assert stack.is_empty()

    # verifica se os numeros estão dentro dos números possíveis
    assert all(1 <= num <= 99 for num in result)

def test_sort_empty_stack():
    stack = CustomStack(6)
    
    # cria 2 variaveis, uma para os valores vindos do NumberAsc e outro feito localmente para comparar
    sorter = NumberAscOrder()
    result = sorter.sort(stack)
    
    # verifica se a lista de teste e a original voltam vazias
    assert result == []
    assert stack.is_empty()

def test_sort_non_integer_elements():
    stack = CustomStack(6)
    
    # Adicionar elemento não inteiro
    stack.push("42")
    
    sorter = NumberAscOrder()
    
    # verifica se retorna o problema
    with pytest.raises(TypeError, match="Elemento 42 não é um número inteiro"):
        sorter.sort(stack)

def test_sort_out_of_range_numeros():
    stack = CustomStack(6)
    
    # adiciona um número fora da faixa
    stack.push(100)
    
    sorter = NumberAscOrder()
    
    # Verificar se levanta ValueError
    with pytest.raises(ValueError, match="Número 100 fora da faixa de 1 a 99"):
        sorter.sort(stack)