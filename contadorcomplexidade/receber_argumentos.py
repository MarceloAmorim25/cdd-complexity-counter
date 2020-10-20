import argparse

def recebe_argumentos():

    parser = argparse.ArgumentParser(description='Definir classe a ser analisada')

    parser.add_argument('--controller', action="store", dest='controller')
    parser.add_argument('--model', action="store", dest='model')

    nome_da_classe = parser.parse_args()

    classe_java = open(f"../Controllers/{nome_da_classe.controller}.java")

    classe_analisada = classe_java.read()

    return classe_analisada