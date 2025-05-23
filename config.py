import os
class Config:
    SQLALCHEMY_DATABASE_URI = 'mssql://Adminbd:Admin123*@serversqlazureag.database.windows.net:1433/PeliculasFlask?driver=ODBC+Driver+18+for+SQL+Server&Encrypt=yes'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY = 'tu_clave_secreta_segura_aqui'  # Cambia esto por una clave segura
    OMDB_API_KEY = '52321182'  # Tu API key de OMDb
    OMDB_URL = "https://www.omdbapi.com/"
