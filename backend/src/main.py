# main.py: Punto de entrada del proyecto "Mini Cámara Retro"

from utils.logger_config import logger_config
import logging

logger = logging.getLogger(__name__)

def main():
    """
    Punto de entrada principal del proyecto.
    Aquí se inicializarán los módulos principales como la cámara, el display, 
    los botones y el almacenamiento.
    """    
    logger.debug("Iniciando Mini Cámara Retro...")

    # TODO: Inicializar módulos principales
    # Por ejemplo:
    # camera = Camera()
    # display = Display()
    # io = IOManager()
    # storage = Storage()

    logger.info("Sistema inicializado correctamente. Listo para capturar imágenes.")

if __name__ == "__main__":
    main()
