FROM openjdk:8u312-slim


RUN apt update && \
    apt install -y openssh-client openssh-server vim 

RUN mkdir /run/sshd

COPY hadoop-2.6.0-cdh5.5.1.tar.gz /opt


COPY ssh-key /root/.ssh

RUN tar zxvf /opt/hadoop-2.6.0-cdh5.5.1.tar.gz -C /root && \
    mv /root/hadoop-2.6.0-cdh5.5.1 /root/hadoop

COPY hadoop/*.xml /root/hadoop/etc/hadoop

RUN echo 'export JAVA_HOME=/usr/local/openjdk-8'                    >> /root/.bashrc && \
    echo 'export HADOOP_HOME=/root/hadoop'                          >> /root/.bashrc && \
    echo 'export HADOOP_MAPRED_HOME=$HADOOP_HOME'                   >> /root/.bashrc && \
    echo 'export HADOOP_COMMON_HOME=$HADOOP_HOME'                   >> /root/.bashrc && \
    echo 'export HADOOP_HDFS_HOME=$HADOOP_HOME'                     >> /root/.bashrc && \
    echo 'export HADOOP_CONF_DIR=$HADOOP_HOME/etc/hadoop'           >> /root/.bashrc && \
    echo 'export YARN_HOME=$HADOOP_HOME'                            >> /root/.bashrc && \            
    echo 'export YARN_CONF_DIR=$HADOOP_HOME/etc/hadoop'             >> /root/.bashrc && \
    echo 'export PATH=$PATH:$HADOOP_HOME/bin:$HADOOP_HOME/sbin'     >> /root/.bashrc 


# install web terminal, https://github.com/Senzing/docker-xterm.git

COPY requirements.txt /root
COPY ./web-terminal /

RUN apt install -y python3-pip && \
    pip3 install -r /root/requirements.txt 

WORKDIR /root

COPY entry.sh /root
CMD ["bash", "/root/entry.sh"]
