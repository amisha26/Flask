#user will login. provide a token
#token has expiry period. 
#user hits ep

from flask import Flask, request, jsonify 

app = Flask(__name__)

user_db = {"amrita":"12", "amisha":"13", "amitej":"14"}

flag = False
c=0

def token_gen():
    return c+1

t=1
def curr_time():
    return t

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    user, passd = data["user"], data["passd"]
    if user in user_db:
        flag=True
        x=token_gen()
        return x
    else:
        return jsonify({"msg":"User not available. Signup instead"})

@app.route('/x')
def hit_x(flag):
    if flag==False:
        return jsonify({"msg":"login first"})
    else:
        x = login()
        tnew = curr_time()
        return jsonify({"msg":"your token expiry time is {tnew+5}"})

@app.route('/y')
def hit_y():
    if flag==False:
        return jsonify({"msg":"login first"})
    else:
        x = login()
        #tnew = curr_time()
        return jsonify({"msg":"your token has expired"})
#@app.route('/z')


if __name__=='__main__':
    app.run(debug=True)