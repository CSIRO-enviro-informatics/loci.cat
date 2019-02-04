class DefQueries():
    @staticmethod
    def get_title(uri, g):
        title = g.query("""
            PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
            PREFIX dct: <http://purl.org/dc/terms/>
            PREFIX dc: <http://purl.org/dc/elements/1.1/>
            PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
            SELECT *
            WHERE {{
                <{}> (dct:title | dc:title | rdfs:label | skos:prefLabel) ?t .
            }}""".format(uri))
        for row in title:
            return row['t']

    @staticmethod
    def get_versionIRI(uri, g):
        v = g.query("""
            PREFIX owl: <http://www.w3.org/2002/07/owl#>
            SELECT *
            WHERE {{
                <{}> owl:versionIRI ?v
            }}""".format(uri))
        for row in v:
            return row['v']

    @staticmethod
    def get_versionInfo(uri, g):
        v = g.query("""
            PREFIX owl: <http://www.w3.org/2002/07/owl#>
            SELECT *
            WHERE {{
                <{}> owl:versionInfo ?v
            }}""".format(uri))
        for row in v:
            return row['v']

    @staticmethod
    def get_description(uri, g):
        result = DCATQueries.get_description(uri, g)
        if result:
            return result
        else:
            d = g.query("""
                PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
                SELECT * 
                WHERE {{
                    <{}> rdfs:comment ?d .
                }}""".format(uri))
            for row in d:
                return row['d']

    @staticmethod
    def get_imports(uri, g):
        result = g.query("""
            PREFIX owl: <http://www.w3.org/2002/07/owl#>
            SELECT *
            WHERE {{
                <{}> owl:imports ?import
            }}""".format(uri))
        imports = []
        for row in result:
            imports.append(row['import'])
        return imports

    @staticmethod
    def get_seeAlso(uri, g):
        s = g.query("""
            PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
            SELECT *
            WHERE {{
                <{}> rdfs:seeAlso ?s
            }}""".format(uri))
        for row in s:
            return row['s']

    @staticmethod
    def get_creators(uri, g):
        return DCATQueries.get_creators(uri, g)

    @staticmethod
    def get_date(uri, g):
        d = g.query("""
            PREFIX dc: <http://purl.org/dc/elements/1.1/>
            PREFIX dct: <http://purl.org/dc/terms/>
            SELECT *
            WHERE {{
                <{}> (dc:date | dct:date) ?d
            }}""".format(uri))
        for row in d:
            return row['d']

    @staticmethod
    def get_modified(uri, g):
        m = g.query("""
            PREFIX dct: <http://purl.org/dc/terms/>
            PREFIX dc: <http://purl.org/dc/elements/1.1/>
            SELECT *
            WHERE {{
                <{}> (dct:modified | dc:modified) ?m
            }}""".format(uri))
        for row in m:
            return row['m']

    @staticmethod
    def get_rights(uri, g):
        r = g.query("""
            PREFIX dct: <http://purl.org/dc/terms/>
            PREFIX dc: <http://purl.org/dc/elements/1.1/>
            SELECT *
            WHERE {{
                <{}> (dct:rights | dc:rights) ?r
            }}""".format(uri))
        for row in r:
            return row['r']


class LinksetQueries():
    @staticmethod
    def get_title(uri, g):
        return DCATQueries.get_title(uri, g)

    @staticmethod
    def get_description(uri, g):
        return DCATQueries.get_description(uri, g)

    @staticmethod
    def get_publisher(uri, g):
        publisher = g.query("""
            PREFIX dct: <http://purl.org/dc/terms/>
            PREFIX dc: <http://purl.org/dc/elements/1.1/>
            SELECT *
            WHERE {{
                <{}> (dct:publisher | dc:publisher) ?publisher .
            }}""".format(uri))
        for row in publisher:
            return row['publisher']

    @staticmethod
    def get_issued(uri, g):
        issued = g.query("""
            PREFIX dct: <http://purl.org/dc/terms/>
            PREFIX dc: <http://purl.org/dc/elements/1.1/>
            SELECT *
            WHERE {{
                <{}> (dct:issued | dc:issued) ?issued .
            }}""".format(uri))
        for row in issued:
            return row['issued']

    @staticmethod
    def get_modified(uri, g):
        modified = g.query("""
            PREFIX dct: <http://purl.org/dc/terms/>
            PREFIX dc: <http://purl.org/dc/elements/1.1/>
            SELECT *
            WHERE {{
                <{}> (dct:modified | dc:modified) ?modified .
            }}""".format(uri))
        for row in modified:
            return row['modified']

    @staticmethod
    def get_contributors(uri, g):
        return DCATQueries.get_contributors(uri, g)

    @staticmethod
    def get_objectsTarget(uri, g):
        o = g.query("""
            PREFIX void: <http://rdfs.org/ns/void#>
            SELECT *
            WHERE {{
                <{}> void:objectsTarget ?o .
            }}""".format(uri))
        for row in o:
            return row['o']

    @staticmethod
    def get_subjectsTarget(uri, g):
        s = g.query("""
            PREFIX void: <http://rdfs.org/ns/void#>
            SELECT *
            WHERE {{
                <{}> void:subjectsTarget ?s .
            }}""".format(uri))
        for row in s:
            return row['s']

    @staticmethod
    def get_prov_plan(uri, g):
        s = g.query("""
            PREFIX : <{}>
            PREFIX loci: <http://linked.data.gov.au/def/loci/>
            PREFIX prov: <http://www.w3.org/ns/prov#>
            PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
            PREFIX vcard: <http://www.w3.org/2006/vcard/ns#>
            SELECT ?label ?text_source ?comment ?time ?name ?email ?extra
            WHERE {{
                : loci:hadGenerationMethod ?plan .
                ?plan rdfs:label ?label .
                ?plan prov:value ?text_source .
                ?plan rdfs:comment ?comment .
                ?plan prov:generatedAtTime ?time .
                ?plan prov:wasAttributedTo ?person .
                ?person vcard:fn ?name .
                ?person vcard:hasEmail ?email .
                ?person rdfs:seeAlso ?extra .
            }}""".format(uri))
        if len(s) > 0:
            for row in s:
                import requests
                return {
                    'label': row['label'],
                    'text': requests.get(row['text_source']).text,
                    'comment': row['comment'],
                    'time': row['time'],
                    'name': row['name'],
                    'email': row['email'],
                    'extra': row['extra']
                }

        s = g.query("""
            PREFIX : <{}>
            PREFIX loci: <http://linked.data.gov.au/def/loci/>
            PREFIX prov: <http://www.w3.org/ns/prov#>
            PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
            PREFIX vcard: <http://www.w3.org/2006/vcard/ns#>
            SELECT ?label ?text_source ?comment ?time ?name ?email ?extra
            WHERE {{
                : prov:wasGeneratedBy ?activity .
                ?activity prov:qualifiedAssociation ?blank .
                ?blank prov:hadPlan ?plan .
                ?plan rdfs:label ?label .
                ?plan prov:value ?text_source .
                ?plan rdfs:comment ?comment .
                ?plan prov:generatedAtTime ?time .
                ?plan prov:wasAttributedTo ?person .
                ?person vcard:fn ?name .
                ?person vcard:hasEmail ?email .
                ?person rdfs:seeAlso ?extra .
            }}
            """.format(uri))
        for row in s:
            import requests
            return {
                'label': row['label'],
                'text': requests.get(row['text_source']).text,
                'comment': row['comment'],
                'time': row['time'],
                'name': row['name'],
                'email': row['email'],
                'extra': row['extra']
            }


class DCATQueries():
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