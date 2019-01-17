from pyldapi import Renderer, View
import harvester
from flask import Response, render_template
from rdflib import URIRef, RDF, Graph
from rdflib.namespace import Namespace, DC
import tools


class DCAT_queries():
    @staticmethod
    def get_contributors(uri, g):
        contributors = g.query("""
            PREFIX dct: <http://purl.org/dc/terms/>
            PREFIX dc: <http://purl.org/dc/elements/1.1/>
            SELECT *
            WHERE {{
                <{}> (dct:contributor | dc:contributor) ?contributor .
            }}""".format(uri))
        result = []
        for row in contributors:
            result.append(row['contributor'])
        return result

    @staticmethod
    def get_creators(uri, g):
        creators = g.query("""
            PREFIX dct: <http://purl.org/dc/terms/>
            PREFIX dc: <http://purl.org/dc/elements/1.1/>
            SELECT *
            WHERE {{
                <{}> (dct:creator | dc:creator) ?creator .
            }}""".format(uri))
        result = []
        for row in creators:
            result.append(row['creator'])
        return result

    @staticmethod
    def get_title(uri, g):
        title = g.query("""
            PREFIX dct: <http://purl.org/dc/terms/>
            PREFIX dc: <http://purl.org/dc/elements/1.1/>
            SELECT *
            WHERE {{
                <{}> (dct:title | dc:title) ?title .
            }}""".format(uri))
        for row in title:
            return row['title']

    @staticmethod
    def get_description(uri, g):
        description = g.query("""
            PREFIX dct: <http://purl.org/dc/terms/>
            PREFIX dc: <http://purl.org/dc/elements/1.1/>
            SELECT *
            WHERE {{
                <{}> (dct:description | dc:description) ?description .
            }}""".format(uri))
        for row in description:
            return row['description']

    @staticmethod
    def get_endpointDescription(uri, g):
        description = g.query("""
            PREFIX dcat: <http://www.w3.org/ns/dcat#>
            SELECT * 
            WHERE {{
                <{}> dcat:endpointDescription ?description .
            }}""".format(uri))
        for row in description:
            return row['description']

    @staticmethod
    def get_endpointURL(uri, g):
        url = g.query("""
            PREFIX dcat: <http://www.w3.org/ns/dcat#>
            SELECT * 
            WHERE {{
                <{}> dcat:endpointURL ?url .
            }}""".format(uri))
        for row in url:
            return row['url']

    @staticmethod
    def get_servesDataset(uri, g):
        s = g.query("""
        PREFIX dcat: <http://www.w3.org/ns/dcat#>
        SELECT *
        WHERE {{
            <{}> dcat:servesDataset ?s .
        }}""".format(uri))
        for row in s:
            return row['s']


class DCATModel():
    def __init__(self, uri, g):
                 # contributors,
                 # creators,
                 # descrption,
                 # license,
                 # title,
                 # contactPoint,
                 # endpointDescription,
                 # endpointURL,
                 # servesDataset
        pass

        # get DCAT properties
        self.uri = uri
        self.contributors = DCAT_queries.get_contributors(uri, g)
        self.creators = DCAT_queries.get_creators(uri, g)
        self.description = DCAT_queries.get_description(uri, g)
        self.title = DCAT_queries.get_title(uri, g)
        self.contactPoint = None # TODO: Not sure how to write a query for this
        self.endpointDescription = DCAT_queries.get_endpointDescription(uri, g)
        self.endpointURL = DCAT_queries.get_endpointURL(uri, g)
        self.servesDataset = DCAT_queries.get_servesDataset(uri, g)


class DatasetRenderer(Renderer):
    def __init__(self, uri, request):
        self.g = harvester.get_graphs()#Graph().parse(uri+'.ttl', format='turtle')

        self.DCATDataset = DCATModel(uri, self.g)

        super(DatasetRenderer, self).__init__(request, uri, self.get_views(), 'dcat')

    def render(self):
        if self.view == 'alternates':
            return self._render_alternates_view()
        else:
            if self.format in Renderer.RDF_SERIALIZER_MAP:
                return self._render_dcat_rdf()
            else:
                return self._render_dcat_html()

    def _render_dcat_rdf(self):
        raise NotImplementedError

    def _render_dcat_html(self):
        _template_context = {
            'model': self.DCATDataset,
            'view': self.views[self.view].label,
            't': tools
        }

        return Response(
            render_template(
                'dataset.html',
                **_template_context
            ),
            headers=self.headers
        )

    def get_views(self):
        return {
            'dcat': View(
                'Dataset Catalogue Vocabulary (DCAT)',
                'DCAT is an RDF vocabulary designed to facilitate interoperability between data catalogs published on '
                'the Web.',
                ['text/html', 'application/json'] + self.RDF_MIMETYPES,
                'text/html',
                languages=['en'],  # default 'en' only for now
                namespace='http://www.w3.org/ns/dcat#'
            )
        }