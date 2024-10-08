# Objetivo
- O objetivo deste estudo é colocar em prática os conceitos aprendidos no MBA Data Science & Analytics da USP/Esalq relacionados a Regressão Linear. Para isso foi escolhido um problema de Regressão Linear Múltipla disponível na plataforma Kaggle.

## Conceitos 
- Dentre os conceitos que serão abordados, estão:
    * Análise exploratória dos dados;
    * Criação do modelo;
    * Análise da significância estatística das variáveis independentes (f test, t test);
    * Problemas de Multicolinearidade (VIF e Tolerance);
    * Probelmas de Heterocedasticidade (Breusch-Pagan e Goldfeld-Quandt);
    * Stepwise;
    * Verificar a aderência dos resíduos à normalidade (Shapiro Fracia);
    * Transformação da variável dependente (Box-Cox), caso os resíduos não tenham aderência à normalidade;
    * Comparação e seleção do melhor modelo (R2, R2 ajustado, EQM, RMSE);

## Resultado esperado
- Obter o melhor modelo e criar um deploy em cloud para testes.

## Observações
- O resultado da previsão pode não respeitar a interpolação em que o modelo foi treinado;
- O formulário do frontend, para consumo do modelo, não possui travas para interpolação;
- O deploy do Frontend e Backend foram feitos no Render;

<br /><br />
# Tutorial para rodar o projeto localmente



## Instalação
Certifique-se de ter o python instalado na sua máquina.
Após clonar este repositório, se você quiser alterar o código, você pode criar um ambiente virtual ou apenas siga para sessão de como rodar o projeto:
```
python -m venv environment_name
```
Ativação:
__Windows__:
```
environment_name\\Scripts\\activate
```
__MacOS or Linux__:
```
source environment_name/bin/activate
```

## Rodando o projeto
Instalar as dependências:
```
pip install -r requirements.txt
```
### Rodando o projeto com uvicorn
```
uvicorn main:app --reload
```
### Rodando o projeto com Docker
Criando a imagem do Docker
```
docker build -t image_name .
```
Rodando a imagem criada:
```
docker run -d --name container_name -p 80:80 image_name
```

## URIs
Backend: https://housing-price-serc.onrender.com/predict<br />
Frontend: https://housing-price-frontend.onrender.com<br /><br />

## Repositórios
Frontend: [Link](https://github.com/robson-quaresma/housing-price-frontend)<br />
Jupyter Notebook do modelo: [Link](https://github.com/robson-quaresma/multiple-regression-housing-price/blob/main/jupyter-notebook/boston_housing_price.ipynb)

Utilizar o método POST
### JSON
```
{
    "taxa_crime_p_cidade": 0.00632,
    "proporcao_terreno_zoneados": 18.0,
    "proporcao_negocios_p_cidade": 2.31,
    "rio_charles": 1,
    "concentracao_oxidos_nitricos": 0.469,
    "numero_medio_comodos": 7.147,
    "proporcao_proprietarios_casas_1940": 78.9,
    "distancia_centro_empresarial": 4.0900,
    "indice_accessibilidade_rodovias": 3,
    "taxa_imposto": 273.0,
    "proporcao_alunos_x_professor_p_cidade": 18.7,
    "proporcao_comunidade_negra_p_cidade": 394.63,
    "proporcao_pobreza": 9.67
}
```
