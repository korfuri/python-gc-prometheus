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

See the prometheus_client
[documentation](https://github.com/prometheus/client_python) to see
how to export the metrics via an HTTP server. If you're using Django,
check out
[django-prometheus](https://github.com/korfuri/django-prometheus)
which can export metrics to a Django view, and exports metrics
relevant to Django.

To aggregate the exported variables, see the [Prometheus.io documentation](http://prometheus.io/).

## Advanced usage

This package contains two series of metrics:

* gc stats, which simply export counters exposed by the
  [gc](https://docs.python.org/library/gc.html) module. This is mostly
  counters of objects. You can import these metrics alone by importing
  `gc_prometheus.stats`.
* gc profiling stats, which register callbacks with the gc module and
  add some negligible overhead to the garbage collection process. This
  is mostly counters of time spent in the GC process. You can import
  these metrics alone by importing `gc_prometheus.profile`.

Importing `gc_prometheus` imports both sets of metrics.
