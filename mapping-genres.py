from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/")
def hello():
	return render_template('index.html')


@app.route("/visualizations/aas-map")
def aas_map():
	return render_template('visualizations/aas-voronoi-map.html')

if __name__ == '__main__':
	app.run()