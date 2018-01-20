from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import scoped_session, sessionmaker, session
from sqlalchemy.ext.declarative import declarative_base

#engine="mysql+mysqldb://root:mm2017@127.0.0.1:3307/testdb?charset=utf8"
engine="mysql+mysqldb://bpet:bpet112358@39.106.145.2:4000/bpet?charset=utf8"
#engine = create_engine('sqlite:////tmp/test.db', convert_unicode=True)
metadata = MetaData(engine)
engine = create_engine(engine, convert_unicode=True)
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))

Base = declarative_base(metadata=metadata)
Base.query = db_session.query_property()

def init_db():
    import models
    Base.metadata.create_all(bind=engine)
