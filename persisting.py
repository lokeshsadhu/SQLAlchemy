from models import User,Comment
from main import session

lokesh = User(
    user_name = 'Lokesh',
    email = "lokesh@sql.irg",
    comments = [
        Comment(text="Hello World"),
        Comment(text="Please subscribe")
    ]
)

ajay = User(
    user_name = 'Ajay',
    email = "ajay@sql.irg",
    comments = [
        Comment(text="What's up?"),
        Comment(text="How are you?")
    ]
)

sai = User(
    user_name = 'Sai',
    email = "sai@sql.irg",
)


session.add_all([lokesh,ajay,sai])

session.commit()