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

    for n in range(2, ceil(usr_num ** 0.5) + 1) : #Square root of usr_num plus one, rounded up.
        if usr_num % n and n != usr_num :
            return f"{usr_num} is not a prime number, {n} is a factor."

    return f"{usr_num} is a prime number."

# Discovers all factors of given number.
@app.route("/api/slack/findFactors", methods=['POST'])
def apiSlack_findFactors () :
    usr_num = request.values.get('text')
    usr_num = int(usr_num)
    usr_numFactors = []

    for n in range(2, ceil((usr_num / 2) + 2)) : #Two more then half of usr_num, rounded up.
        if usr_num % n == 0 and n != usr_num :
            usr_numFactors.append(n)
    
    if len(usr_numFactors) == 0 :
        return f"{usr_num} is a prime number and as such, has no distinct factors."
    else :
        usr_numFactors_str = "" 
        for j in range(len(usr_numFactors)) :
            if j == len(usr_numFactors) - 1 :
                usr_numFactors_str = usr_numFactors_str + str(usr_numFactors[j])
                break
            usr_numFactors_str = usr_numFactors_str + str(usr_numFactors[j]) + ", "

        return f"{usr_num} has the distinct factors of {usr_numFactors_str}."

if __name__ == '__main__' :
    # Start the web server!
    app.run()