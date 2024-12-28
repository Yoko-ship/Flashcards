from dotenv import load_dotenv
import os
import psycopg2
import random
load_dotenv()
class DB:
    def __init__(self):
        self.host = os.getenv("host")
        self.password = os.getenv("password")
        self.user = os.getenv("user")
        self.db = os.getenv("db_name")
        self.port = os.getenv("port")

    def set_up(self):
        connect = psycopg2.connect(database=self.db,user=self.user,password=self.password,port=self.port)
        self.cursor = connect.cursor()
        connect.autocommit = True
        self.connection()


    def connection(self):
        query = """
        CREATE TABLE IF NOT EXISTS cards(
        ID SERIAL PRIMARY KEY,
        word VARCHAR NOT NULL,
        translated_word VARCHAR NOT NULL,
        month VARCHAR NOT NULL
        )"""
        self.cursor.execute(query)


    def add_to_db(self,word,translated_word,month):
        query = "INSERT INTO cards(word,translated_word,month) VALUES(%s,%s,%s)"
        self.cursor.execute(query,[word,translated_word,month])

    def show_words(self):
        query = "SELECT word,translated_word FROM cards"
        self.cursor.execute(query)
        information = self.cursor.fetchall()
        hashed_list = dict(information)
        return hashed_list


    def give_random(self):
        query = "SELECT word, translated_word FROM cards"
        self.cursor.execute(query)
        all_words = dict(self.cursor.fetchall())
        result = []
        while len(result) < 2 :
            true_random_key = random.choice(list(all_words.keys()))
            true_values = all_words[true_random_key]
            new = random.choice(list(all_words.values()))
            result.append(new)
        
        return true_random_key,true_values,result
    
    def get_for_graph(self,month):
        query = "SELECT word FROM cards WHERE month = %s"
        self.cursor.execute(query,[month])
        info = self.cursor.fetchall()
        return info