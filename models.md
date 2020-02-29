---
permalink: /models.html
---

# Models


## Background Models

There are a series of well-known OWL models that are used for concepts relevant to Loc-I. These include both the technical, structural, models of how to represent data elements generally and also the conceptual models of particular domains' concepts. The following models are used by Loc-I:

Table M1: Background models used in LongSpine

|Ontology	| Description	| Role in Loc-I |
|-----------|---------------|---------------|
|Resource Description Framework (RDF)	|The fundamental data model used for Semantic Web and Linked Data applications. It models objects and relations.	|Required for any RDF-based system|
|RDF Schema (RDFS)	|A schema on top of RDF for modelling types of things and specailisations	|Required for most RDF-based systems|
|Web Ontology Language (OWL)	|An extension to RDFS that uses set theory to describe detailed relationships between things	|Allows for nuanced classes of object, like different Organisations|
|Dublin Core Terms	|A vocabulary of basic annotation properties for things like title, description, source, created date etc.	|Allows for basic annotations on many LongSpine objects|
|schema.org	|A large, general-purpose, OWL model of common classes of objects and relations	|Used for basic object types like Person and properties like birthDate|
|Time Ontology in OWL (TIME)	|An OWL ontology of temporal concepts, for describing the temporal properties of resources	|Used for all LongSpine real-world temporality|
|The Dataset Catalogue Vocabulary (DCAT)	|An OWL ontology designed to facilitate interoperability between data catalogs published on the Web	|Used to describe LongSpine Datasets at the whole-of-dataset level|
|Vocabulary of Interlinked Datasets (VoID)	|An OWL ontology for expressing metadata about RDF datasets, particularly relations between them	|Used primarily for its definition of a Linkset|
|The Organization Ontology (ORG)	|An OWL core ontology for organizational structures	|Used as the basis for LongSpine organisations modelling|
|Simple Knowledge Organization System (SKOS)	|An OWL model for expressing the basic structure and content of concept schemes such as thesauri, classification schemes, subject heading lists, taxonomies, folksonomies	| Used to structure the vocabularies and thesauri of government functions |


All of these models are loaded into the [Loc-I reference cache](ref-cache.md), i.e. individual Datasets and Linksets, as a series of Named Graphs which means, they can be selected for use, or excluded, within individual queries against the [Loc-I reference cache](ref-cache.md).
