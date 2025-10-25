import pytest
from src.agendamento import Agendamento
from src.medico import Medico
from src.paciente import Paciente
import datetime

def _fmt(dt):
    return dt.strftime("%d/%m/%Y %H:%M")

def test_criacao_agendamento_valido():
    futuro = _fmt(datetime.datetime.now() + datetime.timedelta(days=30))
    m = Medico("Dr. Teste", "Geral")
    p = Paciente("Paciente", "12345678901")
    ag = Agendamento(m, p, futuro)
    assert ag.medico is m
    assert ag.paciente is p
    assert ag.horario == futuro
    assert futuro in m.agenda

def test_agendamento_duplicado_medico_levanta_erro():
    futuro = _fmt(datetime.datetime.now() + datetime.timedelta(days=31))
    m = Medico("Dr. Teste", "Geral", futuro)
    p = Paciente("Paciente2", "09876543210")
    with pytest.raises(ValueError):
        Agendamento(m, p, futuro)

def test_cancelar_agendamento_remove_da_agenda_medico():
    futuro = _fmt(datetime.datetime.now() + datetime.timedelta(days=32))
    m = Medico("Dr. Teste", "Geral")
    p = Paciente("Paciente3", "11122233344")
    ag = Agendamento(m, p, futuro)
    ag.cancelar()
    assert futuro not in m.agenda

def test_agendamento_em_data_passada_levanta_erro():
    passado = _fmt(datetime.datetime.now() - datetime.timedelta(days=1))
    m = Medico("Dr. Teste", "Geral")
    p = Paciente("Paciente4", "22233344455")
    with pytest.raises(ValueError):
        Agendamento(m, p, passado)

def test_agendamento_formato_invalido_levanta_erro():
    m = Medico("Dr. Teste", "Geral")
    p = Paciente("Paciente5", "33344455566")
    with pytest.raises(ValueError):
        Agendamento(m, p, "2025-05-05 14:00")

