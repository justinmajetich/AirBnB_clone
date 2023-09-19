from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///hospital_department.db')
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()


class Hospital(Base):
    __tablename__ = 'hospitals'
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)

    # Establish a one-to-many relationship with Department
    departments = relationship(
        'Department', back_populates='hospital', cascade='all, delete-orphan')


class Department(Base):
    __tablename__ = 'departments'
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)

    # Create a foreign key relationship to Hospital
    hospital_id = Column(Integer, ForeignKey('hospitals.id'))

    # Create a reference to the Hospital object using the relationship
    hospital = relationship('Hospital', back_populates='departments')


Base.metadata.create_all(engine)

# Create hospitals and departments
hospital1 = Hospital(name='General Hospital')
department1 = Department(name='Cardiology', hospital=hospital1)
department2 = Department(name='Pediatrics', hospital=hospital1)

hospital2 = Hospital(name='Children\'s Hospital')
department3 = Department(name='Neonatology', hospital=hospital2)

session.add(hospital1)
session.add(department1)
session.add(department2)
session.add(hospital2)
session.add(department3)
session.commit()

# Query the database
general_hospital = session.query(Hospital).filter_by(
    name='General Hospital').first()
print(f'{general_hospital.name} has departments:')
for department in general_hospital.departments:
    print(f'- {department.name}')

# Delete a hospital and check if linked departments are deleted automatically
session.delete(general_hospital)
session.commit()

departments_in_general_hospital = session.query(
    Department).filter_by(hospital_id=general_hospital.id).all()
if not departments_in_general_hospital:
    print("All departments in General Hospital have been deleted.")
