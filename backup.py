import os
import shutil
import time
import tkinter as tk
from tkinter import filedialog, font, messagebox

class EletronicaLj:
    def __init__(self, master):
        self.master = master
        master.title("EletronicaLj")

        # Configurações do rótulo
        label_font = font.Font(size=24)
        self.label = tk.Label(master, text="EletronicaLj", font=label_font, relief="groove")
        self.label.pack(pady=20)

        # Configura um frame para conter os botões de backup e restauração
        button_frame = tk.Frame(master)
        button_frame.pack()

        # Configurações do botão de backup
        self.backup_button = tk.Button(button_frame, text="Fazer Backup", command=self.backup)
        self.backup_button.pack(side="left", padx=5)

        # Configurações do botão de restauração
        self.restore_button = tk.Button(button_frame, text="Restaurar Backup", command=self.restore)
        self.restore_button.pack(side="left", padx=5)

    def backup(self):
        # Seleciona a pasta para salvar o arquivo de backup
        save_dir = filedialog.askdirectory(title="Selecione a pasta para salvar o backup")

        # Gera o nome do arquivo de backup
        timestamp = time.strftime("%Y%m%d-%H%M%S")
        backup_filename = f"gavetario_{timestamp}.db"

        # Copia o arquivo de banco de dados para a pasta de backup com o novo nome
        source_file = os.path.join("banco_de_dados", "gavetario.db")
        dest_file = os.path.join(save_dir, backup_filename)
        shutil.copy(source_file, dest_file)

        # Exibe uma mensagem de conclusão
        message = f"Backup salvo em {dest_file}"
        messagebox.showinfo("Backup concluído", message)

    def restore(self):
        # Seleciona o arquivo de backup para restaurar
        restore_file = filedialog.askopenfilename(title="Selecione o arquivo de backup para restaurar")

        if restore_file:
            # Pergunta ao usuário se ele realmente deseja restaurar o backup
            confirmation = messagebox.askyesno("Confirmar restauração", "Tem certeza que deseja restaurar o backup?")

            if confirmation:
                # Copia o arquivo de backup para o diretório do banco de dados com o nome padrão
                dest_file = os.path.join("banco_de_dados", "gavetario.db")
                shutil.copy(restore_file, dest_file)

                # Exibe uma mensagem de conclusão
                message = f"Backup restaurado de {restore_file} para {dest_file}"
                messagebox.showinfo("Backup restaurado", message)

root = tk.Tk()
app = EletronicaLj(root)
root.geometry("300x200")

# Posiciona o frame dos botões no centro da janela
app.master.eval('tk::PlaceWindow %s center' % app.master.winfo_toplevel())
app.master.update()

root.mainloop()
