# service_a/app.py
from flask import Flask, request, render_template_string
import requests

app = Flask(__name__)

index_html = """
<!doctype html>
<html>
    <head><title>Microservice A</title></head>
    <body>
        <h1>Enter values to calculate sum</h1>
        <form action="/calculate" method="post">
            Enter a: <input type="text" name="a" value="7"><br>
            Enter b: <input type="text" name="b" value="5"><br>
            <input type="submit" value="Calculate">
        </form>
    </body>
</html>
"""

result_html = """
<!doctype html>
<html>
    <head><title>Result</title></head>
    <body>
        <h1>The result is: {{ result }}</h1>
    </body>
</html>
"""

@app.route('/index.html')
def index():
    return render_template_string(index_html)

@app.route('/calculate', methods=['POST'])
def calculate():
    a = int(request.form['a'])
    b = int(request.form['b'])
    response = requests.get(f'http://service_b:8081/add?a={a}&b={b}')
    result = response.json()['result']
    return render_template_string(result_html, result=result)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)

