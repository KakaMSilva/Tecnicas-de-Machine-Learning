# -*- coding: utf-8 -*-
"""ML  Parte I

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1FYWJ5cDmQ8zDp_lEmykDsjXl8Y0yH_Aw
"""

import pandas as pd # importando o pandas para manipularmos o dataset
import numpy as np # biblioteca para manipulação de vetores e matrizes grandes além de outras manipulações de dados de larga escala
import seaborn as sns # importando o Seaborn para visualizar o comportamento dos dados
import matplotlib.cm as mcm # biblioteca para mostrar gráficos (espeficamente uma parte para cores)
import matplotlib.pyplot as plt # importando o Matplotlib para o elbow method
import pandas_profiling

from pandas_profiling import ProfileReport # importando o pandas-profiling para fazer o profile do dataset
from sklearn.model_selection import train_test_split # utilizado para o split entre treinamento e teste
from sklearn.neighbors import KNeighborsRegressor # KNN para regressão
from sklearn.linear_model import LinearRegression # Regressão linear
from sklearn.svm import SVR # SVM para regressão
from sklearn.decomposition import PCA # PCA como aprendizagem não-supervisionada
from sklearn.preprocessing import RobustScaler # utilizado para que todas as entradas estejam na mesma escala numérica
from sklearn.preprocessing import StandardScaler
from sklearn.feature_selection import * # importando todas as funções específicas de seleção de atributos do scikit-learn
from sklearn.decomposition import * # importando todas as funções específicas para a extração de atributos do scikit-learn
from sklearn.cluster import * # importando todas as funções específicas para o agrupamento

#seleção do dataset
df_nba = pd.read_csv('/content/nba_stats.csv') #carrega o dataset do diretorio 
df_nba.describe() #mostra destacaria os dados
#display(df_nba.columns)

df_nba

df_nba.info()

for col in df_nba.columns:
 if df_nba[col].isnull().sum():
  total_null=df_nba[col].isnull().sum() 
  print('Column: {} total null {}, i.e. {} %'.format(col,total_null,round(total_null*100/len(df_nba),2)))

#Limpando dados nulos
df_nba.isnull().sum()
df_nba.dropna(inplace = True)
df_nba.isnull().sum()

df_nba.head()

#Substitui String para Float 
df_nba['Posicao'] = df_nba['Posicao'].replace({'PF':1, 'SG':2, 'C':3, 'SF':4, 'PG':5, 'G':6, 'F-C':6, 'G-F':6, 'F-G':6, 'C-F':6, 'C-PF':6, 'SG-SF':6, 'F':6, 'PF-C':6, 'SG-PG':6, 'SF-SG':6, 'PG-SG':6,         
                                               'PF-SF':6, 'SF-PF':6, 'SG-PF':6, 'C-SF':6, 'SF-PG':6, 'PG-SF':6})

#transforma os dados da variavel em porcentagem 
df_nba['TrueShootingPercentage'] = df_nba['TrueShootingPercentage'] = 100
df_nba['FieldGoalPercentage'] = df_nba['FieldGoalPercentage'] = 100
df_nba['TwoPointFieldGoalPercentage'] = df_nba['TwoPointFieldGoalPercentage'] = 100
df_nba['EffectiveFieldGoalPercentage'] = df_nba['EffectiveFieldGoalPercentage'] = 100
df_nba['FreeThrowPercentage'] = df_nba['FreeThrowPercentage'] = 100

df_nba.head(n=2)

#Gera relatórios de perfil de um dataset
profile = ProfileReport(df_nba)
profile.to_widgets()

sns.pairplot(df_nba, hue='WinShares') # criando o pairplot

"""#Sem o scaler
#Divisão entre treino e teste
"""

