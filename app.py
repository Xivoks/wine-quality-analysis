from flask import Flask, jsonify, send_from_directory
from config import DB_CONFIG
from models.models import WineData, db
import charts

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql+mysqlconnector://{DB_CONFIG['MYSQL_DATABASE_USER']}@{DB_CONFIG['MYSQL_DATABASE_HOST']}/{DB_CONFIG['MYSQL_DATABASE_DB']}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

@app.route('/')
def default_route():
    return "Hello"

@app.route('/get_wine_data', methods=['GET'])
def get_wine_data():
    wine_data = WineData.query.all()
    wine_data_list = [data.to_dict() for data in wine_data]
    return jsonify({'wine_data': wine_data_list})

@app.route('/average_alcohol_chart')
def average_alcohol_chart():
    chart_filename = charts.create_plot(app)
    return send_from_directory('static', 'images/chart1.png')

if __name__ == '__main__':
    app.run(debug=True)
