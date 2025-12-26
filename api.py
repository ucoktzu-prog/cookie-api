from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/checkcookie", methods=["GET"])
def checkcookie():
    cookie = request.args.get("cookie")

    if not cookie:
        return jsonify({
            "status": "failed",
            "message": "Cookie kosong"
        })

    if cookie != "validcookie":
        return jsonify({
            "status": "failed",
            "message": "Cookie invalid"
        })

    return jsonify({
        "status": "success",
        "message": "Cookie valid"
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
