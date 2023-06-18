FROM nvidia/cuda:12.1.0-devel-ubuntu22.04

ENV HOME /home
ENV PYTHON_VERSION 3.11.2
ENV TZ=Asia/Tokyo
WORKDIR /workspace

RUN apt-get update && apt-get -y upgrade
RUN apt-get install -y git python3 python3-pip build-essential

COPY ./app/diffusion_app/requirements.txt .

RUN pip install -r requirements.txt
RUN pip install torch --index-url https://download.pytorch.org/whl/cu118
