import pytest
from datetime import timedelta
from aiobreaker import CircuitBreaker, CircuitBreakerError


async def always_fail():
    raise Exception("Сетевая ошибка")


@pytest.mark.asyncio
async def test_circuit_breaker_opens_after_failures():
    breaker = CircuitBreaker(
        fail_max=5, timeout_duration=timedelta(seconds=30))
    breaker._expected_exception = Exception

    # Первые 4 ошибки - обычные
    for _ in range(4):
        with pytest.raises(Exception, match="Сетевая ошибка"):
            await breaker.call_async(always_fail)

    # На 5й раз - breaker должен открыться и выбросить CircuitBreakerError
    with pytest.raises(CircuitBreakerError):
        await breaker.call_async(always_fail)

    # И на 6й раз - breaker уже "разомкнут", снова сразу CircuitBreakerError
    with pytest.raises(CircuitBreakerError):
        await breaker.call_async(always_fail)
