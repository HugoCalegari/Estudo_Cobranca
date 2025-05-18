########################################################  Pacotes

# Carrega pacotes necessários
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.preprocessing import StandardScaler, MinMaxScaler
import pickle
import seaborn as sns
import os

########################################################  Funções

# Função para contagem de observações em cada categoria
def conta_categorias(variavel, df, dropna=True):
    # variavel é uma string
    # df é um pandas dataframe

    # contagem absoluta
    versao1 = pd.DataFrame(df[variavel].value_counts()).reset_index().sort_values(by='count', ascending=False)
    
    # contagem relativa
    versao2 = pd.DataFrame(df[variavel].value_counts()/df.shape[0]*100).reset_index().sort_values(by='count', ascending=False)
    
    return(versao1, versao2)


# Função que faz o gráfico da variável numérica escolhida

def plot_histograma(variavel, df, label=None, bins=10):
    # variavel é uma string
    # df é um pandas dataframe
    # label é uma string com a informação de rótulo (variável target)
    # plotando um histograma básico

    if label == None:

        plt.hist(df[variavel], color='skyblue', edgecolor='black', label=label, bins=bins)
                    
        # Adicionando legenda e títulos
        plt.xlabel('Valores')
        plt.ylabel('Frequência')
        plt.title('Histograma')

        # Display do plot
        plt.show()
  
    else:
        
        plt.hist(df[df[label] == 0][variavel],  
                 alpha = 0.5,
                 label=[label],
                 bins=bins)
        
        plt.hist(df[df[label] == 1][variavel],  
                 alpha = 0.5,
                 label=[label],
                 bins=bins)

        # Adicionando legenda e títulos
        plt.xlabel('Valores')
        plt.ylabel('Frequência')
        plt.title('Histograma')
        plt.legend()

        # Display do plot
        plt.show()


# Função que retorna uma lista de variáveis correlacionadas

def Vars_Correl(dataframe, list_vars_num, limiar = 0.7, metodo = 'spearman'):
    # dataframe é um pandas dataframe
    # list_vars_num é uma lista das colunas do dataframe que são numéricas
    # limiar é o valor mínimo para o qual consideraremos a correlação. Valores superiores ao limiar serão considerados altamente correlacionados
    # metodo é o critério de correlação dos dados. Pode ser spearman ou pearson
    
    aux1 = dataframe[list_vars_num]
    matriz_correl = aux1.corr(method = metodo)
    
    linha = []
    coluna = []
    valor = []
    
    for i in matriz_correl.index:
        for j in matriz_correl.columns:
            if ((i != j) & (np.abs(matriz_correl[i][j]) >= limiar)):
                linha.append(i)
                coluna.append(j)
                valor.append(matriz_correl[i][j])
    
    Var1 = pd.DataFrame({'Var1': linha})
    Var2 = pd.DataFrame({'Var2': coluna})
    Valores = pd.DataFrame({'Valores': valor})
    Resultado_correl = pd.concat([Var1, Var2, Valores], axis = 1)
    Resultado_correl = Resultado_correl.drop_duplicates(subset=['Valores']).reset_index(drop = 'True')

    return(Resultado_correl)


# Função que ajusta os níveis das categorias

