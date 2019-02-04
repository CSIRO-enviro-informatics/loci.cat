import harvester.config as config
from os import path, _Environ
from rdflib import Graph, Namespace, RDF
import owlrl
import requests
import pickle
import os.path


def harvest_defs():
    print('Harvesting Defs')
    print('---------------')
    g = Graph()
    # DCAT (rev)
    g1 = Graph()
    g1.load(os.path.join(config.APP_DIR, 'dcat.ttl'), format='turtle')
    print('From DCAT (rev) local file got {} triples'.format(len(g1)))
    g = g + g1

    for d in config.DEFS:
        print('Harvesting {}'.format(d))
        g1 = Graph()
        r = requests.get(d, headers={'Accept': 'text/turtle'})
        g1.parse(data=r.content.decode('utf-8'), format='turtle')
        print('From {} got {} triples'.format(d, len(g1)))
        g = g + g1

    # Geofabric harvest
    g1 = Graph()
    g1.load(os.path.join(config.APP_DIR, 'hy_features_entailed.ttl'), format='turtle')
    print('From Geofabric local file got {} triples'.format(len(g1)))
    g = g + g1

    # expand the graph
    print('Graph size {}'.format(len(g)))
    owlrl.DeductiveClosure(owlrl.OWLRL_Semantics).expand(g)
    print('Expanded to {}'.format(len(g)))

    # pickle the graph for page loads until next refresh
    pickle.dump(g, open(os.path.join(config.APP_DIR, 'defs.p'), 'wb'))

    print('Defs graph stored')

    return g


def harvest_datasets():
    print('Harvesting Datasets')
    print('---------------')
    # for each dataset in the config file, pull down its DCAT description
    g = Graph()

    if config.DEF_MIXIN:
        r = requests.get(config.DEF_MIXIN, headers={'Accept': 'text/turtle'})
        g.parse(data=r.content.decode('utf-8'), format='turtle')

    for d in config.DATASETS:
        print('Harvesting {}'.format(d))
        r = requests.get(d, params={'_view': 'void', '_format': 'text/turtle'})
        g.parse(data=r.content.decode('utf-8'), format='turtle')
        print('From {} got {} triples'.format(d, len(g)))

    # expand the graph
    owlrl.DeductiveClosure(owlrl.OWLRL_Semantics).expand(g)
    print('Expanded to {}'.format(len(g)))

    # pickle the graph for page loads until next refresh
    pickle.dump(g, open(os.path.join(config.APP_DIR, 'datasets.p'), 'wb'))

    print('Datasets graph stored')

    return g


def harvest_linksets():
    print('Harvesting Linksets')
    print('---------------')
    g = Graph()

    if config.DEF_MIXIN:
        r = requests.get(config.DEF_MIXIN, headers={'Accept': 'text/turtle'})
        g.parse(data=r.content.decode('utf-8'), format='turtle')

    for l in config.LINKSETS:
        print('Harvesting {}'.format(l))
        r = requests.get(l, headers={'Accept': 'text/turtle'})
        g.parse(data=r.content.decode('utf-8'), format='turtle')
        print('From {} got {} triples'.format(l, len(g)))

    # expand the graph
    owlrl.DeductiveClosure(owlrl.OWLRL_Semantics).expand(g)
    print('Expanded to {}'.format(len(g)))

    # pickle the graph for page loads until next refresh
    pickle.dump(g, open(os.path.join(config.APP_DIR, 'linksets.p'), 'wb'))
    print('Linksets graph stored')
    return g


def harvest_tools():
    # TODO:
    print('Harvesting Tools')
    print('---------------')
    g = Graph()

    if config.DEF_MIXIN:
        r = requests.get(config.DEF_MIXIN, headers={'Accept': 'text/turtle'})
        g.parse(data=r.content.decode('utf-8'), format='turtle')

    for t in config.TOOLS:
        print('Harvesting {}'.format(t))
        r = requests.get(t, headers={'Accept': 'text/turtle'})
        g.parse(data=r.content.decode('utf-8'), format='turtle')
        print('From {} got {} triples'.format(t, len(g)))

    # expand the graph
    owlrl.DeductiveClosure(owlrl.OWLRL_Semantics).expand(g)
    print('Expanded to {}'.format(len(g)))

    # pickle the graph for page loads until next refresh
    pickle.dump(g, open(os.path.join(config.APP_DIR, 'linksets.p'), 'wb'))
    print('Linksets graph stored')
    return g


def harvest():
    harvest_defs()
    harvest_datasets()
    harvest_linksets()


def load_graph(graph_file):
    # just return None if there's no file
    try:
        g = pickle.load(open(path.join(config.APP_DIR, graph_file), 'rb'))
        return g
    except IOError:
        return None


def get_graphs():
    # load an owlrl-expanded graph

    g = Graph()
    o = load_graph('defs.p')
    if not o:
        o = harvest_defs()
    g += o

    d = load_graph('datasets.p')
    if not d:
        d = harvest_datasets()
    g += d

    l = load_graph('linksets.p')
    if not l:
        l = harvest_linksets()
    g += l

    # make new inferences with the combined graph
    print('Currently all graphs combined have {} triples'.format(len(g)))
    owlrl.DeductiveClosure(owlrl.OWLRL_Semantics).expand(g)
    print('Expanded to {}'.format(len(g)))

    return g


if __name__ == '__main__':
    # harvest_defs()

    g = get_graphs()

    # get all datasets
    DCAT = Namespace('http://www.w3.org/ns/dcat#')
    for s in g.subjects(RDF.type, DCAT.DataDistributionService):
        print(s)
