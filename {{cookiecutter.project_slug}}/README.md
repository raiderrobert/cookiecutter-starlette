# { cookiecutter.project_name }}
{{ cookiecutter.description}}

## Quickstart
Run the following commands to bootstrap your environment

git clone https://github.com/{{cookiecutter.github_username}}/{{cookiecutter.app_name}}
cd {{cookiecutter.app_name}}
{%- if cookiecutter.use_pipenv == "yes" %}
pipenv install --dev
{%- else %}
pip install -r requirements/dev.txt
{%- endif %}
cp .env.example .env
npm install
npm start  # run the webpack dev server and flask server using concurrently
You will see a pretty welcome screen.

Once you have installed your DBMS, run the following to create your app's database tables and perform the initial migration

flask db init
flask db migrate
flask db upgrade
npm start
Deployment
To deploy:

export FLASK_ENV=production
export FLASK_DEBUG=0
export DATABASE_URL="<YOUR DATABASE URL>"
npm run build   # build assets with webpack
flask run       # start the flask server
In your production environment, make sure the FLASK_DEBUG environment variable is unset or is set to 0.

Shell
To open the interactive shell, run

flask shell
By default, you will have access to the flask app.