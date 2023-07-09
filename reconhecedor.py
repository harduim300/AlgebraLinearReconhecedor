from PIL import Image
import random
import os
import numpy as np
import cv2
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import sklearn.decomposition as decomp

# Falso infinito, porém suficiente
AUX = 9999999999999

# Função para gerar o mapeamento conforme o banco
def escolhaMap(escolha):
    if escolha == 'VE' or escolha == 'EAS':
        return {'2':[],'11':[],'15':[],'16':[],'87':[]}
    elif escolha == 'MED'or escolha == 'HAR':
        return {str(i): [] for i in range(1, 51)}
    elif escolha == 'FB' or escolha == 'FB2':
        return {str(i): [] for i in range(1, 6)}
    elif escolha == 'PER' or escolha == 'PER2':
        pessoas = int(input("Diga o maior indice da pessoa do banco indicado?\n"))
        return {str(i): [] for i in range(1, pessoas+1)}
    

# Treinamento considerando a nao insersao de imagem de teste
# Sendo tomada imagens unicas para cada pessoa    
def treinamentoDeBasesUnicas(usarPCA, banco_imagens, tipo_Mapeamento, n_indices, insersaoTeste):
    imagensDeTeste = []
    vetorImagens = []
    imagensLabel = []
    imagensDeTreino = None
    mapeamentoFB = tipo_Mapeamento == 'FB'or tipo_Mapeamento == 'FB2'
    if mapeamentoFB:
        caminho = banco_imagens + "crop-inner/"
    else:
        caminho = banco_imagens
    mapeamento = escolhaMap(tipo_Mapeamento)
    for ids in mapeamento:
        ids_escolh = random.randrange(1,n_indices+1)
        for i in range(1,n_indices+1):
            if tipo_Mapeamento == 'HAR' and i+1 < 10:
                arquivo_img_escolh = ids + "-0" + str(i+1) + '.jpg'
            else:
                if tipo_Mapeamento == 'FB2' or tipo_Mapeamento == 'PER2':
                    arquivo_img_escolh = ids + "-" + str(i) + '.png'
                else:
                    arquivo_img_escolh = ids + "-" + str(i) + '.jpg'
            # Verificacao se o arquivo esta realmente presente
            if os.path.exists(caminho + arquivo_img_escolh):
                if i == ids_escolh and insersaoTeste == "S":
                    imagensDeTeste.append(arquivo_img_escolh)
                    mapeamento[ids].append(arquivo_img_escolh)
                    if usarPCA == True:
                        if mapeamentoFB:
                            imgCinza = cv2.imread(os.path.join(caminho, arquivo_img_escolh), cv2.IMREAD_GRAYSCALE)
                            matrizImagem = np.array(imgCinza).flatten()
                            vetorImagens.append(matrizImagem)
                            imagensLabel.append(arquivo_img_escolh.split("-")[0])
                        else:    
                            vetorImagens.append(leituraImagem(caminho,arquivo_img_escolh))
                            imagensLabel.append(arquivo_img_escolh.split("-")[0])
                elif i == ids_escolh and insersaoTeste == "N":
                    imagensDeTeste.append(arquivo_img_escolh)
                else:
                    mapeamento[ids].append(arquivo_img_escolh)
                    if usarPCA == True:
                        if mapeamentoFB:
                            imgCinza = cv2.imread(os.path.join(caminho, arquivo_img_escolh), cv2.IMREAD_GRAYSCALE)
                            matrizImagem = np.array(imgCinza).flatten()
                            vetorImagens.append(matrizImagem)
                            imagensLabel.append(arquivo_img_escolh.split("-")[0])
                        else:    
                            vetorImagens.append(leituraImagem(caminho,arquivo_img_escolh))
                            imagensLabel.append(arquivo_img_escolh.split("-")[0])

                
    imagensDeTreino = mapeamento
    return imagensDeTeste, imagensDeTreino, imagensLabel, vetorImagens

