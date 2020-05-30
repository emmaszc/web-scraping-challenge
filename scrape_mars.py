from flask import Flask, render_template
import pymongo

app = Flask(__name__)

conn = 'mongodb://localhost:5000'

client = pymongo.MongoClient(conn)

# Set route
@app.route('/scrape')
def scrape():
    # Store the entire team collection in a list
    teams = list(db.team.find())
    print(teams)

    # Return the template with the teams list passed in
    return render_template('index.html', teams=teams)


if __name__ == "__main__":
    app.run(debug=True)