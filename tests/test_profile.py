import gc
import sys
import unittest
from prometheus_client import REGISTRY
import gc_prometheus


@unittest.skipIf(sys.version_info < (3, 3),
                 'gc_prometheus.profile is only available for python>=3.3')
class TestGcProfile(unittest.TestCase):
    def test_collection_time(self):
        current_total = REGISTRY.get_sample_value(
            'python_gc_collection_process_time_total_s')
        gc.collect()
        self.assertTrue(current_total < REGISTRY.get_sample_value(
            'python_gc_collection_process_time_total_s'))


if __name__ == '__main__':
    unittest.main()
