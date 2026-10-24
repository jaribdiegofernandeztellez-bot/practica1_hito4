from saludo_app.domain.entities import PersonaSaludo
from saludo_app.domain.ports import SaludarInputPort

class SaludarUseCase(SaludarInputPort):
    def ejecutar(self, nombre: str) -> str:
        persona = PersonaSaludo(nombre=nombre)
        return persona.generar_mensaje()