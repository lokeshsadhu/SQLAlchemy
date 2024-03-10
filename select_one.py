from main import session
from models import User

lokesh = session.query(User).filter_by(username = 'Lokesh').first()

print(lokesh)