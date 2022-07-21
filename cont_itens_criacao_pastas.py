from importlib.resources import path
from itertools import count
import os

caminho_arquivos = os.path.join('H:\\','teste')
caminho_pasta_raiz = os.path.join('H:\\','teste')
paradigma = 6


def teste_de_tamanho(path, paradigma) -> bool:
    """
    Testa a quantidade de itens em determinada pasta. Recebe os atributos 'path' e 'paradigma'. Retorna booleano
    Args:
        path (str): caminho da pasta a ser analisada
        paradigma (int): número de itens que se quer verificar dentro da pasta
    """
    count_list = os.listdir(path)
    if len(count_list) <= paradigma: #é maior ou igual ao paradigma
        return True
    else: #não é maior que o paradigma
        return False

#cria pasta caso teste determine

def cria_pasta(path, contador=0):
    """Cria uma nova pasta em sequência numérica. Recebe dois atributos: path e paradigma.

    Args:
        path (str): é o caminho da pasta de destino. Use o formato 'os.path.join("H:\\","teste")' para evitar erros.
        contador (int, optional): É o primeiro nome da pasta numérica a ser buscada. Defaults to 0.

    Returns:
        _type_: _description_
    """
    if os.path.exists(os.path.join(path,str(contador))): #existe pasta
        contador+=1
        return cria_pasta(path,contador)
    else: #não existe pasta
        os.mkdir(os.path.join(path,str(contador)))       #cria pasta 
#/cria pasta caso teste determine
    
#acionamento    
print (teste_de_tamanho(caminho_arquivos,paradigma))

if teste_de_tamanho(caminho_arquivos,paradigma) == True: #chama a criação de pasta caso verdadeiro
    cria_pasta(caminho_pasta_raiz)
#/acionamento
