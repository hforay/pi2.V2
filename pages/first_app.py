import streamlit as st
# To make things easier later, we're also importing numpy and pandas for
# working with sample data.
import numpy as np
import pandas as pd
import time
import matplotlib.pyplot as plt
from yahoofinancials import YahooFinancials


#""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
import matplotlib.pyplot as plt
from yahoofinancials import YahooFinancials
@st.cache
def random_weights(n): #permet de créer un vecteur de taille n avec somme(xi)=1
    k=np.random.rand(n)
    return k/sum(k)
@st.cache
def component(returns):
    weights=np.asmatrix(random_weights(returns.shape[0])) #création d'un vecteur de poids, de taille=nombre d'instruments financiers
    p=np.asmatrix(np.mean(returns,axis=1)) #création d'un vecteur de rendement des stocks
    cov=np.asmatrix(np.cov(returns)) #matrice de covariance
    mu=np.dot(p.T,weights.T) #calcul du rendement du portefeuille
    sigma=np.sqrt(np.dot(weights,np.dot(cov,weights.T))) #calcul de l'écart-type du portefeuille
    return mu,sigma,weights
 
n_portfolios=5000 #Possibilité de changer le nombre de portefeuilles à étudier
 

#"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""



st.title('My first app')
st.write("Here's our first attempt at using data to create a table:")
st.write(pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
}))
df = pd.DataFrame({
  'first column': [1, 2, 3, 4],
  'second column': [10, 20, 30, 40]
})

df
chart_data = pd.DataFrame(
     np.random.randn(20, 3),
     columns=['a', 'b', 'c'])

st.line_chart(chart_data)
map_data = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.76, -80.4],
    columns=['lat', 'lon'])

st.map(map_data)
if st.checkbox('Show dataframe'):
    chart_data = pd.DataFrame(
       np.random.randn(20, 3),
       columns=['a', 'b', 'c'])

    chart_data
    
@st.cache
def EfficientPortfolio():
    ticker=[]
    res=True
    data=pd.DataFrame()
    while res==True:
        path1 = st.text_input("Quel stock souhaitez-vous avoir dans votre portefeuille ?")
        choice=str(path1) 
        #il faut récupérer les noms sur yahoo 
        #finance pour que ça corresponde avec l'écriture dans data[ticker]
        ticker.append(choice)
        path2 = st.text_input("Souhaitez vous ajouter de nouveaux stocks à votre portefeuille ? (oui/non)")
        choice2=str(path2)
        if choice2.lower()=="non":
            res=False
        path3 = st.date_input("Quelle est la date de début de l'étude ? (format AAAA-MM-DD)")
        start1 = path3.strftime("%Y-%m-%d")
         #Faire attention de bien rentrer la date pour permettre au calcul de se faire, ex : 2020-12-28
        path4 = st.date_input("Quelle est la date de fin de l'étude ? (format AAAA-MM-DD)")
        end1 = path4.strftime("%Y-%m-%d")
        yahoo_financials = YahooFinancials(choice)
        data_init = yahoo_financials.get_historical_price_data(start_date=start1, end_date=end1, time_interval='weekly')
        st.write(data_init[choice])
        ticker1 = pd.DataFrame(data_init[choice]['prices'])
        ticker1 = ticker1.drop('date', axis=1).set_index('formatted_date')
        data[choice]=ticker1['adjclose']
    returns=data.pct_change()
    returnTranspose=np.matrix(returns[1:]).T #On prend return[1:] car la première ligne est composée de "nan" car la formule du rendement dépend du jour précédent qui n'est pas disponible pour le premier jour de l'étude
    means=[]
    stds=[]
    weights=[]
    for i in range(n_portfolios):
            meansfloat,stdsfloat,weightsfloat=component(returnTranspose) #Création des vecteurs de rendement, écart-type et poids
            meansfloat=np.array(meansfloat)[0] #les 4 prochaines lignes permettent de convertir une matrice de taille 1,1 en float
            stdsfloat=np.array(stdsfloat)[0]
            means.append(meansfloat[0])
            stds.append(stdsfloat[0])
            weights.append(weightsfloat)
    dataessai={'Returns':means,'Volatility':stds}
    portfolios=pd.DataFrame(dataessai)
    
    path=st.text_input("Quel est le rendement sans risque que vous souhaitez ?")
    rf = float(path)
    
    optimal_port=portfolios.iloc[((portfolios['Returns']-rf)/portfolios['Volatility']).idxmax()] #On calcule le portefeuille efficient à l'aide du ratio de Sharpe, on cherche donc le portefeuille avec un rendement "éloigné positivement" du rendement sans risque et avec une volatilité faible
    opt_weights=[]
    for i in range(len(means)):
            if(means[i]==optimal_port[0]):
                opt_weights.append(weights[i]) #On cherche notre vecteur de poids correspondant
    plt.plot(stds,means,'o')
    plt.plot(optimal_port[1],optimal_port[0],marker='+',color='red') #On affiche les n_portfolios points ainsi que le point du portefeuille efficient en rouge
    plt.show()
    rep=""
    for i in range(len(ticker)):
            opt_weightsfloat=np.array(opt_weights)[0]
            st.write(ticker)
            st.write(opt_weightsfloat[0])
            rep+="\nLe poids à allouer pour le stock "+ticker[i]+" est "+str(opt_weightsfloat[0][i]) #Affichage pour la compréhension de l'utilisateur
    st.write(rep)
    


path = st.text_input('label')
if path:
    st.write(type(path))

my_date = st.date_input("Select date")
my_new_date = my_date.strftime("%Y-%m-%d")
st.write(my_new_date)
st.write(type(my_new_date))

option = st.sidebar.selectbox(
    'Which number do you like best?',
     df['first column'])

'You selected:', option

left_column, right_column = st.columns(2)
pressed = left_column.button('Press me?')
if pressed:
  right_column.write("Woohoo!")
  left_column.write("njbjbbj")

expander = st.expander("FAQ")
expander.write("Here you could put in some really, really long explanations...")
'Starting a long computation...'

# Add a placeholder
latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
  # Update the progress bar with each iteration.
  latest_iteration.text(f'Iteration {i+1}')
  bar.progress(i + 1)
  time.sleep(0.1)

'...and now we\'re done!'