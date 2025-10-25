
class Agendamento:
    """Controla o ciclo de vida de uma consulta médica."""
    def __init__(self, paciente, medico, horario: str):
        self.paciente = paciente
        self.medico = medico
        self.horario = horario
        self.status = "CRIADO"
        
    def confirmar(self):
        """Confirma o agendamento."""
        if self.medico.disponivel(self.horario) and self.paciente.ativo:
            self.medico.remover_horario(self.horario)
            self.status = "CONFIRMADO"
        else:
            raise ValueError("Horário não disponível ou paciente inativo.")
        
    def cancelar(self):
        """Cancela o agendamento."""
        if self.status == "REALIZADO":
            raise ValueError("Agendamento já realizado.")
        elif self.status == "CANCELADO":
            raise ValueError("Agendamento já cancelado.")
        
        if self.status == "CONFIRMADO":
            self.medico.adicionar_horario(self.horario)

        self.status = "CANCELADO"

    def realizar(self):
        """Realiza o agendamento."""
        if self.status != "CONFIRMADO":
            raise ValueError("Agendamento não confirmado.")
        self.status = "REALIZADO"
    
