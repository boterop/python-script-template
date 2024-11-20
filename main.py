import os
import asyncio
import shutil
from src.settings import Settings
from dotenv import load_dotenv

load_dotenv(override=True)

FILE_PATH = "tmp"


def clean_tmp():
    shutil.rmtree(FILE_PATH)


async def main():
    os.makedirs(FILE_PATH, exist_ok=True)
    settings = Settings()

    print("Done")
    clean_tmp()


if __name__ == "__main__":
    asyncio.run(main())
