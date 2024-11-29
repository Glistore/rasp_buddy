import asyncio
from bleak import BleakClient
from bleak import BleakScanner
import subprocess
import math


async def RSSI(device):
    while True:
        try:
            # Obtém o RSSI
            rssi = device.rssi
                    
            print(f"RSSI: {rssi}")
            break  # Para evitar múltiplas impressões para o mesmo dispositivo
            
        except Exception as e:
            print(f"Erro: {e}")
            await asyncio.sleep(5)  # Espera antes de tentar novamente

async def get_device(address):
    while True:
        try:
            # Descobre dispositivos Bluetooth disponíveis
            devices = await BleakScanner.discover()
            
            for device in devices:
                if device.address == address:
                    print("Dispositivo encontrado")
                    return device
            
        except Exception as e:
            print(f"Erro: {e}")
            await asyncio.sleep(5)  # Espera antes de tentar novamente
            
def get_connected_device():
    try:
        result = subprocess.run(["bluetoothctl", "info"], capture_output=True, text=True)
        output = result.stdout
        if "Device" in output:
            # Extrair MAC Address
            for line in output.splitlines():
                if line.strip().startswith("Device"):
                    return line.split()[1]  # O MAC Address está na segunda posição
        else:
            print("Nenhum dispositivo conectado.")
    except Exception as e:
        print(f"Erro ao verificar dispositivo conectado: {e}")
    return None



if __name__ == "__main__":
    mac_address = get_connected_device()
    print(mac_address)
    device = asyncio.run(get_device(mac_address))
    try:
        # Obtém o RSSI
        asyncio.run(RSSI(device))
    except KeyboardInterrupt:
        print("\nEncerrando o programa...")

