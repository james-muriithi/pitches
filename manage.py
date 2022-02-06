from app import create_app, db
from flask_script import Manager,Server
from decouple import config
from flask_migrate import Migrate, MigrateCommand
from app.models import User, Role, Pitch, Comment, Category, Vote
import os

app = create_app(config('ENV', default="development"))

manager = Manager(app)
manager.add_command('server',Server)

def path_exists(path):
    return os.path.exists(path)

@app.context_processor
def handle_context():
    return dict(path_exists=path_exists)

@manager.shell
def make_shell_context():
    return dict(app = app,db = db, User=User, Role=Role, Comment = Comment, 
        Category = Category, Pitch = Pitch, Vote = Vote )

@manager.command
def test():
    """Run the unit tests."""
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)        

migrate = Migrate(app,db)
manager.add_command('db',MigrateCommand)

if __name__ == '__main__':
    manager.run()