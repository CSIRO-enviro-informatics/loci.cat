from flask import Blueprint, render_template, redirect, Response
import locicat.config as config
import markdown
from flask import Markup
from rdflib import Namespace, RDF

routes = Blueprint('routes', __name__)


# @routes.before_first_request
# def load_graph():
#     print('getting graphs')
#     import sys
#     import os
#     sys.path.insert(0, os.path.join(os.path.dirname(config.APP_DIR), 'harvester'))
#     g = get_graphs()


@routes.route('/')
def index():
    return render_template(
        'index.html',
        title='loci.cat'
    )


@routes.route('/dataset/')
def datasets():
    # DCAT = Namespace('http://www.w3.org/ns/dcat#')
    # for s in g.subjects(RDF.type, DCAT.Distribution):
    #     print(s)

    import harvester
    g = harvester.get_graphs()
    DCAT = Namespace('http://www.w3.org/ns/dcat#')
    DCT = Namespace('http://purl.org/dc/terms/')
    o = []
    for s in g.subjects(RDF.type, DCAT.DataDistributionService):
        for t in g.objects(s, DCT.title):
            o.append('<li><a href="{0}">{1}</a></li>'.format(s, t))
    # for d in g.query(q):
    #     o += '<li><a href="{0}">{1}</a></li>'.format(d['d'], d['title'])
    sorted(o)  # TODO: improve sort
    o = '<html><ul>{}</ul></html>'.format('\n'.join(o))
    return Response(o)


@routes.route('/linkset/')
def linksets():
    return 'Coming!'


@routes.route('/def/')
def defs():
    return 'Coming!'


@routes.route('/tool/')
def tools():
    return 'Coming!'


@routes.route('/about')
def about():
    import os

    # using basic Markdown method from http://flask.pocoo.org/snippets/19/
    with open(os.path.join(os.path.dirname(config.APP_DIR), 'README.md')) as f:
        content = f.read()

    # make images come from web dir
    # content = content.replace('view/static/system.svg',
    #                           '/static/system.svg')
    content = Markup(markdown.markdown(content))

    return render_template(
        'about.html',
        title='About',
        navs={},
        content=content
    )


@routes.route('/LICENSE')
def license():
    redirect('https://github.com/CSIRO-enviro-informatics/loci.cat/blob/master/LICENSE')
