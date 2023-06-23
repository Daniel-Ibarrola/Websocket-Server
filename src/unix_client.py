#!/usr/bin/env python

import asyncio
import websockets


async def main():
    path = "websocket.sock"
    async with websockets.unix_connect(path) as websocket:
        while True:
            msg = input(">>> ")
            await websocket.send(msg)
            response = await websocket.recv()
            print(f"<<< {response}")

if __name__ == "__main__":
    asyncio.run(main())
