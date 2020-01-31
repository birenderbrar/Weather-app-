from flask import Flask, render_template, request
import requests
import serial


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/temperature', methods=['POST'])
def temperature():
	# Initalizing serial port and baudrate same as arduino baudrate and parsing temprature and humidity data
    ser = serial.Serial('COM8', baudrate=9600)
    stream = ser.readline().decode('ascii')
    values = stream.rstrip().split('|')
    temp_indoor = float(values[0])
    humidity_indoor = float(values[1])
    # fetching outside data and parsing temprature and humidity data based on provided zip code
    # This api is capable for us zip codes only, to use other country's zip codes plz check the documentation of api
    zipcode = request.form['zip']
    r = requests.get('http://api.openweathermap.org/data/2.5/weather?zip=' +
                     zipcode + ',us&appid= provide your own api key')
    json_object = r.json()
    temp_k = float(json_object['main']['temp'])
    temp_outdoor = temp_k - 273
    humidity_outdoor = float(json_object['main']['humidity'])
    # Inserting fetched data to html page.
    return render_template('temperature.html', temp1=temp_outdoor, hum1=humidity_outdoor, temp2=temp_indoor, hum2=humidity_indoor)




if __name__ == '__main__':
    app.run(debug=True)
