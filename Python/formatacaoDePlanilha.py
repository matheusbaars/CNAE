

def geraPlanilha():
    import pandas as pd
    import easygui
    try:
        #easygui.msgbox("This is a message!", title="simple gui")
        df = pd.read_csv('C:\\Users\\Matheus\\Documents\\UiPath\\teste\\cnae.csv', sep=',')

        descricao = ['Secção', 'Divisão', 'Grupo', 'Classe', 'Subclasse']

        # lowercase
        for column in df.columns:
            if column != 'Codigo Secção':        
                df[column] = df[column].astype(str).str.lower()

        # Remove acentos
        for column in descricao:
            df[column] = df[column].str.normalize('NFKD').str.encode('ascii', errors='ignore').str.decode('utf-8')

        # Deixa apenas o texto
        for column in descricao:
            df[column] = df[column].astype(str).str.replace('(\d|[.]|-|\/)', '')


        # In[219]:


        # Remove texto de código de classe
        df['Código Classe'] = df['Código Classe'].astype(str).str.normalize('NFKD').str.encode('ascii', errors='ignore').str.decode('utf-8')
        df['Código Classe'] = df['Código Classe'].astype(str).str.replace('([a-zA-Z])', '')

        # Deixa apenas os números das colunas de códigos
        colunasCodigos = ['Código Divisão', 'Código Grupo', 'Código Classe', 'Código Subclasse']
        for column in colunasCodigos:
            df[column] = df[column].astype(str).str.replace('([.]|-|\/)', '')

        print(df.head(2))
        # Gerar planilha Excel
        #easygui.msgbox("gerar", title="simple gui")
        df.to_excel('C:\\Users\\Matheus\\Documents\\UiPath\\teste\\resultado\\cnae.xlsx', sheet_name='cnae', index=False)
    except Exception as e:
        print(e)

    return str('Planilha gerada com sucesso.')
#geraPlanilha()





