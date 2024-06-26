from app import app, db
from flask_migrate import MigrateCommand
from flask.cli import FlaskGroup

def create_app():
    return app

cli = FlaskGroup(create_app=create_app)
cli.add_command('db', MigrateCommand)

if __name__ == '__main__':
    cli()
