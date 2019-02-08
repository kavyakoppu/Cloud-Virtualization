
from flask import Flask, render_template, request, jsonify
app = Flask(__name__, template_folder='HTML')

app.static_folder = 'static'

@app.route('/', methods=['GET','POST'])
def sendIndex():
    return render_template('index.html')

@app.route('/isPrime', methods=['GET', 'POST'])
def isPrime():
    givenNum = int(request.form['number'])
    noOfFactors = 0
    halfPlusOne = givenNum/2+1
    if givenNum<0:
        _isPrime = "Please enter a non-negative number!"
    elif givenNum<2:
        _isPrime= "It is neither a prime nor a composite"
    else :
        for i in range(2,halfPlusOne):
            if givenNum%i==0:
                noOfFactors+=1
        
        if noOfFactors>=1:
            _isPrime=False
        else:
            _isPrime=True
        
    return jsonify(isPrime = _isPrime, number = givenNum)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=443, ssl_context=('prime.crt','prime.key'))
    #app.run(host="0.0.0.0", port=80)

