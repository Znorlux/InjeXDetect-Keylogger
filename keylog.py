import csv
from datetime import datetime
from pynput import keyboard

log_file = "key_log.csv"  # archivo para guardar los logs de las teclas
# Estructura del archivo: Timestamp - Tecla presionada - Intervalo entre teclas (ms) - Chars per Second - Error Count

# Crear o abrir el archivo CSV de los logs
with open(log_file, mode='w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['Timestamp', 'Key', 'Interval_ms', 'Chars_per_Second', 'Error_Count'])

# Variables para llevar el estado del Ctrl izquierdo, calcular intervalos, caracteres por segundo y errores
cmd_pressed = False
last_time = None
last_key_count = 0
error_count = 0  # Contador de errores (Backspace)

# Función que se ejecuta cada vez que se presiona una tecla
def on_press(key):
    global cmd_pressed, last_time, last_key_count, error_count
    current_time = datetime.now()  # Obtener el tiempo actual
    interval = 0  # Inicializar intervalo a 0
    chars_per_second = 0  # Inicializar velocidad a 0

    # Calcular el intervalo de tiempo entre la pulsación actual y la anterior
    if last_time is not None:
        interval = (current_time - last_time).total_seconds() * 1000  # Intervalo en milisegundos

        # Calcular la velocidad en caracteres por segundo si el intervalo no es 0
        if interval > 0:
            chars_per_second = round(1000 / interval, 2)  # Convertir a segundos y calcular velocidad

    # Actualizar el último tiempo
    last_time = current_time

    timestamp = current_time.strftime("%Y-%m-%d %H:%M:%S")  # Obtener la marca de tiempo
    key_str = ''  # Inicializar la cadena de la tecla

    try:
        # Si es una tecla normal (letra, número, etc.)
        key_str = key.char
    except AttributeError:
        # Si es una tecla especial
        if key == keyboard.Key.space:
            key_str = "[SPACE]"  # Representar espacio con un espacio real
        elif key == keyboard.Key.enter:
            key_str = "[ENTER]"  # Representar enter con un salto de línea
        elif key == keyboard.Key.tab:
            key_str = "[TAB]"  # Representar tab con una tabulación
        elif key == keyboard.Key.backspace:
            key_str = "[BACKSPACE]"  # tecla de retroceso
            error_count += 1  # Incrementar contador de errores
        elif key == keyboard.Key.shift or key == keyboard.Key.shift_r:
            key_str = "[SHIFT]"
        elif key == keyboard.Key.ctrl_l:  # Ctrl izquierdo
            key_str = "[CTRL]"
        elif key == keyboard.Key.alt or key == keyboard.Key.alt_r:
            key_str = "[ALT]"
        elif key == keyboard.Key.esc:
            key_str = "[ESC]"
        elif key == keyboard.Key.cmd:
            cmd_pressed = True
            key_str = "[CMD (WINDOWS)]"
        else:
            key_str = f"[{key}]"  # Mantener cualquier otra tecla especial

    # Verificar si Ctrl está presionado y si se presionó Esc
    if cmd_pressed and key == keyboard.Key.esc:
        print("Cerrando el keylogger...")
        return False  # Detener el listener y cerrar el programa

    # Escribir la información en el archivo CSV
    with open(log_file, mode='a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([timestamp, key_str, round(interval, 2), chars_per_second, error_count])  # Guardar el intervalo, velocidad y errores

def on_release(key):
    global cmd_pressed
    if key == keyboard.Key.ctrl_l:
        cmd_pressed = False  # Liberar el estado de Ctrl

# Configurar el listener para el teclado
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
