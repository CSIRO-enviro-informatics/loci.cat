---
permalink: /link-statements.html
---

# Linksets and linking statements
## Motivation
Linksets can be assembled for various reasons, including, but not limited to:

* a set of links between members of a single dataset
* a set of links between members of two specified datasets

## Definitions

Classes and properties for Loc-I linking statements and linksets are defined formally as part of the [Loc-I Ontology](http://linked.data.gov.au/def/loci). 

A `loci:Linkset` is composed of a set of `loci:LinkingStatement` individuals. 
The membership predicate is `loci:isMemberOf`. 

Each `loci:LinkingStatement` describes a relationship between a two `features` - i.e. geospatial entities. 
There are many potential linking predicates, but for the purposes of Loc-I the most important are the spatio-topological relationships:

* `geo:sfContains` and its inverse `geo:sfWithin`
* `geo:sfOverlaps`
* `geo:sfEquals`

The link is instantiated as an `rdf:Statement` which 'reifies' the relationship, so that additional information can be associated with the link. 
This should include provenance information, and may include a measurement of the amount of overlap (using `geox:hasArea` as a property of the linking statement). 

## Example
The direct relationship 
```
<http://linked.data.gov.au/dataset/asgs2016/meshblock/20663930000> geo:sfOverlaps <http://linked.data.gov.au/dataset/geofabric/contractedcatchment/12101547> .
```
is reified as 
```
<http://linked.data.gov.au/dataset/mb16cc/statement/to98614>
  rdf:type loci:LinkingStatement ;
  rdf:type rdf:Statement ;
#
# the features involved in the link
#
  rdf:subject <http://linked.data.gov.au/dataset/asgs2016/meshblock/20663930000> ;
  rdf:predicate geo:sfOverlaps ;
  rdf:object <http://linked.data.gov.au/dataset/geofabric/contractedcatchment/12101547> ;
#
# the amount of overlap
#
  geox:hasAreaM2 567000.0 ;
#
# the provenance of the link
#
  dcterms:creator <https://orcid.org/0000-0002-3884-3420> ;
  dcterms:created "2019-12-20"^^xsd:date ;
  loci:hadGenerationMethod <linked.data.gov.au/def/plan/manual> ;
#
# part of a registered Linkset
#
  loci:isMemberOf <http://linked.data.gov.au/dataset/mb16cc> ;
.
```
where 

```
<http://linked.data.gov.au/dataset/mb16cc>
  rdf:type loci:Linkset ;
  dcterms:created "2019-12-20"^^xsd:date ;
  dcterms:creator <https://orcid.org/0000-0002-3884-3420> ;
.

<linked.data.gov.au/def/plan/manual>
  rdf:type prov:Plan ;
  dcterms:description "individual assignment through manual inspection" ; 
.
```
The latter item is an entry from a _set_ of standard link-generation methods. 
This is currently notional, but shoudl be regularized as part of ongoing Loc-I work. 

## Converting linking statements to links
To extract direct links from a set of reified linking-statements, a simple SPARQL CONSTRUCT query can be used:
```
CONSTRUCT {?s ?p ?o . }
WHERE {
	?t a rdf:Statement ;
		rdf:subject ?s ;
		rdf:predicate ?p ;
		rdf:object ?o .
}
```

## Building the initial linkset

The [sample linkset](https://github.com/CSIRO-enviro-informatics/loci-testdata/blob/master/loci-ld-dataset/loci-linkset-instances-1.ttl) was remediated using the following SPARQL

```
INSERT { ?l a loci:LinkingStatement , rdf:Statement . }
WHERE { ?l rdf:subject ?s . }

INSERT { ?l loci:isMemberOf ?ls . }
WHERE { ?l dcterms:isPartOf ?ls . }

DELETE { ?l dcterms:isPartOf ?ls . }
WHERE { ?l dcterms:isPartOf ?ls . }

INSERT { ?s rdf:predicate geo:sfOverlaps }
WHERE { 
	?s a loci:LinkingStatement ;
	rdf:predicate geox:transitiveSfOverlap .  
}

DELETE { ?s rdf:predicate geox:transitiveSfOverlap }
WHERE { 
	?s a loci:LinkingStatement ;
	rdf:predicate geox:transitiveSfOverlap .  
}
```