# Insere o banco de treino com tamanho variado
def treinamentoDeBasesTamannhoVariado(usarPCA, banco_imagens, tipo_Mapeamento, n_indices, insersaoTeste):
    imagensDeTeste = []
    vetorImagens = []
    imagensLabel = []
    imagensDeTreino = None
    mapeamentoFB = tipo_Mapeamento == 'FB'or tipo_Mapeamento == 'FB2'
    if mapeamentoFB:
        caminho = banco_imagens + "crop-inner/"
    else:
        caminho = banco_imagens

    mapeamento = escolhaMap(tipo_Mapeamento)
    for ids in mapeamento:
        ids_escolh = random.randrange(1,n_indices+1)
        for i in range(1,ids_escolh+1):
            if tipo_Mapeamento == 'HAR' and i < 10:
                arquivo_img_escolh = ids + "-0" + str(i) + '.jpg'
            else:
                if tipo_Mapeamento == 'FB2' or tipo_Mapeamento == 'PER2':
                    arquivo_img_escolh = ids + "-" + str(i) + '.png'
                else:
                    arquivo_img_escolh = ids + "-" + str(i) + '.jpg'

            # Verificacao se o arquivo esta realmente presente
            if os.path.exists(caminho + arquivo_img_escolh):
                if i == ids_escolh and insersaoTeste == "S":
                    imagensDeTeste.append(arquivo_img_escolh)
                    mapeamento[ids].append(arquivo_img_escolh)
                    if usarPCA == True:
                        if mapeamentoFB:
                            imgCinza = cv2.imread(os.path.join(caminho, arquivo_img_escolh), cv2.IMREAD_GRAYSCALE)
                            matrizImagem = np.array(imgCinza).flatten()
                            vetorImagens.append(matrizImagem)
                            imagensLabel.append(arquivo_img_escolh.split("-")[0])
                        else:    
                            vetorImagens.append(leituraImagem(caminho,arquivo_img_escolh))
                            imagensLabel.append(arquivo_img_escolh.split("-")[0])
                elif i == ids_escolh and insersaoTeste == "N":
                    imagensDeTeste.append(arquivo_img_escolh)
                else:
                    mapeamento[ids].append(arquivo_img_escolh)
                    if usarPCA == True:
                        if mapeamentoFB:
                            imgCinza = cv2.imread(os.path.join(caminho, arquivo_img_escolh), cv2.IMREAD_GRAYSCALE)
                            matrizImagem = np.array(imgCinza).flatten()
                            vetorImagens.append(matrizImagem)
                            imagensLabel.append(arquivo_img_escolh.split("-")[0])
                        else:    
                            vetorImagens.append(leituraImagem(caminho,arquivo_img_escolh))
                            imagensLabel.append(arquivo_img_escolh.split("-")[0])

                
    imagensDeTreino = mapeamento
    return imagensDeTeste, imagensDeTreino, imagensLabel, vetorImagens

def PCA(X, img):

    # O Pca é um metodo de redução de dimensionalidade
    Xtreino = np.array(X, dtype=np.float32)
    imagemTeste = img.reshape(1,-1)
    #Aplica o PCA
    num_componentes = 50
    
    pca = decomp.PCA().fit(Xtreino)
    
    autoFaces = pca.components_[:num_componentes]

    
    #Calcula o Peso de cada face
    pesos = autoFaces @ (Xtreino - pca.mean_).T
    
    pesoImagem = autoFaces @ (imagemTeste - pca.mean_).T

    
    
    distanciaEuclidiana = np.linalg.norm(pesos - pesoImagem, axis=0)
    indiceClassificacao = np.argmin(distanciaEuclidiana)
    
    return indiceClassificacao,min(distanciaEuclidiana)


def leituraImagem(banco_imagens ,nome_arquivo):
    imgCinza = Image.open(banco_imagens + nome_arquivo).convert('L')
    matrizImagem = np.array(imgCinza)
    return matrizImagem.flatten()

def leituraImagemFB(faceCascade, banco_imagens ,nome_arquivo):
    imgCinza = cv2.imread(os.path.join(banco_imagens, nome_arquivo), cv2.IMREAD_GRAYSCALE)
    detectarFaces = faceCascade.detectMultiScale(imgCinza,scaleFactor=1.3,minNeighbors=3, minSize=(30, 30))
    
    if len(detectarFaces) == 0:
        # Se nenhum rosto for encontrado, continue para a próxima imagem
        return [], leituraImagem(banco_imagens ,nome_arquivo)
    
    # Pegando localização do rosto detectado, como só possui um rosto por foto!
    (x, y, w, h) = detectarFaces[0]

    # Isolando o rosto da imagem
    faceExtraida = imgCinza[y:y+h, x:x+w]

    # Redimensionando a imagem do rosto para um tamanho padrão
    faceExtraidaRedimencionando = cv2.resize(faceExtraida, (100, 100))
    return np.array(faceExtraidaRedimencionando).flatten(), leituraImagem(banco_imagens ,nome_arquivo)


def classificador(nome_arquivo):
    return nome_arquivo.split("-")[0] 


def forcaBrutaClassificacao(banco_imagens, img, imagens_treino):
    aux = AUX
    vet_c = 0
    vet_i = []

    # Metodo de verificacao pixel a pixel
    for indice in imagens_treino:
        for i in imagens_treino[indice]:
            img_compare = leituraImagem(banco_imagens,i)
            aux_pessoa = np.linalg.norm(img-img_compare)
            if aux_pessoa < aux:
                aux = aux_pessoa
                figura_vet_i = img_compare
                vet_c = indice
    return aux, vet_c, figura_vet_i

def pcaClassificacao(img, imagensLabel, vetorImagens):
    vet_c = 0
    
            
    indiceClassificacao, aux = PCA(vetorImagens,img)
    
    figura_vet_i = vetorImagens[indiceClassificacao]
    vet_c = imagensLabel[indiceClassificacao]
    
    return aux, vet_c, figura_vet_i


