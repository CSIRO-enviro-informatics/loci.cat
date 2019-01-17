from flask import Response
import pyldapi
import harvester
from rdflib import URIRef, Literal, RDF
from rdflib.namespace import DCTERMS, DC, OWL, RDFS
import locicat.config as config
from harvester.config import DATASETS, DEFS


class LociRegisterRenderer(pyldapi.RegisterRenderer):
    def _get_def_items(self, s, g):
        items = []
        # for t in g.objects(s, RDFS.label):
        #     if cic == config.URI_DEF_CLASS and str(s) in DEFS:
        #         items.append((self.request.url_root + 'def/?uri=' + str(s), str(t), None))
        results = g.query("""
            PREFIX dct: <http://purl.org/dc/terms/>
            PREFIX dc: <http://purl.org/dc/elements/1.1/>
            PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>    
            SELECT *
            WHERE {{
                <{}> (dct:title | dc:title | rdfs:label) ?t .
            }}""".format(s))
        for row in results:
            items.append((self.request.url_root + 'def/?uri=' + str(s), str(row['t']), None))
        return items

    def _get_subjects_by_title(self, s, cic, g):
        items = []
        for t in g.objects(s, DCTERMS.title):
            if cic == config.URI_DATASET_CLASS and str(s) in DATASETS:
                items.append((self.request.url_root + 'dataset/?uri=' + str(s), str(t), None))
            elif cic == config.URI_LINKSET_CLASS:
                items.append((self.request.url_root + 'linkset/?uri=' + str(s), str(t), None))
        return items

    def _get_items_from_graph(self, page, per_page):
        g = harvester.get_graphs()
        cic = self.contained_item_classes[0]
        start = (page - 1) * per_page  # where in the list of all items to start listing from

        try:
            if cic == config.URI_DATASET_CLASS:
                self.label = 'VoID Datasets'
            elif cic == config.URI_LINKSET_CLASS:
                self.label = 'VoID Linksets'
            elif cic == config.URI_DEF_CLASS:  # TODO: cater for other def types, not just onts
                self.label = 'Definitional Resource'
            else:
                raise RuntimeError("Cannot get register objects")

            # loop for all subjects of the cic type
            for i, s in enumerate(g.subjects(RDF.type, URIRef(cic))):
                if i >= start:
                    # loop for all the labels of this subject
                    if cic == config.URI_DATASET_CLASS or cic == config.URI_LINKSET_CLASS:
                        self.register_items += self._get_subjects_by_title(s, cic, g)
                    elif cic == config.URI_DEF_CLASS:
                        self.register_items += self._get_def_items(s, g)

                if len(self.register_items) == per_page:  # ensure we only list as many as the per_page
                    break

            # sort the register items by label
            self.register_items.sort(key=lambda tup: tup[1])
        except Exception as e:
            print(e)

    def __init__(
            self,
            _request,
            uri,
            label,
            comment,
            contained_item_classes,
            register_total_count,
            *args,
            views=None,
            default_view_token=None,
            **kwargs
    ):
        kwargs.setdefault('alternates_template', 'alternates.html')
        kwargs.setdefault('register_template', 'register.html')
        super(LociRegisterRenderer, self).__init__(
            _request,
            uri,
            label,
            comment,
            [],
            contained_item_classes,
            register_total_count,
            *args,
            views=views,
            default_view_token=default_view_token,
            **kwargs
        )
        try:
            vf_error = self.vf_error
            if vf_error:
                if not hasattr(self, 'view') or not self.view:
                    self.view = 'reg'
                if not hasattr(self, 'format') or not self.format:
                    self.format = 'text/html'
        except AttributeError:
            pass
        if self.view == "alternates":
            pass
        else:
            self._get_items_from_graph(self.page, self.per_page)

    def render(self):
        try:
            return super(LociRegisterRenderer, self).render()
        except Exception as e:
            from flask import request
            return render_error(request, e)

    def _render_alternates_view_html(self, template_context=None):
        _template_context = {
            'class_uri': "http://purl.org/linked-data/registry#Register",
            'instance_uri': None
        }
        if template_context is not None and isinstance(template_context, dict):
            _template_context.update(template_context)
        return super(LociRegisterRenderer, self)\
            ._render_alternates_view_html(template_context=_template_context)


def render_error(request, e):
    try:
        import traceback
        traceback.print_tb(e.__traceback__)
    except Exception:
        pass
    if isinstance(e, pyldapi.ViewsFormatsException):
        error_type = 'Internal View Format Error'
        error_code = 406
        error_message = e.args[0] or "No message"
    elif isinstance(e, NotImplementedError):
        error_type = 'Not Implemented'
        error_code = 406
        error_message = e.args[0] or "No message"
    elif isinstance(e, RuntimeError):
        error_type = 'Server Error'
        error_code = 500
        error_message = e.args[0] or "No message"
    else:
        error_type = 'Unknown'
        error_code = 500
        error_message = "An Unknown Server Error Occurred."

    resp_text = '''<?xml version="1.0"?>
    <error>
      <errorType>{}</errorType>
      <errorCode>{}</errorCode>
      <errorMessage>{}</errorMessage>
    </error>
    '''.format(error_type, error_code, error_message)
    return Response(resp_text, status=error_code, mimetype='application/xml')