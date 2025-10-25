import pytest
from src.medico import Medico
from datetime import datetime

def test_representacao_medico():
    m = Medico("Dr. Silva", "Cardiologia")
    m.adicionar_horario("01/01/2025 10:00")
    assert m.nome == "Dr. Silva"
    assert m.especialidade == "Cardiologia"
    assert m.agenda == [datetime(2025, 1, 1, 10, 0)]

def test_agenda_com_lista():
    m = Medico("Dr. Alves", "Dermatologia")
    m.adicionar_horario("02/02/2025 09:00")
    m.adicionar_horario("03/03/2025 11:00")
    assert m.agenda == [datetime(2025, 2, 2, 9, 0), datetime(2025, 3, 3, 11, 0)]

def test_criacao_sem_agenda_inicial():
    m = Medico("Dr. Costa", "Pediatria")
    assert isinstance(m.agenda, list)
    assert m.agenda == []

def test_adicionar_consulta():
    m = Medico("Dr. Ramos", "Neurologia")
    m.adicionar_horario("05/05/2025 14:00")
    assert m.disponivel("05/05/2025 14:00")

def test_cancelar_consulta():
    m = Medico("Dr. Lima", "Clínico Geral")
    m.adicionar_horario("06/06/2025 15:00")
    m.remover_horario("06/06/2025 15:00")
    assert not m.disponivel("06/06/2025 15:00")

def test_agendar_consulta_existente_levanta_erro():
    m = Medico("Dr. Sousa", "Ortopedia")
    m.adicionar_horario("07/07/2025 16:00")
    with pytest.raises(ValueError):
        m.adicionar_horario("07/07/2025 16:00")

def test_adicionar_horario_formato_invalido_levanta_erro():
    m = Medico("Dr. House", "Diagnóstico")
    with pytest.raises(ValueError, match="Formato de horário inválido. Use 'DD/MM/YYYY HH:MM'."):
        m.adicionar_horario("2025-01-01 10:00") # Formato YYYY-MM-DD

def test_remover_horario_inexistente_levanta_erro():
    m = Medico("Dr. Strange", "Misticismo")
    m.adicionar_horario("10/10/2025 10:00")
    with pytest.raises(ValueError, match="Horário não encontrado."):
        m.remover_horario("11/11/2025 11:00")

def test_disponivel_com_formato_invalido_retorna_false():
    m = Medico("Dr. Dolittle", "Veterinária")
    m.adicionar_horario("12/12/2025 12:00")
    assert m.disponivel("formato-invalido") is False
    assert m.disponivel("32/12/2025 10:00") is False # Dia inválido
