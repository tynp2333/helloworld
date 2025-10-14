import dramatiq
from dramatiq.brokers.redis import RedisBroker
import time, logging

class SafeRedisBroker(RedisBroker):
    def consume(self, *args, **kwargs):
        while True:
            try:
                super().consume(*args, **kwargs)
            except Exception as e:
                logging.warning(f"Redis temporarily unreachable: {e}")
                time.sleep(5)  # sleep tránh spam
            else:
                break

broker = SafeRedisBroker(url="redis://localhost:6379/0")
dramatiq.set_broker(broker)
