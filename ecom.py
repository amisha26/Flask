#product details
#Product using id
#Update any product
#delete the product

from flask import Flask, request, jsonify

app = Flask(__name__)

product = {"1":"Watch", "2":"Shoes", "3":"Mobile", "4":"TV"}

@app.route('/products')
def getListOfProducts():
    return product


@app.route('/products/<id>', methods=['PUT','GET','DELETE'])
def getProductById(id):
    #print(id)
    if request.method=='GET':
        if id in product:
            return jsonify({id:product[id]})
        else:
            return jsonify({"msg":"Product not available"})
    elif request.method=='PUT':
        data = request.get_json()
        #print(data)
        pId, pName = data["id"], data["name"]
        if pId in product:
            product[pId] = pName
            return product
        else:
            return jsonify({"msg":"Product not available"})
    elif request.method=='DELETE':
        if id in product:
            del product[id]
            return product
        else:
            return jsonify({"msg":"Product not available"})



if __name__ == '__main__':
    #app.run(debug=True, port=50000)
    app.run(debug=True)