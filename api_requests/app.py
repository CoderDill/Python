from flask import Flask, render_template, request
import requests
from secrets import VALRONT_API_KEY, API_SECRET_KEY

API_BASE_URL = "http://www.mapquestapi.com/geocoding/v1"

key = API_SECRET_KEY
valorant_key = VALRONT_API_KEY

app = Flask(__name__)


def get_coords(address):
    res = requests.get(f"{API_BASE_URL}/address",
                       params={'key': key, 'location':  address})
    data = res.json()
    lat = data["results"][0]['locations'][0]['latLng']['lat']
    lng = data["results"][0]['locations'][0]['latLng']['lng']
    coords = {'lat': lat, 'lng': lng}

    return coords


@app.route('/')
def show_address_form():
    return render_template("address_form.html")


@app.route('/geocode')
def get_location():
    address = request.args["address"]
    coords = get_coords(address)
    return render_template('address_form.html', coords=coords)


@app.route('/valorant')
def show_valorant():
    res = requests.get(
        "https://na.api.riotgames.com/val/content/v1/contents", params={'api_key': valorant_key})
    data = res.json()
    agents = data["characters"]
    maps = data["maps"]
    weapons = data["chromas"]
    return render_template("show_valorant.html", data=data, agents=agents, maps=maps, weapons=weapons)
