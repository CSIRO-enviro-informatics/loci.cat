# Linksets and linking statements
## Definitions

Classes and properties for Loc-I linksets are defined in the [Loc-I Ontology](http://www.linked.data.gov.au/def/loci). 
The base uri for this ontology is `http://www.linked.data.gov.au/def/loci#`. The token for `{scope}` is `loci`. 

The separator to the `{defID}` is `#`. 

The value for `{defID}` is the class- or property-name. 

## Data 

A `loci:Linkset` is composed of a set of `loci:LinkingStatement` individuals. 
The membership predicate is `loci:isMemberOf`. 

Linksets can be assembled for various reasons, including, but not limited to:

* a full set of links between members of a single dataset
* a full set of links between members of two specified datasets

Each `loci:LinkingStatement` describes a relationship between a two `features` - i.e. geospatial entities. 
There are many potential linking predicates, but for the purposes of Loc-I the most important are the spatio-topological relationships:

* `geo:sfContains` and its inverse `geo:sfWithin`
* `geo:sfOverlaps`
* `geo:sfEquals`

The relationship is instantiated as a reified statement, which allows additional information to be associated with the link. This can include provenance information, or might measure the amount of overlap (using `geox:hasArea` as a property of the linking statement). 

## Example
```
<http://linked.data.gov.au/dataset/mb16cc/statement/to98614>
  rdf:type loci:LinkingStatement ;
  rdf:type rdf:Statement ;
  geox:hasAreaM2 567000.0 ;
  loci:hadGenerationMethod "by hand" ;
  loci:isMemberOf <http://linked.data.gov.au/dataset/mb16cc> ;
  dcterms:created "2019-12-20"^^xsd:date ;
  dcterms:creator <https://orcid.org/0000-0002-3884-3420> ;
  rdf:object <http://linked.data.gov.au/dataset/geofabric/contractedcatchment/12101547> ;
  rdf:predicate geo:sfOverlaps ;
  rdf:subject <http://linked.data.gov.au/dataset/asgs2016/meshblock/20663930000> ;
.

<http://linked.data.gov.au/dataset/mb16cc>
  rdf:type loci:Linkset ;
  loci:hadGenerationMethod "by hand" ;
  dcterms:created "2019-12-20"^^xsd:date ;
  dcterms:creator <https://orcid.org/0000-0002-3884-3420> ;
.

```

## SPARQL used in remediating [sample linkset](https://github.com/CSIRO-enviro-informatics/loci-testdata/blob/master/loci-ld-dataset/loci-linkset-instances-1.ttl) 

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
