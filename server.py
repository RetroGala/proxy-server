import asyncio
import websockets
import ssl
import base64
import os

PASSWORD = os.environ.get("PASSWORD", "defaultpass123")
PORT = int(os.environ.get("PORT", 8080))

async def handle(ws):
    try:
        auth = await ws.recv()
        if auth != PASSWORD:
            await ws.close()
            return
        while True:
            data = await ws.recv()
            # echo back (gerçek proxy mantığı buraya)
            await ws.send(data)
    except:
        pass

async def main():
    async with websockets.serve(handle, "0.0.0.0", PORT):
        await asyncio.Future()

asyncio.run(main())
