---
permalink: /URI-conventions.html
---

# Loc-I URI conventions
Web identifiers (URIs) for Loc-I resources must conform to [AGLDWG URI Conventions](#summary-of-agldwg-uri-guidelines). 

## Data 

### Datasets
```
http://linked.data.gov.au/dataset/{datasetID}
```

### Data items
```
http://linked.data.gov.au/dataset/{datasetID}[/{collectionID}]{separator}{individualID}
```

### Examples  
#### ASGS 
##### ABS Structures

URI | explanation 
--- | --- 
`http://linked.data.gov.au/dataset/asgs2016/meshblock/20675580000` | MB 20675580000 from 2016 ASGS dataset
`http://linked.data.gov.au/dataset/asgs2011/statisticalarealevel1/20703116718` | SA1 20703116718 from 2011 ASGS dataset
`http://linked.data.gov.au/dataset/asgs2016/statisticalarealevel1/20703116718` | SA1 20703116718 from 2016 ASGS dataset

The 'ABS Structures' within ASGS are updated for each census - 2011, 2016, 2021 etc. 
Each release is considered to be a new dataset - asgs2011, asgs2016, etc. 

##### Non-ABS Structures

URI | explanation 
--- | --- 
`http://linked.data.gov.au/dataset/asgs/commonwealthelectoraldivision/208/2011-07` | CED 208 (Chisholm) from 2011 (July) release of the ASGS CEDs
`http://linked.data.gov.au/dataset/asgs/commonwealthelectoraldivision/208/2013-07` | CED 208 (Chisholm) from 2013 (July) release of the ASGS CEDs
`http://linked.data.gov.au/dataset/asgs/commonwealthelectoraldivision/208/2016-07` | CED 208 (Chisholm) from 2016 (July) release of the ASGS CEDs
`http://linked.data.gov.au/dataset/asgs/commonwealthelectoraldivision/208/2017-07` | CED 208 (Chisholm) from 2017 (July) release of the ASGS CEDs
`http://linked.data.gov.au/dataset/asgs/commonwealthelectoraldivision/207/2018-07` | CED 207 (Chisholm) from 2018 (July) release of the ASGS CEDs
`http://linked.data.gov.au/dataset/asgs/commonwealthelectoraldivision/207` | CED 207 (Chisholm) from current (most recent) release of the ASGS CEDs
`http://linked.data.gov.au/dataset/asgs/commonwealthelectoraldivision/208/2018-07` | CED 208 (Cooper) from 2018 (July) release of the ASGS CEDs
`http://linked.data.gov.au/dataset/asgs/commonwealthelectoraldivision/208` | CED 208 (Cooper) from current (most recent) release of the ASGS CEDs

'Non-ABS Structures' are revised more frequently. 
There is a new release of Non-ABS Structures in July of each year, only for those feature-types (entity-types) that have changed. 
For example, Electoral Districts (EDs) (Commonwealth and State) are in an annual release if there have been adjustments to boundaries (which is not every year). 
However, each new release mentions all individuals of the entity-type, including those that have not changed. 

'Non-ABS Structures' are composed from 'ABS Structures' (primarily Meshblocks or SA1s) taken from the most recent release. 
Thus, Non-ABS Structures described between 2011-2015 are composed from asgs2011 ABS Structures, while Non-ABS Structures described between 2016-2020 are composed from asgs2016 ABS Structures

Because of the irregular update schedule, the Non-ABS stuctures are considered to be from a single dataset 'asgs', with the release date appended to the URI at an entity-level (rather than dataset-level which is used for ABS Structures). 

Dataset | {datasetID} | {collectionID} | separator | 
--- | --- | --- | --- 
ASGS | `asgs2016` | `meshblock` <br/>`statisticalarealevel1` <br/>`statisticalarealevel2` <br/>`statisticalarealevel3` <br/>`statisticalarealevel4` <br/>`stateorterritory` <br/>`australia` | `/`
G-NAF | `gnaf` | `address` <br/>`streetLocality` <br/>`locality` | `/`
GeoFabric | `geofabric` | `contractedcatchment` <br/>`drainagedivision` <br/>`riverregion` | `/`
Meshblock-ControlledCatchment links | `mb16cc` | `statement` | `/`


Definitions, vocabularies, ontologies, schemas
```
http://linked.data.gov.au/def/{scope}(/#){defID}
```

## Data

## Classes and Feature-types

Ontology | {scope} | separator | {defID}
--- | --- | --- | --- 
[ASGS](http://linked.data.gov.au/def/asgs) |  `asgs` | `#` | `MeshBlock`<br/>`StatisticalAreaLevel1` <br/>`StatisticalAreaLevel2` <br/>`StatisticalAreaLevel3` <br/>`StatisticalAreaLevel4` <br/>`StateOrTerritory` <br/>`Country`
[G-NAF](http://linked.data.gov.au/def/gnaf) |  `gnaf` | `#` | `Address` <br/>`StreetLocality` <br/>`Locality`
[GeoFabric](http://linked.data.gov.au/def/geofabric) |  `geofabric` | `#` | `ContractedCatchment` <br/>`DrainageDivision` <br/>`RiverRegion`
[Loc-I](http://linked.data.gov.au/def/loci) | `loci` | `#` | `DataPublisher` <br/>`Dataset` <br/>`DatasetLinkingStatement` <br/>`Feature` <br/>`Linkset`

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

Note that [version 2.1 of the AGLDWG URI Guideline](https://github.com/AGLDWG/guidelines/blob/master/PID-URI-Guidelines-v2.1.md) specifies the use of `https:` throughout. We are considering how to migrate the current systems to HTTPS. 

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
The recently released [OGC API - Features - Part 1: Core](http://www.opengis.net/doc/IS/ogcapi-features-1/1.0) specifies a set of URI patterns for accessing features. 
This is similar to the Loc-I/AGLDWG, but with different keywords and a slightly deeper structure. 

### Terminology
* feature = individual item
* collection = dataset

### Schemas
Response structure is defined in a [set of YAML patterns](http://schemas.opengis.net/ogcapi/features/part1/1.0/openapi/schemas/)

Note that the response must be provided in HTML and JSON, other formats optional. 

### URI patterns for Data

Resource + spec-link | relative URI pattern | response + example
--- | --- | --- 
[Service](http://docs.opengeospatial.org/is/17-069r3/17-069r3.html#_api_landing_page) | `/` | [Landing page](https://geo.weather.gc.ca/geomet/features/)
[API description](http://docs.opengeospatial.org/is/17-069r3/17-069r3.html#_api_definition_2) | `/api` | [Swagger with API details](https://geo.weather.gc.ca/geomet/features/api)
[Conformance](http://docs.opengeospatial.org/is/17-069r3/17-069r3.html#_declaration_of_conformance_classes) | `/conformance` | [List of conformance classes implemented by this service](https://geo.weather.gc.ca/geomet/features/conformance)
[Collections](http://docs.opengeospatial.org/is/17-069r3/17-069r3.html#_collections_) | `/collections` | [List of collections available from this service](https://geo.weather.gc.ca/geomet/features/collections)
[Specific collection](http://docs.opengeospatial.org/is/17-069r3/17-069r3.html#_collection_) | `/collections/{collectionId}` | [Description of a collection (but not including the members)](https://geo.weather.gc.ca/geomet/features/collections/climate-stations)
[Features](http://docs.opengeospatial.org/is/17-069r3/17-069r3.html#_items_) | `/collections/{collectionId}/items` | [List of members of a collection](https://geo.weather.gc.ca/geomet/features/collections/climate-stations/items)
[Specific feature](http://docs.opengeospatial.org/is/17-069r3/17-069r3.html#_feature_) | `/collections/{collectionId}/items/{featureId}` | [Description of a feature](https://geo.weather.gc.ca/geomet/features/collections/climate-stations/items/1128958)