# split entre treinamento e teste
X_train_win, X_test_win, y_train_win, y_test_win = train_test_split(df_nba.drop('WinShares', axis=1), # aqui informamos os atributos
                                                                        df_nba['WinShares'], # aqui informamos as labels e na mesma ordem dos atributos
                                                                        test_size=0.25, # informamos a porcentagem de divisão da base. Geralmente é algo entre 25% (0.25) a 35% (0.35)
                                                                        random_state=0) # aqui informamos um "seed". É um valor aleatório e usado para que alguns algoritmos i

"""#Treinamento do modelo"""

modelo_knn = KNeighborsRegressor().fit(X_train_win, y_train_win)
modelo_knn.score(X_test_win, y_test_win)

modelo_lr = LinearRegression().fit(X_train_win, y_train_win)
modelo_lr.score(X_test_win, y_test_win)

modelo_svm = SVR().fit(X_train_win, y_train_win)
modelo_svm.score(X_test_win, y_test_win)

"""#Com o scaler
## Divisão entre treino e teste
"""

X_train_win, X_test_win, y_train_win, y_test_win = train_test_split(RobustScaler().fit_transform(df_nba.drop('WinShares', axis=1)), # aqui informamos os atributos
                                                                        df_nba['WinShares'], # aqui informamos as labels e na mesma ordem dos atributos
                                                                        test_size=0.25, # informamos a porcentagem de divisão da base. Geralmente é algo entre 20% (0.20) a 35% (0.35)
                                                                        random_state=0) # aqui informamos um "seed". É um valor aleatório e usado para que a

"""#Treinamento do modelo"""

modelo_knn = KNeighborsRegressor().fit(X_train_win, y_train_win)
modelo_knn.score(X_test_win, y_test_win)

modelo_lr = LinearRegression().fit(X_train_win, y_train_win)
modelo_lr.score(X_test_win, y_test_win)

modelo_svm = SVR().fit(X_train_win, y_train_win)
modelo_svm.score(X_test_win, y_test_win)

"""#PCA"""

pca = PCA().fit(RobustScaler().fit_transform(df_nba.drop('WinShares', axis=1)))
plt.plot(pca.explained_variance_ratio_)

plt.figure(figsize=(15, 5)) # criando um gráfico retangular para facilitar a visualização
plt.plot(pca.explained_variance_ratio_, color='r') # colocando a porcentagem de variância que cada componente nos trouxe
plt.xticks(np.arange(df_nba.shape[1])) # mostrando todos os números no eixo x
plt.show() # mostrando o gráfico final

# split entre treinamento e teste
X_train_win, X_test_win, y_train_win, y_test_win = train_test_split(PCA(n_components=5).fit_transform(RobustScaler().fit_transform(df_nba.drop('WinShares', axis=1))), # aqui informamos os atributos
                                                                        df_nba['WinShares'], # aqui informamos as labels e na mesma ordem dos atributos
                                                                        test_size=0.25, # informamos a porcentagem de divisão da base. Geralmente é algo entre 20% (0.20) a 35% (0.35)
                                                                        random_state=0) # aqui informamos um "seed". É um valor aleatório e usado para que a

modelo_knn = KNeighborsRegressor().fit(X_train_win, y_train_win)
modelo_knn.score(X_test_win, y_test_win)

modelo_lr = LinearRegression().fit(X_train_win, y_train_win)
modelo_lr.score(X_test_win, y_test_win)

modelo_svm = SVR().fit(X_train_win, y_train_win)
modelo_svm.score(X_test_win, y_test_win)

"""Mostrando as previsões"""

modelo_knn.predict(X_test_win)

df_test = pd.DataFrame(X_test_win) #pd.DataFrame(X_test_wine, columns=df_wine.drop('quality', axis=1).columns)
df_test['Quality_Real'] = y_test_win.values
df_test['Quality_Predicao_KNN'] = modelo_knn.predict(X_test_win)
df_test['Quality_Predicao_Linear'] = modelo_lr.predict(X_test_win)
df_test['Quality_Predicao_SVM'] = modelo_svm.predict(X_test_win)
df_test





