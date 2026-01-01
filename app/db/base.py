from sqlalchemy.orm import DeclarativeBase


# base = DeclarativeBase()  ==> Old version
# New version seem confuse
class Base(DeclarativeBase):
    pass
