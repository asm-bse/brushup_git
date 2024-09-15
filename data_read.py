import gspread
from gspread_dataframe import get_as_dataframe
from google.colab import auth
from oauth2client.client import GoogleCredentials
from google.auth import default
import pandas as pd

# Authenticate and create a client
auth.authenticate_user()
creds, _ = default()
gc = gspread.authorize(creds)