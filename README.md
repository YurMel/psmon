# PSMON

PSMON is a sipmle python script that collects metrics about your linux server
It is capable of collecting cpu, memory, network, i/o, load and disk metrics

## Getting Started

  * Install `sudo apt-get install python-pip git`.

## Install psutil

  * Install via `pip install psutil`.

## Usage

  systax: `./psmon <arg>`
  Argument `<arg>` can be `cpu` or `mem`

  ```sh
    ./psmon mem
  ```

## Build

  `docker build . -t psmon`

## Run into Docker

  `docker run psmon <arg>`