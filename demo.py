from app import app, db
from app.models import New


@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'New': New}