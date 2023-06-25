from flask import Flask, render_template
from weather import get_weather

app = Flask(__name__)

@app.route('/')
def index():
    weather_data = get_weather()
    return render_template('index.html', weather=weather_data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
