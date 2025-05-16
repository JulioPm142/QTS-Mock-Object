import pytest
import random
from src.custom_stack_class import CustomStack
from src.NumberAscOrder import NumberAscOrder

def test_sort_six_numeros():
    stack = CustomStack(6)
    
    stack = CustomStack(6)
    
    # Gerar 6 números aleatórios únicos entre 1 e 99 (Mega Sena)
    numeros = random.sample(range(1, 99), 6)
    
    #fazendo mock do push para adicionar a pilha
    mocker.patch.object(stack, "push")
    
    #adicionando numeros a pilha
    for x in numeros:
        stack.push(x)
    
    # Mock usando metodo size
    mocker.patch.object(stack, "size", return_value=6)
    
    # Mock usando metodo pop
    mocker.patch.object(stack, "pop", side_effect=numeros)
    
    # Mock usando metodo is_empty
    mocker.patch.object(stack, "is_empty", return_value=True)
    
    # Cria o sorter e ordena a pilha
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

def test_sort_empty_stack(mocker):
    # Cria a pilha
    stack = CustomStack(6)
    
    # Mock do método size esperado 0 
    mocker.patch.object(stack, "size", return_value=0)
    
    # Mock do método is_empty deveria voltar como verdadeiro
    mocker.patch.object(stack, "is_empty", return_value=True)
    
    # Cria o sorter e ordena a pilha
    sorter = NumberAscOrder()
    result = sorter.sort(stack)
    
    # Verifica se a lista de teste e a original voltam vazias
    assert result == []
    assert stack.is_empty()

def test_sort_non_integer_elements(mocker):
    # Cria a pilha
    stack = CustomStack(6)
    
    # Mock do método push para simular a adição de um elemento não inteiro
    mocker.patch.object(stack, "push")
    
    # Adicionar elemento não inteiro
    stack.push("42")
    
    # Mock do método size, esperado 1
    mocker.patch.object(stack, "size", return_value=1)
    
    # Mock do método pop para retornar o elemento não inteiro "42"
    mocker.patch.object(stack, "pop", return_value="42")
    
    # Cria o sorter
    sorter = NumberAscOrder()
    
    # Verifica se retorna o problema esperado
    with pytest.raises(TypeError, match="Elemento 42 não é um número inteiro"):
        sorter.sort(stack)

def test_sort_out_of_range_numeros(mocker):

    stack = CustomStack(6)
    
    mocker.patch.object(stack, "push")
    
    # Adicionar número fora da faixa
    stack.push(100)
    
    # Mock do método size, esperado 1
    mocker.patch.object(stack, "size", return_value=1)
    
    # Mock do método pop para devolver o número fora da faixa
    mocker.patch.object(stack, "pop", return_value=100)
    
    # Mock do método is_empty para simular que a pilha tem elementos antes do pop
    mocker.patch.object(stack, "is_empty", side_effect=[False, True])
    
    # Cria o sorter
    sorter = NumberAscOrder()
    
    # Verifica se levanta ValueError
    with pytest.raises(ValueError, match="Número 100 fora da faixa de 1 a 99"):
        sorter.sort(stack)