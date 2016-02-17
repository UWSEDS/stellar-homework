#!/bin/bash  

find . | grep -E "(__pycache__|\.pyc|\.pyo|\.zip|\.csv)" | xargs rm -rf
