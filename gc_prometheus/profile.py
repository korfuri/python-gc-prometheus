import gc
import gc_prometheus  # Forces an import of the common metrics
import prometheus_client
import sys
import time

if sys.version_info < (3, 3):
    raise ImportError(
        'gc_prometheus.profile is only available for Python >=3.3')

collection_total = prometheus_client.Gauge(
    'python_gc_collection_process_time_total_s',
    'Total process time spent in garbage collection')


class GcProfiler(object):
    def __init__(self):
        self.last_collection_start = None

    def Now(self):
        return time.process_time()

    def UpdateMetrics(self, interval):
        collection_total.inc(interval)

    def Callback(self, phase, info):
        if phase == 'start':
            self.last_collection_start = self.Now()
        elif phase == 'stop':
            now = self.Now()
            self.UpdateMetrics(now - self.last_collection_start)

profiler = GcProfiler()
gc.callbacks.append(profiler.Callback)
