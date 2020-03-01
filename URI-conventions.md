---
permalink: /URI-conventions.html
---

# Loc-I URI conventions
Web identifiers (URIs) for Loc-I resources must conform to [AGLDWG URI Conventions](#summary-of-agldwg-uri-guidelines). 

Definitions
```
http://linked.data.gov.au/def/{scope}(/#){defID}
```

Datasets
```
http://linked.data.gov.au/dataset/{datasetID}
```

Data items
```
http://linked.data.gov.au/dataset/{datasetID}[/{collectionID}](/#){individualID}
```

## Classes and Feature-types

Ontology | {scope} | separator | {defID}
--- | --- | --- | --- 
[ASGS](http://linked.data.gov.au/def/asgs) |  `asgs` | `#` | `MeshBlock`<br/>`StatisticalAreaLevel1` <br/>`StatisticalAreaLevel2` <br/>`StatisticalAreaLevel3` <br/>`StatisticalAreaLevel4` <br/>`StateOrTerritory` <br/>`Country`
[G-NAF](http://linked.data.gov.au/def/gnaf) |  `gnaf` | `#` | `Address` <br/>`StreetLocality` <br/>`Locality`
[GeoFabric](http://linked.data.gov.au/def/geofabric) |  `geofabric` | `#` | `ContractedCatchment` <br/>`DrainageDivision` <br/>`RiverRegion`
[Loc-I](http://linked.data.gov.au/def/loci) | `loci` | `#` | `DataPublisher` <br/>`Dataset` <br/>`DatasetLinkingStatement` <br/>`Feature` <br/>`Linkset`

## Data
Examples of URI patterns for specific datasets: 

Dataset | {datasetID} | {collectionID} | separator | 
--- | --- | --- | --- 
ASGS | `asgs2016` | `meshblock` <br/>`statisticalarealevel1` <br/>`statisticalarealevel2` <br/>`statisticalarealevel3` <br/>`statisticalarealevel4` <br/>`stateorterritory` <br/>`australia` | `/`
G-NAF | `gnaf` | `address` <br/>`streetLocality` <br/>`locality` | `/`
GeoFabric | `geofabric` | `contractedcatchment` <br/>`drainagedivision` <br/>`riverregion` | `/`
Meshblock-ControlledCatchment links | `mb16cc` | `statement` | `/`

## Examples
### ASGS Summary and examples

Example individual | Class | Collection 
--- | --- | --- 
http://linked.data.gov.au/dataset/asgs2016/meshblock/50259230000 |  http://linked.data.gov.au/def/asgs#MeshBlock | http://linked.data.gov.au/dataset/asgs2016/meshblock 
http://linked.data.gov.au/dataset/asgs2016/statisticalarealevel1/50102100504 | http://linked.data.gov.au/def/asgs#StatisticalAreaLevel1 | http://linked.data.gov.au/dataset/asgs2016/statisticalarealevel1  
http://linked.data.gov.au/dataset/asgs2016/statisticalarealevel2/308031218 | http://linked.data.gov.au/def/asgs#StatisticalAreaLevel2 | http://linked.data.gov.au/dataset/asgs2016/statisticalarealevel2 
http://linked.data.gov.au/dataset/asgs2016/statisticalarealevel3/80106 | http://linked.data.gov.au/def/asgs#StatisticalAreaLevel3 | http://linked.data.gov.au/dataset/asgs2016/statisticalarealevel3 
http://linked.data.gov.au/dataset/asgs2016/statisticalarealevel4/207 | http://linked.data.gov.au/def/asgs#StatisticalAreaLevel4 | http://linked.data.gov.au/dataset/asgs2016/statisticalarealevel4 
http://linked.data.gov.au/dataset/asgs2016/stateorterritory/2 | http://linked.data.gov.au/def/asgs#StateOrTerritory | http://linked.data.gov.au/dataset/asgs2016/stateorterritory 
http://linked.data.gov.au/dataset/asgs2016/australia/036 | http://linked.data.gov.au/def/asgs#Country | http://linked.data.gov.au/dataset/asgs2016/australia  
http://linked.data.gov.au/dataset/mb16cc/statement/to98614 | http://linked.data.gov.au/def/loci#LinkingStatement | http://linked.data.gov.au/dataset/mb16cc

Note: in the 2nd-last line, for the SAL6 'Australia' the _individual_ and _collection_ URIs use /australia/ rather than the _class name_ i.e. /country/ . This follows a [pattern](https://www.abs.gov.au/websitedbs/D3310114.nsf/4a256353001af3ed4b2562bb00121564/c453c497aadde71cca2576d300026a38/Body/0.D64!OpenElement&FieldElemFormat=jpg) inherited from the [ASGS reference](https://www.abs.gov.au/websitedbs/D3310114.nsf/home/Australian+Statistical+Geography+Standard+(ASGS)). 

### G-NAF Summary and examples

Example individual | Class | Collection |
--- | --- | --- |
http://linked.data.gov.au/dataset/gnaf/address/GAACT714845933 | http://linked.data.gov.au/def/gnaf#Address| http://linked.data.gov.au/dataset/gnaf/address 
http://linked.data.gov.au/dataset/gnaf/streetLocality/NSW2856338 | http://linked.data.gov.au/def/gnaf#StreetLocality | http://linked.data.gov.au/dataset/gnaf/streetLocality 
http://linked.data.gov.au/dataset/gnaf/locality/198023 | http://linked.data.gov.au/def/asgs#Locality| http://linked.data.gov.au/dataset/gnaf/locality 

### Geofabric Summary and examples

Example individual | Class | Collection |
--- | --- | --- |
http://linked.data.gov.au/dataset/geofabric/contractedcatchment/9550009 | http://linked.data.gov.au/def/geofabric#ContractedCatchment | http://linked.data.gov.au/dataset/geofabric/contractedcatchment 
http://linked.data.gov.au/dataset/geofabric/drainagedivision/9400214 | http://linked.data.gov.au/def/geofabric#DrainageDivision | http://linked.data.gov.au/dataset/geofabric/drainagedivision 
http://linked.data.gov.au/dataset/geofabric/riverregion/9400228 | http://linked.data.gov.au/def/geofabric#RiverRegion | http://linked.data.gov.au/dataset/geofabric/riverregion |

## Summary of AGLDWG URI guidelines

Names in the linked.data.gov.au domain must follow the [AGLDWG URI Guideline](https://github.com/AGLDWG/guidelines/blob/master/PID-URI-Guidelines-v2.0.md).

### Definitions

The [URI pattern for a _definition_](https://github.com/AGLDWG/guidelines/blob/master/PID-URI-Guidelines-v2.0.md#Definitional) (i.e. a class, concept, controlled-vocabulary or vocabulary item) is:
```
http://linked.data.gov.au/def/{scope}(/#){defID}
```
where `{scope}` identifies the vocabaulary or ontology, and `{defID}` the class, concept, property-type, vocabaulary item, etc.  

### Data
#### Dataset
The URI pattern for a [dataset as a whole](https://github.com/AGLDWG/guidelines/blob/master/PID-URI-Guidelines-v2.0.md#61-dataset-pid-uri-pattern) is:
```
http://linked.data.gov.au/dataset/{datasetID}
```

#### (Optional) Collection
The URI pattern for a [collection within a dataset](https://github.com/AGLDWG/guidelines/blob/master/PID-URI-Guidelines-v2.0.md#61-dataset-pid-uri-pattern) is:
```
http://linked.data.gov.au/dataset/{datasetID}/{collectionID}
```
In Loc-I cache all individuals from a class are allocated to a _collection_ for that class with the URI `http://linked.data.gov.au/dataset/{datasetID}/{collectionID}`. 
This is used for paging in [pyLDAPI](https://github.com/RDFLib/pyLDAPI). 

#### Item
Individual [items in a dataset](https://github.com/AGLDWG/guidelines/blob/master/PID-URI-Guidelines-v2.0.md#61-dataset-pid-uri-pattern) (such as geographic features or entities) are denoted by a URI which is an extension of the dataset      URI or collection URI, following the pattern:
```
http://linked.data.gov.au/dataset/{datasetID}[/{collectionID}](/#){individualID}
```

**N.B.** If the optional `/{collectionID}` path element is included, and corresponds with a class name, then the classification of each item must be known when the identifier is assigned, and can compromise some lifecycle transitions (e.g. re-classification of an individual feature).
Furthermore, since some individuals are members of more than one class, a single `{collectionID}` can make the identifier ambiguous or non-unique.

## OGC API
The recently released [OGC API for Features](http://www.opengis.net/doc/IS/ogcapi-features-1/1.0) has similar URI patterns, but with different keywords and a slightly deeper structure - see summary at [OGC-API](OGC-API.md)

