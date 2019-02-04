from os import path


APP_DIR = path.dirname(__file__)

DEF_MIXIN = ''

DEFS = [
    'http://linked.data.gov.au/def/loci',
    'http://linked.data.gov.au/def/asgs',
    # Geofabric - harvested from local file
    'http://linked.data.gov.au/def/gnaf'
]

DATASETS = [
    'http://linked.data.gov.au/dataset/asgs2016',
    # 'http://linked.data.gov.au/dataset/geofabric',
    'http://linked.data.gov.au/dataset/gnaf-2016-05',
]

LINKSETS = [
    'https://raw.githubusercontent.com/CSIRO-enviro-informatics/addressescatchments-linkset/master/header.ttl'
]

TOOLS = []