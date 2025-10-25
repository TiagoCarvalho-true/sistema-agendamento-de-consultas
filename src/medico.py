from datetime import datetime


class Medico:
    """Representa um médico e sua agenda de horários."""
    def __init__(self, nome: str, especialidade: str, agenda=None):
        self.nome = nome
        self.especialidade = especialidade
        if agenda is None:
            self.agenda = []
        elif isinstance(agenda, str):
            self.agenda = [agenda]
        elif isinstance(agenda, list):
            self.agenda = agenda.copy()
        else:
            raise TypeError("agenda deve ser str, list ou None")

    def _parse_horario(self, horario: str) -> datetime:
        """Converte a string de horário para um objeto datetime."""
        try:
            return datetime.strptime(horario, "%d/%m/%Y %H:%M")
        except ValueError as e:
            raise ValueError("Formato de horário inválido. Use 'DD/MM/YYYY HH:MM'.") from e

    def agendar(self, horario: str):
        """Adiciona um horário à agenda."""
        if horario in self.agenda:
            raise ValueError("Horário já agendado.")
        self.agenda.append(horario)

    def cancelar(self, horario: str):
        """Remove um horário da agenda."""
        if horario not in self.agenda:
            raise ValueError("Horário não encontrado.")
        self.agenda.remove(horario)

    def disponivel(self, horario: str) -> bool:
        """Retorna True se o horário estiver disponível."""
        try:
            horario_dt = self._parse_horario(horario)
            return horario_dt in self.agenda
        except ValueError:
            return False
