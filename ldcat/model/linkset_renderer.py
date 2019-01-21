from pyldapi import Renderer, View
import harvester
from ldcat import tools
from flask import render_template, Response
from ldcat.queries import LinksetQueries


class LinksetModel():
    def __init__(self, uri, g):
        self.uri = uri
        self.title = LinksetQueries.get_title(uri, g)
        self.description = LinksetQueries.get_description(uri, g)
        self.publisher = LinksetQueries.get_publisher(uri, g)
        self.issued = LinksetQueries.get_issued(uri, g)
        self.modified = LinksetQueries.get_modified(uri, g)
        self.contributors = LinksetQueries.get_contributors(uri, g)
        self.objectsTarget = LinksetQueries.get_objectsTarget(uri, g)
        self.subjectsTarget = LinksetQueries.get_subjectsTarget(uri, g)


class LinksetRenderer(Renderer):
    def __init__(self, uri, request):
        g = harvester.get_graphs()

        self.model = LinksetModel(uri, g)

        super(LinksetRenderer, self).__init__(request, uri, self._get_views(), 'loci')

    def render(self):
        if self.view == 'alternates':
            return self._render_alternates_view()
        else:
            if self.format in Renderer.RDF_SERIALIZER_MAP:
                return self._render_rdf()
            else:
                return self._render_html()

    def _render_rdf(self):
        raise NotImplementedError

    def _render_html(self):
        _template_context = {
            'model': self.model,
            'view': self.views[self.view].label,
            't': tools
        }

        return Response(
            render_template(
                'linkset.html',
                **_template_context
            ),
            headers=self.headers
        )

    def _get_views(self):
        return {
            'loci': View(
                'Location Index (Loc-I) Linkset',
                'This Loc-I view provides basic metadata information on a Loc-I Linkset.',
                ['text/html', 'application/json'] + self.RDF_MIMETYPES,
                'text/html',
                languages=['en'],  # default 'en' only for now
                namespace=''
            )
        }