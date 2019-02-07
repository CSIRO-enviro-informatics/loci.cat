from pyldapi import Renderer, View
import harvester
from flask import Response, render_template, redirect
from ldcat import helper
from ldcat.queries import DCATQueries


class DCATModel():
    def __init__(self, uri, g):
        # get DCAT properties
        self.uri = uri
        self.contributors = DCATQueries.get_contributors(uri, g)
        self.creators = DCATQueries.get_creators(uri, g)
        self.description = DCATQueries.get_description(uri, g)
        self.title = DCATQueries.get_title(uri, g)
        self.contactPoint = None # TODO: Not sure how to write a query for this
        self.endpointDescription = DCATQueries.get_endpointDescription(uri, g)
        self.endpointURL = DCATQueries.get_endpointURL(uri, g)
        self.servesDataset = DCATQueries.get_servesDataset(uri, g)


class DatasetRenderer(Renderer):
    def __init__(self, uri, request):
        try:
            g = harvester.load_graph('datasets.p')
        except:
            g = harvester.get_graphs()

        self.DCATDataset = DCATModel(uri, g)

        super(DatasetRenderer, self).__init__(request, uri, self._get_views(), 'dcat')

    def render(self):
        if self.view == 'alternates':
            return self._render_alternates_view()
        else:
            if self.format in Renderer.RDF_SERIALIZER_MAP:
                return self._render_dcat_rdf()
            else:
                return self._render_dcat_html()

    def _render_dcat_rdf(self):
        return redirect(self.uri + '?_view=' + self.view + '&_format=' + self.format)

    def _render_dcat_html(self):
        _template_context = {
            'model': self.DCATDataset,
            'view': self.views[self.view].label,
        }

        return Response(
            render_template(
                'dataset.html',
                **_template_context
            ),
            headers=self.headers
        )

    def _get_views(self):
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