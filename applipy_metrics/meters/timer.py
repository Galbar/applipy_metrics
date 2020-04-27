import time
from .base_metric import BaseMetric

from .histogram import Histogram, DEFAULT_SIZE, DEFAULT_ALPHA
from .meter import Meter


class Chronometer:
    def __init__(self, clock=time, on_stop=None):
        super().__init__()
        self.clock = clock
        self.start_time = self.clock.time()
        self.on_stop = on_stop

    def stop(self):
        elapsed = self.clock.time() - self.start_time

        if self.on_stop:
            self.on_stop(elapsed)

        return elapsed

    def __enter__(self):
        self.start_time = self.clock.time()

    def __exit__(self, t, v, tb):
        self.stop()


class Timer(BaseMetric):

    """
    A timer metric which aggregates timing durations and provides duration statistics, plus
    throughput statistics via Meter and Histogram.

    """

    def __init__(
        self,
        key,
        size=DEFAULT_SIZE,
        alpha=DEFAULT_ALPHA,
        clock=time,
        sink=None,
        sample=None,
        tags=None
    ):
        super(Timer, self).__init__(key, tags)
        self.meter = Meter(key=key, tags=tags, clock=clock)
        self.hist = Histogram(
            key=key,
            tags=tags,
            size=size,
            alpha=alpha,
            clock=clock,
            sample=sample
        )
        self.sink = sink

    def get_count(self):
        "get count from internal histogram"
        return self.hist.get_count()

    def get_sum(self):
        "get sum from snapshot of internal histogram"
        return self.get_snapshot().get_sum()

    def get_max(self):
        "get max from snapshot of internal histogram"
        return self.get_snapshot().get_max()

    def get_min(self):
        "get min from snapshot of internal histogram"
        return self.get_snapshot().get_min()

    def get_mean(self):
        "get mean from snapshot of internal histogram"
        return self.get_snapshot().get_mean()

    def get_stddev(self):
        "get stddev from snapshot of internal histogram"
        return self.get_snapshot().get_stddev()

    def get_var(self):
        "get var from snapshot of internal histogram"
        return self.get_snapshot().get_var()

    def get_snapshot(self):
        "get snapshot from internal histogram"
        return self.hist.get_snapshot()

    def get_mean_rate(self):
        "get mean rate from internal meter"
        return self.meter.get_mean_rate()

    def get_one_minute_rate(self):
        "get 1 minut rate from internal meter"
        return self.meter.get_one_minute_rate()

    def get_five_minute_rate(self):
        "get 5 minute rate from internal meter"
        return self.meter.get_five_minute_rate()

    def get_fifteen_minute_rate(self):
        "get 15 rate from internal meter"
        return self.meter.get_fifteen_minute_rate()

    def update(self, seconds):
        if seconds >= 0:
            self.hist.add(seconds)
            self.meter.mark()
            if self.sink:
                self.sink.add(seconds)

    def time(self):
        """
        Parameters will be sent to signal, if fired.
        Returns a timer context instance which can be used from a with-statement.
        Without with-statement you have to call the stop method on the context
        """
        return Chronometer(self.meter.clock, on_stop=self.update)

    def clear(self):
        "clear internal histogram and meter"
        self.hist.clear()
        self.meter.clear()
