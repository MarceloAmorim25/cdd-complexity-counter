import contador 
import receber_argumentos
import re 

# identificadores fáceis de serem localizados

indicadores_de_complexidade = [

        "if",
        "else",
        "try",
        "Autowired",
        "?",
        ":",
        "switch",
        "case",
        "forEach"

]


# identificando funções passadas como parâmetro


classe_analisada = receber_argumentos.recebe_argumentos()


# a identificação é feita pelo padrão seguido pelos parênteses e pontos 
# um '.()' significa uma função. Um '.(.())' significa uma função passado como parâmetro.


regex1 = r'[)(.]' 

padrao_parenteses = re.findall(regex1, classe_analisada)

padrao_parenteses_string = ''.join(padrao_parenteses)

funcoes_como_parametro = padrao_parenteses_string.count('.(.())')


# limpando a string


for char in ';}{)(@-.,\n':
    classe_analisada=classe_analisada.replace(char,' ')

# gerando as listas

lista_palavras_classe_inicial = classe_analisada.split()

rest_controller_index = lista_palavras_classe_inicial.index('RestController')

lista_palavras_classe = []

for t in range(0, len(lista_palavras_classe_inicial)):
    if t >= rest_controller_index: lista_palavras_classe.append(lista_palavras_classe_inicial[t])


# contando os pontos


contador.contar_pontos_listados(lista_palavras_classe, indicadores_de_complexidade, funcoes_como_parametro)