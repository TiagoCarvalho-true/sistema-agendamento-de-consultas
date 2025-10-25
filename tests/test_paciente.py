import pytest
from src.paciente import Paciente

def test_criacao_paciente_valido():
    p = Paciente("Maria", "12345678901")
    assert p.nome == "Maria"
    assert p.cpf == "12345678901"
    assert p.ativo is True

def test_cpf_invalido():
    with pytest.raises(ValueError):
        Paciente("João", "123456")

def test_cpf_com_letras():
    with pytest.raises(ValueError):
        Paciente("João", "123abc45678")

def test_cpf_vazio():
    with pytest.raises(ValueError):
        Paciente("João", "")