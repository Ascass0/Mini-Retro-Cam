# main.py: Punto de entrada del proyecto "Mini Cámara Retro"

from utils.logger_config import logger_config
import logging, time, signal

logger = logging.getLogger(__name__)


def handle_exit_signal(signum, frame):
    """Manejador para señales del sistema.
    Args:
        signum (int): Número de la señal recibida.
        frame (object): Objeto del frame de la señal.
    """
    logger.info(f"Recibida la señal {signum}. Deteniendo aplicación...")
    exit(0)

def initialize_modules():
    """
    Inicializa los módulos principales del sistema.
    """
    logger.info("Inicializando módulos principales...")
    
    # TODO: Crear instancias de los módulos principales
    # camera = Camera()
    # display = Display()
    # io_manager = IOManager()
    # storage = Storage()

    logger.info("Todos los módulos se han inicializado correctamente.")
    
    # TODO: Devuelve las instancias de los módulos si es necesario
    # return camera, display, io_manager, storage

def run():
    """Bucle principal del sistema."""
    while True:
        logger.debug("El sistema está funcionando correctamente.")
        time.sleep(1)

def main():
    """ Función principal que coordina el inicio del sistema. """
    logger.info("Iniciando Mini Cámara Retro...")

    try:
        logger.info('-------- MINI RETRO CAM --------')
        initialize_modules()
        run()

    except KeyboardInterrupt:
        logger.info("Deteniendo aplicación...")
    except Exception as e:
        logger.error(f"Se produjo un error inesperado: {e}")
    finally:
        logger.info("Sistema apagado correctamente.")

if __name__ == "__main__":
    signal.signal(signal.SIGINT, handle_exit_signal)
    signal.signal(signal.SIGTERM, handle_exit_signal)
    main()
