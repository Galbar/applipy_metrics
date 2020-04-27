class Version:
    MAJOR: str = '0'
    MINOR: str = '1'
    PATCH: str = '0'

    VERSION: str = '.'.join((MAJOR, MINOR))
    RELEASE: str = '.'.join((MAJOR, MINOR, PATCH))


__version__ = Version.RELEASE


__all__ = [
    'MetricsRegistry',
    'clear',
    'count_calls',
    'counter',
    'dump_metrics',
    'gauge',
    'global_registry',
    'hist_async_calls',
    'hist_calls',
    'histogram',
    'meter',
    'meter_calls',
    'set_global_registry',
    'time_async_calls',
    'time_calls',
    'timer',
]


from .registry import (
    MetricsRegistry,
    clear,
    counter,
    dump_metrics,
    gauge,
    global_registry,
    histogram,
    meter,
    set_global_registry,
    timer,
)
from .decorators import (
    count_calls,
    hist_async_calls,
    hist_calls,
    meter_calls,
    time_async_calls,
    time_calls,
)
