from flask import Flask, request, jsonify

app = Flask(__name__)

user_db = {"amisha" : "123", "amrita" : "321"}

@app.route('/signup', methods=['POST'])
def user_signup():
    data = request.get_json()
    user, passd = data["user"], data["passd"]
    if user in user_db:
        return jsonify({"msg":"User already exists"})
    user_db[user] = passd
    print(user_db,"---> user db")
    return jsonify({"msg":"signup successful"})

@app.route('/list')
def returnListOfUsers():
    return jsonify(user_db)

        
if __name__ == '__main__':
    app.run(debug=True)