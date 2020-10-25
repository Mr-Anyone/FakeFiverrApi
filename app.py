import csv
import os
from flask import Flask, send_file
from flask_restful import Api, Resource
import urllib.parse

app = Flask(__name__)
api = Api(app)
post_per_page = 10

domain = "https://2cd60989f482.ngrok.io"


class PageContent(Resource):
    def get(self, page):  # Being able to access a name variable that is defined
        with open(os.path.join(os.curdir, "templates", "Scrape.csv")) as f:
            file = csv.reader(f, delimiter=',')

            contents = []
            index = 0
            for row in file:
                if row[0] != "Search Tag" and index >= ((page-1)*post_per_page) and index <= (page*post_per_page -1):
                    contents.append({
                        "Search_Tag": row[0],
                        "Title": row[1],
                        "Seller_Name": row[4],
                        "Gig_Picture" : f"{domain}/get_image/{urllib.parse.quote(row[1]+ ' 0 ' +row[4]+ '.png')}",
                        "Seler_Picure" : f"{domain}/get_image/{urllib.parse.quote(row[4]+'.png')}",
                    })
                index += 1

                if index > page*post_per_page -1:
                    break

        return {"Results": contents}

@app.route('/get_image/<filename>')
def get_image(filename):
    # This would reutrn the image
    if filename:
        return send_file(os.path.join(os.curdir, "templates", "Images", filename), mimetype="image/png")
    else:
        return "ERROR"



api.add_resource(PageContent, "/api/<int:page>")

if __name__ == "__main__":
    app.run(debug=True)
