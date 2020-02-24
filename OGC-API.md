The recently released [OGC API - Features - Part 1: Core](http://www.opengis.net/doc/IS/ogcapi-features-1/1.0) specifies a set of URI patterns for accessing features.

## Terminology
* feature = individual item
* collection = dataset

## Schemas
Response structure is defined in a [set of YAML patterns](http://schemas.opengis.net/ogcapi/features/part1/1.0/openapi/schemas/)

Note that the response must be provided in HTML and JSON, other formats optional. 

## URI patterns
 Resource + spec-link | relative URI pattern | response + example
 --- | --- | --- 
[Service](http://docs.opengeospatial.org/is/17-069r3/17-069r3.html#_api_landing_page) | `/` | [Landing page](https://geo.weather.gc.ca/geomet/features/)
[API description](http://docs.opengeospatial.org/is/17-069r3/17-069r3.html#_api_definition_2) | `/api` | [Swagger with API details](https://geo.weather.gc.ca/geomet/features/api)
[Conformance](http://docs.opengeospatial.org/is/17-069r3/17-069r3.html#_declaration_of_conformance_classes) | `/conformance` | [List of conformance classes implemented by this service](https://geo.weather.gc.ca/geomet/features/conformance)
[Collections](http://docs.opengeospatial.org/is/17-069r3/17-069r3.html#_collections_) | `/collections` | [List of collections available from this service](https://geo.weather.gc.ca/geomet/features/collections)
[Specific collection](http://docs.opengeospatial.org/is/17-069r3/17-069r3.html#_collection_) | `/collections/{collectionId}` | [Description of a collection (but not including the members)](https://geo.weather.gc.ca/geomet/features/collections/climate-stations)
[Features](http://docs.opengeospatial.org/is/17-069r3/17-069r3.html#_items_) | `/collections/{collectionId}/items` | [List of members of a collection](https://geo.weather.gc.ca/geomet/features/collections/climate-stations/items)
[Specific feature](http://docs.opengeospatial.org/is/17-069r3/17-069r3.html#_feature_) | `/collections/{collectionId}/items/{featureId}` | [Description of a feature](https://geo.weather.gc.ca/geomet/features/collections/climate-stations/items/1128958)
