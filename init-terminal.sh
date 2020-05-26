#!/bin/bash
set -e

cd src && python main.py -f "../dist/input-routes.csv"
