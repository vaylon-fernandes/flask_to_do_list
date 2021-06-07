# flask_to_do_list
A To Do list application created using flask-sqlalchemy and bootstrap<br>

## Demo
See a live version deployed on heroku [here](https://flask-web-todo.herokuapp.com/)
<br>
Clone the project

```bash
  git clone https://github.com/vaylon-fernandes/flask_weather_app.git
```

Go to the project directory

```bash
  cd flask_to_do_list
```
Create a virtual enviroment. [Read more](https://realpython.com/python-virtual-environments-a-primer/)
```bash 
  venv <environment name>
```
##### Note: Linux users might have to install venv using the following command

```bash
   apt-get install python3-venv
```

#### Activate the virtual environment 
On Linux:
```bash 
source venv/bin/activate
```
On Windows:
```bash
venv\Scripts\activate
```
#### Install Reqirements
```bash 
  pip install -r requirements.txt
```
## Configuring environment Variables
- Firstly Generate a `Secret Key`. This is required by the Flask [Sessions](https://flask.palletsprojects.com/en/2.0.x/quickstart/#sessions). 
Do read the section on  ***How to generate good secret keys***  in the flask documentation under 
sessions [here](https://flask.palletsprojects.com/en/2.0.x/quickstart/#sessions)
- Next export the secret key  to Enviroment Variables using one of the following commands based on your terminal
Bash command 
```bash
  export SECRET_KEY=<your secret key>
```
CMD command
```bash
  set SECRET_KEY=<your secret key>
```
Powershell command
```powershell
  $env:SECRET_KEY=<your secret key>
```
The enviroment variables are then read using the [os.environ object](https://www.geeksforgeeks.org/python-os-environ-object/)
#### Running the app 
To run the app, first export the `FLASK_APP` variable, using one of the following commands based on your terminal<br>
Bash command 
```bash
  export FLASK_APP=main
```
CMD command
```bash
  set FLASK_APP=main
```
Powershell command
```powershell
  $env:FLASK_APP = "hello"
```
#### Run command
```bash
flask run
```
This creates a simple server, go to `http://127.0.0.1:5000/` in your browser to view the site <br>
#### Debug mode 
To run the server in Debug mode, export the `FLAK_ENV` variable befor running `flask run`
Bash command 
```bash
  export FLASK_ENV=development
```
CMD command
```bash
  set FLASK_ENV=development
```
Powershell command
```powershell
  $env:FLASK_ENV="development"
```
Run command
```bash
flask run
```
Read more here: https://flask.palletsprojects.com/en/2.0.x/quickstart/#debug-mode
## Deploying to Heroku
- There's a good explanation of this given in this [repo](https://github.com/MirelaI/flask_heroku_example)
- Another good read on the topic is on the Real Python [website](https://realpython.com/flask-by-example-part-1-project-setup/)
#### References
1. Freecodecamp video - https://youtu.be/Z1RJmh_OqeA
2. Tech With Tim youtube video - https://youtu.be/dam0GPOAvVI
3. Flask Docs - https://flask.palletsprojects.com/en/2.0.x/
4. Flask SQLAlchemy - https://flask-sqlalchemy.palletsprojects.com/en/2.x/
5. Flask login docs - https://flask-login.readthedocs.io/en/latest/
