import customtkinter
from tkinter import Label, Tk, ttk
import tkinter
import calendar



# Classe para um campo de entrada personalizado com suporte a texto de espaço reservado
class CustomTkinterEntry(ttk.Entry):
    def __init__(self, master=None, **kwargs):
        ttk.Entry.__init__(self, master, **kwargs)
        self.placeholder_text = kwargs.get('placeholder_text', '')
        self.insert(0, self.placeholder_text)
        self.bind("<FocusIn>", self.clear_placeholder)
        self.bind("<FocusOut>", self.restore_placeholder)
        self.restore_placeholder(None)

    def clear_placeholder(self, event):
        if self.get() == self.placeholder_text:
            self.delete(0, tkinter.END)

    def restore_placeholder(self, event):
        if not self.get():
            self.insert(0, self.placeholder_text)

# Classes para botão e rótulo personalizados
class CustomTkinterButton(ttk.Button):
    pass

class CustomTkinterLabel(ttk.Label):
    pass

# Classe principal para a aplicação tkinter
class CustomTkinter(Tk):
    pass

# Função para mostrar o calendário
def mostrar_calendario():
    # Obter o ano e mês a partir dos campos de entrada
    year = int(ano_entry.get())
    month = int(mes_entry.get())

    # Obter a matriz do calendário
    cal_matrix = calendar.monthcalendar(year, month)

    # Criar uma tabela para exibir o calendário
    for row_idx, week in enumerate(cal_matrix):
        for col_idx, day in enumerate(week):
            if day == 0:
                day_str = ""
            else:
                day_str = str(day)

            # Criar rótulos para cada dia
            cell_label = Label(calendario_frame, text=day_str, width=4, font=('arial 14'), background='#EEEEFB')
            cell_label.grid(row=row_idx + 1, column=col_idx, padx=2, pady=2)  # Adicionando 1 a row_idx para acomodar os rótulos dos dias da semana

janela = customtkinter.CTk()
janela.geometry('325x325+100+100')
janela.resizable(False, False)
janela.title('Calendario Dev Joel 2023')
janela.iconbitmap(r'C:\Users\HP\Desktop\Programas em python\Calendario\Dev Joel\icon.ico')

# Widgets
ano_entry = customtkinter.CTkEntry(janela, placeholder_text='ano')
ano_entry.grid(row=1, column=0, padx=5, pady=5)

mes_entry = customtkinter.CTkEntry(janela, placeholder_text='Mês')
mes_entry.grid(row=1, column=1, padx=5, pady=5)

calendario_frame = ttk.Frame(janela)
calendario_frame.place(x=10, y=130)

botao_mostrar = customtkinter.CTkButton(janela, text="Mostrar Calendário", command=mostrar_calendario)
botao_mostrar.place(x=40, y=55)

dias_da_semana = ["Seg", "Ter", "Qua", "Qui", "Sex", "Sáb", "Dom"]
for col_idx, dia_semana in enumerate(dias_da_semana):
        dia_semana_label = CustomTkinterLabel(calendario_frame, text=dia_semana, font=('arial', 14), background='#C5D0E3')
        dia_semana_label.grid(row=0, column=col_idx, padx=2, pady=2)  # Usar grid em vez de place






janela.mainloop()