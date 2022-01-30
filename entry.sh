#!/bin/bash


/usr/sbin/sshd -D &

python3 /app/xterm.py &

wait -n
exit $?