from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods =['GET'])
def helloworld():
    return 'Hello World'

@app.route('/aboutus')
def aboutUs():
    return 'this is about page'

@app.route('/contactus', methods=['POST'])
def contactUs():
    return 'contact us now'

if __name__ == '__main__':
    app.run(port=3000, debug=True)
