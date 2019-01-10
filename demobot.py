# Import flask
from flask import Flask, request
from math import ceil

# Create your app (web server)
app = Flask(__name__)

# Judges if a given number is prime
@app.route("/api/slack/isPrime", methods=['POST'])
def apiSlack_isPrime () :
    usr_num = request.values.get('text')
    usr_num = int(usr_num)

    for n in range(2, ceil(usr_num ** 0.5)) : #Square root of usr_num.
        if usr_num % n == 0 :
            return f"{usr_num} is not a prime number, {n} is a factor."

    return f"{usr_num} is a prime number."

# Discovers all factors of given number.
def apiSlack_findFactors () :
    usr_num = request.values.get('text')
    usr_num = int(usr_num)
    usr_numFactors = []

    for n in range(2, ceil(usr_num ** 0.5)) : #Square root of usr_num.
        if usr_num % n == 0 :
            usr_numFactors.append(n)
    
    if len(usr_numFactors) == 0 :
        return f"{usr_num} is a prime number."
    else :
        return f"{usr_num} has the factors {usr_numFactors}."

if __name__ == '__main__' :
    # Start the web server!
    app.run()