import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

from models.models import WineData

AVG_ALCOHOL_CHART_PATH = 'static/images/chart1.png'
CORRELATION_MATRIX_PATH = 'static/images/correlation_matrix.png'


def fetch_wine_data():
    return WineData.query.all()


def create_avg_alcohol_by_class_plot(app):
    with app.app_context():
        wine_data = fetch_wine_data()
        alcohol_means = [[] for _ in range(3)]

        for data in wine_data:
            class_idx = int(round(data.Class)) - 1
            alcohol_means[class_idx].append(data.alcohol)

        means = [sum(alcohol) / len(alcohol) for alcohol in alcohol_means]

        plt.figure(figsize=(8, 6))
        plt.bar(['Class 1', 'Class 2', 'Class 3'], means, color=['r', 'g', 'b'])
        plt.xlabel('Klasa Wina')
        plt.ylabel('Średnia Zawartość Alkoholu')
        plt.title('Średnia Zawartość Alkoholu w Poszczególnych Klasach Wina')
        plt.savefig(AVG_ALCOHOL_CHART_PATH)

    return AVG_ALCOHOL_CHART_PATH


def create_correlation_chart(app):
    with app.app_context():
        wine_data = WineData.query.all()

        df = pd.DataFrame([(data.Class, data.alcohol, data.malic_acid, data.ash, data.alcalinity_of_ash, data.magnesium,
                            data.total_phenols, data.flavanoids, data.nonflavanoid_phenols, data.proanthocyanins,
                            data.color_intensity, data.hue, data.od280_od315_of_diluted_wines, data.proline)
                           for data in wine_data],
                          columns=['Class', 'Alcohol', 'Malic_acid', 'Ash', 'Alcalinity_of_ash', 'Magnesium',
                                   'Total_phenols', 'Flavanoids', 'Nonflavanoid_phenols', 'Proanthocyanins',
                                   'Color_intensity', 'Hue', 'OD280_OD315_of_diluted_wines', 'Proline'])

        correlation_matrix = df.corr()

        correlation_matrix = correlation_matrix.round(2)

        mask = np.triu(np.ones_like(correlation_matrix, dtype=bool))

        plt.figure(figsize=(12, 10))

        cmap = sns.diverging_palette(240, 10, as_cmap=True)  # Paleta kolorów od niebieskiego do czerwonego

        sns.heatmap(correlation_matrix, annot=True, cmap=cmap, linewidths=0.5, mask=mask)

        plt.title('Macierz Korelacji Właściwości Wina', fontsize=16)
        plt.xticks(fontsize=12)
        plt.yticks(fontsize=12)

        plt.tight_layout()
        plt.savefig(CORRELATION_MATRIX_PATH)

    return CORRELATION_MATRIX_PATH
