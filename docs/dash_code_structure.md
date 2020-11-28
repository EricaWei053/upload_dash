
## What my dash code should look like? 

#### 1. Please follow the code structure of this if you only use dash: 

At the top of your code please include those two lines, 
the optional arguments are allowed to put as your preference. 
```
app = dash.Dash(__name__, optional)
app.layout = html.Div()
```

At the bottom of your code pleas make sure use these two lines to start dash application. 
```
if __name__ == '__main__':
    app.run_server(debug=True)
```
You should be able to add any components in the layout and add data you want to display. 
There is an example file provided to give an idea about the code. 
```
Example file: /template/only_dash.py 
```


#### 2. If you want to embed dash to flask, please look at this: 
Make sure you import those three lines in the file, 
werkzeug is the middleware we need to use combine dash and flask apps. 
``` 
import flask
from werkzeug.middleware.dispatcher import DispatcherMiddleware
from werkzeug.serving import run_simple
```
Here we need to embed dash app into flask app. 
At top of your code please include those two lines, 
the optional arguments are allowed to put as your preference. 

```
app = flask.Flask(__name__)
dash_app = dash.Dash(__name__, server=app, url_base_pathname='/plots/', optional)
dash_app.layout = html.Div()
```

For the different route you want to add on flask, it will be the same as original flask app: 
```
@app.route('/hello')
def hello():
    return 'hello world!'

```

For the dash route on flask, you need to first embed them and get a new app, 
which including both dash and flask, here we name it as app_embeds, 
also define the route of dash in the embed app. 
```
app_embeds = DispatcherMiddleware(app, {
    '/dash_plot': dash_app.server
})
```
Then you can redirect flask route to dash route: 
```
@app.route('/plots/')
def render_reports():
    """
    Redirect to dosh route for visualization.
    :return:
    """
    return flask.redirect('/dash_plot')
```

At bottom of your code pleas make sure use these two lines to start embedding application, 
we use run_simple function here.  
```
if __name__ == "__main__":
    run_simple('0.0.0.0', 5000, app_embeds, use_reloader=True, use_debugger=True)
```

You should be able to add any components in the layout and add data you want to display. 
There is an example file provided to give an idea about the code. 
```
Example file: /template/only_dash.py 
```
 

#### dash.testing will be added later here. 