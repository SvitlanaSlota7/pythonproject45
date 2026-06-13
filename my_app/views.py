import asyncio
from django.http import JsonResponse

# Тепер це асинхронні функції
async def get_users(request):
    await asyncio.sleep(1)  # Не блокує інші запити
    return JsonResponse({"status": "success", "data": "List of users (async)"})

async def get_products(request):
    await asyncio.sleep(1)
    return JsonResponse({"status": "success", "data": "List of products (async)"})

async def get_orders(request):
    await asyncio.sleep(1)
    return JsonResponse({"status": "success", "data": "List of orders (async)"})
