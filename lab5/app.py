from flask import Flask, render_template
from datetime import date
import requests


app = Flask(__name__)

@app.route('/')
def about():
    return '<p>Welcome to the About Coaches Site</p>'

@app.route('/Michael')
def michael():
    return render_template('stone.html')

@app.route('/Stephanie')
def stephanie():
    return render_template('stephanie.html')

@app.route('/Okra')
def okra():
    return render_template('okra.html')

@app.route('/nasa')
def show_nasa_pic():
    today = str(date.today())
    response = requests.get('https://api.nasa.gov/planetary/apod?api_key=wjlnR0Xw9B5Sh3WEIJa9kmVd368hNMiUVIGahGPi&date='+today)
    data = response.json()
    return render_template('nasa.html',data=data)


if __name__ == '__main__':
    app.run(debug = True, host='127.0.0.1')

# @app.route('/nasa')
# def nasa_image():
#     today = str(date.today())
#     response = requests.get('https://api.nasa.gov/planetary/apod?api_key=wjlnR0Xw9B5Sh3WEIJa9kmVd368hNMiUVIGahGPi&date='+today)

#     data = response.json()

#     return render_template('nasa.html',data=data)
