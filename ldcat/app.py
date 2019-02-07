import logging
import ldcat.config as config
from flask import Flask
import ldcat.controller as cont
import ldcat.helper as helper

app = Flask(__name__, template_folder=config.TEMPLATES_DIR, static_folder=config.STATIC_DIR)
app.register_blueprint(cont.routes)


@app.before_first_request
def startup():
    import harvester
    if harvester.config.HARVEST:
        harvester.harvest()


@app.context_processor
def context_processor():
    """
    A set of global variables available to 'globally' for jinja templates.
    :return: A dictionary of variables
    :rtype: dict
    """
    return dict(h=helper)


# run the Flask app
if __name__ == '__main__':
    logging.basicConfig(filename=config.LOGFILE,
                        level=logging.DEBUG,
                        datefmt='%Y-%m-%d %H:%M:%S',
                        format='%(asctime)s %(levelname)s %(filename)s:%(lineno)s %(message)s')
    app.run(debug=config.DEBUG, threaded=True)


