from flaskblog import db
from flaskblog.models import User, Post

#create db
#db.create_all()

#stage a change
#db.session.add()
#commit session
#db.session.commit()

User.query.all()


