class SessaoService:

    def validar_publico(self, publico, capacidade):
        if publico > capacidade:
            raise Exception(
                "O público não pode ultrapassar a capacidade do cinema."
            )

        return True
