FROM golang:1.8

RUN mkdir /docker_boom
COPY main.go  /docker_boom
WORKDIR /docker_boom
RUN go build main.go

EXPOSE 8080
CMD ["./main"]
