package main

import (
	"fmt"
	"log"

	"github.com/StackExchange/wmi"
)

// Win32_PnPEntity es la estructura que representa la entidad de Plug and Play.
type Win32_PnPEntity struct {
	Name         string
	Manufacturer string
	Description  string
	DeviceID     string
	Present      bool
}

func main() {
	var devices []Win32_PnPEntity
	query := "SELECT * FROM Win32_PnPEntity"
	err := wmi.Query(query, &devices)
	if err != nil {
		log.Fatal(err)
	}

	// Mostrar todos los dispositivos PnP
	for _, device := range devices {
		if device.Present {
			fmt.Println("Device Name:", device.Name)
			fmt.Println("Manufacturer:", device.Manufacturer)
			fmt.Println("Description:", device.Description)
			fmt.Println("Device ID:", device.DeviceID)

			// Marcar dispositivos que son teclados
			if device.Description == "Dispositivo de teclado HID" || device.Description == "Teclado estándar" {
				fmt.Println("<< Este dispositivo es un teclado HID >>")
			}
			fmt.Println("----------------------------------------")
		}
	}

	// Esperar a que el usuario presione Enter
	fmt.Println("Presiona Enter para salir...")
	fmt.Scanln()
}
