from controllers.sessao_controller import SessaoController

class SessaoView:

    def __init__(self):
        self.controller = SessaoController()

    def menu(self):

        print("=== CADASTRO DE SESSÃO ===")

        data = input("Data: ")
        horario = input("Horário: ")
        publico = int(input("Público: "))
        cinema_id = int(input("ID Cinema: "))
        filme_id = int(input("ID Filme: "))
        capacidade = int(input("Capacidade do cinema: "))

        self.controller.criar_sessao(
            data,
            horario,
            publico,
            cinema_id,
            filme_id,
            capacidade
        )
