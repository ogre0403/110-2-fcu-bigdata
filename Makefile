REPO=ogre0403
IMAGE=train-fcu-bigdata
TAG = $(shell date '+%Y%m%d')



build:
	docker build -t ${REPO}/$(IMAGE):tensorflow-$(TAG) -f tensorflow/Dockerfile ./tensorflow
	docker build -t ${REPO}/$(IMAGE):spark-$(TAG) -f spark/Dockerfile ./spark
	docker build -t ${REPO}/$(IMAGE):hadoop-$(TAG) -f hadoop/Dockerfile ./hadoop

