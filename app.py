from flask import Flask, request

app=Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def odd_even():
    if request.method == "GET":
        return """
        以下に整数を入力...
        <form action="/" method="POST">
        <input name="num"></input>
        </from>"""
    else:
        return """
        {}は{}
        <form action="/" method="POST">
        <input name="num"></input>
        </form>""".format(str(request.form["num"]), ["偶数", "奇数"][int(request.form["num"])%2])

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=8888, threaded=True)