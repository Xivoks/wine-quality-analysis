from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class WineData(db.Model):
    __tablename__ = 'wine_data'

    id = db.Column(db.Integer, primary_key=True)
    Class = db.Column(db.Integer)
    Alcohol = db.Column(db.Float)
    Malic_acid = db.Column(db.Float)
    Ash = db.Column(db.Float)
    Alcalinity_of_ash = db.Column(db.Float)
    Magnesium = db.Column(db.Float)
    Total_phenols = db.Column(db.Float)
    Flavanoids = db.Column(db.Float)
    Nonflavanoid_phenols = db.Column(db.Float)
    Proanthocyanins = db.Column(db.Float)
    Color_intensity = db.Column(db.Float)
    Hue = db.Column(db.Float)
    OD280_OD315_of_diluted_wines = db.Column(db.Float)
    Proline = db.Column(db.Integer)

    def __init__(self, Class, Alcohol, Malic_acid, Ash, Alcalinity_of_ash, Magnesium, Total_phenols, Flavanoids,
                 Nonflavanoid_phenols, Proanthocyanins, Color_intensity, Hue, OD280_OD315_of_diluted_wines,
                 Proline):
        self.Class = Class
        self.Alcohol = Alcohol
        self.Malic_acid = Malic_acid
        self.Ash = Ash
        self.Alcalinity_of_ash = Alcalinity_of_ash
        self.Magnesium = Magnesium
        self.Total_phenols = Total_phenols
        self.Flavanoids = Flavanoids
        self.Nonflavanoid_phenols = Nonflavanoid_phenols
        self.Proanthocyanins = Proanthocyanins
        self.Color_intensity = Color_intensity
        self.Hue = Hue
        self.OD280_OD315_of_diluted_wines = OD280_OD315_of_diluted_wines
        self.Proline = Proline
