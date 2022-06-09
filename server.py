from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/temp')
def func():
    return "Hi amisha", 200

@app.route('/name/<name>')
def func1(name):
    return "Hi {}".format(name)


#/login?surname=tiwari
@app.route('/login')
def func4():
    data = request.args
    return data["surname"]

    

if __name__=='__main__':
    app.run(debug=True)
