
#Instalação e importação

import pandas as pd

#Data frame e series

dados = {
      "Nome": ["Ana","Bruno","Carlos"],
      "Idade": [25,47,32]
}

df = pd.DataFrame(dados)
display(df)

s = pd.Series([10,20,30])
s

#Lendo tabelas

df = pd.read_csv("funcionarios.csv") #lendo csv, caso fosse excel necessario alterar read_excel e extensão do arquivo
df

#Manipulação basica de dados

df.head() #5 primeiros

df.tail() #5 ultimos

df[["Nome","Idade"]]  #selecionando colunas

df["Idade"] #apenas uma coluna

df["Idade"] > 30  #series booleanas

#Filtrando

df[df["Idade"]> 30]  #utilizando como FILTRO

df[df["Salário"] > 5000]  #filtrando salarios maiores que 5000 dentro do df

#Combinando filtros

filtro_idade = df["Idade"] > 30
filtro_salario = df["Salário"] > 5000
df[filtro_idade & filtro_salario]

#Criando e removendo colunas

df["Salario Anual"] = df["Salário"] * 12   #passo a coluna que vou criar, e utilizo uma existente para retornar o valor
df

df

#removendo a coluna

df = df.drop("Salario Anual", axis=1)  #axis=1 identifica que é uma coluna

#Resumindo dados

df.info() #retorna tipo de dados

df.describe() #resumo estatistico, média, std desvio padrao, minimo, mediana e maxima.

df["Salário"].sum()  #soma de todos salarios

df["Salário"].mean()  #media

#Limpeza de dados

df2 = pd.read_csv("funcionarios_nulos.csv")
df2

df2.dropna() #remove linhas com valores nulos

df2.dropna(subset="Idade") #remove valores nulos só da coluna informada

idade_media = df2["Idade"].mean()
df2["Idade"] = df2["Idade"].fillna(idade_media) #preenche valores nulos com a media
df

df2["Idade"] = df2["Idade"].astype(int) #era float,converte para inteiro

#Contando Ocorrencias

df = pd.read_csv("funcionarios.csv")
df

df["Ativo"].value_counts()  #quanto tem de funcionario ativos e não ativos

df["ID Departamento"].value_counts()  #quantos funcionarios por departamento

#Operações de agregação

df.groupby("ID Departamento")  #groupby

df.groupby("ID Departamento")["Salário"].sum()  #agrupando por departamento e somando salario de todos de cada departamento

df.groupby("ID Departamento")["Salário"].max()  #maior salario de cada departamento

#Ordenando dados

df.sort_values(by="Salário")  #ordenando dados do menor salario para o maior

df.sort_values(by="Salário", ascending=False) #ordenando salario do maior para o menor, ascending false está mostrando que nao é crescente, mas sim decrescente

#Combinando dados de dois dataframes

df_deptos = pd.read_csv("departamentos.csv")
df_deptos

df_final = pd.merge(df, df_deptos, left_on="ID Departamento", right_on="ID Departamento")  #juntando DF como uma nova coluna e sinalizando o relacionamento das duas tabelas
df_final

df_novos = pd.read_csv("novos_funcionarios.csv")
df_novos

df_todos = pd.concat([df,df_novos], ignore_index=True)  #concatenando dois data frames
df_todos

#Escrevendo dados em arquivos

df_todos.to_csv("Todos_funcionarios.csv") #exportando para csv
