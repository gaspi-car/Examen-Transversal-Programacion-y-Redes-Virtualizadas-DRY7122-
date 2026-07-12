while True:
    entrada = input("Ingrese el numero de VLAN (o 'q' para salir): ")

    if entrada.lower() in ("q", "quit"):
        print("Saliendo del programa.")
        break

    if not entrada.isdigit():
        print("Entrada invalida. Debe ingresar un numero entero.\n")
        continue

    vlan = int(entrada)

    if vlan < 1 or vlan > 4094:
        print(f"VLAN {vlan} fuera de rango. El rango valido es 1-4094.\n")
    elif 1 <= vlan <= 1005:
        print(f"La VLAN {vlan} pertenece al RANGO NORMAL (1-1005).\n")
    elif 1006 <= vlan <= 1024:
        print(f"La VLAN {vlan} esta en el RANGO RESERVADO (1006-1024), no asignable.\n")
    else:
        print(f"La VLAN {vlan} pertenece al RANGO EXTENDIDO (1025-4094).\n")
