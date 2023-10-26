from flask import Flask
import requests


app = Flask(__name__)


@app.route("/members")

def members():

    url = 'https://restcountries.com/v3.1/name/colombia?fullText=true'

    col = requests.get(url)

    return col.json()

if __name__ == '__main__':
    
    
    app.run(debug=True)


