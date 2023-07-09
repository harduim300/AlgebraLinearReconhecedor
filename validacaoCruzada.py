from reconhecedor import *



# Metodo Main para avaliar para execucao dos metodos e avaliacao de taxa de acerto
# Implementando dessa forma a validacao cruzada
def mainExecucao(kIteracoes, usarPCA, banco_imagens, tipo_Mapeamento, n_indices):
    percentual = 0
    escolhaBancoTreino = int(input("Qual tipo de modelo de treino deseja trabalhar ? \n" + 
                           "1) Banco de treino com imagens em mesma quantidade\n"+
                           "2) Banco de treino com imagens em difer quantidade\n"+
                           "Digite opcao 1 ou 2:\n"))
    insersaoTeste = input("Deseja inserir as imagens teste no banco de treino ? S ou N\n")
    for i in range(kIteracoes):
        if escolhaBancoTreino == 1:
            imagens_teste, imagens_treino, imagensLabel, vetorImagens = treinamentoDeBasesUnicas(usarPCA,banco_imagens, tipo_Mapeamento, n_indices, insersaoTeste)
        if escolhaBancoTreino == 2:
            # OBS IMPORTANTE: NOS CASOS VERY EASY, POR TER APENAS 2 FOTOS POR PESSOA EXISTE CHANCE DE O BANCO DE TREINO
            # SER CONSTRUIDO VAZIO OU COM APENAS UMA IMAGEM ATRAPALHANDO O PCA, LOGO É NECESSÁRIO REPETIR O MÉTODO
            imagens_teste, imagens_treino, imagensLabel, vetorImagens = treinamentoDeBasesTamannhoVariado(usarPCA,banco_imagens, tipo_Mapeamento, n_indices, insersaoTeste)
        percentual = percentual + reconhecedor(False, usarPCA, banco_imagens, imagens_teste, imagens_treino,  imagensLabel, vetorImagens, tipo_Mapeamento)
    return float(percentual)/kIteracoes


# ResultFB = "Força Bruta: " + str(mainExecucao(5, False, 'recdev-master/very-easy/', 'VE', 2)) + "%"
# ResultPCA = "PCA: " + str(mainExecucao(10, True, 'recdev-master/very-easy/', 'VE', 2)) + "%"
# print("-----------------------------------------")
# print("TAXAS DE ACERTO PARA: ")
# print("VERY-EASY")
# print(ResultFB)
# print(ResultPCA)
# print("-----------------------------------------")
# ResultFB = "Força Bruta: " + str(mainExecucao(5, False, 'recdev-master/easy/', 'EAS', 8)) + "%"
# ResultPCA = "PCA: " + str(mainExecucao(10, True, 'recdev-master/easy/', 'EAS', 8)) + "%"
# print("-----------------------------------------")
# print("TAXAS DE ACERTO PARA: ")
# print("EASY")
# print(ResultFB)
# print(ResultPCA)
# print("-----------------------------------------")
# ResultFB = "Força Bruta: " + str(mainExecucao(1, False, 'recdev-master/medium/', 'MED', 7)) + "%"
# ResultPCA = "PCA: " + str(mainExecucao(1, True, 'recdev-master/medium/', 'MED', 7)) + "%"
# print("-----------------------------------------")
# print("TAXAS DE ACERTO PARA: ")
# print("MEDIUM")
# print(ResultFB)
# print(ResultPCA)
# print("-----------------------------------------")
# ResultFB = "Força Bruta: " + str(mainExecucao(1, False, 'recdev-master/hard/', 'HAR', 14)) + "%"
# ResultPCA = "PCA: " + str(mainExecucao(1, True, 'recdev-master/hard/', 'HAR', 14)) + "%"
# print("-----------------------------------------")
# print("TAXAS DE ACERTO PARA: ")
# print("HARD")
# print(ResultFB)
# print(ResultPCA)
# print("-----------------------------------------")
ResultFB = "Força Bruta: " + str(mainExecucao(1, False, 'recdev-master/extras/facebookfaces/', 'FB', 9)) + "%"
ResultPCA = "PCA: " + str(mainExecucao(1, True, 'recdev-master/extras/facebookfaces/', 'FB', 9)) + "%"
print("-----------------------------------------")
print("TAXAS DE ACERTO PARA: ")
print("FACEBOOK 1 TESTE INNER-OUTER")
print(ResultFB)
print(ResultPCA)
print("-----------------------------------------")
ResultFB = "Força Bruta: " + str(mainExecucao(1, False, 'recdev-master/extras/facebookfaces-2/', 'FB2', 10)) + "%"
ResultPCA = "PCA: " + str(mainExecucao(1, True, 'recdev-master/extras/facebookfaces-2/', 'FB2', 10)) + "%"
print("-----------------------------------------")
print("TAXAS DE ACERTO PARA: ")
print("FACEBOOK 2 TESTE INNER-OUTER")
print(ResultFB)
print(ResultPCA)
print("-----------------------------------------")
ResultFB = "Força Bruta: " + str(mainExecucao(1, False, 'recdev-master/extras/facebookfaces/crop-inner/', 'PER', 9)) + "%"
ResultPCA = "PCA: " + str(mainExecucao(1, True, 'recdev-master/extras/facebookfaces/crop-inner/', 'PER', 9)) + "%"
print("-----------------------------------------")
print("TAXAS DE ACERTO PARA: ")
print("FACEBOOK 1 TESTE INNER")
print(ResultFB)
print(ResultPCA)
print("-----------------------------------------")
ResultFB = "Força Bruta: " + str(mainExecucao(1, False, 'recdev-master/extras/facebookfaces-2/crop-inner/', 'PER2', 10)) + "%"
ResultPCA = "PCA: " + str(mainExecucao(1, True, 'recdev-master/extras/facebookfaces-2/crop-inner/', 'PER2', 10)) + "%"
print("-----------------------------------------")
print("TAXAS DE ACERTO PARA: ")
print("FACEBOOK 2 TESTE INNER")
print(ResultFB)
print(ResultPCA)
print("-----------------------------------------")
ResultFB = "Força Bruta: " + str(mainExecucao(1, False, 'recdev-master/extras/facebookfaces/crop-outer/', 'PER', 9)) + "%"
ResultPCA = "PCA: " + str(mainExecucao(1, True, 'recdev-master/extras/facebookfaces/crop-outer/', 'PER', 9)) + "%"
print("-----------------------------------------")
print("TAXAS DE ACERTO PARA: ")
print("FACEBOOK 1 TESTE OUTER")
print(ResultFB)
print(ResultPCA)
print("-----------------------------------------")
ResultFB = "Força Bruta: " + str(mainExecucao(1, False, 'recdev-master/extras/facebookfaces-2/crop-outer/', 'PER2', 10)) + "%"
ResultPCA = "PCA: " + str(mainExecucao(1, True, 'recdev-master/extras/facebookfaces-2/crop-outer/', 'PER2', 10)) + "%"
print("-----------------------------------------")
print("TAXAS DE ACERTO PARA: ")
print("FACEBOOK 2 TESTE OUTER")
print(ResultFB)
print(ResultPCA)
print("-----------------------------------------")