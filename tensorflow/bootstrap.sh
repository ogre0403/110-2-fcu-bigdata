#! /bin/bash

tensorboard  --logdir /workspace/logs --host 0.0.0.0 --debugger_port 6064 &

jupyter notebook --allow-root --ip=* --NotebookApp.token='' --notebook-dir=/workspace

