

# WeConnect-Cupra-python
[![GitHub sourcecode](https://img.shields.io/badge/Source-GitHub-green)](https://github.com/lordyavin/WeConnect-Cupra-python)
[![GitHub release (latest by date)](https://img.shields.io/github/v/release/lordyavin/WeConnect-Cupra-python)](https://github.com/lordyavin/WeConnect-Cupra-python/releases/latest)
[![GitHub](https://img.shields.io/github/license/lordyavin/WeConnect-Cupra-python)](https://github.com/lordyavin/WeConnect-Cupra-python/blob/master/LICENSE)
[![GitHub issues](https://img.shields.io/github/issues/lordyavin/WeConnect-Cupra-python)](https://github.com/lordyavin/WeConnect-Cupra-python/issues)
[![PyPI - Downloads](https://img.shields.io/pypi/dm/weconnect-cupra-daern?label=PyPI%20Downloads)](https://pypi.org/project/weconnect-cupra-daern/)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/weconnect-cupra-daern)](https://pypi.org/project/weconnect-cupra-daern/)

Python API for the MyCupra Services. If you are not a developer and ended up here you probably want to check out a project using this library (see below).

## Projects in which the library is used
- [Cupra WeConnect Home Assistant Integration](https://github.com/lordyavin/cupra_we_connect)

## Install
```
pip3 install weconnect-cupra-lordyavin[Images]
```

## Package
```
python3 -m pip install --upgrade build
python3 -m build --sdist
python3 -m build --wheel
```

## Distribute
```
python3 -m pip install --upgrade twine
python3 -m twine upload --repository pypi dist/*
```

## Getting started
- To get started have a look in the [examples folder](https://github.com/lordyavin/WeConnect-Cupra-python/tree/main/examples)

## Tested with
- Cupra Born Model year 2022/23

## Login & Consent
WeConnect-python is based on the new WeConnect ID API that was introduced with the new series of ID cars. If you use another car or hybrid you probably need to agree to the terms and conditions of the WeConnect ID interface. Easiest to do so is by installing the WeConnect ID app on your smartphone and login there. If necessary you will be asked to agree to the terms and conditions.

## Reporting Issues
Please feel free to open an issue at [GitHub Issue page](https://github.com/lordyavin/WeConnect-Cupra-python/issues) to report problems you found.

See also https://github.com/daernsinstantfortress/WeConnect-Cupra-python/issues.

### Known Issues
- The API is in alpha state and may change unexpectedly at any time! Please conscider this and pin to a specific version if you depend on it.
- Examples and API documentation is missing

## Credits
Largely based on
* WeConnect-python for Cupra https://github.com/daernsinstantfortress/WeConnect-Cupra-python by daern
* WeConnect-python for VW from https://github.com/tillsteinbach/WeConnect-python, with the initial Cupra port developed by Alan Gibson
Inspired by [TA2k/ioBroker.vw-connect](https://github.com/TA2k/ioBroker.vw-connect/) that gave me a point to start working with the API