def reconhecedor(resultado, usarPCA,banco_imagens, imagens_teste, imagens_treino, imagensLabel, vetorImagens, tipo_Mapeamento):
    errado = 0
    certo = 0

    if tipo_Mapeamento == 'FB' or tipo_Mapeamento == 'FB2':
        # Carregando o classificador pré-treinado para detecção de rostos
        faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + '/haarcascade_frontalface_default.xml')
    for fn in imagens_teste:
        caminho = ""
        if tipo_Mapeamento == 'FB' or tipo_Mapeamento == 'FB2':
            caminho = banco_imagens + "crop-outer/"
            img, imgNaoEncontrado = leituraImagemFB(faceCascade, caminho, fn)
        else:
            caminho = banco_imagens
            img = leituraImagem(caminho, fn)

        if len(img) != 0:
            if usarPCA == True:
                aux, vet_c, figura_vet_i = pcaClassificacao(img, imagensLabel, vetorImagens)
            else:
                aux, vet_c, figura_vet_i = forcaBrutaClassificacao(caminho, img, imagens_treino)
        else:
            vet_c = 0
            aux = None
            
        if classificador(fn) == str(vet_c):
            
            certo = certo + 1
        else:
            errado = errado + 1

        # Permitir ou nao exibir a comparacao de fotos
        if resultado:

            if classificador(fn) == str(vet_c):
                print("IGUAL")
            else:
                print("DIFERENTE " + classificador(fn) + " != " + str(vet_c))
            print('Minima_Norma_de_Diferenca = ' + str(aux))
            print('class = ' + str(vet_c))
            
            if usarPCA == True:
                if len(img) != 0:
                    fig, axes = plt.subplots(1,2,sharex=True,sharey=True,figsize=(8,6))
                    if classificador(fn) == str(vet_c):
                        fig.suptitle('PCA retorna: Igual')
                    else:
                        fig.suptitle('PCA retorna: Diferente')
                    axes[0].imshow(img.reshape(100,100), cmap="gray")
                    axes[0].set_title("Imagem Teste")
                    axes[1].imshow(figura_vet_i.reshape(100,100), cmap="gray")
                    axes[1].set_title("Imagem Encontrada")
                    plt.show()
                else:
                    fig, axes = plt.subplots(1,2,sharex=True,sharey=True,figsize=(8,6))
                    fig.suptitle('PCA retorna: Não encontrado')
                    axes[0].imshow(imgNaoEncontrado.reshape(100,100), cmap="gray")
                    axes[0].set_title("Imagem Teste")
                    plt.show()
            else:
                if len(img) != 0: 
                    fig, axes = plt.subplots(1, 2,sharex=True,sharey=True,figsize=(8,6))
                    if classificador(fn) == str(vet_c):
                        fig.suptitle('Forca bruta retorna: Igual')
                    else:
                        fig.suptitle('Forca bruta retorna: Diferente')
                    axes[0].imshow(img.reshape(100,100), cmap="gray")
                    axes[0].set_title('Imagem Teste')
                    axes[1].imshow(figura_vet_i.reshape(100,100), cmap="gray")
                    axes[1].set_title('Imagem Encontrada')
                    plt.show()
                else:
                    fig, axes = plt.subplots(1,2,sharex=True,sharey=True,figsize=(8,6))
                    fig.suptitle('Forca Bruta: Não encontrado')
                    axes[0].imshow(imgNaoEncontrado.reshape(100,100), cmap="gray")
                    axes[0].set_title("Imagem Teste")
                    plt.show()
    return (certo*100.)/(certo+errado)

def reconhecimento(imgTeste, usarPCA, banco_imagens, tipo_Mapeamento, n_indices):
    escolhaBancoTreino = int(input("Qual tipo de modelo de treino deseja trabalhar ? \n" + 
                           "1) Banco de treino com imagens em mesma quantidade\n"+
                           "2) Banco de treino com imagens em difer quantidade\n"+
                           "Digite opcao 1 ou 2:\n"))
    insersaoTeste = input("Deseja inserir as imagens teste no banco de treino ? S ou N\n")
    if escolhaBancoTreino == 1:
        imagens_teste, imagens_treino, imagensLabel, vetorImagens = treinamentoDeBasesUnicas(usarPCA,banco_imagens, tipo_Mapeamento, n_indices, insersaoTeste)
    if escolhaBancoTreino == 2:
        # OBS IMPORTANTE: NOS CASOS VERY EASY, POR TER APENAS 2 FOTOS POR PESSOA EXISTE CHANCE DE O BANCO DE TREINO
        # SER CONSTRUIDO VAZIO OU COM APENAS UMA IMAGEM ATRAPALHANDO O PCA, LOGO É NECESSÁRIO REPETIR O MÉTODO
        imagens_teste, imagens_treino, imagensLabel, vetorImagens = treinamentoDeBasesTamannhoVariado(usarPCA,banco_imagens, tipo_Mapeamento, n_indices, insersaoTeste)
    print(imagens_teste)
    percentual = reconhecedor(True, usarPCA, banco_imagens, imgTeste, imagens_treino,  imagensLabel, vetorImagens, tipo_Mapeamento)


# Imagens-Teste, Usar Pca, Exibir Imagens Comparacao, Caminho Imagens banco, Tipo modelo, Numero de imagens por pessoa
reconhecimento(["3-1.jpg", "2-6.jpg", "4-3.jpg", "2-4.jpg", "5-5.jpg"],True, 'recdev-master/extras/facebookfaces/', 'FB', 9)