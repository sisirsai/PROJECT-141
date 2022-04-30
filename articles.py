from flask import Flask,jsonify,request
import csv

all_articles = []

with open('articles.csv',encoding = 'UTF-8') as f:
    reader = csv.reader(f)
    data = list(reader)
    all_articles = data[1:]

like_articles = []
dislike_articles = []

app = Flask(__name__)

@app.route('/get-article')

def get_articles():
    return jsonify({
        'data' : all_articles[0],
        'status' : 'success'
    }),200

@app.route('/like-article',methods = ['POST'])

def like_articles():
    article = all_articles[0]
    all_articles = all_articles[1:]
    like_articles.append(article)
    return jsonify({
        'status' : 'success'
    }),200

@app.route('/dislike-article',methods = ['POST'])

def dislike_articles():
    article = all_articles[0]
    all_articles = all_articles[1:]
    dislike_articles.append(article)
    return jsonify({
        'status' : 'success'
    }),200

if __name__ == '__main__':
    app.run()