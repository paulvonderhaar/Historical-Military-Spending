import os
import inspect
import pandas as pd
import numpy as np
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from sqlalchemy import inspect
from flask import Flask, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)


#################################################
# Database Setup
#################################################

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db/bellybutton.sqlite"
db = SQLAlchemy(app)

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(db.engine, reflect=True)

#country = db.Table("countries",db.metadata,autoload=True,autoload_with=db.engine)

country = Base.classes.MyCountry

@app.route("/")
def index():
    """Return the homepage."""
    return render_template("index.html")




@app.route("/country/<name>")

def countries(name):
    stmt = db.session.query(country).filter(country.Name==name).all()
    inst = inspect(country)
    MyDict={}
    for result in stmt:
        MyDict['Name'] = result.Name
        MyDict['1960'] = result.one
        MyDict['1961'] = result.two
        MyDict['1962'] = result.three
        MyDict['1963'] = result.four
        MyDict['1964'] = result.five
        MyDict['1965'] = result.six
        MyDict['1966'] = result.seven
        MyDict['1967'] = result.eight
        MyDict['1968'] = result.nine
        MyDict['1969'] = result.ten
        MyDict['1970'] = result.eleven
        MyDict['1971'] = result.twelve
        MyDict['1972'] = result.thirteen
        MyDict['1973'] = result.fourteen
        MyDict['1974'] = result.fifteen
        MyDict['1975'] = result.sixteen
        MyDict['1976'] = result.seventeen
        MyDict['1977'] = result.eighteen
        MyDict['1978'] = result.nineteen
        MyDict['1979'] = result.twenty
        MyDict['1980'] = result.twentyone
        MyDict['1981'] = result.twentytwo
        MyDict['1982'] = result.twentythree
        MyDict['1983'] = result.twentyfour
        MyDict['1984'] = result.twentyfive
        MyDict['1985'] = result.twentysix
        MyDict['1986'] = result.twentyseven
        MyDict['1987'] = result.twentyeight
        MyDict['1988'] = result.twentynine
        MyDict['1989'] = result.thirty
        MyDict['1990'] = result.thirtyone
        MyDict['1991'] = result.thirtytwo
        MyDict['1992'] = result.thirtythree
        MyDict['1993'] = result.thirtyfour
        MyDict['1994'] = result.thirtyfive
        MyDict['1995'] = result.thirtysix
        MyDict['1996'] = result.thirtyseven
        MyDict['1997'] = result.thirtyeight
        MyDict['1998'] = result.thirtynine
        MyDict['1999'] = result.fourty
        MyDict['2000'] = result.fourtyone
        MyDict['2001'] = result.fourtytwo
        MyDict['2002'] = result.fourtythree
        MyDict['2003'] = result.fourtyfour
        MyDict['2004'] = result.fourtyfive
        MyDict['2005'] = result.fourtysix
        MyDict['2006'] = result.fourtyseven
        MyDict['2007'] = result.fourtyeight
        MyDict['2008'] = result.fourtynine
        MyDict['2009'] = result.fifty
        MyDict['2010'] = result.fiftyone
        MyDict['2011'] = result.fiftytwo
        MyDict['2012'] = result.fiftythree
        MyDict['2013'] = result.fiftyfour
        MyDict['2014'] = result.fiftyfive
        MyDict['2015'] = result.fiftysix
        MyDict['2016'] = result.fiftyseven
        MyDict['2017'] = result.fiftyeight
        MyDict['2018'] = result.fiftynine

    return jsonify(MyDict)



if __name__ == "__main__":
    app.run()
