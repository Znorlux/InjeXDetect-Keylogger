package main

import (
	"fmt"
	"log"

	"github.com/StackExchange/wmi"
)

// Win32_PnPEntity es una estructura que representa la clase Win32_PnPEntity de WMI (Windows Management Instrumentation) (https://docs.microsoft.com/en-us/windows/win32/cimwin32prov/win32-pnpentity)
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

	
	for _, device := range devices {
		if device.Present {
			fmt.Println("Device Name:", device.Name)
			fmt.Println("Manufacturer:", device.Manufacturer)
			fmt.Println("Description:", device.Description)
			fmt.Println("Device ID:", device.DeviceID)

			// dispositivos que son teclados (se debe mejorar su detección)
			if device.Description == "Dispositivo de teclado HID" || device.Description == "Teclado estándar" {
				fmt.Println("<< Este dispositivo es un teclado HID >>")
			}
			fmt.Println("----------------------------------------")
		}
	}

	fmt.Println("Presiona Enter para salir...")
	fmt.Scanln()
}
