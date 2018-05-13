# PSMON

PSMON is a sipmle python script that collects metrics about your linux server.
It is capable of collecting cpu, memory, network, i/o, load and disk metrics

## Getting Started

  * Install `sudo apt-get install python-pip git`.

## Install psutil

  * Install via `pip install psutil`.

## Usage python script

  * Systax: `./psmon.py <arg>`
  * Options `<arg>`
    - `cpu`
    - `mem`
    - `swap`
    - `disk`

  Run scritps in workspace directory (**Example**)
  ```sh
  ./psmon.py mem
  ```

## Run into the Docker
  * Install docker according official [documentation](https://docs.docker.com/install/linux/docker-ce/debian/)
  * Build `docker build . -t psmon`
  * Run into Docker `docker run psmon <arg>`
