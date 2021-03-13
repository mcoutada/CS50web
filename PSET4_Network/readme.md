See this tutorial to understand how react is implemented in the frontend (videos 1, 2 and 3)

# Django & React Tutorial #1 - Full Stack Web App With Python & JavaScript
  
[https://www.youtube.com/watch?v=JD-age0BPVo&list=RDCMUC4JX40jDee_tINbkjycV4Sg](https://www.youtube.com/watch?v=JD-age0BPVo&list=RDCMUC4JX40jDee_tINbkjycV4Sg)
  
### Some commands used in the Tutorial### 
pip install djangorestframework
django-admin startproject music_controller
cd music_controller
django-admin startapp api
python manage.py makemigrations
python manage.py migrate
python manage.py runserver


The steps below are the adaptation of the 3rd video.

Download and unzip Network base code:
https://cs50.harvard.edu/web/2020/projects/4/network/#getting-started

### make the initial setup to the db and admin
cd C:\PSET4_Network\project4
python manage.py makemigrations
python manage.py migrate

### Create a Django app called frontend
cd C:\PSET4_Network\project4
django-admin startapp frontend

### Move the templates folder from the network app to frontend
move templates
from
C:\PSET4_Network\project4\network
to
C:\PSET4_Network\project4\frontend

### Move static folder from network to frontend. Create css, frontend and images folders inside of it. Move styles.css inside the css folder 
move static
from
C:\PSET4_Network\project4\network
to
C:\PSET4_Network\project4\frontend

Create 3 folders inside "static", called "css" and "frontend" and "images"

move styles.css
from
C:\PSET4_Network\project4\frontend\static\network
to
C:\PSET4_Network\project4\frontend\static\css

Delete the network folder that was originally inside the static folder
C:\PSET4_Network\project4\frontend\static\network

### Copy views.py from network to frontend views.py
copy views.py
from
C:\PSET4_Network\project4\network
to
C:\PSET4_Network\project4\frontend

### Erase the network views.py content and just leave the index function
```
from django.shortcuts import render

def index(request):
    return render(request, "network/index.html")
```

### On views.py in frontend set ".models" to "network.models"
On views.py. Located at
C:\PSET4_Network\project4\frontend
change line 7 from
from .models import User
to
from network.models import User

### Create a urls.py for frontend, copy everything from urls.py from Network to urls.py on frontend
Copy urls.py
from
C:\PSET4_Network\project4\network
to
C:\PSET4_Network\project4\frontend
it should have this content:
```
from django.urls import include, path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
]
```


### Leave only path(“”, views.index, name=“index”), on urls.py from network.
Open urls.py
located at:
C:\PSET4_Network\project4\network
Erase the needed to match this content:
```
from django.urls import path

from . import views

urlpatterns = [path("", views.index, name="index")]
```

### Create folders src and src/components inside frontend
create folders
C:\PSET4_Network\project4\frontend\src
and
C:\PSET4_Network\project4\frontend\src\components

### run the following commands in frontend
cd C:\PSET4_Network\project4\frontend
npm init -y
npm i webpack webpack-cli --save-dev
npm i @babel/core babel-loader @babel/preset-env @babel/preset-react --save-dev
:: (we are not going to use material-ui so no need to run "npm install @material-ui/core")
npm i react react-dom --save-dev
npm install @babel/plugin-proposal-class-properties
npm install react-router-dom
:: (no need to tun "npm install @material-ui/icons" either)

### create babel.config.json inside frontend
create a file called
babel.config.json
inside
C:\PSET4_Network\project4\frontend
with this content:
```
{
    "presets": [
        [
            "@babel/preset-env",
            {
                "targets": {
                    "node": "10"
                }
            }
        ],
        "@babel/preset-react"
    ],
    "plugins": ["@babel/plugin-proposal-class-properties"]
}
```

### create webpack.config.json inside frontend
create a file called
webpack.config.json
inside
C:\PSET4_Network\project4\frontend
```
const path = require("path");
const webpack = require("webpack");

module.exports = {
    entry: "./src/index.js",
    output: {
        path: path.resolve(__dirname, "./static/frontend"),
        filename: "[name].js",
    },
    module: {
        rules: [
            {
                test: /\.js$/,
                exclude: /node_modules/,
                use: {
                    loader: "babel-loader",
                    options: {
                        presets: ["@babel/react"],
                    },
                },
            },
        ],
    },
    optimization: {
        minimize: true,
    },
    plugins: [
        new webpack.DefinePlugin({
            "process.env": {
                // This has effect on the react lib size
                NODE_ENV: JSON.stringify("production"),
            },
        }),
    ],
};
```
(I needed to add this line
'presets: ["@babel/react"]'
in order for this code to work as the original from the tutorial was causing me errors)
original:
https://github.com/techwithtim/Music-Controller-Web-App-Tutorial/blob/main/Tutorial%201%20-%204/frontend/webpack.config.js


### Replace the scripts tag in package.json
Open C:\PSET4_Network\project4\frontend\package.json
Change "scripts":
from:
```
  "scripts": {
    "test": "echo \"Error: no test specified\" && exit 1"
  },
```

to:
```
  "scripts": {
    "dev": "webpack --mode development --watch",
    "build": "webpack --mode production",
    "test": "echo \"Error: no test specified\" && exit 1"
  },
```


### We are going to create a simple App to display a Hello World message. Create App.js inside frontend\src\components
Create
Apps.js
in
C:\PSET4_Network\project4\frontend\src\components
```
import React from 'react';

const Apps = () => {
    return (
        <div>
            <h1>Hello World</h1>
        </div>
    )
}

export default Apps
```

### Create the file index.js inside project4\frontend\src
Create
index.js
in
C:\PSET4_Network\project4\frontend\src
```
import React from 'react';
import ReactDOM from 'react-dom';
import App from './components/App'

const AppDiv = document.getElementById('app');
ReactDOM.render(<div><App/></div>, AppDiv);
```

### add a div with id=main, and a script html tag for main.js before closing the body tag in layout.html
Add
    <div id="app"></div>
    <script src="{% static "frontend/main.js" %}"></script>
before
    </body>
in
C:\Users\asd\Desktop\tests\CS50Web\mygithub\PSET4_Network\project4\frontend\templates\network\layout.html
Last part of layout.html should look like this:
```
        <div class="body">
            {% block body %}
            {% endblock %}
        </div>
    </div>
    <div id="app"></div>
    <script src="{% static "frontend/main.js" %}"></script>
</body></html>
```

### change the styles.css path at the top of layout.html
Open layout.html
located at
C:\Users\asd\Desktop\tests\CS50Web\mygithub\PSET4_Network\project4\frontend\templates\network
On line 8, change this:
        <link href="{% static 'network/styles.css' %}" rel="stylesheet">
To this:
        <link href="{% static 'css/styles.css' %}" rel="stylesheet">

### On the main urls.py located at project4\project4. Add path("", include("frontend.urls")) to urlpatterns
Open urls.py in
C:\PSET4_Network\project4\project4\
Edit urlpatterns (lines 19 to 23) to match this content:
```
urlpatterns = [
    path("admin/", admin.site.urls),
    # path("", include("network.urls")),
    path("", include("frontend.urls")),
]
```

### Add frontend.apps.FrontendConfig to INSTALLED_APPS in project4\project4\settings.py
open settings.py in
C:\PSET4_Network\project4\project4
Add
'frontend.apps.FrontendConfig'
at the end of INSTALLED_APPS
```
INSTALLED_APPS = [
    'network',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'frontend.apps.FrontendConfig'
]
```

### Run the backend and the frontend to see if you can render the Hello World message:
Open a Terminal and run:
cd C:\PSET4_Network\project4
python manage.py runserver

Open another Terminal and run:
cd C:\PSET4_Network\project4\frontend
npm run dev
Open
http://localhost:8000/

Everything should look like in this repository up to this commit
https://github.com/mcoutada/CS50web/tree/ee559432fabdb58d5b388aad12b1e16e795a388e

### Now that everything works let's undo the Hello World App. And Create the Home and Register Apps.

### Erase div="app" in layout.html
Open layout.html in
C:\PSET4_Network\project4\frontend\templates\network
Erase line 49:
<div id="app"></div>

### Delete App.js
Located at
C:\PSET4_Network\project4\frontend\src\components\App.js


### Create Home.js and Register.js in components (use the rafce shortcut to create an arrow function inside), return a simple message

C:\PSET4_Network\project4\frontend\src\components\Home.js
```
import React from 'react'

const Home = () => {
    return (
        <div>
            <h1>Home is working</h1>
        </div>
    )
}

export default Home
```

C:\PSET4_Network\project4\frontend\src\components\Register.js
```
import React from 'react'

const Register = () => {
    return (
        <div>
            <h1>Register is working</h1>
        </div>
    )
}

export default Register
```


### Edit index.js to erase App and render Register and Home
```
import React from "react";
import ReactDOM from "react-dom";
import Register from "./components/Register";

const home = (
    <div>
        <Home />
    </div>
);

const register = (
    <div>
        <Register />
    </div>
);

const rootElement = document.getElementById("index");
if (rootElement) {
    ReactDOM.render(home, rootElement);
}

const registerElement = document.getElementById("index");
if (registerElement) {
    ReactDOM.render(register, registerElement);
}
```


### Edit project4\frontend\templates\network\index.html to add a div with id=index
Open
index.html
located at
C:\PSET4_Network\project4\frontend\templates\network
Add
<div id="index"></div>
inside body
```
{% extends "network/layout.html" %}

{% block body %}
    <div id="index"></div>
{% endblock %}
```


### Edit project4\frontend\templates\network\register.html to add a div with id=register
Open
register.html
located at
C:\PSET4_Network\project4\frontend\templates\network
Add
<div id="register"></div>

The end of the file should look like:
```
    </form>

    Already have an account? <a href="{% url 'login' %}">Log In here.</a>
    <div id="register"></div>
{% endblock %}
```

If everything went well, the messages should appear in
http://localhost:8000/
http://localhost:8000/register