from os import path

#
# -- Harvest Settings --------------------------------------------------------------------------------------------------
#

#
# Harvest on server startup (before first request) if set to True. Useful to have it on False while in development.
#
HARVEST = True

APP_DIR = path.dirname(__file__)

#
# -- Register Settings -------------------------------------------------------------------------------------------------
#

#
# Mixin for primary ontology of the catalogue so that items know about specific properties.
#
DEF_MIXIN = 'http://linked.data.gov.au/def/loci'

#
# Definitional items register
#
DEFS = [
    'http://linked.data.gov.au/def/loci',
    'http://linked.data.gov.au/def/asgs',
    # Geofabric - harvested from local file
    'http://linked.data.gov.au/def/gnaf'
]

#
# Datasets register
#
DATASETS = [
    'http://linked.data.gov.au/dataset/asgs2016',
    'http://linked.data.gov.au/dataset/geofabric',
    'http://linked.data.gov.au/dataset/gnaf-2016-05',
    'http://linked.data.gov.au/dataset/gnaf',
]

#
# Linksets register
#
LINKSETS = [
    'https://raw.githubusercontent.com/CSIRO-enviro-informatics/addressescatchments-linkset/master/header.ttl',
    'https://raw.githubusercontent.com/CSIRO-enviro-informatics/meshblockscatchments-linkset/master/head.ttl',
    'https://raw.githubusercontent.com/CSIRO-enviro-informatics/addrmb11-linkset/master/header.ttl',
    'https://raw.githubusercontent.com/CSIRO-enviro-informatics/addrmb16-linkset/master/header.ttl',
    'https://raw.githubusercontent.com/CSIRO-enviro-informatics/addr1605mb16-linkset/master/header.ttl',
    'https://raw.githubusercontent.com/CSIRO-enviro-informatics/addr1605mb11-linkset/master/header.ttl',
    'https://raw.githubusercontent.com/CSIRO-enviro-informatics/meshblockscontractedcatchments-linkset/master/head.ttl',
]

#
# Tools register
#
TOOLS = []