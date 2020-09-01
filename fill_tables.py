import pandas as pd
import psycopg2
import datetime

connection = psycopg2.connect(user = "postgres", password= "666333", host = "127.0.0.1", port = "5432", database = "project9")

url = "https://raw.githubusercontent.com/barmej/data-science-project-7/master/IMDB_Dataset.csv"
data = pd.read_csv(url)
data.index.name = 'index'

cursor = connection.cursor()


for i in range(len(data)):
        sentiment = data['sentiment'][i]
        review = data['review'][i]
        label_id = 0 if sentiment=='negative' else 1 if sentiment=='positive' else 2
        cursor.execute("INSERT INTO data_input (id , review , date) values (%s ,%s, %s)" , (i , review , datetime.datetime.now() ))
        cursor.execute("INSERT INTO data_labeling (review_id , label_id , timestamp) values (%s ,%s, %s)" , (i , label_id , datetime.datetime.now() ))



connection.commit()
cursor.close()
connection.close()
