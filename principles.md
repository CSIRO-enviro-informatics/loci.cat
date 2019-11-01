---
permalink: /principles.html
---

# Principles

Loc-I is tackling the challenge of stabilising the identity of geographies and their locations. 
By stabilising the identity of geographies and their locations, people and systems are able to reference locations more precisely and interoperate across geographies in a more seamless way. 
This is achieved using ontologies and Linked Data identifiers for items in the respective datasets. 

## Ontologies 

An ontology is a document which captures the conceptual model of things in the world. The ontologies provide the foundational semantic definitions needed for consistently describing the respective geography dataset, their members and its relationships to other objects, e.g. ASGS 2016 and its features such as each Mesh Block, SA1, SA2, SA3, and SA4 region. The figure below show how the ASGS dataset is “spatially-enabled” into Loc-I by documenting the semantic concepts and relationships of the ASGS dataset. 

Figure 1. Example of the ASGS dataset that has been spatially-enabled into Loc-I using the ASGS ontology
![ASGS ontology example](images/asgs-ont-dataset-ex1.png "ASGS ontology example")

In the current version of Loc-I, ontologies have been developed for each geography, i.e. ASGS, Geofabric, G-NAF.  More details on the Loc-I ontologies can be found here: http://locationindex.org/definitional.html


Linksets introduces a consistent way to access, analyse and use location data to support reliable and repeatable processes through automation and application of standards. Streamline data access and analysis provides faster and more accurate way to support a range of policy questions. Linking data together is a good way to extract inforamtiion from different sources.

## Linked Data Identifiers

Linked Data uses the Web to connect related data together via web identifiers. These web identifiers are the building blocks on which descriptions of data can attached. These then form a graph of data that is scalable online. Web identifiers are minted for each Loc-I location to enable linking that is unambiguous, i.e. instead of linking terms like “ACT”, we can now unambiguously use the web identifier ‘http://linked.data.gov.au/dataset/asgs2016/stateorterritory/8’ to reference the location, which resolves to a ASGS State or Territory Feature. This Feature is also a concept that has been explicitly captured and defined in the ASGS ontology as a concept. Looking up the web identifier provides additional information about the resource and related objects, which in turn could be resolved to get more information. 

We can also similarly apply these for other Feature types that is defined in the data and captured in the respective ontology, such as ASGS Statistical Area 1 Features. These in turn can then be used to resolve and annotate relevant information about the feature using Linked Data systems, for example, for the ASGS 2016 SA1 of 80105104902, we can mint the Linked Data web identifier of http://linked.data.gov.au/dataset/asgs2016/statisticalarealevel1/80105104902, and annotate information such as which regions in the ASGS 2016 that they are within or contain, what are the alternate labels used to identify this region, and other regions that this feature intersects with. 

The figure below shows an excerpt of the Linked Data graph view of the ASGS 2016 dataset where  http://linked.data.gov.au/dataset/asgs2016/stateorterritory/8 is linked with the SA1 region http://linked.data.gov.au/dataset/asgs2016/statisticalarealevel1/80105104902 by the ‘within state’ property and additional information about each data item has more details annotated as nodes in the graph, such as the label, the category the SA1 region belongs to and the area. 

![ASGS Data Example](images/asgs-data-ex.png "ASGS Data Example")

Nodes such as these can then be easily connected to other Dataset nodes and scaled up across the world-wide-web (WWW) as a web of data. Users can then traverse these links using standard web protocols. The Loc-I infrastructure also caches these nodes in a central RDF triple store and provides APIs to query these resources via a Hybrid Spatial Knowledge Graph (see the next section for more details).

## Loc-I Datasets

As discussed above, in order to create a Loc-I dataset from a spatial dataset such as the ASGS, the semantics and identity of the resources of the spatial dataset is required. 

## Loc-I Linksets

Loc-I Linksets are a special kind of data asset. The aim of Loc-I Linksets is to provide a set of relationships between spatial datasets in a consistent way with clear provenance and governance. Linksets encode the relationships 

 a consistent way to access, analyse and use location data to support reliable and repeatable processes through automation and application of standards. Streamline data access and analysis provides faster and more accurate way to support a range of policy questions.
Linking data together is a good way to extract inforamtiion from different sources.


## Hybrid Spatial Knowledge Graph 

The Loc-I project is exploring tools and infrastructure for enabling improved analysis and decision making capability that integrates data across multiple geographies. Loc-I is exploring the use of semantics of the geographies in a consistent manner using ontologies, including their topology, semantic hierarchies and other relationships. These semantics are deployed as Linked Data on the web, so that each geography and its features are able to be identified precisely, unambiguously, with rich descriptions and semantics, via multiple views that are both human- and machine-readable, and available in multiple formats. 

The Loc-I project is providing a reference spatial knowledge graph, called the Loc-I cache, that aggregates and indexes all relevant Linked Data resources. This enables a Hybrid Spatial Knowledge Graph (refer to the figure below) for querying for Loc-I resources through a graph query engine (SPARQL), and REST APIs for full-text search and spatial searches. 

In particular, these provide users the ability to:
* Understand a location resource, alternate identifiers, and its semantic relationships
* Lookup spatial identifiers by text label or location (e.g. lat-lon coordinate)
* Query geometric topological relationships of a given location, e.g. show me all locations in a geography (or multiple geographies) that are contained within a given location. 

![Loc-I Cache Architecture](images/loci-architecture-oct19.png "Loc-I Cache Architecture")
