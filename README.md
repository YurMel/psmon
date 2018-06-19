# PSMON

PSMON is a sipmle python script that collects metrics about your linux server.
It is capable of collecting cpu, memory, network, i/o, load and disk metrics

## Getting Started

  * Install `sudo apt-get install python3-pip git` (for Python 2.7+).
  * Install `sudo apt-get install python-pip git` (for Python 3.4+).

## Install psutil

  * Install via `pip install psutil` (for Python 2.7+).
  * Install via `pip3 install psutil` (for Python 3.4+).

## Usage python script

  * Systax: `./psmon.py <arg>`
  * Options `<arg>`
    - `cpu`
    - `mem`
    - `swap`
    - `disk`

  Run scritps in workspace directory (**Example**)
  ```sh
  ./psmon3.py mem
  ```

## Run into the Docker
  * Install docker according official [documentation](https://docs.docker.com/install/linux/docker-ce/debian/)
  * Build `docker build . -t psmon3`
  * Run into Docker `docker run psmon3 <arg>`
