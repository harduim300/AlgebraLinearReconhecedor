# AlgebraLinearReconhecedor
Este é um código em Python para realizar o reconhecimento facial utilizando o método de Análise de Componentes Principais (PCA)e força bruta.

Requisitos
Certifique-se de ter as seguintes bibliotecas instaladas:
time
Pillow (PIL)
random
os
numpy
opencv-python (cv2)
matplotlib
scikit-learn
Você pode instalá-las usando o pip com o seguinte comando:

pip install -r requirements.txt
Certifique-se de criar um arquivo requirements.txt no diretório do projeto com as bibliotecas listadas acima.

Como usar
Clone este repositório para o seu ambiente de desenvolvimento.

Certifique-se de ter um conjunto de dados de imagens de faces disponível para treinamento e teste. Organize as imagens em uma estrutura de diretórios, onde cada diretório representa uma pessoa e contém as imagens correspondentes a essa pessoa.

Abra o arquivo valicadacaoCruzada.py e defina as configurações do reconhecedor, como o caminho para o diretório de imagens e o número de componentes principais a serem usados.

Execute o arquivo valicadacaoCruzada.py para treinar o reconhecedor e realizar o reconhecimento facial nas imagens de teste.

python valicadacaoCruzada.py