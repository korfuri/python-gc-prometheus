import gc
import unittest
from prometheus_client import REGISTRY
import gc_prometheus.stats


class TestGcPrometheus(unittest.TestCase):
    def test_enabled(self):
        self.assertEqual(1, REGISTRY.get_sample_value('python_gc_enabled'))
        try:
            gc.disable()
            self.assertEqual(0, REGISTRY.get_sample_value('python_gc_enabled'))
        finally:
            gc.enable()

    def test_debug(self):
        self.assertEqual(0, REGISTRY.get_sample_value('python_gc_debug'))
        try:
            gc.set_debug(gc.DEBUG_STATS)
            self.assertEqual(gc.DEBUG_STATS, REGISTRY.get_sample_value(
                'python_gc_enabled'))
        finally:
            gc.set_debug(0)

    def test_thresholds(self):
        self.assertTrue(REGISTRY.get_sample_value(
            'python_gc_threshold', labels={'generation': '0'}) is not None)
        self.assertTrue(REGISTRY.get_sample_value(
            'python_gc_threshold', labels={'generation': '1'}) is not None)
        self.assertTrue(REGISTRY.get_sample_value(
            'python_gc_threshold', labels={'generation': '2'}) is not None)
        original_thresholds = gc.get_threshold()
        try:
            gc.disable()
            gc.set_threshold(42, 43, 44)
            self.assertEqual(42, REGISTRY.get_sample_value(
                'python_gc_threshold', labels={'generation': '0'}))
            self.assertEqual(43, REGISTRY.get_sample_value(
                'python_gc_threshold', labels={'generation': '1'}))
            self.assertEqual(44, REGISTRY.get_sample_value(
                'python_gc_threshold', labels={'generation': '2'}))
        finally:
            gc.set_threshold(*original_thresholds)
            gc.enable()


if __name__ == '__main__':
    unittest.main()
