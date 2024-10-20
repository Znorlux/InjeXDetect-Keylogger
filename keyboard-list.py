import wmi

# Crear una instancia de WMI
c = wmi.WMI()

# Consultar dispositivos USB conectados
print("Dispositivos USB conectados:")
print("-" * 40)

for usb in c.Win32_USBControllerDevice():
    # Obtener el dispositivo relacionado
    device = usb.Dependent
    # Acceder a los detalles del dispositivo
    device_info = c.query(f"SELECT * FROM Win32_PnPEntity WHERE DeviceID = '{device.DeviceID}'")

    for dev in device_info:
        # Verificar si el dispositivo está presente
        if dev.Present:
            # Marcar el dispositivo como teclado si contiene "keyboard" en su nombre
            is_keyboard = "[TECLADO]" if "keyboard" in dev.Name.lower() else ""
            print(f"Device Name: {dev.Name} {is_keyboard}")
            print(f"Manufacturer: {dev.Manufacturer}")
            print(f"Description: {dev.Description}")
            print(f"Device ID: {dev.DeviceID}")
            print("-" * 40)
