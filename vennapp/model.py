from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from vennapp.business_logic import BusinessLogic

db = SQLAlchemy()
ma = Marshmallow()


class Record(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    geographic_area_borough = db.Column(db.String(80), nullable=True)
    geographic_area_2010_census_fips_county_code = db.Column(db.Integer, nullable=True)
    geographic_area_neighborhood_tabulation_area_nta_code = db.Column(db.String(80), nullable=True)
    geographic_area_neighborhood_tabulation_area_nta_name = db.Column(db.String(80), nullable=True)
    total_population_2000_number = db.Column(db.Integer, nullable=True)
    total_population_2010_number = db.Column(db.Integer, nullable=True)
    total_population_change_2000_2010_number = db.Column(db.Integer, nullable=True)
    total_population_change_2000_2010_percent = db.Column(db.Float, nullable=True)
    our_rate = db.Column(db.Integer, nullable=True)

    def set_rate(self):
        service = BusinessLogic(self)
        return service.calc_rate()



class RecordSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Record


records_schema = RecordSchema(many=True)
