#!/bin/bash

pyfiglet QUALITY


echo "Apply linting..."
autopep8 --aggressive --in-place --recursive .
isort . --quiet
LINTING=$(flake8 .)
if [[ "$LINTING" != "0" ]]; then
  echo "Linting failure:"
  echo "${LINTING}"
  exit 1
fi
echo "Linting success!"

echo "Running unit tests..."
coverage erase
TESTS=$(coverage run -m unittest $1 2>&1 >/dev/null)
FAILED="(failures="
ERRORS="(errors="
if [[ "$TESTS" == *"$FAILED"* || "$TESTS" == *"$ERRORS"* ]]; then
  echo "Unit tests failure:"
  echo "${TESTS}"
  exit 1
fi
echo "All unit tests passed!"

echo "Checking coverage..."
FAILURE="failure"
COVERAGE=$(coverage report)
if [[ "$COVERAGE" == *"$FAILURE"* ]]; then
  echo "Coverage failure:"
  echo "${COVERAGE}"
  exit 1
fi
coverage xml
echo "Coverage success!"

