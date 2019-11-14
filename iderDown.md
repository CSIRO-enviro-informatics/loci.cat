---
permalink: /iderDown.html
---

# Loc-I IderDown 

[https://excelerator.loci.cat/iderdown](https://excelerator.loci.cat/iderdown)

The following provides a description of IderDown and what has been delivered, with an indication of future planned additional functionality for a more fully featured prototype.

## What

IderDown provides discovery and download of related Loc-I identifiers for selected spatial features. This tool will allow users to discover and download authoritative identifiers for spatial features published as Linked Data for a given set of spatial identifiers, specifically, the ability to query and filter spatial identifiers using one or more parent (containing) spatial features in the same dataset or one or more spatial features in a different Loc-I dataset. e.g. Give me a list of all the Meshblock identifiers in SA1 numbers 123 and 456; or give me a list of all GNAF address identifiers in ASGS SA1 number 123. 
Why: The primary use case for IDerDown is to be able to download spatial feature identifiers and relationships and append them to current spatial object identifiers for offline use in data integration and processing tasks.

## How
* Users are able to select an identifier set to be downloaded from a dropdown list. Users can then select a Loc-I dataset and spatial feature to filter the downloaded identifier set. Outputs returned to user in tabular form as a list of identifiers. 
* MVP: A web accessible user interface that will enable users to select a Loc-I dataset for which identifiers are to be downloaded. The selected download type (e.g Meshblock) will be able to be filtered by a parent feature type (e.g SA2) within that same dataset. The MVP release (version 1) provides functionality to access the current CSIRO release of the LOC-I cache which loads these datasets: ASGS 2016, Geofabric v2.1.1 and GNAF current.

## Anticipated future functionality 

* Enabling GNAF 2016 and relevant linksets (addr2catch, addr2mb) - estimate delivery as Release v2 December 2019
* Update of Geofabric v2.1.1. dataset with geometric topological relationship available (complete contracted catchment coverage via sfWithins, sfContains) - estimate delivery as Release v2 December 2019
* Filter by spatial features in a different Loc-I dataset (i.e. crosswalk via LinkSets) - estimate delivery as Release v2 December 2019
* Spatial query functions e.g. select identifiers to be downloaded using a selection box or area on a map  - not currently planned in FY2019-2020
