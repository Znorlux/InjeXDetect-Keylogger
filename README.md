# InjeXDetect Detección de Inyecciones Maliciosas con Dispositivos HID

Este repositorio contiene scripts y desarrollos iniciales para un sistema de detección proactiva de inyecciones de malware a través de dispositivos USB utilizando machine learning. El objetivo del proyecto es fortalecer la seguridad ante ataques físicos a través de la conexión de dispositivos USB no confiables. A largo plazo, el sistema evolucionará hacia un modelo que analizará los comportamientos de los dispositivos conectados y tomará decisiones automáticas para mitigar posibles amenazas.

## Contexto

En la actualidad, los ataques mediante dispositivos USB son una amenaza importante para la seguridad de los sistemas, dado que pueden eludir la protección de la red e incluso comprometer equipos sin conexión a internet. Casos como el ataque Stuxnet han demostrado el poder de los USB maliciosos para ejecutar malware y comprometer sistemas críticos. Además, estudios recientes destacan que los ataques por USB representan una porción significativa de las filtraciones de datos en empresas, lo que resalta la necesidad de una solución proactiva que detecte y bloquee estos ataques.

## Problemática

Las soluciones tradicionales de seguridad como los antivirus y firewalls no están diseñadas para detectar inyecciones maliciosas a través de dispositivos USB. Esta brecha de seguridad es aprovechada por los ciberdelincuentes para realizar ataques rápidos y difíciles de detectar, lo que plantea la necesidad de un sistema especializado en la protección en tiempo real frente a estas amenazas.

## Descripción del Proyecto

El objetivo principal es desarrollar un prototipo basado en machine learning que monitoree las conexiones USB, detecte comportamientos anómalos y mitigue automáticamente los ataques. Esto incluirá:

- **Detección de dispositivos conectados**: Inicialmente, el sistema detecta y lista los dispositivos conectados al sistema, incluyendo teclados, ratones y otros dispositivos HID.
- **Registro de actividad de entrada**: A través de un keylogger en desarrollo, el sistema monitorea la actividad del teclado para identificar posibles patrones maliciosos.
- **Modelo de Machine Learning**: En futuras fases, se implementará un modelo de machine learning que analizará patrones de uso y características de los dispositivos USB para detectar comportamientos sospechosos en tiempo real.

## Scripts Actuales

1. **keyboard-list.go**: Script en Go que lista los dispositivos de entrada conectados, como teclados y ratones. A futuro, este script evolucionará para identificar dispositivos USB potencialmente peligrosos.
2. **keylog.py**: Script en Python que registra la actividad de teclas. Este es un componente clave para alimentar el modelo de machine learning con datos sobre el comportamiento del usuario.

## Tecnologías Utilizadas

- **Python**: Para el desarrollo inicial de scripts de monitoreo como el keylogger.
- **Go**: Para la detección de dispositivos conectados al sistema.
- **ESP32/Digispark ATtiny85** (futuro): Microcontroladores que se utilizarán para implementar el modelo de detección en tiempo real.
- **Machine Learning** (futuro): Entrenamiento de modelos para identificar patrones anómalos en los dispositivos USB.

## Compilación y Ejecución de los Scripts

### Keylogger (Python)

```bash
pyinstaller --onefile --noconsole keylog.py
```

Luego ejecutar en

```bash
./dist/keylog.exe
```

Para cerrar el keylogger presionar "[CMD] (tecla windows) + ESCAPE"

### Listador de dispositivos HID (Go)

Para compilar el script de Go, asegúrate de tener configurado tu entorno de desarrollo con Go instalado. Luego, ejecuta:

```bash
cd ./Keyboard-list
```

```bash
go build keyboard-list.go
```

Para ejecutar el script compilado:

```bash
./keyboard-list.exe
```
