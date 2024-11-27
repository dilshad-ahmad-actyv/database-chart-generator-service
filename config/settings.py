import os
from dotenv import load_dotenv

load_dotenv()
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
SERVER= os.getenv('SERVER')
DATABASE = os.getenv('DATABASE')

DATABASE_CONFIG = {
    'DRIVER': '{ODBC Driver 17 for SQL Server}',
    'SERVER': 'DILSHAD0194',
    'DATABASE': 'PD11.2.411',
    'Trusted_Connection': 'yes',
    'TrustServerCertificate': 'yes',
}
