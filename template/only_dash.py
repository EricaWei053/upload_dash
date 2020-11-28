import flask
import plotly.express as px
import pandas as pd
import dash_bootstrap_components as dbc
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd


app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
app.layout = html.Div()


def plot():
    path1 = "./data/STRG1.csv"
    df1 = pd.read_csv(path1)
    fig1 = px.line(df1, x='date', y='pnl', title='PNL with data1')

    path = "./data/STRG2.csv"
    df = pd.read_csv(path)
    fig = px.line(df, x='date', y='pnl', title='PNL with data1')

    fig.update_xaxes(
        rangeslider_visible=True,
        rangeselector=dict(
            buttons=list([
                dict(count=1, label="1m", step="month", stepmode="backward"),
                dict(count=6, label="6m", step="month", stepmode="backward"),
                dict(count=1, label="YTD", step="year", stepmode="todate"),
                dict(count=1, label="1y", step="year", stepmode="backward"),
                dict(step="all")
            ])
        )
    )

    fig1.update_xaxes(
        rangeslider_visible=True,
        rangeselector=dict(
            buttons=list([
                dict(count=1, label="1m", step="month", stepmode="backward"),
                dict(count=6, label="6m", step="month", stepmode="backward"),
                dict(count=1, label="YTD", step="year", stepmode="todate"),
                dict(count=1, label="1y", step="year", stepmode="backward"),
                dict(step="all")
            ])
        )
    )

    app.layout = html.Div(children=[
        # All elements from the top of the page
        html.Div([
            html.Div([
                html.H1(children='Hello Dash'),

                html.Div(children='''
                    PnL for data1
                '''),

                dcc.Graph(
                    id='graph1',
                    figure=fig
                ),
            ], className='six columns'),

            
            html.Div([
                html.H1(children='Hello Dash'),

                html.Div(children='''
                    PnL for data2 
                '''),

                dcc.Graph(
                    id='graph2',
                    figure=fig1
                ),
            ], className='six columns'),
        ], className='row'),

    ])

if __name__ == '__main__':
    plot()
    app.run_server(debug=True)

