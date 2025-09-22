import os
import asyncio
from motor.motor_asyncio import AsyncIOMotorClient
from dotenv import load_dotenv

load_dotenv()

MONGO_URL = os.getenv("MONGO_URL")
MONGO_DB = os.getenv("MONGO_DB")

async def main():
    client = AsyncIOMotorClient(MONGO_URL)
    db = client[MONGO_DB]
    res = await db["messages"].insert_one({"test": "ok"})
    print("Inserido id:", res.inserted_id)
    client.close()

if __name__ == "__main__":
    asyncio.run(main())
