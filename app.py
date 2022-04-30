from flask import Flask, render_template, redirect, url_for
import pandas as pd

app = Flask(__name__)

def readingData():
    myData1 = pd.read_csv('images.csv')
    myData2 = pd.read_csv('styles.csv')
    # print(myData2.iloc[0])
    return myData1.link,myData2

@app.route('/')
def landing():
    return render_template('index.html')

products,metaData = readingData()

@app.route('/home')
def home():
    return render_template('home.html', products=products,metaData=metaData)

arr = [-1]
@app.route('/image/<id>')
def image(id):
    arr[0] = id
    return redirect("/product")

@app.route("/product")
def product():
    prod = products[int(arr[0])-1]
    data = metaData.iloc[int(arr[0])-1]
    # print(products[int(arr[0])-1])
    # print(data)
    return render_template('product.html', product=prod,metaData=data)

app.run(host='0.0.0.0', port=3000, debug=True)
