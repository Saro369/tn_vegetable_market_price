from dotenv import load_dotenv
import os
from datetime import datetime
import sys

load_dotenv()

OUTPUT_PATH = os.getenv('OUTPUT_PATH')
DIST = os.getenv('DIST')
BASE_URL = os.getenv('BASE_URL')

# Parse date strings into date objects
START_DATE = datetime.strptime(os.getenv('START_DATE'), '%Y-%m-%d').date()
END_DATE = datetime.strptime(os.getenv('END_DATE'), '%Y-%m-%d').date()
