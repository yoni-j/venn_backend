from sodapy import Socrata
from vennapp.model import db, Record

client = Socrata("data.cityofnewyork.us", None)

def get_data():
    results = client.get("rnsn-acs2", limit=1000)
    for record in results:
        new_record = Record(**record)
        new_record.our_rate = new_record.set_rate()
        db.session.add(new_record)
        db.session.commit()

