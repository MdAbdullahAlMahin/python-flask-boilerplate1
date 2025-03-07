import logging
import socket
from endpoints import app
logger = logging.getLogger(__name__)

@app.route('/', methods=['GET'])
def default_route():
    return "Python Template"

# logging information
logger = logging.getLogger()
handler = logging.StreamHandler()
formatter = logging.Formatter(
        '%(asctime)s %(name)-12s %(levelname)-8s %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)
logger.setLevel(logging.INFO)


# server handling
if __name__ == "__main__":
    logging.info("Starting application ...")
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(('localhost', 8080))  # defaulted to port 8080
    port = sock.getsockname()[1]
    sock.close()
    app.run(port=port, debug=True)  # debug mode is on
