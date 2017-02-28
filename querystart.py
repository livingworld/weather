from flask import Flask
from flask import request
from flask import render_template
from getweather import dumpTianqi,fetchWeather,history_weather
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
        if request.form['button'] == 'Help':
            return render_template('weather_query.html',
                help='  ')
        elif request.form['button'] == 'History':
            history = history_weather()
            return render_template('weather_query.html',
                history = history)
        elif request.form['button'] == 'Search':
            location = request.form['location']
            result = fetchWeather(location)
            if 'status' in result:
                return render_template('404.html')
            else:
                weather=dumpTianqi(result)
                return render_template('weather_query.html',
                    weather = weather)
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
