#!/bin/bash


/usr/sbin/sshd -D &

sleep 10s

DIR="/tmp/work/hadoop_dir/dfs/name"



source /root/.bashrc

ssh-keyscan localhost >> /root/.ssh/known_hosts
ssh-keyscan 0.0.0.0 >> /root/.ssh/known_hosts

if [ -d "$DIR" ]; then
  ### Take action if $DIR exists ###
  echo "HDFS already formated"
else
  ###  Control will jump here if $DIR does NOT exists ###
  echo "Format HDFS"
  hadoop namenode -format
fi

start-dfs.sh
start-yarn.sh

python3 /app/xterm.py &

wait -n
exit $?