import harvester.config as config
import requests

if __name__ == '__main__':
    # for each dataset in the config file, pull down its DCAT description
    for d in config.DATASETS:
        r = requests.get('http://gnafld.net', params={'_view': 'dcat', '_format': 'text/turtle'})
        print(r.content.decode('utf-8'))
