"""
THe idea is that each field has rate and high, and low values. field with higher rate gives the neighborhood more points in the total calc.
For example  - a neighborhood with total population of 55000 in year 2000 will get 6 points for that (the high level is 3 points * rate is 2 points),
another neighborhood with total population of 10000 in year 2000 will get for that 2 points (low level is 1 point * rate is 2 points)
a neighborhood with total population change percent between 2000-2010 of 25% will get 15 points (high level is 1 point * rate is 3 points),
"""

business_logic_schema = {
    "total_population_2000_number": {
        "high": 50000,
        "low": 5000,
        "mid": 25000,
        "rate": 2
    },
    "total_population_2010_number": {
        "high": 65000,
        "low": 9000,
        "mid": 30000,
        "rate": 3
    },
    "total_population_change_2000_2010_number": {
        "high": 20000,
        "low": 1000,
        "mid": 8000,
        "rate": 4
    },
    "total_population_change_2000_2010_percent": {
        "high": 20,
        "low": 3,
        "mid": 9,
        "rate": 5
    },
}


class BusinessLogic:
    def __init__(self, record):
        self.record = record

    def calc_rate(self):
        total = 0
        for key in business_logic_schema.keys():
            attr = getattr(self.record, key)
            if attr:
                attr = float(attr)
                if attr >= business_logic_schema[key]["low"]:
                    total += business_logic_schema[key]["rate"]
                if attr >= business_logic_schema[key]["mid"]:
                    total += business_logic_schema[key]["rate"]
                if attr >= business_logic_schema[key]["high"]:
                    total += business_logic_schema[key]["rate"]
        return total
