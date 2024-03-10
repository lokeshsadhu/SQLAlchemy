from main import session
from models import User ,Comment
from sqlalchemy import select


statement = (select(Comment)
            .join(Comment.user)
            .where(User.user_name == 'Lokesh')
            .where(Comment.text == 'Hello World'))

result = session.scalars(statement).one()

print(result)