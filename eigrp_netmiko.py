from netmiko import ConnectHandler

router = {
    "device_type": "cisco_ios",
    "host": "192.168.56.105",
    "username": "cisco",
    "password": "cisco123!",
    "secret": "cisco123!",
}

conexion = ConnectHandler(**router)
conexion.enable()

print("Conexion establecida con el router.\n")

comandos_eigrp = [
    "ipv6 unicast-routing",
    "router eigrp EXAMEN-DRY7122",
    " address-family ipv4 unicast autonomous-system 100",
    "  af-interface default",
    "   passive-interface",
    "  exit-af-interface",
    "  network 0.0.0.0",
    " exit-address-family",
    " address-family ipv6 unicast autonomous-system 100",
    "  af-interface default",
    "   passive-interface",
    "  exit-af-interface",
    " exit-address-family",
]

salida_config = conexion.send_config_set(comandos_eigrp)
print("Configuracion EIGRP aplicada:")
print(salida_config)


salida_eigrp = conexion.send_command("show running-config | section eigrp")
print("\n===== show running-config | section eigrp =====")
print(salida_eigrp)


salida_interfaces = conexion.send_command("show ip interface brief")
print("\n===== show ip interface brief =====")
print(salida_interfaces)


salida_running = conexion.send_command("show running-config")
print("\n===== show running-config =====")
print(salida_running)

salida_version = conexion.send_command("show version")
print("\n===== show version =====")
print(salida_version)

conexion.disconnect()
print("\nSesion cerrada.")
