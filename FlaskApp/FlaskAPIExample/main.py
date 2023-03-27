from flask import Flask, request

app = Flask(__name__)

@app.route('/get-quantity', methods=['GET'])
def get_quantity():
    #we are taking a hardcoded data, but you may choose a database or another data source
    fruits = {('apple', 25), ('banana', 48), ('cherry', 146)}
    if request.method == 'GET':
        #read URL query parameter
        fruitname = request.args['fruitname']
        quantity = 0
        for item in fruits:
            if item[0] == fruitname:
                #if a match is found set the quantity and come out of the loop
                quantity = item[1]
                break
        return {fruitname: quantity}
    else:
        return 'Invalid request.'

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)