# Estudo de Cobranca

# Descrição

Estudo de cobrança para o produto financiamento de veículos. Na base de dados, temos informações de veículos leves, motos e pesados (este com somente 12 registros). São 300.000 linhas e 328 colunas, com 316 colunas mascaradas. A base está safrada de 202203 até 202301. Para o desenvolvimento do modelo, as safras consideradas são 202203-202209 e as safras out of time são 202210-202301.

# Objetivo 

Melhorar a taxa de conversão de dívidas. Desconsiderando os custos de recuperação, pode-se pensar em identificar os indivíduos com maiores chances de pagar os saldos em atraso, seja parcial ou totalmente (no cenário de pagamento parcial, pode-se pensar em estratégias para a conversão total do pagameto). Isso faria com que os esforços fossem mais direcionados, com a expectativa de: minimizar o atrito com o cliente, estabelecer uma política de cobrança mais aderente ao perfil de pagamento e aumentar o valor pago dos saldos em atraso.

Uma outra proposta poderia ser estimar qual é o valor pago pelo indivíduo para aquela parcela em atraso. Dado isso, pode-se pensar em estratégias para aumentar o percentual pago das operações.

# Etapas

## Avalia dados

Avaliacao_Inicial.ipynb: Etapa de estudo da base, identificação de dados ausentes e duplicados (essa etapa foi feita agora, para não precisar carregas as variáveis nas demais análises), criação de target para uso em outros notebooks e separação das bases em treino, validação e out of time (oot). A base de validação foi construída com os mesmos meses que foram considerados na bse de treino.

Algumas análises que compõem essa etada de avaliação dos dados foram feitas no Google Colab, como a identificação de dados duplicados por mês.

Algumas sugestões para posterior análise: dias entre o último e primeiro atraso, dívida restante acumulada (isso gera comprometimento da renda nos meses posteriores).