from applipy_metrics.registry import MetricsRegistry

from applipy import Module


class MetricsModule(Module):

    def configure(self, bind, register):
        bind(MetricsRegistry)
