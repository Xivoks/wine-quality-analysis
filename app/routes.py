from app import app

@app.route('/')
def index():
    return 'Welcome, this is the main page!'

@app.route('/data_analysis', methods=['GET'])
def data_analysis():
    return 'This is data analysis!'
