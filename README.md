# flask_to_do_list
A To Do list application created using flask-sqlalchemy <br>
Try it [here](https://flask-web-todo.herokuapp.com/)
<br>
## Local Setup and Installation 
#### Clone the repository and cd to it
```bash 
git clone <repo url>
cd flask_to_do_list
```
#### Create a virtual enviroment. [Read more](https://realpython.com/python-virtual-environments-a-primer/)
```bash 
  venv <environment name>
```
##### Note: Linux user might have to install venv using the following command

#### Activate the virtual environment 
```bash
   apt-get install python3-venv
```
#### Install Reqirements
```bash 
  pip install -r requirements.txt
```
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

#### References
1. Freecodecamp video - https://youtu.be/Z1RJmh_OqeA
2. Tech With Tim youtube video - https://youtu.be/dam0GPOAvVI
3. Flask Docs - https://flask.palletsprojects.com/en/2.0.x/
4. Flask SQLAlchemy - https://flask-sqlalchemy.palletsprojects.com/en/2.x/
5. Flask login docs - https://flask-login.readthedocs.io/en/latest/
