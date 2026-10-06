import customtkinter as ctk

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.geometry("500x350")
app.title("Minha aplicação")

titulo = ctk.CTkLabel(
    app,
    text="Olá, CustomTkinter!",
    font=("Arial", 24)
)
titulo.pack(pady=30)

entrada = ctk.CTkEntry(
    app,
    placeholder_text="Digite seu nome"
)
entrada.pack(pady=10)

def clicar():
    nome = entrada.get()
    resultado.configure(text=f"Olá, {nome}!")

botao = ctk.CTkButton(
    app,
    text="Enviar",
    command=clicar
)
botao.pack(pady=10)

resultado = ctk.CTkLabel(app, text="")
resultado.pack(pady=20)

app.mainloop()