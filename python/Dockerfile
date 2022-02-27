FROM python:3.10.2-bullseye

COPY requirements.txt /root


RUN pip3 install -r /root/requirements.txt  && \
    rm /root/requirements.txt

RUN mkdir -p /workspace/course
COPY basic /workspace/course
COPY simple-stock /workspace/course

EXPOSE 8888

CMD ["jupyter","notebook", "--allow-root", "--ip=*","--NotebookApp.token=''","--notebook-dir=/workspace"]
