[![noforza](https://circleci.com/gh/nforoza/covid19-dashboards.svg?style=svg)](https://github.com/nforoza/covid19-dashboards)

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

## Bokeh aplication files

* An __init__.py file that marks this directory as a package. Package relative imports, e.g. from . import mymod and from .mymod import func will be possible.

* A request_handler.py file that allows declaring an optional function which processes the HTTP request and returns a dictionary of items to be included in the session token, as described in Request Handler Hooks.

* A app_hooks.py file that allows optional callbacks to be triggered at different stages of application execution, as described in Lifecycle Hooks and Request Handler Hooks.

* A static subdirectory that can be used to serve static resources associated with this application.

* A theme.yaml file that declaratively defines default attributes to be applied to Bokeh model types.

* A templates subdirectory with index.html Jinja template file. The directory may contain additional Jinja templates for index.html to refer to. The template should have the same parameters as the FILE template. See Customizing the Application’s Jinja Template for more details.

## Resources
### Datasets

### Data on COVID-19 (coronavirus) by Our World in Data
* https://github.com/owid/covid-19-data/tree/master/public/data

## License

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](https://opensource.org/licenses/MIT)