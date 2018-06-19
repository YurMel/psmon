FROM python:3.6

MAINTAINER Yuri Melnik <y_mel@ukr.net>

# Set workspace directory psmon Environment
ENV PATH /opt/psmon:$PATH

# Install dependencies packages Debian.
RUN apt-get update \
    && apt-get install -y git python3-pip \
    && rm -rf /var/lib/apt/lists/*

# Install python modules
RUN pip3 install psutil

# Clone psmon utility into the docker container
RUN git clone https://github.com/YurMel/psmon.git /opt/psmon

ENTRYPOINT ["python3", "/opt/psmon/psmon3.py"]