def ajusta_categorias(df):
    # df é um pandas dataframe

    DePara1 = {
        'leves': 0, 
        'motos': 1
    }

    DePara2 = {
        'A': 0,
        'B': 1,
        'C': 2,
        'D': 3,
        'E': 4,
        'Sem_Info': 5
    }

    DePara3 = {
        'Sem_Info': -1,
        'S': 1,
        'N': 0
    }

    DePara4 = {
        'Sem_Info': -1,
        'MUITO LONGE': 1,
        'PROXIMO': 0
    }

    df['segmento_veiculo'] = df['segmento_veiculo'].map(DePara1)
    df['VAR_2'] = df['VAR_2'].map(DePara2)

    df['VAR_42'] = df['VAR_42'].map(DePara3)
    df['VAR_44'] = df['VAR_44'].map(DePara3)
    df['VAR_45'] = df['VAR_45'].map(DePara3)
    df['VAR_46'] = df['VAR_46'].map(DePara3)
    df['VAR_47'] = df['VAR_47'].map(DePara3)
    df['VAR_48'] = df['VAR_48'].map(DePara3)
    df['VAR_50'] = df['VAR_50'].map(DePara3)
    df['VAR_51'] = df['VAR_51'].map(DePara3)
    df['VAR_52'] = df['VAR_52'].map(DePara3)
    df['VAR_53'] = df['VAR_53'].map(DePara3)
    df['VAR_55'] = df['VAR_55'].map(DePara3)
    df['VAR_56'] = df['VAR_56'].map(DePara3)
    df['VAR_57'] = df['VAR_57'].map(DePara3)
    df['VAR_256'] = df['VAR_256'].map(DePara3)

    df['VAR_113'] = df['VAR_113'].map(DePara4)

    return df


# Função que retorna os dados numéricos padronizados ou normalizados e o caminho onde o padronizador foi saldo em formato pickle

def Padronizacao(dataframe, lista_variaveis_numericas, tipo = 'padro', path = os.getcwd(), nome_sclr = 'scaler.pkl'):
    # dataframe é um pandas dataframe
    # lista_variaveis_numericas é uma lista de variáveis numéricas
    # tipo é uma string com o tipo de padronizador selecionado, pode ser a padronização ou narmalização dos dados
    # nome_sclr é o nome com o qual o padronizador será salvo

    if tipo == 'padro':
        SC = StandardScaler()
        SC.fit(dataframe[lista_variaveis_numericas])
        dados_new = pd.DataFrame(SC.transform(dataframe[lista_variaveis_numericas]), columns=dataframe[lista_variaveis_numericas].columns)

        # Salva o StandardScaler para aplicação em dados futuros
        # path = os.getcwd()

        path = path + '/' + nome_sclr
        print('O StandardScaler será salvo no caminho:', path)
        
        with open(path,'wb') as f:
            pickle.dump(SC, f)

    elif tipo == 'norm':
        MMS = MinMaxScaler()
        MMS.fit(dataframe[lista_variaveis_numericas])
        dados_new = pd.DataFrame(MMS.transform(dataframe[lista_variaveis_numericas]), columns=dataframe[lista_variaveis_numericas].columns)

        # Salva o StandardScaler para aplicação em dados futuros
        # path = os.getcwd()

        path = path + '/' + nome_sclr
        print('O MinMaxScaler será salvo no caminho:', path)
        
        with open(path,'wb') as f:
            pickle.dump(MMS, f)
        
    return([dados_new, path])


# Função que faz o gráfico da importância das variáveis

def plot_feature_importance(importance, names, model_type):
    # importance é a variável dos valores de importância: MODELO.feature_importances_
    # names é a variável com os nomes para os respectivos valores de importância: MODELO.feature_names_in_
    # model_type é a variável string com o nome do modelo

    feature_importance = np.array(importance)
    feature_names = np.array(names)

    # Cria dicionário com nomes das variáveis e com os valores de importância
    data={'feature_names':feature_names,'feature_importance':feature_importance}
    fi_df = pd.DataFrame(data)

    # Ordena de forma decrescente a importância das variáveis
    fi_df.sort_values(by=['feature_importance'], ascending=False, inplace=True)

    # Define o tamanho da imagem
    plt.figure(figsize=(15,10))

    # Gráfico 
    sns.barplot(x=fi_df['feature_importance'], y=fi_df['feature_names'])
    
    # Rótulos
    plt.title(model_type + ' FEATURE IMPORTANCE')
    plt.xlabel('FEATURE IMPORTANCE')
    plt.ylabel('FEATURE NAMES')