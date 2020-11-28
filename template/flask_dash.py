import flask
import plotly.express as px
import pandas as pd
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd
from werkzeug.middleware.dispatcher import DispatcherMiddleware
import flask
from werkzeug.serving import run_simple

app = flask.Flask(__name__)
dash_app = dash.Dash(__name__, server=app, url_base_pathname='/plots/')
dash_app.layout = html.Div()


@app.route('/')
@app.route('/hello')
def hello():
    return 'hello world!'


@app.route('/plots/')
def render_reports():
    """
    Redirect to dosh route for visualization.
    :return:
    """
    get_plot()
    return flask.redirect('/dash_plot')


app_embeds = DispatcherMiddleware(app, {
    '/dash_plot': dash_app.server
})


def get_plot():

    path1 = "./STRG1.csv"
    df1 = pd.read_csv(path1)
    fig1 = px.line(df1, x='date', y='pnl', title='PNL with data1')

    path2 = "STRG2.csv"
    df = pd.read_csv(path2)
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

    dash_app.layout = html.Div(children=[
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


def main():
    get_plot()
    run_simple('0.0.0.0', 5000, app_embeds, use_reloader=True, use_debugger=True)


if __name__ == "__main__":
    main()