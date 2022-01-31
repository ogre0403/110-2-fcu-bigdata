FROM openjdk:8u312-slim


# setup sshd

RUN sed -i 's/deb.debian.org/free.nchc.org.tw/g' /etc/apt/sources.list && \
    apt update && \
    apt install -y openssh-client openssh-server vim 
COPY ssh-key /root/.ssh
RUN mkdir /run/sshd

# install web terminal, https://github.com/Senzing/docker-xterm.git

COPY requirements.txt /root
COPY ./web-terminal /

RUN apt install -y python3-pip && \
    pip3 install -r /root/requirements.txt  && \
    rm /root/requirements.txt


# setup hadoop
# TODO: download from mirror site

ENV HADOOP_VERSION=hadoop-2.6.0-cdh5.5.1

COPY ${HADOOP_VERSION}.tar.gz /opt

RUN tar zxvf /opt/${HADOOP_VERSION}.tar.gz -C /opt && \
    mv /opt/${HADOOP_VERSION} /opt/hadoop && \
    rm /opt/${HADOOP_VERSION}.tar.gz

COPY hadoop/*.xml /opt/hadoop/etc/hadoop

RUN echo 'export JAVA_HOME=/usr/local/openjdk-8'                    >> /root/.bashrc && \
    echo 'export HADOOP_HOME=/opt/hadoop'                          >> /root/.bashrc && \
    echo 'export HADOOP_MAPRED_HOME=$HADOOP_HOME'                   >> /root/.bashrc && \
    echo 'export HADOOP_COMMON_HOME=$HADOOP_HOME'                   >> /root/.bashrc && \
    echo 'export HADOOP_HDFS_HOME=$HADOOP_HOME'                     >> /root/.bashrc && \
    echo 'export HADOOP_CONF_DIR=$HADOOP_HOME/etc/hadoop'           >> /root/.bashrc && \
    echo 'export YARN_HOME=$HADOOP_HOME'                            >> /root/.bashrc && \            
    echo 'export YARN_CONF_DIR=$HADOOP_HOME/etc/hadoop'             >> /root/.bashrc && \
    echo 'export PATH=$PATH:$HADOOP_HOME/bin:$HADOOP_HOME/sbin'     >> /root/.bashrc 

# setup HIVE

# setup Mahout

# setup Spark


WORKDIR /root

COPY entry.sh /opt
CMD ["bash", "/opt/entry.sh"]
