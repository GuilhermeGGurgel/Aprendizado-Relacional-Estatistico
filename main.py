from pyswip import Prolog
import pandas as pd
from sklearn.linear_model import LogisticRegression
import warnings
warnings.filterwarnings('ignore') 

# ---------------------------------------------------------
# Parte 1: Extraindo Features Lógicas com pyswip
# ---------------------------------------------------------
prolog = Prolog()
prolog.consult("rede_social.pl") 

df = pd.read_csv("dados_financeiros.csv")

def obter_grau_risco(nome):
   
    query = list(prolog.query(f"risco_conexao({nome}, daniel, Grau)"))
    if query:
        return query[0]["Grau"] 
    return 999 

df['grau_risco_rede'] = df['cliente_id'].apply(obter_grau_risco)

# ---------------------------------------------------------
# Parte 2: Treinando o Classificador Estatístico
# ---------------------------------------------------------
X = df[['renda_mensal', 'score_classico', 'grau_risco_rede']]
y = df['inadimplente_historico']

modelo = LogisticRegression()
modelo.fit(X, y)

print("--- Treinamento Concluído ---")
print("Coeficientes Aprendidos:", modelo.coef_)

# ---------------------------------------------------------
# Parte 3: Teoria Neuro-Simbólica 
# ---------------------------------------------------------
cliente_novo_x = [[4000, 600, 2]] 

prob = modelo.predict_proba(cliente_novo_x)[0][1]

print("\n--- Saída Relacional Estatística ---")
print(f"{prob:.2f} :: risco(cliente_novo_x) :- conectado_a(cliente_novo_x, daniel, 2).")