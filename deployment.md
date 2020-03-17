---
permalink: /deployment.html
---


## Application and Backend Docker Images Required

### Backend 

 
| Component            | Repo  |   Images |
|---------------------| -------| -------- |
| loci-integration-api |  * Github repo: https://github.com/CSIRO-enviro-informatics/loci-integration-api  | Main API based on `sanicframework/sanic:LTS`. [Dockerfile](https://github.com/CSIRO-enviro-informatics/loci-integration-api/blob/master/Dockerfile) ;  <BR> Elasticsearch image: `docker.elastic.co/elasticsearch/elasticsearch:6.3.1` |
|loci-cache | https://github.com/CSIRO-enviro-informatics/loci-cache-scripts/ |  Cache build docker image (based on `ubuntu:18.04`). See [Dockerfile](https://github.com/CSIRO-enviro-informatics/loci-cache-scripts/blob/jyucsiro/feature/gnaf_gf_harvest/docker/cache/Dockerfile) |
| loci-geometry-data-service |  https://github.com/CSIRO-enviro-informatics/loci-geometry-data-service |  Image name: `csiroenvinf/geometry-data-service`.  See https://hub.docker.com/r/csiroenvinf/geometry-data-service <br> Image name: `kartoza/postgis:12.0` | 



### Application

| Component            | Repo  |   Images |
|---------------------| -------| -------- |
| loci-explorer |  https://github.com/CSIRO-enviro-informatics/loci-integration-app |  Based on `node:10`. See [Dockerfile](https://github.com/CSIRO-enviro-informatics/loci-integration-app/blob/master/Dockerfile) |
| loci-excelerator (Excelerator / IderDown) |  https://github.com/CSIRO-enviro-informatics/loci-excelerator/ |  No docker deployment yet |
| loci-notebooks (Jupyter notebooks for Loc-I) |  https://github.com/CSIRO-enviro-informatics/loci-notebooks |  Image:  Based on `jupyter/minimal-notebook`. See [Dockerfile](https://github.com/CSIRO-enviro-informatics/loci-notebooks/blob/master/Dockerfile) | 

