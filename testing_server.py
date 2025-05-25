import asyncio
import websockets
import json
import random

# Function with correct parameters
async def send_data(websocket):
    print("Client connected")
    while True:
        data = {"value": random.randint(0, 100)}
        print("Sending:", data)
        await websocket.send(json.dumps(data))
        await asyncio.sleep(1)

async def main():
    # Use the async context manager
    async with websockets.serve(send_data, "localhost", 8000):
        print("WebSocket server started on ws://localhost:8000")
        await asyncio.Future()  # Run forever

if __name__ == "__main__":
    asyncio.run(main())