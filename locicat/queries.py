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