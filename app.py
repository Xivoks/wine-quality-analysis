from flask import Flask, jsonify, send_from_directory

from charts import create_plot
from config import DB_CONFIG
from models.models import WineData
from models.models import db

app = Flask(__name__)

app.config[
    'SQLALCHEMY_DATABASE_URI'] = f"mysql+mysqlconnector://{DB_CONFIG['MYSQL_DATABASE_USER']}@{DB_CONFIG['MYSQL_DATABASE_HOST']}/{DB_CONFIG['MYSQL_DATABASE_DB']}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

@app.route('/')
def default_route():
    return "Hello"

@app.route('/get_wine_data', methods=['GET'])
def get_wine_data():
    wine_data = WineData.query.all()
    print(wine_data)
    wine_data_list = []
    for data in wine_data:
        wine_data_list.append({
            'Class': data.Class,
            'Alcohol': data.Alcohol,
            'Malic_acid': data.Malic_acid,
            'Ash': data.Ash,
            'Alcalinity_of_ash': data.Alcalinity_of_ash,
            'Magnesium': data.Magnesium,
            'Total_phenols': data.Total_phenols,
            'Flavanoids': data.Flavanoids,
            'Nonflavanoid_phenols': data.Nonflavanoid_phenols,
            'Proanthocyanins': data.Proanthocyanins,
            'Color_intensity': data.Color_intensity,
            'Hue': data.Hue,
            'OD280_OD315_of_diluted_wines': data.OD280_OD315_of_diluted_wines,
            'Proline': data.Proline
        })

    return jsonify({'wine_data': wine_data_list})

@app.route('/chart1')
def show_chart1():
    chart_filename = create_plot(app)
    return send_from_directory('static', 'chart1.png')

if __name__ == '__main__':
    app.run(debug=True)
