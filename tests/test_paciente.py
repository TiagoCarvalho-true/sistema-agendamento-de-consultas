import pytest
from src.paciente import Paciente

def test_criacao_paciente_valido():
    p = Paciente("Maria", "12345678901")
    assert p.nome == "Maria"
    assert p.cpf == "12345678901"
    assert p.ativo is True
