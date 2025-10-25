from datetime import datetime
from src.medico import Medico
from src.paciente import Paciente

class Agendamento:

    def __init__(self, medico, paciente, horario: str):
        if not isinstance(medico, Medico):
            raise TypeError("medico deve ser instância de Medico")
        if not isinstance(paciente, Paciente):
            raise TypeError("paciente deve ser instância de Paciente")

        # valida formato do horário
        try:
            horario_dt = datetime.strptime(horario, "%d/%m/%Y %H:%M")
        except ValueError as e:
            raise ValueError("Formato de horário inválido. Use 'DD/MM/YYYY HH:MM'.") from e

        # não permite agendar em data passada
        if horario_dt < datetime.now():
            raise ValueError("Não é possível agendar em data passada")

        # registra/agende no médico (Medico.agendar deve levantar ValueError se conflito)
        medico.agendar(horario)

        self.medico = medico
        self.paciente = paciente
        self.horario = horario
        self.status = "CRIADO"

    def confirmar(self):
        """Confirma o agendamento: paciente ativo e médico disponível."""
        if not self.paciente.ativo:
            raise ValueError("Paciente inativo.")
        # se já estiver confirmado ou realizado, não tenta reagendar
        if self.status == "CONFIRMADO":
            return
        if self.status in ("REALIZADO", "CANCELADO"):
            raise ValueError("Não é possível confirmar agendamento neste estado.")
        # Se o médico já tem o horário agendado por este agendamento, considera confirmado.
        # Caso contrário, tenta agendar (pode levantar ValueError se conflito)
        if self.horario not in self.medico.agenda:
            self.medico.agendar(self.horario)
        self.status = "CONFIRMADO"

    def cancelar(self):
        """Cancela o agendamento. Se estiver confirmado, libera o horário no médico."""
        if self.status == "REALIZADO":
            raise ValueError("Agendamento já realizado.")
        if self.status == "CANCELADO":
            raise ValueError("Agendamento já cancelado.")

        # se o horário estiver presente na agenda do médico, remove-o
        if self.horario in getattr(self.medico, "agenda", []):
            self.medico.cancelar(self.horario)

        self.status = "CANCELADO"

    def realizar(self):
        """Marca o agendamento como realizado. Só é permitido se estiver CONFIRMADO."""
        if self.status != "CONFIRMADO":
            raise ValueError("Agendamento não confirmado.")
        self.status = "REALIZADO"

