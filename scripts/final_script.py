import asyncio
from bleak import BleakScanner
import subprocess


async def monitor_rssi(address):
    print(f"Iniciando a verificação contínua do RSSI para o dispositivo {address}...")
    try:
        while True:
            # Escaneia dispositivos Bluetooth próximos
            devices = await BleakScanner.discover(timeout=0.5)  # Timeout reduzido para maior responsividade
            
            # Filtra o dispositivo desejado
            device = next((d for d in devices if d.address == address), None)
            if device:
                rssi = device.rssi
                print(f"RSSI: {device.rssi}")
                if rssi < -85:
                   print("STOP")
                else:
                   print("FRENTE")
            #else:
                #print("Dispositivo fora de alcance.")

            await asyncio.sleep(0.3)  # Intervalo reduzido entre leituras
    except Exception as e:
        print(f"Erro ao monitorar RSSI: {e}")


def get_connected_device():
    try:
        # Usa bluetoothctl para verificar dispositivos conectados
        result = subprocess.run(["bluetoothctl", "info"], capture_output=True, text=True)
        output = result.stdout
        if "Device" in output:
            # Extrai o endereço MAC do dispositivo conectado
            for line in output.splitlines():
                if line.strip().startswith("Device"):
                    return line.split()[1]
        else:
            print("Nenhum dispositivo conectado.")
    except Exception as e:
        print(f"Erro ao verificar dispositivo conectado: {e}")
    return None


if __name__ == "__main__":
    mac_address = get_connected_device()
    if not mac_address:
        print("Nenhum dispositivo conectado. Encerrando...")
    else:
        print(f"Endereço MAC do dispositivo conectado: {mac_address}")
        try:
            # Inicia o loop otimizado para obter o RSSI
            asyncio.run(monitor_rssi(mac_address))
        except KeyboardInterrupt:
            print("\nEncerrando o programa...")

