import matplotlib.pyplot as plt
import numpy as np
from keras.preprocessing.image import ImageDataGenerator
from keras.datasets import mnist
from keras.datasets import fashion_mnist
import tensorflow as tf
from pylab import *




#class_names = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

def plot_single(img):
    plt.figure()
    plt.imshow(img)
    plt.colorbar()
    plt.grid(False)
    

def plot_batch(images, labels,class_names, n):
    plt.figure(figsize=(10,10))
    for i in range(n):
        plt.subplot(5,5,i+1)
        plt.xticks([])
        plt.yticks([])
        plt.grid(False)
        plt.imshow(images[i], cmap=plt.cm.binary)
        plt.xlabel(class_names[labels[i]])
    
def show_train_history(train_history,train,validation):
    plt.plot(train_history.history[train])
    plt.plot(train_history.history[validation])
    plt.title('Train History')
    plt.ylabel(train)
    plt.xlabel('Epoch')
    plt.legend(['train', 'validation'], loc='upper left')
    plt.show()
    
    
def plot_images_labels_prediction(images,labels,prediction,idx,num=10):
    fig = plt.gcf()
    fig.set_size_inches(12, 14)
    if num>25: num=25 
    for i in range(0, num):
        ax=plt.subplot(5,5, 1+i)
        ax.imshow(images[idx], cmap='binary')
        title= "label=" +str(labels[idx])
        if len(prediction)>0:
            title+=",predict="+str(prediction[idx]) 
            
        ax.set_title(title,fontsize=10) 
        ax.set_xticks([]);ax.set_yticks([])        
        idx+=1 
    plt.show()
    
def plot_image(i, predictions_array, true_label, img, class_names):
  predictions_array, true_label, img = predictions_array[i], true_label[i], img[i]
  plt.grid(False)
  plt.xticks([])
  plt.yticks([])
  
  plt.imshow(img, cmap=plt.cm.binary)

  predicted_label = np.argmax(predictions_array)
  if predicted_label == true_label:
    color = 'blue'
  else:
    color = 'red'
  
  plt.xlabel("{} {:2.0f}% ({})".format(class_names[predicted_label],
                                100*np.max(predictions_array),
                                class_names[true_label]),
                                color=color)

def plot_value_array(i, predictions_array, true_label):
  predictions_array, true_label = predictions_array[i], true_label[i]
  plt.grid(False)
  plt.xticks([])
  plt.yticks([])
  thisplot = plt.bar(range(10), predictions_array, color="#777777")
  plt.ylim([0, 1]) 
  predicted_label = np.argmax(predictions_array)
 
  thisplot[predicted_label].set_color('red')
  thisplot[true_label].set_color('blue')
    
    
def generate_shift_mnist_data(n):
    (X_train, y_train), (X_test, y_test) = mnist.load_data()
    X_train = X_train.reshape(X_train.shape[0], 1, 28, 28)
    X_test = X_test.reshape(X_test.shape[0], 1, 28, 28)
    # convert from int to float
    X_train = X_train.astype('float32')
    X_test = X_test.astype('float32')


    shift = 0.2
    datagen = ImageDataGenerator(width_shift_range=shift, height_shift_range=shift)
    # fit parameters from data
    datagen.fit(X_train)
    # configure batch size and retrieve one batch of images

    aa = 0
    bb = 0
    for X_batch, y_batch in datagen.flow(X_train, y_train, batch_size=n):
        aa = X_batch.reshape(n,28,28)
        bb = y_batch.reshape(n,)
        return aa, bb
        

def generate_shift_fashion_mnist_data(n):
    (X_train, y_train), (X_test, y_test) = fashion_mnist.load_data()
    X_train = X_train.reshape(X_train.shape[0], 1, 28, 28)
    X_test = X_test.reshape(X_test.shape[0], 1, 28, 28)
    # convert from int to float
    X_train = X_train.astype('float32')
    X_test = X_test.astype('float32')


    shift = 0.2
    datagen = ImageDataGenerator(width_shift_range=shift, height_shift_range=shift)
    # fit parameters from data
    datagen.fit(X_train)
    # configure batch size and retrieve one batch of images

    aa = 0
    bb = 0
    for X_batch, y_batch in datagen.flow(X_train, y_train, batch_size=n):
        aa = X_batch.reshape(n,28,28)
        bb = y_batch.reshape(n,)
        return aa, bb        


def layer(output_dim,input_dim,inputs, activation=None):
    W = tf.Variable(tf.random_normal([input_dim, output_dim]))
    b = tf.Variable(tf.random_normal([1, output_dim]))
    XWb = tf.matmul(inputs, W) + b
    if activation is None:
        outputs = XWb
    else:
        outputs = activation(XWb)
    return outputs


def show_activation(activation,y_lim=5):
    x=np.arange(-10., 10., 0.01)
    ts_x = tf.Variable(x)
    ts_y =activation(ts_x )
    with tf.Session() as sess:
        init = tf.global_variables_initializer()
        sess.run(init)
        y=sess.run(ts_y)
    ax = gca()
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    ax.spines['bottom'].set_position(('data',0))
    ax.spines['left'].set_position(('data',0))
    ax.xaxis.set_ticks_position('bottom')
    ax.yaxis.set_ticks_position('left')
    lines=plt.plot(x,y)
    plt.setp(lines, color='b', linewidth=3.0)
    plt.ylim(y_lim*-1-0.1,y_lim+0.1) 
    plt.xlim(-10,10) 

    plt.show()      