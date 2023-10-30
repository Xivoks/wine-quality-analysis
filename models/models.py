from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class WineData(db.Model):
    __tablename__ = 'wine_data'

    id = db.Column(db.Integer, primary_key=True)
    Class = db.Column(db.Integer)
    alcohol = db.Column(db.Float)
    malic_acid = db.Column(db.Float)
    ash = db.Column(db.Float)
    alcalinity_of_ash = db.Column(db.Float)
    magnesium = db.Column(db.Float)
    total_phenols = db.Column(db.Float)
    flavanoids = db.Column(db.Float)
    nonflavanoid_phenols = db.Column(db.Float)
    proanthocyanins = db.Column(db.Float)
    color_intensity = db.Column(db.Float)
    hue = db.Column(db.Float)
    od280_od315_of_diluted_wines = db.Column(db.Float)
    proline = db.Column(db.Integer)

    def to_dict(self):
        return {
            'Class': self.Class,
            'Alcohol': self.alcohol,
            'Malic_acid': self.malic_acid,
            'Ash': self.ash,
            'Alcalinity_of_ash': self.alcalinity_of_ash,
            'Magnesium': self.magnesium,
            'Total_phenols': self.total_phenols,
            'Flavanoids': self.flavanoids,
            'Nonflavanoid_phenols': self.nonflavanoid_phenols,
            'Proanthocyanins': self.proanthocyanins,
            'Color_intensity': self.color_intensity,
            'Hue': self.hue,
            'OD280_OD315_of_diluted_wines': self.od280_od315_of_diluted_wines,
            'Proline': self.proline
        }
