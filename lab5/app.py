from flask import Flask, render_template, request, json, jsonify, current_app as app
from datetime import date
import os
import requests


app = Flask(__name__)
json_info = ''
movies_path = os.path.join(app.static_folder, 'data', 'movies.json')
with open(movies_path, 'r') as raw_json:
	json_info = json.load(raw_json)


@app.route('/')
def about():
    return '<p>Flask Server is Running</p>'

@app.route('/api/v1/michael', methods=['GET'])
def michael_json():
	michael_info = os.path.join(app.static_folder, 'data', 'Michael.json')
	with open(michael_info, 'r') as json_data:
		json_info = json.load(json_data)
		return jsonify(json_info)

@app.route('/api/v1/movies')
def all_movies():
		return jsonify(json_info)

@app.route('/api/v1/movies/search_title', methods=['GET'])
def search_title():
	results = []
	if 'title' in request.args:
		title = request.args['title']

		for movie in json_info:
			if title in movie['title']:
				results.append(movie)

	if len(results) < 1:
		return "No results found"
	return render_template("index.html", results=results)




if __name__ == '__main__':
    app.run(debug = True, host='127.0.0.1')

# @app.route('/nasa')
# def nasa_image():
#     today = str(date.today())
#     response = requests.get('https://api.nasa.gov/planetary/apod?api_key=wjlnR0Xw9B5Sh3WEIJa9kmVd368hNMiUVIGahGPi&date='+today)

#     data = response.json()

#     return render_template('nasa.html',data=data)
