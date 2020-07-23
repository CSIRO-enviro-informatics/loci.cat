---
permalink: /integration-api.html
---

# Loc-I Integrated API

[Link to API here](https://api2.loci.cat).

## What

A REST API to a Loc-I Integrated Cache and other related data sources.

Example use of the Loc-I Integrated API in a Jupyter Notebook:
<iframe width="560" height="315" src="https://www.youtube.com/embed/EYlroy7sAtA?start=1084" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

## Why

Provides developers and technical analysts with interfaces to the [Loc-I reference cache](ref-cache.md) and other sources, to build applications and query a Loc-I cache without having to know SPARQL. This allows rapid development of applications using the REST API.

## How 

Via the REST API. Swagger doc available [here](https://api.loci.cat/api/v1/doc).

     
## MVP 

![Loc-I Technical Architecture Overview](images/loci-integrated-api-1.PNG "Loc-I Technical Architecture Overview")


## Anticipated future functionality

* Added API endpoints to handle "L-shaped" and "U-shaped" crosswalks between geographies


## /location/overlaps 

A note on the /location/overlaps endpoint - for operations needing area calculations, the loci-integration-api is currently limited to these feature types due to availability of albers areas values (or just point data):

### ASGS


### ASGS 2016 Main Structures (see https://asgsld.net/2016/)

| Feature Type  | Prefix | Shortcode | Alias  |  
|---|---|---|---|---|
| [State or Territory](https://asgsld.net/2016/stateorterritory/)  | http://linked.data.gov.au/dataset/asgs2016/stateorterritory/  | asgs16_ste  |  STE |  
| [Statistical Area Level 1](https://asgsld.net/2016/statisticalarealevel1/)  | http://linked.data.gov.au/dataset/asgs2016/statisticalarealevel1/   |  asgs16_sa1 |  SA1 |  
| [Statistical Area Level 2](https://asgsld.net/2016/statisticalarealevel2/)  | http://linked.data.gov.au/dataset/asgs2016/statisticalarealevel2/   |  asgs16_sa2 |  SA2 |  
| [Statistical Area Level 3](https://asgsld.net/2016/statisticalarealevel3/)  |  http://linked.data.gov.au/dataset/asgs2016/statisticalarealevel3/ |  asgs16_sa3 | SA3  |  
| [Statistical Area Level 4](https://asgsld.net/2016/statisticalarealevel4/)  |  http://linked.data.gov.au/dataset/asgs2016/statisticalarealevel4/ |  asgs16_sa4 |  SA4 |  
| [MeshBlock](https://asgsld.net/2016/meshblock/)  | http://linked.data.gov.au/dataset/asgs2016/meshblock/  |  asgs16_mb | MB  |  

### ASGS 2016 Other ABS Structures (see https://asgsld.net/2016/)

| Feature Type  | Prefix | Shortcode | Alias  |  
|---|---|---|---|---|
| [Greater Capital City Statistical Areas](https://asgsld.net/2016/greatercapitalcitystatisticalarea/)  | http://linked.data.gov.au/dataset/asgs2016/greatercapitalcitystatisticalarea/   |  asgs16_gccsa |  GCCSA |  
| [Remoteness Areas](https://asgsld.net/2016/remotenessarea/)  |  http://linked.data.gov.au/dataset/asgs2016/remotenessarea/ |  asgs16_ra | RA  |  

### ASGS 2016 Other Non-ABS Structures 

These are ABS's approximations (based on Mesh Blocks) of the feature types.

| Feature Type  | Prefix | Shortcode | Alias  |  
|---|---|---|---|---|
| [Local Government Areas](https://asgsld.net/2016/localgovernmentarea/)  | http://linked.data.gov.au/dataset/asgs2016/localgovernmentarea/  | asgs16_lga  |  LGA |  


### Geofabric v2.1.1 (see https://geofabricld.net/)

| Feature Type  | Prefix | Shortcode | Alias  |  
|---|---|---|---|---|
| [AWRADrainageDivision](https://geofabricld.net/drainagedivision/)  | http://linked.data.gov.au/dataset/geofabric/drainagedivision/  | geofabric2_1_1_awradrainagedivision  |  dd |  
| [HR River Region](https://geofabricld.net/riverregion/)  | http://linked.data.gov.au/dataset/geofabric/riverregion/  | geofabric2_1_1_riverregion  |  rr |  
| [AHGFContractedCatchments](https://geofabricld.net/contractedcatchment/)  | http://linked.data.gov.au/dataset/geofabric/contractedcatchment/  | geofabric2_1_1_ahgfcontractedcatchment  |  cc | 
 

### G-NAF 2016 (see https://gnafld.net/)


| Feature Type  | Prefix | Shortcode | Alias  |  
|---|---|---|---|---|
| [Address](https://gnafld.net/2016-05/address/)  | http://linked.data.gov.au/dataset/gnaf-2016-05/address/  | gnaf1605_addr  |  addr |  
| [Street Locality](https://gnafld.net/2016-05/streetLocality/)  | http://linked.data.gov.au/dataset/gnaf-2016-05/streetLocality/  | gnaf1605_streetlocality  |  streetlocality |  
| [Locality](https://gnafld.net/2016-05/locality/)  | http://linked.data.gov.au/dataset/gnaf-2016-05/locality/  | gnaf1605_locality  |  locality | 
