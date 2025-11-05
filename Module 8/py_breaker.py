import httpx
import pybreaker


circuit_breaker = pybreaker.CircuitBreaker(
    fail_max=5,
    reset_timeout=10,
    name="AuthorServiceBreaker"
)


async def fetch_with_breaker():
    async with httpx.AsyncClient(base_url="https://httpbin.org/status") as client:
        try:

            response = await circuit_breaker.async_call(
                client.get, "/503"
            )
            response.raise_for_status()
            print("Ответ:", response.text)

        except httpx.HTTPStatusError as e:
            print(f"Ошибка HTTP: {e.response.status_code}")

        except pybreaker.CircuitBreakerError:
            print("Circuit Open: API временно отключено.")

        except Exception as e:
            print(f"Другая ошибка: {e}")
