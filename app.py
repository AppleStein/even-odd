from flask import Flask, request

app=Flask(__name__)

@app.route("/")
def odd_even():
    return """
    以下に整数を入力...
    <form action="/" method="POST">
    <input name="num"></input>
    </from>"""

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=8888, threaded=True)