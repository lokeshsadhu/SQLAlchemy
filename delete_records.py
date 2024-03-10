from main import session
from models import User,Comment

comment = session.query(Comment).filter_by(id=1).first()
session.delete(comment)
session.commit()

# sandy = session.get(User, 2)
# sandy.addresses.remove(sandy_address)

# session.flush()

# session.delete(patrick)