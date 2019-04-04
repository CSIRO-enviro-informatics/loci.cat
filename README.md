# LD Cat
A simple Lined Data catalogue tool that contains both a harvester and a web display framework.

This web-based catalogue tool harvests the metadata for and lists Datasets, Linksets, definitional items and anything else available as [Linked Data](https://www.w3.org/standards/semanticweb/data) that is "pointed at" (given the identifying URI for). It only contains information extracted from the items via their URIs and doesn't store anything locally except for caching purposes.

## Instances
This tool is used for the following catalogues:

* The LocI Project - [http://loci.cat](http://loci.cat)
* The Longitudinal Spine of Government Functions - [http://longspine.cat](http://longspine.cat) - *not fully working yet*

The items that constitute the catalogues in the instances above are different and specified per-installation in a config file. The branding they use for their web pages is maintained in branches of this repository.

## Catalogue Implementation
### Harvester
The harvesting component of this catalogue uses a series of very simple [Python programming language](https://www.python.org/) scripts to collect Datasets, Linksets, ontologies and tools metadata from their points of truth. It is able to do this very simple since all of those items present basic [DCAT (revised)](https://www.w3.org/TR/vocab-dcat-2/) metadata at easy-to-find web addresses and using the [RDF Turtle](https://www.w3.org/TR/turtle/) data format. 

For example, the [GNAF Dataset](http://linked.data.gov.au/dataset/gnaf) is online at the persistent URI of [http://linked.data.gov.au/def/gnaf](http://linked.data.gov.au/def/gnaf) and its DCAT (rev.) metadata is accessible by adding the Query Strong Arguments *_view* and *_format* to that URI: <a href="http://linked.data.gov.au/def/gnaf?_view=dcat&format=text/turtle">http://linked.data.gov.au/def/gnaf<strong>?_view=dcat&format=text/turtle</strong></a>.

The harvester uses Python's [Requests](http://docs.python-requests.org/en/master/) module to retrieve all item's DCAT (rev.) RDF and then it stores it in a Python [rdflib](https://rdflib.readthedocs.io/en/latest/) data graph. It then applies some rule-based reasoning to that graph using the [OWL-RL](https://owl-rl.readthedocs.io/en/latest/) Web Ontology Language ([OWL](https://www.w3.org/2001/sw/wiki/OWL)) rule engine to create generic generic properties from the items' specialised ones.

The harvester validates each item's RDF data by using the [pySHACL](https://pypi.org/project/pyshacl/), [SHACL](https://www.w3.org/TR/shacl/) to comparing the information it retries to 'shapes' templates of expected information.  

When done, the harvester stores the items' validated information in a single on-disk graph that it can use to service catalogue requests for information (see next section).

### Web catalogue
This catalogue uses a very simple Python [Flask](http://flask.pocoo.org/) HTTP framework instance to service requests for the information it contains. In general, it receives a request (someone or some tool clicking on a web link at `http://{IMPLEMENTATION_URI}/...`) and translates that into a Python function call that accesses the information the catalogue contains. Since the catalogue stores all of its information within an RDF data graph, it uses either [rdflib loop queries](https://rdflib.readthedocs.io/en/stable/intro_to_graphs.html) or [SPARQL](https://www.w3.org/TR/sparql11-query/) queries facilitated by rdflib.

#### Sitemap
The full sitemap of the LocI project's implementation of this catalogue is:

* [Home](http://loci.cat) - catalogue home and the *Register of Registers*
    * [Dataset Register](http://loci.cat/dataset/)
    * [Linkset Register](http://loci.cat/linkset/)
    * [Ontology Register](http://loci.cat/def/)
    * [Tool Register](http://loci.cat/tool/)
* [About Page](http://loci.cat/about) - *this page*


## Dependencies
See the [requirements.txt](https://github.com/CSIRO-enviro-informatics/ld.cat/blob/master/requirements.txt) standard Python dependency listing file.


## License
This code is licensed using the GPL v3 licence. See the [LICENSE file](LICENSE) for the deed.


## Contacts
*Author*:  
**Nicholas Car**  
*Senior Experimental Scientist*  
CSIRO Land & Water, Environmental Informatics Group  
<nicholas.car@csiro.au>  


*Co-maintainer*:  
**Edmond Chuc**  
*Junior Developer*  
CSIRO Land & Water, Environmental Informatics Group  
<edmond.chuc@csiro.au>  
 
