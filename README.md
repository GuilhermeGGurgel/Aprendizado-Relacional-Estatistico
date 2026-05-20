# Análise de Risco de Crédito Híbrido em Redes Sociais

Aluno: Guilherme Grijo Gurgel Costa Rego - 22352042
---

## ⚙️ Pré-requisitos

Antes de executar, você precisará ter instalado em sua máquina:
* **Python 3.8+**
* **SWI-Prolog** (O executável precisa estar no PATH do sistema para o `pyswip` funcionar corretamente).

---

## 🚀 Como Executar (How-To)

Siga os passos abaixo para reproduzir a análise:

**Passo 1: Instale as bibliotecas necessárias**
Abra o terminal na pasta do projeto e instale as dependências do Python executando:
`bash
pip install pyswip pandas scikit-learn
`

**Passo 2: Verifique os arquivos**
Certifique-se de que os arquivos `rede_social.pl` (base de regras Prolog) e `dados_financeiros.csv` (dataset de clientes) estão na mesma pasta que o script principal `main.py`.

**Passo 3: Execute o pipeline estatístico-relacional**
No terminal, execute o script principal:
`bash
python main.py
`

---

## 📊 Resultado Esperado

Ao executar o script, o sistema fará a extração do grau de risco lógico e o treinamento estatístico. A saída no terminal deverá ser semelhante a esta:

`text
--- Treinamento Concluído ---
Coeficientes Aprendidos: [[-1.69430252e-02 -2.47733392e-03 -1.19685998e-05]]

--- Saída Relacional Estatística ---
0.00 :: risco(cliente_novo_x) :- conectado_a(cliente_novo_x, daniel, 2).
`

---
