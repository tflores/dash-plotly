import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

import dash
from dash import dcc, html
from dash.dependencies import Input, Output

app = dash.Dash(__name__)

url = 'https://sistemas.anac.gov.br/dadosabertos/Aeronaves/drones%20cadastrados/SISANT.csv'
df = pd.read_csv(url, sep=';', encoding='cp1252', skiprows=1)
print(df.head())