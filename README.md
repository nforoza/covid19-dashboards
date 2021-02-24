[![noforza](https://circleci.com/gh/nforoza/microservices-kubernetes.svg?style=svg)](https://github.com/nforoza/microservices-kubernetes)

![Python](https://img.shields.io/badge/python-v3.7+-blue.svg)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](https://opensource.org/licenses/MIT)
![](https://img.shields.io/badge/OS-Linux%20%7CmacOS-blue)

## Covid 19 Dashboards with Kubernetes

This project deploys a Bokeh Server with the last updated data from covid collected from different sources across internet  

## Installation
1. Setup the environment pre requisites:

* [Python](https://www.python.org/)
* [Docker](https://docs.docker.com/)
* [Docker Hub account](https://hub.docker.com/)
* [Kubernetes](https://kubernetes.io/docs/tasks/tools/)
* [minikube](https://minikube.sigs.k8s.io/docs/start/)
* [Bokeh](https://bokeh.org/)

2. On your bash console run
    >`make`

    >`make install`
## Usage

1. Standalone:  
    >`python app.py`
2. Run in Docker:  
    >`./run_docker.sh`
3. Run in Kubernetes:
    >`minikube start`  
    
    >`./run_kubernetes.sh`
## Project files

* `Makefile`
A Makefile which defines the set of tasks to be executed for this project installation.

* `Dockerfile`
Docker container definition for running the house price predictor service.

* `requirements.txt` Python libraries dependencies.

## Resources
### Datasets

## License

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](https://opensource.org/licenses/MIT)