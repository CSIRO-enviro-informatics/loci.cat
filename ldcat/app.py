import logging
import ldcat.config as config
from flask import Flask
import ldcat.controller as cont

app = Flask(__name__, template_folder=config.TEMPLATES_DIR, static_folder=config.STATIC_DIR)
app.register_blueprint(cont.routes)


# run the Flask app
if __name__ == '__main__':
    logging.basicConfig(filename=config.LOGFILE,
                        level=logging.DEBUG,
                        datefmt='%Y-%m-%d %H:%M:%S',
                        format='%(asctime)s %(levelname)s %(filename)s:%(lineno)s %(message)s')
    app.run(debug=config.DEBUG, threaded=True)


