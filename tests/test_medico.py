import pytest
from src.medico import Medico

def test_representacao_medico():
    m = Medico("Dr. Silva", "Cardiologia", "01/01/2025 10:00")
    assert m.nome == "Dr. Silva"
    assert m.especialidade == "Cardiologia"
    assert m.agenda == ["01/01/2025 10:00"]

def test_agenda_com_lista():
    m = Medico("Dr. Alves", "Dermatologia", ["02/02/2025 09:00", "03/03/2025 11:00"])
    assert m.agenda == ["02/02/2025 09:00", "03/03/2025 11:00"]

def test_criacao_sem_agenda_inicial():
    m = Medico("Dr. Costa", "Pediatria")
    assert isinstance(m.agenda, list)
    assert m.agenda == []

def test_adicionar_consulta():
    m = Medico("Dr. Ramos", "Neurologia")
    m.agendar("05/05/2025 14:00")
    assert "05/05/2025 14:00" in m.agenda

def test_cancelar_consulta():
    m = Medico("Dr. Lima", "Clínico Geral", "06/06/2025 15:00")
    m.cancelar("06/06/2025 15:00")
    assert "06/06/2025 15:00" not in m.agenda

def test_agendar_consulta_existente_levanta_erro():
    m = Medico("Dr. Sousa", "Ortopedia", "07/07/2025 16:00")
    with pytest.raises(ValueError):
        m.agendar("07/07/2025 16:00")
