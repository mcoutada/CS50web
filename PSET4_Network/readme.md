# Initial setup React/Django for Network exercise <br />
 <br />
See this tutorial to understand how React is implemented in the frontend (videos 1, 2 and 3) <br />
 <br />
## Django & React Tutorial #1 - Full Stack Web App With Python & JavaScript <br />
   <br />
[https://www.youtube.com/watch?v=JD-age0BPVo&list=RDCMUC4JX40jDee_tINbkjycV4Sg](https://www.youtube.com/watch?v=JD-age0BPVo&list=RDCMUC4JX40jDee_tINbkjycV4Sg) <br />
   <br />
### Some commands used in the Tutorial###  <br />
pip install djangorestframework <br />
django-admin startproject music_controller <br />
cd music_controller <br />
django-admin startapp api <br />
python manage.py makemigrations <br />
python manage.py migrate <br />
python manage.py runserver <br />
 <br />
 <br />
The steps below are the adaptation of the 3rd video. <br />
 <br />
Download and unzip Network base code: <br />
https://cs50.harvard.edu/web/2020/projects/4/network/#getting-started <br />
 <br />
### make the initial setup to the db and admin <br />
cd C:\PSET4_Network\project4 <br />
python manage.py makemigrations <br />
python manage.py migrate <br />
 <br />
### Create a Django app called frontend <br />
cd C:\PSET4_Network\project4 <br />
django-admin startapp frontend <br />
 <br />
### Move the templates folder from the network app to frontend <br />
move templates <br />
from <br />
C:\PSET4_Network\project4\network <br />
to <br />
C:\PSET4_Network\project4\frontend <br />
 <br />
### Move static folder from network to frontend. Create css, frontend and images folders inside of it. Move styles.css inside the css folder  <br />
move static <br />
from <br />
C:\PSET4_Network\project4\network <br />
to <br />
C:\PSET4_Network\project4\frontend <br />
 <br />
Create 3 folders inside "static", called "css" and "frontend" and "images" <br />
 <br />
move styles.css <br />
from <br />
C:\PSET4_Network\project4\frontend\static\network <br />
to <br />
C:\PSET4_Network\project4\frontend\static\css <br />
 <br />
Delete the network folder that was originally inside the static folder <br />
C:\PSET4_Network\project4\frontend\static\network <br />
 <br />
### Copy views.py from network to frontend views.py <br />
copy views.py <br />
from <br />
C:\PSET4_Network\project4\network <br />
to <br />
C:\PSET4_Network\project4\frontend <br />
 <br />
### Erase the network views.py content and just leave the index function <br />
``` <br />
from django.shortcuts import render <br />
 <br />
def index(request): <br />
    return render(request, "network/index.html") <br />
``` <br />
 <br />
### On views.py in frontend set ".models" to "network.models" <br />
On views.py. Located at <br />
C:\PSET4_Network\project4\frontend <br />
change line 7 from <br />
from .models import User <br />
to <br />
from network.models import User <br />
 <br />
### Create a urls.py for frontend, copy everything from urls.py from Network to urls.py on frontend <br />
Copy urls.py <br />
from <br />
C:\PSET4_Network\project4\network <br />
to <br />
C:\PSET4_Network\project4\frontend <br />
it should have this content: <br />
``` <br />
from django.urls import include, path <br />
 <br />
from . import views <br />
 <br />
urlpatterns = [ <br />
    path("", views.index, name="index"), <br />
    path("login", views.login_view, name="login"), <br />
    path("logout", views.logout_view, name="logout"), <br />
    path("register", views.register, name="register"), <br />
] <br />
``` <br />
 <br />
 <br />
### Leave only path(“”, views.index, name=“index”), on urls.py from network. <br />
Open urls.py <br />
located at: <br />
C:\PSET4_Network\project4\network <br />
Erase the needed to match this content: <br />
``` <br />
from django.urls import path <br />
 <br />
from . import views <br />
 <br />
urlpatterns = [path("", views.index, name="index")] <br />
``` <br />
 <br />
### Create folders src and src/components inside frontend <br />
create folders <br />
C:\PSET4_Network\project4\frontend\src <br />
and <br />
C:\PSET4_Network\project4\frontend\src\components <br />
 <br />
### run the following commands in frontend <br />
cd C:\PSET4_Network\project4\frontend <br />
npm init -y <br />
npm i webpack webpack-cli --save-dev <br />
npm i @babel/core babel-loader @babel/preset-env @babel/preset-react --save-dev <br />
:: (we are not going to use material-ui so no need to run "npm install @material-ui/core") <br />
npm i react react-dom --save-dev <br />
npm install @babel/plugin-proposal-class-properties <br />
npm install react-router-dom <br />
:: (no need to tun "npm install @material-ui/icons" either) <br />
 <br />
### create babel.config.json inside frontend <br />
create a file called <br />
babel.config.json <br />
inside <br />
C:\PSET4_Network\project4\frontend <br />
with this content: <br />
``` <br />
{ <br />
    "presets": [ <br />
        [ <br />
            "@babel/preset-env", <br />
            { <br />
                "targets": { <br />
                    "node": "10" <br />
                } <br />
            } <br />
        ], <br />
        "@babel/preset-react" <br />
    ], <br />
    "plugins": ["@babel/plugin-proposal-class-properties"] <br />
} <br />
``` <br />
 <br />
### create webpack.config.json inside frontend <br />
create a file called <br />
webpack.config.json <br />
inside <br />
C:\PSET4_Network\project4\frontend <br />
``` <br />
const path = require("path"); <br />
const webpack = require("webpack"); <br />
 <br />
module.exports = { <br />
    entry: "./src/index.js", <br />
    output: { <br />
        path: path.resolve(__dirname, "./static/frontend"), <br />
        filename: "[name].js", <br />
    }, <br />
    module: { <br />
        rules: [ <br />
            { <br />
                test: /\.js$/, <br />
                exclude: /node_modules/, <br />
                use: { <br />
                    loader: "babel-loader", <br />
                    options: { <br />
                        presets: ["@babel/react"], <br />
                    }, <br />
                }, <br />
            }, <br />
        ], <br />
    }, <br />
    optimization: { <br />
        minimize: true, <br />
    }, <br />
    plugins: [ <br />
        new webpack.DefinePlugin({ <br />
            "process.env": { <br />
                // This has effect on the react lib size <br />
                NODE_ENV: JSON.stringify("production"), <br />
            }, <br />
        }), <br />
    ], <br />
}; <br />
``` <br />
(I needed to add this line <br />
'presets: ["@babel/react"]' <br />
in order for this code to work as the original from the tutorial was causing me errors) <br />
original: <br />
https://github.com/techwithtim/Music-Controller-Web-App-Tutorial/blob/main/Tutorial%201%20-%204/frontend/webpack.config.js <br />
 <br />
 <br />
### Replace the scripts tag in package.json <br />
Open C:\PSET4_Network\project4\frontend\package.json <br />
Change "scripts": <br />
from: <br />
``` <br />
  "scripts": { <br />
    "test": "echo \"Error: no test specified\" && exit 1" <br />
  }, <br />
``` <br />
 <br />
to: <br />
``` <br />
  "scripts": { <br />
    "dev": "webpack --mode development --watch", <br />
    "build": "webpack --mode production", <br />
    "test": "echo \"Error: no test specified\" && exit 1" <br />
  }, <br />
``` <br />
 <br />
 <br />
### We are going to create a simple App to display a Hello World message. Create App.js inside frontend\src\components <br />
Create <br />
Apps.js <br />
in <br />
C:\PSET4_Network\project4\frontend\src\components <br />
``` <br />
import React from 'react'; <br />
 <br />
const Apps = () => { <br />
    return ( <br />
        <div> <br />
            <h1>Hello World</h1> <br />
        </div> <br />
    ) <br />
} <br />
 <br />
export default Apps <br />
``` <br />
 <br />
### Create the file index.js inside project4\frontend\src <br />
Create <br />
index.js <br />
in <br />
C:\PSET4_Network\project4\frontend\src <br />
``` <br />
import React from 'react'; <br />
import ReactDOM from 'react-dom'; <br />
import App from './components/App' <br />
 <br />
const AppDiv = document.getElementById('app'); <br />
ReactDOM.render(<div><App/></div>, AppDiv); <br />
``` <br />
 <br />
### add a div with id=main, and a script html tag for main.js before closing the body tag in layout.html <br />
Add <br />
    <div id="app"></div> <br />
    <script src="{% static "frontend/main.js" %}"></script> <br />
before <br />
    </body> <br />
in <br />
C:\Users\asd\Desktop\tests\CS50Web\mygithub\PSET4_Network\project4\frontend\templates\network\layout.html <br />
Last part of layout.html should look like this: <br />
``` <br />
        <div class="body"> <br />
            {% block body %} <br />
            {% endblock %} <br />
        </div> <br />
    </div> <br />
    <div id="app"></div> <br />
    <script src="{% static "frontend/main.js" %}"></script> <br />
</body></html> <br />
``` <br />
 <br />
### change the styles.css path at the top of layout.html <br />
Open layout.html <br />
located at <br />
C:\Users\asd\Desktop\tests\CS50Web\mygithub\PSET4_Network\project4\frontend\templates\network <br />
On line 8, change this: <br />
        <link href="{% static 'network/styles.css' %}" rel="stylesheet"> <br />
To this: <br />
        <link href="{% static 'css/styles.css' %}" rel="stylesheet"> <br />
 <br />
### On the main urls.py located at project4\project4. Add path("", include("frontend.urls")) to urlpatterns <br />
Open urls.py in <br />
C:\PSET4_Network\project4\project4\ <br />
Edit urlpatterns (lines 19 to 23) to match this content: <br />
``` <br />
urlpatterns = [ <br />
    path("admin/", admin.site.urls), <br />
    # path("", include("network.urls")), <br />
    path("", include("frontend.urls")), <br />
] <br />
``` <br />
 <br />
### Add frontend.apps.FrontendConfig to INSTALLED_APPS in project4\project4\settings.py <br />
open settings.py in <br />
C:\PSET4_Network\project4\project4 <br />
Add <br />
'frontend.apps.FrontendConfig' <br />
at the end of INSTALLED_APPS <br />
``` <br />
INSTALLED_APPS = [ <br />
    'network', <br />
    'django.contrib.admin', <br />
    'django.contrib.auth', <br />
    'django.contrib.contenttypes', <br />
    'django.contrib.sessions', <br />
    'django.contrib.messages', <br />
    'django.contrib.staticfiles', <br />
    'frontend.apps.FrontendConfig' <br />
] <br />
``` <br />
 <br />
### Run the backend and the frontend to see if you can render the Hello World message: <br />
Open a Terminal and run: <br />
cd C:\PSET4_Network\project4 <br />
python manage.py runserver <br />
 <br />
Open another Terminal and run: <br />
cd C:\PSET4_Network\project4\frontend <br />
npm run dev <br />
Open <br />
http://localhost:8000/ <br />
 <br />
Everything should look like in this repository up to this commit <br />
https://github.com/mcoutada/CS50web/tree/ee559432fabdb58d5b388aad12b1e16e795a388e <br />
 <br />
### Now that everything works let's undo the Hello World App. And Create the Home and Register Apps. <br />
 <br />
### Erase div="app" in layout.html <br />
Open layout.html in <br />
C:\PSET4_Network\project4\frontend\templates\network <br />
Erase line 49: <br />
<div id="app"></div> <br />
 <br />
### Delete App.js <br />
Located at <br />
C:\PSET4_Network\project4\frontend\src\components\App.js <br />
 <br />
 <br />
### Create Home.js and Register.js in components (use the rafce shortcut to create an arrow function inside), return a simple message <br />
 <br />
C:\PSET4_Network\project4\frontend\src\components\Home.js <br />
``` <br />
import React from 'react' <br />
 <br />
const Home = () => { <br />
    return ( <br />
        <div> <br />
            <h1>Home is working</h1> <br />
        </div> <br />
    ) <br />
} <br />
 <br />
export default Home <br />
``` <br />
 <br />
C:\PSET4_Network\project4\frontend\src\components\Register.js <br />
``` <br />
import React from 'react' <br />
 <br />
const Register = () => { <br />
    return ( <br />
        <div> <br />
            <h1>Register is working</h1> <br />
        </div> <br />
    ) <br />
} <br />
 <br />
export default Register <br />
``` <br />
 <br />
 <br />
### Edit index.js to erase App and render Register and Home <br />
``` <br />
import React from "react"; <br />
import ReactDOM from "react-dom"; <br />
import Register from "./components/Register"; <br />
 <br />
const home = ( <br />
    <div> <br />
        <Home /> <br />
    </div> <br />
); <br />
 <br />
const register = ( <br />
    <div> <br />
        <Register /> <br />
    </div> <br />
); <br />
 <br />
const rootElement = document.getElementById("index"); <br />
if (rootElement) { <br />
    ReactDOM.render(home, rootElement); <br />
} <br />
 <br />
const registerElement = document.getElementById("index"); <br />
if (registerElement) { <br />
    ReactDOM.render(register, registerElement); <br />
} <br />
``` <br />
 <br />
 <br />
### Edit project4\frontend\templates\network\index.html to add a div with id=index <br />
Open <br />
index.html <br />
located at <br />
C:\PSET4_Network\project4\frontend\templates\network <br />
Add <br />
<div id="index"></div> <br />
inside body <br />
``` <br />
{% extends "network/layout.html" %} <br />
 <br />
{% block body %} <br />
    <div id="index"></div> <br />
{% endblock %} <br />
``` <br />
 <br />
 <br />
### Edit project4\frontend\templates\network\register.html to add a div with id=register <br />
Open <br />
register.html <br />
located at <br />
C:\PSET4_Network\project4\frontend\templates\network <br />
Add <br />
<div id="register"></div> <br />
 <br />
The end of the file should look like: <br />
``` <br />
    </form> <br />
 <br />
    Already have an account? <a href="{% url 'login' %}">Log In here.</a> <br />
    <div id="register"></div> <br />
{% endblock %} <br />
``` <br />
 <br />
If everything went well, the messages should appear in <br />
http://localhost:8000/ <br />
http://localhost:8000/register