#!/bin/bash

source /root/.bashrc



/opt/spark/bin/pyspark &

wait -n
exit $?