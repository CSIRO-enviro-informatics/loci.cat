---
permalink: /excelerator.html
---

# Excelerator  

[http://excelerator.loci.cat](http://excelerator.loci.cat)

## What 

A data reapportionment tool. This tool will enable users to reapportion data referenced using one Loc-I data set to another Loc-I dataset, e.g. population count by ASGS Meshblocks reapportioned to Geofabric contracted catchments. 

## Why 

Reapportioning data is a frequently performed, time-consuming and error prone function. Pre-calculating the correspondences between Loc-I datasets and publishing these in machine-readable ways enable users to access and use reliable recipes for spatial reapportionment of data. 
How: Users are provided an online portal to upload or (reference a web accessible) tabular data file that contains a georeferenced column and a data column with rows containing spatial feature identifiers and corresponding data values. Using the source user input to the tool, the tool will utilise the Loc-I dataset to determine what reapportionments are possible. This is done using pre-calculated linksets that describe the spatial intersection between Loc-I datasets. The user will select a target reapportionment loci dataset and hit go. The system will calculate the reapportionment and provide an output spreadsheet containing the reapportioned data and Loc-I identifiers for each spatial feature in the target Loc-I dataset.

MVP –  An online user interface providing basic ability to reapportion data uploaded in a spreadsheet georeferenced using a source Loc-I dataset to a target Loc-I dataset output as a tabular file for download. The MVP is limited to conversions between dataset base types which are “Meshblock” for the ASGS datasets, “Contracted Catchment” for the Geofabric dataset.

## Anticipated future functionality

* Ability to autodetect uploaded geographies
* Ability to convert reapportion between products at different level e.g. Contracted catchments to SA1s
* Ability to incorporate more sophisticated reapportionment processes including interaction with the “Your Data Your Regions (YDYR)” tool 
* Ability to reapportion data in web accessible files
* More sophisticated tools to assist users in reapportionment – map view of their data 
