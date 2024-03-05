DOCKER_IMAGE_NAME = tr_bg_bot
DOCKER_IMAGE_TAG = latest

all: build run

build:
	docker build -t $(DOCKER_IMAGE_NAME):$(DOCKER_IMAGE_TAG) .

run:
	docker run -it --name $(DOCKER_IMAGE_NAME) --env-file .env $(DOCKER_IMAGE_NAME):$(DOCKER_IMAGE_TAG)

clean:
	docker stop $(DOCKER_IMAGE_NAME)
	docker rm $(DOCKER_IMAGE_NAME)
	docker rmi $(DOCKER_IMAGE_NAME):$(DOCKER_IMAGE_TAG)

re: clean all

.PHONY: all build run clean re