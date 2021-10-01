from flask import Flask, request, redirect, abort

from .models import Link
from .utils import BASE58

app = Flask(__name__)
BASE_URL = 'http://localhost:5000/'


@app.route("/api/link", methods=["POST"])
def new_link():
    data = request.get_json()
    link = Link(data["longURL"])
    link.insert()
    short = BASE58.encode_int(link.id)
    data = {
        'short': short,
        'tinyurl': BASE_URL + short
    }
    return {
        'status': 'success',
        'data': data
    }


@app.route("/<short>", methods=["GET"])
def redirect_link(short):
    id = 0
    try:
        id = BASE58.decode_int(short)
    except KeyError:
        abort(404)
    link = Link.from_redis(id)
    if not link:
        abort(404)
    return redirect(link.longURL, code=302)
