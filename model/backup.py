
# Crie uma janela Tkinter vazia
def cria_backup():
    import tkinter as tk
    from tkinter import filedialog
    import shutil
    import datetime
    import os
    
    root = tk.Tk()
    root.withdraw()
    # Abre o gerenciador de arquivos para selecionar o arquivo de origem
    file_path = filedialog.askopenfilename()

    # Obter a data e hora atual para adicionar ao nome do arquivo de backup
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

    # Cria o nome do arquivo de backup
    backup_name = os.path.basename(file_path) + '_' + timestamp + '.bak'

    # Abre o gerenciador de arquivos para selecionar a pasta de destino para o arquivo de backup
    folder_selected = filedialog.askdirectory()

    # Copia o arquivo selecionado para a pasta de destino com o nome do arquivo de backup
    shutil.copy(file_path, os.path.join(folder_selected, backup_name))

    print('Arquivo de backup criado com sucesso.')

cria_backup()

