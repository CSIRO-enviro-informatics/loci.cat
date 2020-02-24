The ontologies for the initial Loc-I datasets were developed by different teams spread over an extended period. 
As a consequence they follow a variety of design patterns and are highly uneven in their level of detail and the way in which they re-use standard elements from existing RDF vocabularies. Some ontology designers are comfortable borrowing a lot from existing RDF vocabularies, while others prefer to define most things fresh and then map to other RDF vocabularies later, or never. This is partly just a personal preference, but also reflects the level of trust for RDF vocabularies not under local control. 

This is particularly significant in the context of developing [rules for Loc-I dataset](Rules-for-Loc-I-datasets) where we want to include many datasets from multiple sources. Given the diversity of data sources, the use of common ontology elements make it easier to implement common query patterns. For this reason we recommend use of elements from a core set of existing RDF vocabularies _as much as possible_ including:

- [RDF](http://www.w3.org/1999/02/22-rdf-syntax-ns) and [RDFS](http://www.w3.org/2000/01/rdf-schema)
- [Dublin Core terms](http://purl.org/dc/terms/)
- [OWL2](http://www.w3.org/2002/07/owl)
- [GeoSPARQL](http://www.opengis.net/ont/geosparql) and [Simple Features](http://www.opengis.net/ont/sf)
- [AGLDWG Datatypes](http://linked.data.gov.au/def/datatype/) 

and then
- [loc-i ontology](http://linked.data.gov.au/def/loci)
- [GeoSPARQL extensions](http://linked.data.gov.au/def/geox#)

It is proposed to revise the original ontologies to use elements from these vocabularies in preference to elements in local/new namespaces wherever possible, and in particular so that all Loc-I datasets can follow a common core model as described in https://github.com/CSIRO-enviro-informatics/loci.cat/wiki/Rules-for-Loc-I-datasets . We have started this process by refactoring the [ASGS Ontology](https://github.com/AGLDWG/asgs-ont) and making more minor adjustments to the [G-NAF Ontology](https://github.com/AGLDWG/gnaf-ont) and [Geofabric Ontology](http://linked.data.gov.au/def/geofabric#) or usage patterns. 

Conversion of the original data from the cache to the preferred pattern is illustrated by the examples below: 
* [original form](https://raw.githubusercontent.com/CSIRO-enviro-informatics/loci-testdata/simplify-1/loci-ld-dataset/loci-instances-0.ttl)
* [simplified/harmonized form](https://raw.githubusercontent.com/CSIRO-enviro-informatics/loci-testdata/simplify-1/loci-ld-dataset/loci-instances-1.ttl)

## Examples
Details by product: 

* [ASGS](https://github.com/CSIRO-enviro-informatics/asgs-dataset/issues/13)
* [G-NAF](https://github.com/CSIRO-enviro-informatics/gnaf-dataset/issues/11)
* [Geofabric](https://github.com/CSIRO-enviro-informatics/geofabric-dataset/issues/26)
