from flask import Flask,jsonify
import json

app=Flask(__name__)

@app.route('/api',methods=['Get'])
def GetData():
    try:
        with open('data.json','r') as file:
            data=json.load(json)
        return jsonify(data)
    except Expection as e:
        return jsonify({"Error Message",str(e)}),500

if(__name__)=='main':
    app.run(host='0.0.0.0',port=5000,debug=true)
