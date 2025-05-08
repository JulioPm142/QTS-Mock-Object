from .custom_stack_class import CustomStack
    
class NumberAscOrder:
    def sort(self, stack: CustomStack) -> list:
        numbers = []
        
        while not stack.is_empty(): #enquanto a pilha n retornar com vazio:
            element = stack.pop() #retirar o item no topo, e adiciona-lo como uma variavel
            # Verificar se é um número inteiro
            if not isinstance(element, int):
                raise TypeError(f"Elemento {element} não é um número inteiro")
            
            # Verificar se é um número esta dentro da faixa
            if element < 1 or element > 99:
                raise ValueError(f"Número {element} fora da faixa de 1 a 99")
            
            numbers.append(element) #coloca esse item na lista
        
        numbers.sort()
        return numbers                                                                      