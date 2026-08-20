import random


class Figurita:
    def __init__(self, id, jugador, equipo):
        self.id = id
        self.jugador = jugador
        self.equipo = equipo

class Sobre:
    def __init__(self):
        self.contenido = []
        self.generar_figuritas()
        
    def generar_figuritas(self):
        # Genera 5 figuritas aleatorias para el sobre
        for _ in range(5):
            nueva_fig = Figurita(random.randint(1, 100), f"Jugador X", f"Equipo Y")
            self.contenido.append(nueva_fig)
        
class Album:
    def __init__(self, propietario):
        self.propietario = propietario
        self.figuritas_pegadas = []

    def pegar_figurita(self, fig):
        # Lógica para evitar duplicados
        if any(f.id == fig.id for f in self.figuritas_pegadas):
            return False
        self.figuritas_pegadas.append(fig)
        return True
    def contar_faltantes(self):
        total_figuritas = 100  # Supongamos que hay 100 figuritas en total
        return total_figuritas - len(self.figuritas_pegadas)
    
