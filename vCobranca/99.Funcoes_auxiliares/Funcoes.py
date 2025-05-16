########################################################  Pacotes

# Carrega pacotes necessários
import pandas as pd
import matplotlib.pyplot as plt

########################################################  Funções

# Função para contagem de observações em cada categoria
def conta_categorias(variavel, df, dropna=True):
    # variavel = string
    # df = pandas dataframe

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
    
