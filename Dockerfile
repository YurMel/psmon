FROM python:2.7

MAINTAINER Yuri Melnik <y_mel@ukr.net>

# Set workspace directory psmon Environment
ENV PATH /opt/psmon:$PATH

# Install dependencies packages Debian.
RUN apt-get update \
    && apt-get install -y git python-pip \
    && rm -rf /var/lib/apt/lists/*

# Install python modules
RUN pip install psutil

# Clone psmon utility into the docker container
RUN git clone https://github.com/YurMel/psmon.git /opt/psmon

ENTRYPOINT ["python", "/opt/psmon/psmon.py"]
