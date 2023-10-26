import csv
from sqlalchemy import create_engine, text


csv_file = "wine_data.csv"

def import_data_from_csv():

    with open(csv_file, 'r') as file:
        reader = csv.DictReader(file)
        data = list(reader)

    conn = engine.connect()
    transaction = conn.begin()

    try:
        insert_query = text(
            "INSERT INTO wine_table (column1, column2, ...) VALUES (:value1, :value2, ...)"
        )

        for row in data:
            conn.execute(insert_query, **row)

        transaction.commit()
        print("Dane zaimportowane pomyślnie.")

    except Exception as e:
        print(f"Błąd podczas importu danych: {str(e)}")
        transaction.rollback()
    finally:
        conn.close()


import_data_from_csv()
