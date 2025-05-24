class Canister:
    def __init__(self, capacity=12):
        if not isinstance(capacity, int) or capacity < 0:
            raise ValueError("Capacity must be a non-negative integer.")
        self._capacity = capacity
        self._volume = 0

    def __str__(self):
        return "🥤" * self._volume

    def refill(self, n):
        if self._volume + n > self._capacity:
            raise ValueError("Not enough capacity to refill.")
        self._volume += n

    def drink(self, n):
        if n > self._volume:
            raise ValueError("Not enough cans to drink.")
        self._volume -= n

    @property
    def capacity(self):
        return self._capacity

    @property
    def volume(self):
        return self._volume
