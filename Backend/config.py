import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    DB_USER = os.getenv('POSTGRES_USER', 'neurouser')
    DB_PASSWORD = os.getenv('POSTGRES_PASSWORD', 'Rtl8139$')
    DB_HOST = os.getenv('POSTGRES_HOST', 'db')  # Si el backend está en un contenedor, usa 'db'
    DB_PORT = os.getenv('POSTGRES_PORT', '5432')  # Leer el puerto de PostgreSQL
    DB_NAME = os.getenv('POSTGRES_DB', 'neuroattend')
   
    # print ("User :", DB_USER)
    # print ("Pas :", DB_PASSWORD)
    # print ("hOST :",DB_HOST)
    # print ("PORT :", DB_PORT)
    # print ("DB :", DB_NAME)

    # Construir la URL de conexión
    SQLALCHEMY_DATABASE_URI = f'postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}'
    #SQLALCHEMY_DATABASE_URI = f'postgresql://{DB_USER}:{DB_PASSWORD}@db/{DB_NAME}'
    #SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'postgresql://usuario:contraseña@localhost/bd_asistencia')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.getenv('SECRET_KEY', 'una_clave_secreta_muy_segura')