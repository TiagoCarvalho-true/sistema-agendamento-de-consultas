import pytest
from src.agendamento import Agendamento
from src.medico import Medico
from src.paciente import Paciente
from datetime import datetime, timedelta

def _fmt(dt):
    return dt.strftime("%d/%m/%Y %H:%M")

def test_criacao_agendamento_valido():
    futuro = _fmt(datetime.now() + timedelta(days=30))
    m = Medico("Dr. Teste", "Geral")
    m.adicionar_horario(futuro)
    p = Paciente("Paciente", "12345678901", ativo=True)
    ag = Agendamento(p, m, futuro)
    assert ag.medico is m
    assert ag.paciente is p
    assert ag.horario == futuro
    assert ag.status == "CRIADO"

def test_confirmar_agendamento_valido():
    futuro = _fmt(datetime.now() + timedelta(days=31))
    m = Medico("Dr. Teste", "Geral")
    m.adicionar_horario(futuro)
    p = Paciente("Paciente2", "09876543210", ativo=True)
    ag = Agendamento(p, m, futuro)
    ag.confirmar()
    assert ag.status == "CONFIRMADO"
    assert not m.disponivel(futuro)

def test_cancelar_agendamento_confirmado_devolve_horario():
    futuro = _fmt(datetime.now() + timedelta(days=32))
    m = Medico("Dr. Teste", "Geral")
    m.adicionar_horario(futuro)
    p = Paciente("Paciente3", "11122233344")
    ag = Agendamento(p, m, futuro)
    ag.confirmar()
    assert not m.disponivel(futuro)
    ag.cancelar()
    assert ag.status == "CANCELADO"
    assert m.disponivel(futuro)

def test_cancelar_agendamento_criado_nao_devolve_horario():
    futuro = _fmt(datetime.now() + timedelta(days=33))
    m = Medico("Dr. Teste", "Geral")
    m.adicionar_horario(futuro)
    p = Paciente("Paciente3", "11122233344")
    ag = Agendamento(p, m, futuro)
    ag.cancelar()
    assert ag.status == "CANCELADO"
    # O horário não foi removido, então ainda deve estar disponível
    assert m.disponivel(futuro)

def test_confirmar_agendamento_horario_indisponivel_levanta_erro():
    futuro = _fmt(datetime.now() + timedelta(days=34))
    m = Medico("Dr. Teste", "Geral")
    p = Paciente("Paciente4", "22233344455")
    ag = Agendamento(p, m, futuro) # Horário não existe na agenda do médico
    with pytest.raises(ValueError):
        ag.confirmar()

def test_confirmar_agendamento_paciente_inativo_levanta_erro():
    futuro = _fmt(datetime.now() + timedelta(days=35))
    m = Medico("Dr. Teste", "Geral")
    m.adicionar_horario(futuro)
    p = Paciente("Paciente Inativo", "55566677788", ativo=False)
    ag = Agendamento(p, m, futuro)
    with pytest.raises(ValueError, match="Horário não disponível ou paciente inativo."):
        ag.confirmar()

def test_realizar_agendamento_valido():
    futuro = _fmt(datetime.now() + timedelta(days=36))
    m = Medico("Dr. Teste", "Geral")
    m.adicionar_horario(futuro)
    p = Paciente("Paciente Realizado", "66677788899")
    ag = Agendamento(p, m, futuro)
    ag.confirmar()
    ag.realizar()
    assert ag.status == "REALIZADO"

def test_realizar_agendamento_nao_confirmado_levanta_erro():
    futuro = _fmt(datetime.now() + timedelta(days=37))
    m = Medico("Dr. Teste", "Geral")
    m.adicionar_horario(futuro)
    p = Paciente("Paciente Nao Confirmado", "77788899900")
    ag = Agendamento(p, m, futuro) # Status é CRIADO
    with pytest.raises(ValueError, match="Agendamento não confirmado."):
        ag.realizar()

def test_cancelar_agendamento_realizado_levanta_erro():
    futuro = _fmt(datetime.now() + timedelta(days=38))
    m = Medico("Dr. Teste", "Geral")
    m.adicionar_horario(futuro)
    p = Paciente("Paciente Cancelado", "88899900011")
    ag = Agendamento(p, m, futuro)
    ag.confirmar()
    ag.realizar()
    with pytest.raises(ValueError, match="Agendamento já realizado."):
        ag.cancelar()

def test_cancelar_agendamento_ja_cancelado_levanta_erro():
    futuro = _fmt(datetime.now() + timedelta(days=39))
    m = Medico("Dr. Teste", "Geral")
    m.adicionar_horario(futuro)
    p = Paciente("Paciente Duplo Cancelamento", "99900011122")
    ag = Agendamento(p, m, futuro)
    ag.cancelar() # Primeiro cancelamento
    with pytest.raises(ValueError, match="Agendamento já cancelado."):
        ag.cancelar() # Segunda tentativa
