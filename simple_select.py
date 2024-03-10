from main import session
from models import User,Comment
from sqlalchemy import select

statement = select(User).where(User.user_name.in_(["Lokesh", "Ajay"]))

result = session.scalars(statement)

for user in result:
    print(user)
    

# users = session.query(User).all()

# for user in users:
#     print(user) 