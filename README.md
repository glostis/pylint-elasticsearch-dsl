# pylint-elasticsearch-dsl

[![Build Status](https://travis-ci.com/glostis/pylint-elasticsearch-dsl.svg?branch=master)](https://travis-ci.com/glostis/pylint-elasticsearch-dsl)
[![PyPI](https://img.shields.io/pypi/v/pylint-elasticsearch-dsl)](https://pypi.org/project/pylint-elasticsearch-dsl)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

[`pylint`](https://www.pylint.org/) plugin for the
[`elasticsearch-dsl`](https://elasticsearch-dsl.readthedocs.io/en/latest/) package

This plugin is needed to help `pylint` understand the types of some objects of the `elasticsearch-dsl`
package.

## Installation

```
pip install pylint-elasticsearch-dsl
```

## Scope

Currently, this plugin only patches the false positive `invalid-unary-operand-type` error
that is triggered when writing for example:
```python
from elasticsearch_dsl import Q

~Q("exists", field="foo")
```
See [this issue](https://github.com/PyCQA/pylint/issues/3258) for more details.

## Contributing

To work on this project, install the development requirements by running:
```
make install
```

The tests can be run with:
```
make test
```
