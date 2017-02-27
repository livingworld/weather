from flask import Flask
from flask import request
from flask import render_template
from query_tp_requests import dumpTianqi,fetchWeather,history_weather
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from datetime import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard to guess string'

bootstrap = Bootstrap(app)
moment = Moment(app)

@app.route('/weather_query.html', methods=['POST', 'GET'])
def getWeather():
	if request.method == 'POST':
		location = request.form['location']
		result = fetchWeather(location)#这里是一个坑，因为加入weather=dumpTianqi(result)放在之后的话，会导致运行出错。
		if 'status' in result:
			return render_template('404.html')
		else:
			weather=dumpTianqi(result)
			return render_template('weather_query.html',
				weather=weather)

	elif request.method == 'GET':

		if request.args.get('button') == 'Help':
			return render_template('weather_query.html',
				help='  ')
		elif request.args.get('button') == 'History':
			history=history_weather()
			return render_template('weather_query.html',
				history=history)
		else:
			return render_template('weather_query.html')

@app.route('/current_time.html')
def current_time():
	return render_template('current_time.html',
	current_time=datetime.utcnow())

@app.route('/')
def welcome():
	return render_template('welcome.html')

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500

if __name__ == '__main__':
	app.run(debug=True)
