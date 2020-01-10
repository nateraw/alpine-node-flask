SRC?=$(shell 'pwd')/app

build:
	docker build -t nateraw/alpine-node-flask -f Dockerfile .
start: build
	docker run --rm -it -p 80:80 nateraw/alpine-node-flask
