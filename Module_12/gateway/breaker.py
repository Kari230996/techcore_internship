import pybreaker
from prometheus_client import Gauge, Counter

CB_STATE = Gauge(
    "circuit_breaker_state",
    "Current state of the circuit breaker (0=closed,1=open,2=half-open)",
    ["name"]
)

CB_FAILURES = Counter(
    "circuit_breaker_failures_total",
    "Total failures counted by the circuit breaker",
    ["name"]
)

CB_SUCCESSES = Counter(
    "circuit_breaker_successes_total",
    "Total successful calls through circuit breaker",
    ["name"]
)


class PrometheusCircuitBreakerListener(pybreaker.CircuitBreakerListener):

    def state_change(self, cb, old_state, new_state):
        state_map = {
            "closed": 0,
            "open": 1,
            "half-open": 2,
        }
        CB_STATE.labels(cb.name).set(state_map[new_state.name])

    def failure(self, cb, exc):
        CB_FAILURES.labels(cb.name).inc()

    def success(self, cb):
        CB_SUCCESSES.labels(cb.name).inc()


breaker = pybreaker.CircuitBreaker(
    fail_max=1,
    reset_timeout=3,
    name="book_service",
    listeners=[PrometheusCircuitBreakerListener()],
)
