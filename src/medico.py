from datetime import datetime


class Medico:
    """Representa um médico e sua agenda de horários."""
    def __init__(self, nome: str, especialidade: str):
        self.nome = nome
        self.especialidade = especialidade
        self.agenda: list[datetime] = []

    def _parse_horario(self, horario: str) -> datetime:
        """Converte a string de horário para um objeto datetime."""
        try:
            return datetime.strptime(horario, "%d/%m/%Y %H:%M")
        except ValueError as e:
            raise ValueError("Formato de horário inválido. Use 'DD/MM/YYYY HH:MM'.") from e

    def adicionar_horario(self, horario: str):
        """Adiciona um horário à agenda."""
        horario_dt = self._parse_horario(horario)
        if horario_dt in self.agenda:
            raise ValueError("Horário já cadastrado.")

        self.agenda.append(horario_dt)
        self.agenda.sort()

    def remover_horario(self, horario: str):
        """Remove um horário da agenda."""
        horario_dt = self._parse_horario(horario)
        if horario_dt not in self.agenda:
            raise ValueError("Horário não encontrado.")
        self.agenda.remove(horario_dt)

    def disponivel(self, horario: str) -> bool:
        """Retorna True se o horário estiver disponível."""
        try:
            horario_dt = self._parse_horario(horario)
            return horario_dt in self.agenda
        except ValueError:
            return False
