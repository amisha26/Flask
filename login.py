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

@app.route('/login', methods=['POST'])
def func():
    data = request.get_json()
    print(data)
    user, passd = data["user"], data["passd"]
    """ for i in user_db:
        if i==user:
            val = user_db[i]
            print(val, "val")
            if passd == val:
                return "Success", 200
            else:
                return jsonify({"msg":"password in invalid"}) """
    if user in user_db:
        if user_db[user]==passd:
            return "Success", 200
        else:
            return jsonify({"msg":"password in invalid"}) 
   
    else:
        return jsonify({"msg":"User does not exist. Signup instead"})
        #return user_signup(user, passd)

        
if __name__ == '__main__':
    app.run(debug=True)