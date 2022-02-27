REPO=ogre0403
IMAGE=train-fcu-bigdata
TAG = $(shell date '+%Y%m%d%H%M')



# build:
# 	docker build -t ${REPO}/$(IMAGE):tensorflow-$(TAG) -f tensorflow/Dockerfile ./tensorflow
# 	docker build -t ${REPO}/$(IMAGE):spark-$(TAG) -f spark/Dockerfile ./spark
# 	docker build -t ${REPO}/$(IMAGE):hadoop-$(TAG) -f hadoop/Dockerfile ./hadoop

.PHONY: build 

build: build-hadoop build-spark build-python build-tf

build-hadoop:
	docker build -t ${REPO}/$(IMAGE):hadoop-$(TAG) -f hadoop/Dockerfile ./hadoop

build-spark:
	docker build -t ${REPO}/$(IMAGE):spark-$(TAG) -f spark/Dockerfile ./spark

build-python:
	docker build -t ${REPO}/$(IMAGE):python-$(TAG) -f python/Dockerfile ./python

build-tf:
	docker build -t ${REPO}/$(IMAGE):tensorflow-$(TAG) -f tensorflow/Dockerfile ./tensorflow
