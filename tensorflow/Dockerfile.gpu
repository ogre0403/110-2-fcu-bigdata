FROM tensorflow/tensorflow:1.9.0-gpu

RUN pip install keras==2.2.2 

# RUN mkdir -p /workspace/course/
# mkdir -p /workspace/course/keras \
# mkdir -p /workspace/course/tensorflow

COPY util /workspace/course/util
COPY keras /workspace/course/keras
COPY tensorflow /workspace/course/tensorflow

COPY exercise/input /workspace/course/exercise/input
COPY exercise/Keras-fashion-MNIST-CNN.ipynb /workspace/course/exercise
COPY exercise/Keras-fashion-MNIST-MLP.ipynb /workspace/course/exercise
COPY exercise/TF-fashion-MNIST-CNN.ipynb /workspace/course/exercise
COPY exercise/TF-fashion-MNIST-MLP.ipynb /workspace/course/exercise

RUN mkdir -p /workspace/logs

COPY --chmod=755 bootstrap.sh /

EXPOSE 8888

WORKDIR "/workspace"

CMD ["/bootstrap.sh"]
