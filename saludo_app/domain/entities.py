from dataclasses import dataclass

@dataclass(frozen=True)
class PersonaSaludo:
    nombre: str

    def generar_mensaje(self) -> str:
        nombre_limpio = self.nombre.strip()
        if not nombre_limpio:
            raise ValueError("El campo nombre es obligatorio para procesar el saludo.")
        return f"¡Bienvenido a la arquitectura hexagonal, {nombre_limpio}!"