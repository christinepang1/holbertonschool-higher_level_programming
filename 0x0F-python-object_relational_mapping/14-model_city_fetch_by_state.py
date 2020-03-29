#!/usr/bin/python3
import sys
from model_state import Base, State
from model_city import City
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.
                           format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)

    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    results = session.query(State, City).filter(City.state_id == State.id).\
        order_by(City.id).all()

    for i in results:
        print("{}: ({}) {}".format(i.State.name, i.City.id, i.City.name))
    session.close()
