import gc
import sys
import unittest
from prometheus_client import REGISTRY
if sys.version_info >= (3, 3):
    import gc_prometheus.profile


class TestGcProfile(unittest.TestCase):
    def test_import_pre_py33(self):
        if sys.version_info < (3, 3):
            with self.assertRaises(ImportError):
                import gc_prometheus.profile

    def test_collection_time(self):
        current_total = REGISTRY.get_sample_value(
            'python_gc_collection_process_time_total_s')
        gc.collect()
        self.assertTrue(current_total < REGISTRY.get_sample_value(
            'python_gc_collection_process_time_total_s'))


if __name__ == '__main__':
    unittest.main()
