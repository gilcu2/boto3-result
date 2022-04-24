#!/bin/bash

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
PROJECT_DIR=$DIR/..
export PYTHONPATH=$PROJECT_DIR/src/main

TEST_DIR=$PROJECT_DIR/src/test
pytest $TEST_DIR/*