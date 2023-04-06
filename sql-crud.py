from sqlalchemy import (
    create_engine, Column, Integer, String
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


# executing the instructions from the "chinook" database
db = create_engine("postgresql:///chinook")
base = declarative_base()


# create a class-based model for the "Programmer" table
class Programmer(base):
    __tablename__ = "Programmer"
    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    gender = Column(String)
    nationality = Column(String)


# create a class-based model for the "Family" table
class Family(base):
    __tablename__ = "Family"
    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    origin_family = Column(String)
    married = Column(String)


# instead of connecting to the database directly, we will ask for a session
# create a new instance of sessionmaker, then point to our engine (the db)
Session = sessionmaker(db)
# opens an actual session by calling the Session() subclass defined above
session = Session()

# creating the database using declarative_base subclass
base.metadata.create_all(db)


# creating records on our Progammer table
ada_lovelace = Programmer(
    first_name="Ada",
    last_name="Lovelace",
    gender="F",
    nationality="British",
)

alan_turing = Programmer(
    first_name="Alan",
    last_name="Turing",
    gender="M",
    nationality="British",
)

grace_hopper = Programmer(
    first_name="Grace",
    last_name="Hopper",
    gender="F",
    nationality="American",
)

margaret_hamilton = Programmer(
    first_name="Margaret",
    last_name="Hamilton",
    gender="F",
    nationality="American",
)

bill_gates = Programmer(
    first_name="Bill",
    last_name="Gates",
    gender="M",
    nationality="American",
)

tim_berners_lee = Programmer(
    first_name="Tim",
    last_name="Berners-Lee",
    gender="M",
    nationality="British",
)

# abby_humphreys = Programmer(
#     first_name="Abby",
#     last_name="Humphreys",
#     gender="F",
#     nationality="British",
# )

# creating records on the "Family" table
abby_humphreys = Family(
    first_name="Abby",
    last_name="Humphreys",
    origin_family="Heywood",
    married="Yes"
)

matthew_humphreys = Family(
    first_name="Matthew",
    last_name="Humphreys",
    origin_family="Humphreys",
    married="Yes"
)

abby_wood = Family(
    first_name="Abby",
    last_name="Wood",
    origin_family="Humphreys",
    married="Yes"
)
gus_wood = Family(
    first_name="Gus",
    last_name="Wood",
    origin_family="Other",
    married="Yes"
)


# add each instance of our programmers to our session
# session.add(abby_humphreys)
# session.add(matthew_humphreys)
# session.add(gus_wood)
# session.add(abby_wood)

# add each instance of our programmers to our session
# session.add(ada_lovelace)
# session.add(alan_turing)
# session.add(grace_hopper)
# session.add(margaret_hamilton)
# session.add(bill_gates)
# session.add(tim_berners_lee)
# session.add(abby_humphreys)


# updating a single record
# programmer = session.query(Programmer).filter_by(id=11).first()
# programmer.nationality = "Guyanese"


# updating multiple records
# people = session.query(Programmer)
# for person in people:
#     if person.gender == "F":
#         person.gender = "Female"
#     elif person.gender == "M":
#         person.gender = "Male"
#     else:
#         print("Gender not defined") 

# updating mulitple records
people = session.query(Family)
for person in people:
    if person.married == "Yes":
        person.married = "Y"


# deleting a single record
# fname = input("Enter a first name: ")
# lname = input("Enter a last name: ")
# programmer = session.query(Programmer).filter_by(first_name=fname, last_name=lname).first()
# # defensive programming
# if programmer is not None:
#     print("Programmer Found: ", programmer.first_name + " " + programmer.last_name)
#     confirmation = input("Are you sure you want to delete this record? (y/n) ")
#     if confirmation.lower() == "y":
#         session.delete(programmer)
#         session.commit()
#         print("Programmer has been deleted")
#     else:
#         print("Programmer not deleted")    

# else:
#     print("No records found")

# deleting a multiple records
# wrong_records = session.query(Family).filter_by(id=8).first()
# session.delete(wrong_records)
# session.commit()
   


# commit our session to the database
session.commit()


# query the database to find all Programmers
# programmers = session.query(Programmer)
# for programmer in programmers:
#     print(
#         programmer.id,
#         programmer.first_name + " " + programmer.last_name,
#         programmer.gender,
#         programmer.nationality,
#         sep=" | "
#     )


# query the database to find all Family
family = session.query(Family)
for member in family:
    print(
        member.id,
        member.first_name + " " + member.last_name,
        member.origin_family,
        member.married,
        sep=" | "
    )