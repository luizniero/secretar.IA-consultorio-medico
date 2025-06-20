import asyncio
import json
from websockets import serve

from calendar_utils import list_available_slots, create_calendar_event

connected_clients = set()

a_sync_lock = asyncio.Lock()

async def handler(websocket):
    connected_clients.add(websocket)
    try:
        await websocket.send("Aguarde enquanto eu sou conectado...")
        async for message in websocket:
            response = await process_message(message)
            await websocket.send(response)
    finally:
        connected_clients.remove(websocket)

async def process_message(message: str) -> str:
    message = message.lower()
    # Placeholder conversation logic
    if "marcar" in message or "agendar" in message:
        return (
            "Para marcar uma consulta, informe a especialidade e a data desejada."
        )
    if "horarios" in message:
        slots = await list_available_slots()
        if slots:
            formatted = "\n".join(slot.strftime("%d/%m/%Y %H:%M") for slot in slots)
            return f"Horários disponíveis:\n{formatted}"
        return "Não há horários disponíveis."
    if "confirmar" in message:
        # Aqui usaríamos informações coletadas durante a conversa
        event = await create_calendar_event(
            summary="Consulta",
            description="Consulta marcada via sistema inteligente de agendamento",
        )
        return (
            f"Consulta agendada para {event['start'].get('dateTime')}"
        )
    return "Desculpe, ainda estou aprendendo."

async def main():
    async with serve(handler, "0.0.0.0", 8765):
        await asyncio.Future()  # run forever

if __name__ == "__main__":
    asyncio.run(main())
