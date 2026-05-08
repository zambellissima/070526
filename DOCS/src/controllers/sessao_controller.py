from repositories.sessao_repository import SessaoRepository
from services.sessao_service import SessaoService
from models.sessao import Sessao

class SessaoController:

    def __init__(self):
        self.repository = SessaoRepository()
        self.service = SessaoService()

    def criar_sessao(
        self,
        data,
        horario,
        publico,
        cinema_id,
        filme_id,
        capacidade
    ):

        self.service.validar_publico(publico, capacidade)

        sessao = Sessao(
            None,
            data,
            horario,
            publico,
            cinema_id,
            filme_id
        )

        self.repository.insert(sessao)

        print("Sessão criada com sucesso.")
