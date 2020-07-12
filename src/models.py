from app import db


class user_name(db.Model):
    __tablename__ = "more_users"
    id = db.Column(Integer, primary_key=True)
    user = db.Column(String, nullable=False)
    password = db.Column(String, nullable=False)
    def __init__(self,user,password):
        self.password = password
        self.user = user
class user_info(db.Model):
    __tablename__ = "user_info"
    id = db.Column(Integer, primary_key=True)
    user_Fname = db.Column(String, nullable=False)
    user_Lname = db.Column(String, nullable=False)
    user_age = db.Column(String, nullable=False)
    creat_date = db.Column(Date)

    user_id = Column(Integer, db.ForeignKey("more_users.id")) # gets id from more_users
    users = relationship("more_users",
                        backref=db.backref("user_info",
                        order_by=id, lazy=True
                                     ))
    def __init__(self,user_Fname,user_Lname,user_age,creat_date):
        self.user_Fname = user_Fname
        self.user_Lname = user_Lname
        self.user_age = user_age
        self.creat_date = creat_date
