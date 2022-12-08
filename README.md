# Tecnicas-de-Machine-Learning

Criando a sua própria IA – Parte II
Semanas atrás você desenvolveu um notebook em Python na atividade intitulada “Criando a sua 
própria IA – Parte I”. Para lhe relembrar, o contexto da atividade é o seguinte: você entrou para o processo 
seletivo de um programa de estágio de uma grande consultoria. Esta consultoria presta serviços para grandes 
empresas do mundo inteiro, o que inclui empresas de alimentação, de streaming de jogos, na área da saúde, 
do mercado financeiro, entre outros. Sendo assim, eles lhe enviaram algumas bases de dados (também 
chamadas de datasets) para que você pudesse demonstrar os seus conhecimentos ao criar algoritmos de ML 
destinados para elas.
Você recebeu um e-mail explicando que o objetivo disso é o de entender o seu domínio em Python 
aplicado a técnicas de ML – logo, a empresa avaliará a forma pela qual você resolveu o problema, e não 
apenas o resultado do seu algoritmo. Consequentemente, é uma oportunidade para demonstrar o seu 
raciocínio, criatividade e qualidade no processo de desenvolvimento. Este mesmo e-mail possui os seguintes 
detalhes – leia-os atentamente a seguir.
1. O processo seletivo é dividido em duas partes. O trabalho destas duas últimas semanas refere-se à 
segunda parte.
2. A empresa de consultoria nota que os cientistas de dados geralmente trabalham em equipe. Logo, o 
trabalho deverá ser feito em duplas. Não será permitido o desenvolvimento do trabalho de forma 
individual ou em equipes de três ou mais participantes.
3. A mesma dupla que desenvolveu a primeira parte também deverá desenvolver a segunda parte 
(correspondente a esta semana).
4. Da mesma forma, o mesmo dataset que foi utilizado na primeira parte também deverá ser usado 
para a segunda parte. Assim, esta segunda parte será uma continuidade da primeira.
5. Como todo processo seletivo, a avaliação não considera somente o resultado, mas principalmente a 
forma que se chegou ao resultado. Neste sentido, a organização e legibilidade do código são partes 
igualmente importantes no seu trabalho. Também não são toleradas cópias ou quaisquer situações 
que possam qualificar como plágio.
Dito isso, vamos à Parte II do trabalho em si. Você e a sua dupla deverão fazer o seguinte:
1. Crie uma cópia do notebook utilizado na primeira parte para trabalhar nesta segunda parte. Vocês 
continuarão a desenvolver o trabalho em Jupyter e utilizando Python.
2. Quando vocês desenvolveram a Parte I vocês seguiram os seguintes passos:
a. Carregar o dataset;
b. Realizar o passo de preparação dos dados;
c. Realizar a divisão do dataset entre uma base de treinamento e de testes;
d. Realizar o treinamento do algoritmo com um algoritmo de aprendizagem supervisionada;
e. Mostrar as predições para uma base de testes.
 
1
3. Modifique o notebook para que siga os seguintes passos (note somente que alguns passos foram 
invertidos):
a. Carregar o dataset (o mesmo da Parte I);
b. Realizar a divisão do dataset entre uma base de treinamento e de testes;
c. Realizar o passo de preparação dos dados;
d. Realizar o treinamento do algoritmo com um algoritmo de aprendizagem supervisionada (o 
mesmo da Parte I);
e. Mostrar as predições para uma base de testes.
4. Após realizar esta modificação do passo anterior, modifique novamente o notebook para que fique 
da seguinte forma:
a. Carregar o dataset (o mesmo da Parte I);
b. Realizar a divisão do dataset entre uma base de treinamento e de testes;
c. Crie um pipeline o qual inclui os seguintes passos:
i. Preparação dos dados;
ii. Treinamento do algoritmo com um algoritmo de aprendizagem supervisionada (o 
mesmo da Parte I);
d. Mostre as predições do pipeline para uma base de testes.
e. Escolha duas métricas para o tipo de problema que esteja trabalhando (ex.: RMSE, MAE, 
MAPE, MSE para regressão; matriz de confusão, ROC e AUC, precision e recall, balanced 
accuracy e F1 score para classificação) e mostre as métricas a partir da base de testes que 
você selecionou. Problemas de séries temporais podem utilizar as mesmas métricas de 
regressão.
f. Escreva as conclusões da equipe quanto às métricas: os valores são bons ou ruins? Por quê? 
De que forma poderiam melhorar?
5. Não esqueça de deixar o seu notebook apresentável – isto é, divida o seu código em células como 
mostramos anteriormente de uma forma que seja compreensível os diferentes blocos do seu código. 
Utilize também células do tipo markdown (isto é, que permitam códigos em HTML) para explicar 
para pessoas que não entendam de Python o que vocês fizeram durante o trabalho.
6. Entregue três arquivos: o arquivo original do notebook da Parte II (com extensão .ipynb); o mesmo 
notebook em HTML (no Jupyter clique em “File > Export Notebook As... > Export Notebook as HTML” 
ou “File > Download as > HTML”); e o notebook da Parte I em HTML (para fins de comparação)
