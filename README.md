# python-gc-prometheus
Export metrics about the Python garbage collector for Prometheus.io.

[![PyPI version](https://badge.fury.io/py/gc-prometheus.svg)](http://badge.fury.io/py/gc-prometheus)
[![Build Status](https://travis-ci.org/korfuri/python-gc-prometheus.svg?branch=master)](https://travis-ci.org/korfuri/python-gc-prometheus)

## Installation

```shell
pip install gc_prometheus
```

## Usage

Simply `import gc_prometheus` to register the metrics.

On Python 3.3 and above, more metrics are available, regarding the
time spent in the garbage collector. You can `import
gc_prometheus.profile` to register them.

See the prometheus_client
[documentation](https://github.com/prometheus/client_python) to see
how to export the metrics via an HTTP server. If you're using Django,
check out
[django-prometheus](https://github.com/korfuri/django-prometheus)
which can export metrics to a Django view, and exports metrics
relevant to Django.

To aggregate the exported variables, see the [Prometheus.io documentation](http://prometheus.io/).
