import asyncio
from bleak import BleakClient

async def connect_to_device(address):
    try:
        async with BleakClient(address) as client:
            print(f"Conectado ao dispositivo: {address}")
            # Aqui você pode adicionar código para interagir com o dispositivo
            await asyncio.sleep(5)  # Manter a conexão por 5 segundos
    except Exception as e:
        print(f"Erro ao conectar: {e}")

if __name__ == "__main__":
    device_address = "98:D7:42:74:A4:4B"  # Substitua pelo endereço MAC do seu celular
    asyncio.run(connect_to_device(device_address))

