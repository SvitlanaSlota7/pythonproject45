import time
import asyncio
import httpx

BASE_URL = "http://127.0.0.1:8000"
ENDPOINTS = [
    f"{BASE_URL}/api/v1/users/",
    f"{BASE_URL}/api/v1/products/",
    f"{BASE_URL}/api/v1/orders/"
]


# Функція для виконання одного запиту асинхронно
async def fetch_endpoint(client, url):
    start_time = time.time()
    response = await client.get(url)
    duration = time.time() - start_time
    print(f"Запит {url} виконано за {duration:.4f} сек.")
    return response


async def run_asynchronous_test():
    print("\n--- Запуск АСИНХРОННОГО тесту ---")
    total_start_time = time.time()

    async with httpx.AsyncClient() as client:
        # Створюємо список задач, які виконуються одночасно
        tasks = [fetch_endpoint(client, url) for url in ENDPOINTS]
        # Чекаємо на завершення всіх задач
        await asyncio.gather(*tasks)

    total_duration = time.time() - total_start_time
    print(f"Сумарний час усіх асинхронних запитів: {total_duration:.4f} сек.")


if __name__ == "__main__":
    asyncio.run(run_asynchronous_test())