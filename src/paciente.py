class Paciente:
    """Representa um paciente cadastrado no sistema."""
    def __init__(self, nome: str, cpf: str, ativo: bool = True):
        self.nome = nome
        if cpf == "" or len(cpf) != 11 or not cpf.isnumeric():
            raise ValueError("CPF inválido.")
        self.cpf = cpf
        self.ativo = ativo
            
