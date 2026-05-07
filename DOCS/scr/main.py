from repositories.cinema_repository import CinemaRepository
from repositories.filme_repository import FilmeRepository
from repositories.sessao_repository import SessaoRepository

from views.sessao_view import SessaoView

def create_tables():

    CinemaRepository().create_table()
    FilmeRepository().create_table()
    SessaoRepository().create_table()

def main():

    create_tables()

    view = SessaoView()
    view.menu()

if __name__ == "__main__":
    main()
