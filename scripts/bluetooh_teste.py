from bleak import BleakClient

async def is_device_connected(address):
    try:
        async with BleakClient(address) as client:
            if client.is_connected:
                print(f"Dispositivo {address} está conectado.")
                return True
            else:
                print(f"Dispositivo {address} não está conectado.")
                return False
    except Exception as e:
        print(f"Erro ao verificar conexão com {address}: {e}")
        return False

# Exemplo de uso
if __name__ == "__main__":
    import asyncio

    address = "98:D7:42:74:A4:4B"  # Substitua pelo MAC do dispositivo
    asyncio.run(is_device_connected(address))

