FROM openjdk:8u312-slim


# setup sshd

RUN sed -i 's/deb.debian.org/free.nchc.org.tw/g' /etc/apt/sources.list && \
    apt update && \
    apt install -y openssh-client openssh-server vim 


# install python2
RUN apt install -y python curl && \
    curl https://bootstrap.pypa.io/pip/2.7/get-pip.py --output get-pip.py && \
    python2 get-pip.py && \
    pip install jupyter



ENV SPARK_VERSION=spark-2.2.0-bin-hadoop2.7

COPY ${SPARK_VERSION}.tgz /opt

RUN tar zxvf /opt/${SPARK_VERSION}.tgz -C /opt && \
    mv /opt/${SPARK_VERSION} /opt/spark && \
    rm /opt/${SPARK_VERSION}.tgz


RUN echo 'export SPARK_HOME=/opt/spark'             >> /root/.bashrc && \
    echo 'export PATH=$SPARK_HOME/bin:$PATH'        >> /root/.bashrc && \
    echo 'export PYSPARK_DRIVER_PYTHON=jupyter'     >> /root/.bashrc && \
    echo "export PYSPARK_DRIVER_PYTHON_OPTS='notebook --allow-root --ip=0.0.0.0 --no-browser --NotebookApp.token='' --notebook-dir=/tmp/work '" >> /root/.bashrc


WORKDIR /root


COPY entry.sh /opt
CMD ["bash", "/opt/entry.sh"]
