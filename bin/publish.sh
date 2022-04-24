#!/bin/bash

pip install --upgrade twine
twine upload --repository testpypi  -u __token__ -p $PYPIPASS dist/*