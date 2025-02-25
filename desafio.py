#         SEGUNDA ETAPA DO DESAFIO AFL PARA ESTAGIÁRIO:

# 1. O CPF deve ser validado.
# 2. Deverá realizar um script que insira 10000 usuários randomizados;
# 3. Deverá realizar uma análise com pandas para ter as seguintes informações:
#         - Quantos Nomes diferentes existem ?
#         - Qual a Menor, Maior idade E média de idade ?
#         - Qual a distribuição do Sexo da sua base de análise ?
 
# 4. Faça um script para construir pares de pessoas onde o par deve respeitar regras:
#        1. A diff de idades deve ser menor que 10 anos
#        2. Só pode ter par com final de CPF par com par e impar com impar
#        3. Os que não tiverem par, devem ser organizados por nome e idade e realizar par em sequencia, ou seja o 1° com o 2°, 3°com o 4°e assim sucessivamente.
#        4. Os Pares devem ser indicados por qual regra foram montados.


import pandas as pd
import random
from faker import Faker
from validate_docbr import CPF


fake = Faker("pt_BR")
cpf_validator = CPF()

usuarios = {}

def gerar_usuarios_aleatorios(qtd=10000):
    global usuarios
    usuarios = {}
    while len(usuarios) < qtd:
        nome = fake.first_name() + " " + fake.last_name()
        cpf = cpf_validator.generate()
        idade = random.randint(12, 100)
        sexo = random.choice(["Masculino", "Feminino"])
        
        if cpf not in usuarios:
            usuarios[cpf] = {"Nome": nome, "Idade": idade, "Sexo": sexo}

gerar_usuarios_aleatorios()

def analisar_dados():
    df = pd.DataFrame.from_dict(usuarios, orient='index')
    print("\n------ ANÁLISE DE DADOS ------")
    #.nunique() conta quantos nomes diferentes existem.
    print(f"Nomes Diferentes: {df['Nome'].nunique()}")
    print(f"Idade Mínima: {df['Idade'].min()}")
    print(f"Idade Máxima: {df['Idade'].max()}")
    print(f"Média de Idade: {df['Idade'].mean():.2f}")
    #.value_counts() conta quantos usuários são Masculinos e Femininos.
    print(df['Sexo'].value_counts().to_string())

analisar_dados()

def formar_pares():
    df = pd.DataFrame.from_dict(usuarios, orient='index')
    df['CPF'] = df.index
    df['CPF_Final'] = df['CPF'].apply(lambda x: int(x[-1]))
    df_par = df[df['CPF_Final'] % 2 == 0].sort_values(by='Idade')
    df_impar = df[df['CPF_Final'] % 2 != 0].sort_values(by='Idade')
    
    pares = []
    usados = set()
    
    def encontrar_par(df_base, regra):
        # df_base.iterrows() percorre linha por linha do DataFrame.
        for i, user in df_base.iterrows():
            if i in usados:
                continue
                                                       #~df_base.index.isin(usados) filtra apenas usuários ainda não pareados.
            candidato = df_base[(df_base.index != i) & (~df_base.index.isin(usados)) & (abs(df_base['Idade'] - user['Idade']) < 10)]
            if not candidato.empty:
                par_id = candidato.index[0]
                pares.append((user['CPF'], user['Nome'], user['Idade'], par_id, df_base.loc[par_id, 'Nome'], df_base.loc[par_id, 'Idade'], regra))
                usados.add(i)
                usados.add(par_id)
    
    encontrar_par(df_par, "CPF Par e diferença < 10 anos")
    encontrar_par(df_impar, "CPF Ímpar e diferença < 10 anos")
    
    sobraram = df[~df.index.isin(usados)].sort_values(by=['Nome', 'Idade'])
    if len(sobraram) > 1:
        for i in range(0, len(sobraram)-1, 2):
            pares.append((sobraram.index[i], sobraram.iloc[i]['Nome'], sobraram.iloc[i]['Idade'], sobraram.index[i+1], sobraram.iloc[i+1]['Nome'], sobraram.iloc[i+1]['Idade'], "Pares sequenciais"))
    
    df_pares = pd.DataFrame(pares, columns=["CPF 1", "Nome 1", "Idade 1", "CPF 2", "Nome 2", "Idade 2", "Regra"])
    print("\n------------------------------------------------------ PARES FORMADOS ------------------------------------------------------")
    print(df_pares.head(5000))
    return df_pares

pares = formar_pares()
