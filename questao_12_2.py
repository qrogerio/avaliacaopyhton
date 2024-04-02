import flet as ft
def main(page:ft.Page):
    mensagem = ft.Text("Converter nome para letras maiúsculas")
    nome = ft.TextField(label="Digite o seu nome: ")

    def btn_click(e):
        nome_mai = ft.Text(nome.value.upper())
        nome.value = ""
        page.add(nome_mai)
        page.update()

    btn= ft.ElevatedButton("Converter para maiúsculas", on_click=btn_click)
    page.update()
    page.add(mensagem, nome, btn)
            


ft.app(main)
