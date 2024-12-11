# """
# logger_config.py

# Configuración básica del logger utilizando dictConfig.

# Descripción:
# - Configura un logger sencillo con salida por consola.
# - Cambia los colores según el nivel del log (DEBUG, INFO, WARNING, ERROR, CRITICAL).
# """

from logging.config import dictConfig


logger_config = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console_handler': {
            'class': 'colorlog.StreamHandler',
            'formatter': 'colored_formatter',
        },
    },
    'formatters': {
        'colored_formatter': {
            '()': 'colorlog.ColoredFormatter',
            'format': '%(log_color)s[%(asctime)s] [%(levelname)s] - %(message)s%(reset)s',
            'log_colors': {
                'DEBUG': 'cyan',
                'INFO': 'green',
                'WARNING': 'yellow',
                'ERROR': 'red',
                'CRITICAL': 'bold_red',
            },
        },
    },
    'loggers': {
        '': {  # Logger raíz
            'handlers': ['console_handler'],
            'level': 'DEBUG',  # Nivel mínimo de logs que se mostrarán
        },
    },
}

dictConfig(logger_config)
