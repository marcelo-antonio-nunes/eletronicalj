import pandas as pd
from model.placa import Placa
from sqlitehelper.database import DatabaseHelper
from model.placa import Placa
from tkinter import Tk, filedialog

db = DatabaseHelper()

   

def cadastrar_placas_from_file():
    # Abrir o navegador de arquivos para selecionar a planilha
    root = Tk()
    root.withdraw()  # Esconde a janela principal
    file_path = filedialog.askopenfilename(title="Selecione o arquivo da planilha", filetypes=[("Arquivos do Excel", "*.xlsx;*.xls")])
    # Verificar se o usuário selecionou um arquivo
    if not file_path:
        print("Nenhum arquivo selecionado. Operação cancelada.")
        return
    # Carregar o DataFrame a partir do arquivo selecionado
    try:
        df = pd.read_excel(file_path)
    except Exception as e:
        print(f"Erro ao ler o arquivo: {e}")
        return
    # Iterar sobre as linhas do DataFrame e cadastrar as placas
    for index, row in df.iterrows():
        if row.iloc[index]:
            placa = Placa(row['caixa'], row['marca'], row['modelo'], row['tipo'], row['codigo'], row['quantidade'], row['foto'])
            db.cadastar_placas(placa)
    print("Cadastro de placas concluído com sucesso!")

cadastrar_placas_from_file()


