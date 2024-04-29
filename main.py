from flask import Flask, jsonify, request
import pandas as pd

articles_data = pd.read_csv('articles.csv')
all_articles = articles_data[['url' , 'title' , 'text' , 'lang' , 'total_events']]
liked_articles = []
not_liked_articles = []

app = Flask(__name__)

def assign_val():
    m_data = {
        "url": all_articles.iloc[0,0],
        "title": all_articles.iloc[0,1],
        "text": all_articles.iloc[0,2] or "N/A",
        "lang": all_articles.iloc[0,3],
        "total_events": all_articles.iloc[0,4]
    }
    return m_data

# API to display first article
@app.route("/get-article",methods = ["GET"])
def get_article():
  articles_data = assign_val()
  return jsonify({
    "data":all_articles,
    "status":"success"
    
    })

    


# API to move the article into liked articles list
@app.route("/liked-article",methods = ["POST"])
def liked_article():
    liked_articles.drop([0],inplace=True)
    liked_articles = liked_articles.reset_index(drop=True)

    return jsonify({
        "status":"success"

    })


# # API to move the article into not liked articles list
@app.route("/unliked-article",methods = ["POST"])
def unliked_article():
    not_liked_articles.drop([0],inplace=True)
    not_liked_articles = not_liked_articles.reset_index(drop=True)

    return jsonify({
        "status":"success"

    })


# run the application
if __name__ == "__main__":
    app.run()