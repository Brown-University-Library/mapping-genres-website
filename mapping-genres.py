from flask import Flask, redirect, request, url_for
from flask import render_template

app = Flask(__name__)

@app.route("/")
def home():
	return render_template('index.html')

@app.route("/visualizations/aas-map")
def aas_map():
	return render_template('visualizations/aas-map.html')

@app.route("/visualizations/aas-subjects")
def aas_subjects():
	return render_template('visualizations/aas-bubble-subjects.html')

@app.route('/visualizations/brown-map')
def brown_map():
	return render_template('visualizations/brown-map.html')

@app.route('/visualizations/first-brown-map')
def first_brown_map():
	return render_template('visualizations/first-brown-map.html')

@app.route('/visualizations/first-brown-slider')
def first_brown_slider():
	return render_template('visualizations/first-brown-slider.html')

#These routes are redirects from the URL structure of the old site
@app.route("/symbol-maps/hay-jcb-voronoi.html")
def old_maps1():
	return redirect(url_for('brown_map'), 301)

@app.route("/symbol-maps/brownSlider.html")
def old_maps2():
	return redirect(url_for('first_brown_slider'), 301)

@app.route("/symbol-maps/aas-voronoi-map.html")
def old_maps3():
	return redirect(url_for('aas_map'), 301)	

@app.route("/symbol-maps/brown-voronoi-map.html")
def old_maps4():
	return redirect(url_for('first_brown_map'), 301)

@app.route("/bubble-charts/aas-bubble.html")
def old_bubbles():
	return redirect(url_for('aas_subjects'), 301)

if __name__ == '__main__':
	app.run()