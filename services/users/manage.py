import sys
import coverage
import unittest
from flask.cli import FlaskGroup
from project import create_app, db
from project.api.models import User

COV = coverage.coverage(
    branch=True,
    include='project/*',
    omit=[
        'project/tests/*',
        'project/config.py',
    ]
)

COV.start()

app = create_app()
cli = FlaskGroup(create_app=create_app)


print("manage starts here....")
# new
@cli.command('recreate_db')
def recreate_db():
    db.drop_all()
    db.create_all()
    db.session.commit()


@cli.command('test')
def test():
    tests = unittest.TestLoader().discover('project/tests', pattern='test*.py')
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        return 0
    sys.exit(result)


@cli.command('seed_db')
def seed_db():
    """Seeds the database
    """
    db.session.add(User(username='michael', email='michael@gmail.com'))
    db.session.add(User(username='jimmy', email='jimmy@gmail.com'))
    db.session.commit()


@cli.command('cov')
def cov():
    """Runs the unit tests with coverage
    """
    tests = unittest.TestLoader().discover('project/tests', pattern='test*.py')
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        COV.stop()
        COV.save()
        print('Coverage summary:')
        COV.report()
        COV.html_report()
        COV.erase()
        return 0
    sys.exit(result)


if __name__ == '__main__':
    cli()
