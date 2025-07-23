from flask import Flask,jsonify
import json

app=Flask(__name__)

@app.route('/api',methods=['Get'])
def GetData():
    try:
        with open('data.json', 'r') as file:
            data = json.load(file)
        return jsonify(data)
    except Exception as e:
        return jsonify({"error": str(e)}), 500
if(__name__)=='main':
    app.run(host='0.0.0.0',port=5000,debug=true)
