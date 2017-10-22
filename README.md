# About

`cartography` is a example service written to provide reliable, tested and performant geocoding of an address.  The
service attempts to be built in idiomatic python and flask.  The interface is a simple REST API utilizing two resource
objects, the `coordinate` resource and the `cache_entry` resource.

# Installation

Installation is performed using `setuptools` and `setup.py`.

In addition to a Python 3 environment and its required modules the following external services are expected:

* [Hashicorp Consul](https://www.consul.io) for configuration management
* [Redis Cache for caching](https://redis.io)

## Quick Run via `docker-compose`

To assist with the running of this service, it provides a docker compose layout.  This will build the python image
where the service runs, and also deploy other dependencies in a cluster.

## Production run via `Dockerfile`

Running a `docker build` will build an image that contains the flask service entirely self contained.  The external
dependencies are assumed to exist somewhere else on the network (as large scale cache services or configuration
management are often in place in such conditions).

# Testing

Testing is done via python's `unittest` framework.  For convienance there is a test entry point provided at the root
that can be run with `test.py`

# Future Enhancements

