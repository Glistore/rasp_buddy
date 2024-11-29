import asyncio
from bleak import BleakScanner


async def get_distance(address):
    while True:
        try:
            # Descobre dispositivos Bluetooth disponíveis
            devices = await BleakScanner.discover()
            
            for device in devices:
                if device.address == address:
                   
                    # Obtém o RSSI
                    rssi = device.rssi
                    
                    print(f"RSSI: {rssi}")
                    break  # Para evitar múltiplas impressões para o mesmo dispositivo
            
        except Exception as e:
            print(f"Erro: {e}")
            await asyncio.sleep(5)  # Espera antes de tentar novamente

if __name__ == "__main__":
    device_address = "98:D7:42:74:A4:4B"  # Substitua pelo endereço MAC do seu dispositivo
    try:
        asyncio.run(get_distance(device_address))
    except KeyboardInterrupt:
        print("\nEncerrando o programa...")


