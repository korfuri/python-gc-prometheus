import sys
import unittest

class TestImports(unittest.TestCase):

    @unittest.skipIf(sys.version_info >= (3, 3),
                     'gc_prometheus.profile is available on Python>=3.3')
    def test_import_pre_py33(self):
        with self.assertRaises(ImportError):
            import gc_prometheus.profile

    def test_import_successful(self):
        import gc_prometheus
        import gc_prometheus.stats
