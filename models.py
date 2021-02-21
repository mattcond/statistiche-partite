from peewee import *
import mysql.connector


db = MySQLDatabase('statistiche_partite', 
                   user='scraper', 
                   password='scraper',
                   host='127.0.0.1', 
                   port=3306)

def close_connection():
    db.close()

class statistichePartite(Model):
    class Meta:
        database = db


class Campionato(statistichePartite):
    id = AutoField()
    nome = TextField()
    

class Giornata(statistichePartite):
    id = AutoField()
    squadra = TextField()
    posizione = IntegerField()
    punti = IntegerField()
    
    totale_giocate = IntegerField()
    totale_vinte = IntegerField()
    totale_pareggiate = IntegerField()
    totale_perse = IntegerField()
    totale_gol_fatti = IntegerField()
    totale_gol_subiti = IntegerField()
    
    casa_giocate = IntegerField()
    casa_vinte = IntegerField()
    casa_pareggiate = IntegerField()
    casa_perse = IntegerField()
    casa_gol_fatti = IntegerField()
    casa_gol_subiti = IntegerField()
    
    trasferta_giocate = IntegerField()
    trasferta_vinte = IntegerField()
    trasferta_pareggiate = IntegerField()
    trasferta_perse = IntegerField()
    trasferta_gol_fatti = IntegerField()
    trasferta_gol_subiti = IntegerField()
    
    campionato = TextField()#ForeignKeyField(Campionato)
    data_aggiornamento = CharField(max_length = 10)
    url = TextField()
    
class Statistiche(statistichePartite):
    id = AutoField()
    campionato = TextField()
    squadra = TextField()
    performance = DoubleField()
    evento = CharField(max_length = 255)
    data_aggiornamento = CharField(max_length = 10)
    data_run = CharField(max_length = 19)

class Risultati(statistichePartite):
    id = BigAutoField()
    data = CharField(max_length = 10)
    campionato = TextField()
    
    squadra_casa = TextField(null = True)
    squadra_trasferta = TextField(null = True)

    risultato_casa = IntegerField()
    risultato_trasferta = IntegerField()
    
    risultato_pt_casa = IntegerField()
    risultato_pt_trasferta = IntegerField()
    
    data_run = CharField(max_length = 19)
