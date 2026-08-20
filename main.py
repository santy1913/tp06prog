from logica_album import Album, Sobre


def main():
    mi_album = Album("Coleccionista")
    sobre_actual = None
    while True:
        print("\n1. Abrir sobre\n2. Pegar figuritas del sobre\n3. Ver álbum\n4. Salir")
        op = input("Opción: ")

        if op == "1":
            sobre_actual = Sobre()
            print("¡Abriste un sobre! Contenido:")
            for f in sobre_actual.contenido:
                print(f"- {f.jugador} (ID: {f.id})")

        elif op == "2":
            if sobre_actual:
                for f in sobre_actual.contenido:
                    if mi_album.pegar_figurita(f):
                        print(f"Pegaste a {f.jugador}")
                    else:
                        print(f"{f.jugador} ya estaba en el álbum.")
                sobre_actual = None
            else:
                print("No tenés sobres abiertos.")
            # ... resto del menú

        elif op == "3":
            print(f"Álbum de {mi_album.propietario}:")
            for f in mi_album.figuritas_pegadas:
                print(f"- {f.jugador} (ID: {f.id})")
            print(f"Figuritas faltantes: {mi_album.contar_faltantes()}")
        elif op == "4":
            print("¡Hasta luego!")
            break

if __name__ == "__main__":    main()
