import subprocess
print(r"""
              __                                                       
  ________ __|  | _______      ______ ____ _____    ____   ___________ 
 /  ___/  |  \  |/ /\__  \    /  ___// ___\\__  \  /    \_/ __ \_  __ \
 \___ \|  |  /    <  / __ \_  \___ \\  \___ / __ \|   |  \  ___/|  | \/
/____  >____/|__|_ \(____  / /____  >\___  >____  /___|  /\___  >__|   
     \/           \/     \/       \/     \/     \/     \/     \/       v.01
     """)

print("[1]: escaneo basico")
print("[2]: escaneo agresivo")
print("[3]: escaneo de versiones")
print("[4]: esacneo de todos los puertos [!]: puede ser tardado")
print("[5]: salir")
opcion = int(input("elije una opción: "))
match opcion:

    case 1:
        IP = input("IP: ")

        resultado = subprocess.run(
            ["nmap", "-F", IP],
            capture_output=True
        )

        print(resultado.stdout)

    case 2:
        IP = input("IP: ")

        resultado = subprocess.run(
            ["nmap", "-A", IP],
            capture_output=True
        )

        print(resultado.stdout)

    case 3:
        IP = input("IP: ")

        resultado = subprocess.run(
            ["nmap", "-sV", IP],
            capture_output=True
        )

        print(resultado.stdout)

    case 4:
        IP = input("IP: ")

        resultado = subprocess.run(
            ["nmap", "-p-", IP],
            capture_output=True
        )

        print(resultado.stdout)

    case 5:
        print("adios :)")
