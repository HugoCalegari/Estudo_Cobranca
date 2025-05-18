# Estudo de Cobranca

# Descrição

Estudo de cobrança para o produto financiamento de veículos. Na base de dados, temos informações de veículos leves, motos e pesados (este com somente 12 registros). São 300.000 linhas e 328 colunas, com 316 colunas mascaradas. A base está safrada de 202203 até 202301. Para o desenvolvimento do modelo, as safras consideradas são 202203-202209 e as safras out of time são 202210-202301.

# Objetivo 

Melhorar a taxa de conversão de dívidas. 

Enquadramento em classificação: desconsiderando os custos de recuperação, pode-se pensar em identificar os indivíduos com maiores chances de pagar os saldos em atraso, seja parcial ou totalmente (no cenário de pagamento parcial, pode-se pensar em estratégias para a conversão total do pagameto). Isso faria com que os esforços fossem mais direcionados, com a expectativa de: minimizar o atrito com o cliente, estabelecer uma política de cobrança mais aderente ao perfil de pagamento e aumentar o valor pago dos saldos em atraso.

Enquadramento em regressão: uma outra proposta poderia ser estimar qual é o valor pago pelo indivíduo para aquela parcela em atraso. Com o valor estimado, tem-se uma estimativa do percentual convertido (razão entre saldo pago e saldo em atraso). Dado isso, pode-se pensar em estratégias para aumentar o percentual pago das operações.

A segunda proposta será a abordada nos estudos sequenciais, ou seja, será estimado o pagamento efetuado. Posteriormente, pode-se ter uma estimativa de percentual pago. A ideia será focar no público ou grupo com maior saldo pago. A eficiência na cobrança apoiará no incremento de receita, redução de custos de cobrança e, potencialmente, redução de provisionamento dado que a Loss Given Default (LGD) poderá deflacionar a Probabilidade de Default (PD) do associado.

# Etapas

## 0.Avalia_Dados

Avaliacao_Inicial.ipynb: etapa de estudo da base, identificação de dados ausentes e duplicados (essa etapa foi feita agora, para não precisar carregas as variáveis nas demais análises), criação de target para uso em outros notebooks e separação das bases em treino, validação e out of time (oot). A base de validação foi construída com os mesmos meses que foram considerados na bse de treino.

Algumas análises que compõem essa etada de avaliação dos dados foram feitas no Google Colab, como a identificação de dados duplicados por mês.

Algumas sugestões para posterior análise: dias entre o último e primeiro atraso, dívida restante acumulada (isso gera comprometimento da renda nos meses posteriores).

## 1.Estudo_Variaveis

Etapa de avaliação de estratégias de imputação dos dados faltantes e redução de dimensionalidade. 

1.Exploracao_1.ipynb: etapa de estudo de variáveis, teste de imputação, relações entre as variáveis explicativas e testes de independência;

2.Pre_Processamento.ipynb: etapa de escolha das variáveis numéricas e categóricas que serão usadas na etapa de modelagem; pré-processamento das variáveis categóricas e numéricas de treino, validação e teste (oot).

## 2.Modelagem

Fase de estudo de modelos, com objetivo de estimar o valor de pagamento feito pelo indivíduo.

1.Modelos_PT1: fase inicial de estudo de modelos, sem e com otimização de hiperparâmetros. Os modelos foram logados no mlflow e as métricas comparadas. Optou-se pela RandomForest com o tuning de hiperparâmetro usando o hyperopt;

2.Interpretabilidade: interpretabilidade de um dos melhores modelos encontrados na exploração dos modelos anteriormente.