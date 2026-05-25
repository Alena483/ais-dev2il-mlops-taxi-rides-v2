FROM ubuntu:latest
LABEL authors="krylo"

ENTRYPOINT ["top", "-b"]