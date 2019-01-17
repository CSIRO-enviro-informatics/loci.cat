from pyldapi import Renderer, View
from flask import Response, render_template
import harvester
from locicat import tools
from locicat.queries import DefQueries


class DefModel():
    def __init__(self, uri, g):
        self.uri = uri
        self.creators = DefQueries.get_creators(uri, g)
        self.rights = DefQueries.get_rights(uri, g)
        self.modified = DefQueries.get_modified(uri, g)
        self.date = DefQueries.get_date(uri, g)
        self.versionIRI = DefQueries.get_versionIRI(uri, g)
        self.imports = DefQueries.get_imports(uri, g)
        self.description = DefQueries.get_description(uri, g)
        self.title = DefQueries.get_title(uri, g)
        self.seeAlso = DefQueries.get_seeAlso(uri, g)
        self.versionInfo = DefQueries.get_versionInfo(uri, g)


class DefRenderer(Renderer):
    def __init__(self, uri, request):
        g = harvester.get_graphs()

        self.model = DefModel(uri, g)

        super(DefRenderer, self).__init__(request, uri, self._get_views(), 'loci')

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
                'ontology.html',
                **_template_context
            ),
            headers=self.headers
        )

    def _get_views(self):
        return {
            'loci': View(
                'Location Index (Loc-I) Definitional resource',
                'This Loc-I view provides basic metadata information on a Loc-I definitional resource.',
                ['text/html', 'application/json'] + self.RDF_MIMETYPES,
                'text/html',
                languages=['en'],  # default 'en' only for now
                namespace=''
            )
        }