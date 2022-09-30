import logging
import json
from pymongo import MongoClient

from flask import request, jsonify

from endpoints import app

logger = logging.getLogger(__name__)


@app.route('/example', methods=['GET'])
def example():
    client = pymongo.MongoClient("mongodb+srv://MdAbdullahAlMahin:<password>@cluster0.7nvntxs.mongodb.net/?retryWrites=true&w=majority", server_api=ServerApi('1'))
    db = client['testDB']
    collection = db['testCol']
    doc_count = collection.count_documents({})
    return jsonify(doc_count)
