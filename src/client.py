#!/usr/bin/env python

import asyncio
import sys
import websockets


async def main():
    uri = sys.argv[1]
    async with websockets.connect(uri) as websocket:
        while True:
            msg = input(">>> ")
            await websocket.send(msg)
            response = await websocket.recv()
            print(f"<<< {response}")

if __name__ == "__main__":
    asyncio.run(main())
