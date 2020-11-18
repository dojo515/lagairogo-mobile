import json
import urllib.request
from flask import Flask,render_template,url_for,request

app= Flask(__name__,static_folder="static")

@app.route('/')
def home():
	return render_template('index.html')


@app.route('/predict',methods=['POST'])
def predict():


	data = {
        "Inputs": {
                "input1":
                [
                    {
                            'battery_power': request.form['battery_power'],
                            'blue': request.form['blue'],
                            'clock_speed': request.form['clock_speed'],
                            'dual_sim': request.form['dual_sim'],
                            'fc': request.form['fc'],
                            'four_g': request.form['four_g'],
                            'int_memory': request.form['int_memory'],
                            'm_dep': request.form['m_dep'],
                            'mobile_wt': request.form['mobile_wt'],
                            'n_cores': request.form['n_cores'],
                            'pc': request.form['pc'],
                            'px_height': request.form['px_height'],
                            'px_width': request.form['px_width'],
                            'ram': request.form['ram'],
                            'sc_h': request.form['sc_h'],
                            'sc_w': request.form['sc_w'],
                            'talk_time': request.form['talk_time'],
                            'three_g': request.form['three_g'],
                            'touch_screen': request.form['touch_screen'],
                            'wifi': request.form['wifi'],

                    }
                ],
        },
		"GlobalParameters":  {
							}
	}

	body = str.encode(json.dumps(data))
	print(data)
	url = 'https://ussouthcentral.services.azureml.net/workspaces/0cd34c727b2b47238ff7b48522edfe7d/services/1f945513892241e49b08ee98d1629378/execute?api-version=2.0&format=swagger'
	api_key = 'GQk9fDrbqWXw/GHLblOQIIQXAEngbJpl8XdbZ2n0QLozRmuHH72DU1wY4RGXpoQrcWdjXPPaTDAnyYKnjADNHQ==' # Replace this with the API key for the web service
	headers = {'Content-Type':'application/json', 'Authorization':('Bearer '+ api_key)}

	#------------python2 code----------

	#req = urllib2.Request(url, body, headers)
	#response = urllib2.urlopen(req)
	#result = response.read()

	req = urllib.request.Request(url, body, headers)
	response = urllib.request.urlopen(req)
	result = response.read().decode('utf-8')

	y = json.loads(result)
	print(y)
	print(y['Results']['output1'][0]['Scored Labels'])
	y = json.loads(result)
	prediction_value=y['Results']['output1'][0]['Scored Labels']



	return render_template('result.html',prediction = prediction_value)











if __name__ == '__main__':
	app.run(debug=True)
	#app.run('0.0.0.0',port=8000,debug=True)
