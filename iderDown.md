---
permalink: /iderDown.html
---

# Loc-I IderDown 

[https://excelerator.loci.cat/iderdown](https://excelerator.loci.cat/iderdown)


## What

IderDown provides discovery and download of related Loc-I identifiers for selected spatial features. This tool will allow users to discover and download authoritative identifiers for spatial features published as Linked Data for a given set of spatial identifiers, specifically, the ability to query and filter spatial identifiers using one or more parent (containing) spatial features in the same dataset or one or more spatial features in a different Loc-I dataset. e.g. Give me a list of all the Meshblock identifiers in SA1 numbers 123 and 456; or give me a list of all GNAF address identifiers in ASGS SA1 number 123. 

Why: The primary use case for IDerDown is to be able to download spatial feature identifiers and relationships and append them to current spatial object identifiers for offline use in data integration and processing tasks.

The figure below shows the User Interface and visualises an example of using IderDown with an input of a ASGS2016 
Statistical Area Level 2 location and asking IderDown to return related location features in the same and different
geographies -  ASGS2016 Statistical Area Level 1, G-NAF Street Localities, Geofabric Contracted Catchments. 

![iderDown](images/iderdown.png "IderDown overview")


## How
* Users are able to select an identifier set to be downloaded from a dropdown list. Users can then select a Loc-I dataset and spatial feature to filter the downloaded identifier set. Outputs returned to user in tabular form as a list of identifiers. 
* MVP: A web accessible user interface that enables users to select a Loc-I dataset for which identifiers are to be downloaded. The selected download type (e.g Meshblock) will be able to be filtered by a parent feature type (e.g SA2) within that same dataset. 

The MVP release (version 1) provides these features:
* Access the current CSIRO release of the [Loc-I reference cache](ref-cache.md) which loads these datasets: ASGS 2016, Geofabric v2.1.1 and GNAF 2016.
* Filter by spatial features in a different Loc-I dataset (i.e. crosswalk via LinkSets) 


## Anticipated future functionality 

* Spatial query functions e.g. select identifiers to be downloaded using a selection box or area on a map  - not currently planned in FY2019-2020
