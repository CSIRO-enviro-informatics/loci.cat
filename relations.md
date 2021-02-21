# Relations

A number of relationship predicates used to describe **relationships between spatial features** in Loc-I and in the context of individual Loc-I datasets, as follows: 

## Dublin Core

From [Dublin Core](https://dublincore.org/specifications/dublin-core/dcmi-terms/) the following relations describe either part-whole or versioning relationships between resources

Relation | definition 
--- | ---
`relation` | A related resource
`hasPart` | A related resource that is included either physically or logically in the described resource
`isPartOf` | A related resource in which the described resource is physically or logically included
`replaces` | A related resource that is supplanted, displaced, or superseded by the described resource
`isReplacedBy` | A related resource that supplants, displaces, or supersedes the described resource
`hasVersion` | A related resource that is a version, edition, or adaptation of the described resource
`isVersionOf` | A related resource of which the described resource is a version, edition, or adaptation

![DC Relations](images/dc-relations.png)

## GeoSPARQL

From [GeoSPARQL](https://www.ogc.org/standards/geosparql) the following geospatial-topological relationships are of interest

Relation | definition 
--- | ---
`sfContains` |  Exists if the subject SpatialObject spatially contains the object SpatialObject. DE-9IM: T\*\*\*\*\*FF\*
`sfEquals` | Exists if the subject SpatialObject spatially equals the object SpatialObject. DE-9IM: TFFFTFFFT
`sfOverlaps` | Exists if the subject SpatialObject spatially overlaps the object SpatialObject. DE-9IM: T\*T\*\*\*T\*\* 
`sfWithin` | Exists if the subject SpatialObject is spatially within the object SpatialObject. DE-9IM: T\*F\*\*F\*\*\*
`sfDisjoint` | Exists if the subject SpatialObject is spatially disjoint from the object SpatialObject. DE-9IM: FF\*FF\*\*\*\*

## ASGS

In [ASGS](http://linked.data.gov.au/def/asgs) the following implement the relationships defined between different ASGS structures  

Relation | definition 
--- | ---
`isAggregationOf` | The context resource is an aggregation of (composed of) one or more of the target resources 
`aggregatesTo` | The context resource aggregates to the target resource, in a logical, ownership, governance, jurisidictional or 'is-part-of' sense 

## Loc-I

In [Loc-I](http://linked.data.gov.au/def/loci) the following generalized relations are defined

Relation | definition 
--- | ---
`isEquivalentTo`\* | The target feature is intended to represent the same real-world entity as the context feature
`contains`\* | The context resource contains the target resource, in some geospatial, logical, ownership, governance, jurisidictional or compositional sense 
`isWithin`\* | The context resource is within or is part of the target resource, in some geospatial, logical, ownership, governance, jurisidictional or compositional sense
`isDisjointWith` |  The target resource does not touch or intersect with the context 
`sfRelation` | A geospatial-topological relationship

![Loc-I Relations](images/loci-relations.png)

## All relations hierarchy

The Loc-I relations allow us to join the GeoSPARQL and ASGS relations into a single sub-property hierarchy: 

![Loc-I Relations hierarchy](images/loci-relations-hierarchy.png)

This will support more generalized queries across datasets and linksets. 


# Identity and revisions

## ASGS 
More than one dataset (revision cycle) in ASGS
- ABS structures - 5-yearly
- non-ABS structures - annually

Do we treat URIs as a single dataset, with URI's being members of time-stamped datasets
Or do we make the URI's time-stamped and then record feature equivalence relationships explicitly 

## GNAF
Ontology needs a big refresh. 
Has time properties at entity level
(StreetLocality incorrected modelled as sub-class of Street)

