import csv
import os

from flask import Flask
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)
post_per_page = 10


class HelloWorld(Resource):
    def get(self, page):  # Being able to access a name variable that is defined
        with open(os.path.join(os.curdir, "templates", "Scrape.csv")) as f:
            file = csv.reader(f, delimiter=',')

            contents = []
            index = 0
            for row in file:
                if row[0] != "Search_Tag":
                    contents.append({
                        "Search_Tag": row[0],
                        "Title": row[1],
                        "Seller_Name": row[4]
                    })
                    index += 1
                if index == post_per_page:
                    break  # don't send to much data at once

        return {"Results": contents}


api.add_resource(HelloWorld, "/api/<int:page>")

if __name__ == "__main__":
    app.run(debug=True)
