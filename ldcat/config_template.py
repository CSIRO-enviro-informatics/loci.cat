from os import path

#
# -- Application Settings ----------------------------------------------------------------------------------------------
#
APP_DIR = path.dirname(path.abspath(__file__))
TEMPLATES_DIR = path.join(APP_DIR, 'view', 'templates')
STATIC_DIR = path.join(APP_DIR, 'view', 'static')
LOGFILE = path.join(APP_DIR, 'flask.log')
DEBUG = True

#
# -- URIs --------------------------------------------------------------------------------------------------------------
#
URI_BASE = 'http://loci.cat'
URI_DATASET_CLASS = 'http://rdfs.org/ns/void#Dataset'
URI_LINKSET_CLASS = 'http://rdfs.org/ns/void#Linkset'
URI_DEF_CLASS = 'http://www.w3.org/2002/07/owl#Ontology'
URI_TOOL_CLASS = ''

#
# -- Restricted Publishers ---------------------------------------------------------------------------------------------
#
# Resources will only be listed from the list of approved publishers using dct:publisher
#
PUBLISHERS = []