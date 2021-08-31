import json
from dotenv import load_dotenv
from flask import Flask, request, Response, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from sqlalchemy import desc

from vennapp.import_db import get_data
from vennapp.model import db, ma, Record, records_schema
import click

load_dotenv()
app = Flask(__name__)
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///sqlite3.db'
db.init_app(app)
ma.init_app(app)

#get data from public api and store in te db - should run just once
@click.command(name='load-db')
def load_db():
    with app.app_context():
        get_data()


#initilize the db - should run just once
@click.command(name='create-db')
def create_db():
    with app.app_context():
        db.create_all()
        get_data()


with app.app_context():
    app.cli.add_command(load_db)
    app.cli.add_command(create_db)

#Api endpoint to get the records
@app.route("/")
def index():
    args = request.args
    q = Record.query
    if args.get("min2000"):
        q = q.filter(Record.total_population_2000_number >= args["min2000"])
    if args.get("max2000"):
        q = q.filter(Record.total_population_2000_number <= args["max2000"])
    if args.get("min2010"):
        q = q.filter(Record.total_population_2010_number >= args["min2010"])
    if args.get("max2010"):
        q = q.filter(Record.total_population_2010_number <= args["max2010"])
    if args.get("min_total_change"):
        q = q.filter(Record.total_population_change_2000_2010_number >= args["min_total_change"])
    if args.get("max_total_change"):
        q = q.filter(Record.total_population_change_2000_2010_number <= args["max_total_change"])
    if args.get("min_percent_change"):
        q = q.filter(Record.total_population_change_2000_2010_percent >= args["min_percent_change"])
    if args.get("max_percent_change"):
        q = q.filter(Record.total_population_change_2000_2010_percent >= args["max_percent_change"])
    q = q.order_by(desc("our_rate")).limit(30)
    return jsonify(records_schema.dump(q))


if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)
