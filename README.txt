# Proyecto: Mini Cámara Retro

Este proyecto consiste en el desarrollo de un dispositivo compacto basado en una Raspberry Pi y/o ESP32-CAM que funcione como una mini cámara retro. El dispositivo permitirá capturar imágenes, almacenarlas en una tarjeta microSD, y mostrarlas en un pequeño display. Además, incluirá funcionalidades básicas como un flash LED y botones para control.

---

## Características del Proyecto

- **Cámara**: Captura de imágenes usando hardware compatible (Raspberry Pi Camera o ESP32-CAM).
- **Display**: Visualización de imágenes en un pequeño display OLED o TFT.
- **Almacenamiento**: Guardado de imágenes en una tarjeta microSD.
- **Controles**: Botones físicos para interactuar con el dispositivo (captura de imágenes, navegación, etc.).
- **Flash**: LED integrado para iluminación.

---

## Entornos de Ejecución

El proyecto está diseñado para ser ejecutado en dos entornos diferentes:

1. **Producción** (Raspberry Pi o hardware final):
   - Ejecución directa sin Docker, optimizada para el hardware.
   - Control total sobre periféricos como GPIO, cámara y LED.
   
2. **Desarrollo** (PC o entorno de pruebas):
   - Uso de Docker para pruebas rápidas y desarrollo modular.
   - Simulación de componentes (display, cámara, almacenamiento) para facilitar el trabajo en equipo.

---

## Configuración Inicial

1. **Producción**:
   - Instalar dependencias directamente en la Raspberry Pi.
   - Configurar el hardware (cámara, botones, LED, display).

2. **Desarrollo**:
   - Crear un entorno con Docker para pruebas.
   - Configurar volúmenes compartidos y dependencias en el contenedor.

---

## Cómo Empezar

### Para Producción:
1. Configura tu Raspberry Pi siguiendo las instrucciones del archivo `docs/setup_production.md`.
2. Ejecuta el código principal:
   ```bash
   python3 src/main.py
