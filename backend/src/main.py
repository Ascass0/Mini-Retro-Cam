# main.py: Punto de entrada del proyecto "Mini Cámara Retro"

import logging

def main():
    """
    Punto de entrada principal del proyecto.
    Aquí se inicializarán los módulos principales como la cámara, el display, 
    los botones y el almacenamiento.
    """
    # Configurar el sistema de logging
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
    )
    
    logging.info("Iniciando Mini Cámara Retro...")

    # TODO: Inicializar módulos principales
    # Por ejemplo:
    # camera = Camera()
    # display = Display()
    # io = IOManager()
    # storage = Storage()

    logging.info("Sistema inicializado correctamente. Listo para capturar imágenes.")

if __name__ == "__main__":
    main()
