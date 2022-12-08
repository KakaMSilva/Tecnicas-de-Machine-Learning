# -*- coding: utf-8 -*-
"""Ml Parte III

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1wAmlmLPSdLtgN5G2ze6Gfzin1CKyTuWm

# **Carregar o dataset**
"""

import pandas as pd # importando o pandas para manipularmos o dataset
import numpy as np # biblioteca para manipulação de vetores e matrizes grandes além de outras manipulações de dados de larga escala
import seaborn as sns # importando o Seaborn para visualizar o comportamento dos dados
import matplotlib.cm as mcm # biblioteca para mostrar gráficos (espeficamente uma parte para cores)
import matplotlib.pyplot as plt # importando o Matplotlib para o elbow method
import pandas_profiling

from pandas_profiling import ProfileReport # importando o pandas-profiling para fazer o profile do dataset
from sklearn.model_selection import train_test_split, RandomizedSearchCV, GridSearchCV# utilizado para o split entre treinamento e teste
from sklearn.neighbors import KNeighborsRegressor # KNN para regressão
from sklearn.neighbors import KNeighborsClassifier # utilizado para treinar o KNN
from sklearn.linear_model import LinearRegression, LogisticRegression # Regressão linear, utilizado para treinar um modelo de classificação (regressão logística - apesar do nome é para problemas de classificação)
from sklearn.svm import SVR # SVM para regressão
from sklearn.decomposition import PCA # PCA como aprendizagem não-supervisionada
from sklearn.preprocessing import RobustScaler, OrdinalEncoder, OneHotEncoder # utilizado para que todas as entradas estejam na mesma escala numérica
from sklearn.preprocessing import StandardScaler
from sklearn.feature_selection import * # importando todas as funções específicas de seleção de atributos do scikit-learn
from sklearn.decomposition import * # importando todas as funções específicas para a extração de atributos do scikit-learn
from sklearn.cluster import * # importando todas as funções específicas para o agrupamento
from sklearn.ensemble import * # importando vários ensembles para que possamos testá-los posteriormente
from sklearn.pipeline import Pipeline # utilizado para criar pipelines
from sklearn.metrics import f1_score, make_scorer # utilizado para calcular a performance dos pipelines
from lightgbm import LGBMClassifier # utilizado para treinar o LightGBM
from sklearn import set_config # utilizado para mostrar os passos do pipeline de forma visual
from sklearn.impute import SimpleImputer
from sklearn.metrics import *

set_config(display='diagram') # forçando para que os passos do pipeline sejam mostrados em visual

#seleção do dataset
df_nba = pd.read_csv('/content/nba_stats.csv') #carrega o dataset do diretorio 
df_nba.describe() #mostra destacaria os dados
#display(df_nba.columns)

"""# **Divisão do dataset**"""

# criando uma cópia do dataset para fins de teste
df_nba_copy = df_nba[~pd.isnull(df_nba["WinShares"])].copy()
df_nba_copy

# split entre treinamento e teste
X_train, X_test, y_train, y_test = train_test_split(df_nba_copy.drop('WinShares', axis=1), # aqui informamos os atributos
                                                    df_nba_copy['WinShares'], # aqui informamos as labels e na mesma ordem dos atributos
                                                    test_size=0.25, # informamos a porcentagem de divisão da base. Geralmente é algo entre 20% (0.20) a 35% (0.35)
                                                    random_state=0) # aqui informamos um "seed". É um valor aleatório e usado para que alguns algoritmos iniciem de forma aleatória a sua divisão.

"""# **Pipelines sem scaler**"""

classifiers_list = [
    KNeighborsRegressor(),
    LinearRegression(),
    SVR()
]

for classifier in classifiers_list:
    pipe = Pipeline(steps=[('encoder', OrdinalEncoder(handle_unknown='use_encoded_value', unknown_value=-1)), ('impmean', SimpleImputer(missing_values=np.nan, strategy='mean')), ("classifier", classifier)])
    pipe.fit(X_train, y_train)
    print(classifier)
    print("Resultados do score: %.3f" % pipe.score(X_test, y_test))
    
    y_pred_sc = pipe.predict(X_test)
    display(f'Resultados de predict: {y_pred_sc}')
    display(f'Resultados real: {y_test.values}')
    display(f'R2: {r2_score(y_test, y_pred_sc)}')
    display(f'MAE: {mean_absolute_error(y_test, y_pred_sc)}')
    display(f'MSE: {mean_squared_error(y_test, y_pred_sc)}')
    display(f'RMSE: {mean_squared_error(y_test, y_pred_sc, squared=False)}')
    display(f'MAPE: {mean_absolute_percentage_error(y_test, y_pred_sc)}')

"""# **Pipelines com scaler**"""

classifiers_list = [
    KNeighborsRegressor(),
    LinearRegression(),
    SVR()
]

for classifier in classifiers_list:
    pipe = Pipeline(steps=[('encoder', OrdinalEncoder(handle_unknown='use_encoded_value', unknown_value=-1)), ('impmean', SimpleImputer(missing_values=np.nan, strategy='mean')), ('scaler', RobustScaler()), ("classifier", classifier)])
    pipe.fit(X_train, y_train)
    print(classifier)
    print("Resultados do score: %.3f" % pipe.score(X_test, y_test))
    
    y_pred_cs = pipe.predict(X_test)
    display(f'Resultados de predict: {y_pred_cs}')
    display(f'Resultados real: {y_test.values}')
    display(f'R2: {r2_score(y_test, y_pred_cs)}')
    display(f'MAE: {mean_absolute_error(y_test, y_pred_cs)}')
    display(f'MSE: {mean_squared_error(y_test, y_pred_cs)}')
    display(f'RMSE: {mean_squared_error(y_test, y_pred_cs, squared=False)}')
    display(f'MAPE: {mean_absolute_percentage_error(y_test, y_pred_cs)}')

"""#**PCA**"""

classifiers_list = [
    KNeighborsRegressor(),
    LinearRegression(),
    SVR()
]

for classifier in classifiers_list:
    pipe = Pipeline(steps=[('encoder', OrdinalEncoder(handle_unknown='use_encoded_value', unknown_value=-1)), ('impmean', SimpleImputer(missing_values=np.nan, strategy='mean')), ('pca', PCA(n_components=5)), ("classifier", classifier)])
    pipe.fit(X_train, y_train)
    print(classifier)
    print("Resultados do score: %.3f" % pipe.score(X_test, y_test))
    
    y_pred_pca = pipe.predict(X_test)
    display(f'Resultados de predict: {y_pred_pca}')
    display(f'Resultados real: {y_test.values}')
    display(f'R2: {r2_score(y_test, y_pred_pca)}')
    display(f'MAE: {mean_absolute_error(y_test, y_pred_pca)}')
    display(f'MSE: {mean_squared_error(y_test, y_pred_pca)}')
    display(f'RMSE: {mean_squared_error(y_test, y_pred_pca, squared=False)}')
    display(f'MAPE: {mean_absolute_percentage_error(y_test, y_pred_pca)}')

"""# **Conclusão**

LinearRegression(), apresentou a melhor previsão
"""