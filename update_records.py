from main import session
from models import User,Comment
from sqlalchemy import select


comment = session.query(Comment).filter_by(id=1).first()
comment.text = "This is an updated comment"
session.commit()

# statement = select(User).where(User.user_name == "Lokesh")
# lokesh = session.scalars(statement).one()
# lokesh.comments.append(Comment(text="Comment was changed"))
# lokesh.text = "sandy_cheeks@sqlalchemy.org"
# session.commit()