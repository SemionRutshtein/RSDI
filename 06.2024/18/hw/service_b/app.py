from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/add' , methods=['GET'])
def add():
	a = request.args.get('a', type=int)
	b = request.args.get('b', type=int)
	result = a + b
	return jsonify(result=result)

if __name__=='__main__':
	app.run(host='0.0.0.0', port=8081)

