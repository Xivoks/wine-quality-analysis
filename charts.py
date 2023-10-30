import matplotlib.pyplot as plt
from models.models import WineData

def create_plot(app):
    with app.app_context():
        wine_data = WineData.query.all()
        alcohol_means = [[] for _ in range(3)]

        for data in wine_data:
            class_idx = int(round(data.Class)) - 1
            alcohol_means[class_idx].append(data.alcohol)

        class_labels = ['Class 1', 'Class 2', 'Class 3']
        means = [sum(alcohol) / len(alcohol) for alcohol in alcohol_means]

        plt.figure(figsize=(8, 6))
        plt.bar(class_labels, means, color=['r', 'g', 'b'])
        plt.xlabel('Klasa Wina')
        plt.ylabel('Średnia Zawartość Alkoholu')
        plt.title('Średnia Zawartość Alkoholu w Poszczególnych Klasach Wina')

        chart_filename = 'static/images/chart1.png'
        plt.savefig(chart_filename)

    return chart_filename
