from sqlalchemy import create_engine, Column, Integer, String, Date, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class Company(Base):
    __tablename__ = 'Company'
    CompanyID = Column(Integer, primary_key=True)
    CEOName = Column(String(255))
    DateFounded = Column(Date)
    NumEmployees = Column(Integer)
    Industry = Column(String(255))
class Job(Base):
    __tablename__ = 'Job'
    JobID = Column(Integer, primary_key=True)
    JobName = Column(String(255))
    Salary = Column(Integer)
    YearsOfExperience = Column(Integer)
    StartDate = Column(Date)
    EndDate = Column(Date)
    Requirements = Column(String(1000))
    HiringCompany = Column(Integer, ForeignKey('Company.CompanyID'))

class Employer(Base):
    __tablename__ = 'Employer'
    EmployerID = Column(Integer, primary_key=True)
    FirstName = Column(String(255))
    LastName = Column(String(255))
    DOB = Column(Date)
    PhoneNo = Column(String(20))
    Email = Column(String(255))
    YearsOfExperience = Column(Integer)
    CurrentJob = Column(Integer, ForeignKey('Job.JobID'))

class Application(Base):
    __tablename__ = 'Application'
    ApplicationID = Column(Integer, primary_key=True)
    PhoneNo = Column(String(20))
    Email = Column(String(255))
    Location = Column(String(255))
    EmployerListed = Column(Integer, ForeignKey('Employer.EmployerID'))

class Applicant(Base):
    __tablename__ = 'Applicant'
    ApplicantID = Column(Integer, primary_key=True)
    FirstName = Column(String(255))
    LastName = Column(String(255))
    PhoneNo = Column(String(20))
    Email = Column(String(255))
    CurrentApplication = Column(Integer, ForeignKey('Application.ApplicationID'))

class Skill(Base):
    __tablename__ = 'Skill'
    SkillID = Column(Integer, primary_key=True)
    SkillName = Column(String(255))

class JobSkill(Base):
    __tablename__ = 'JobSkill'
    JobID = Column(Integer, ForeignKey('Job.JobID'), primary_key=True)
    SkillID = Column(Integer, ForeignKey('Skill.SkillID'), primary_key=True)

class Qualification(Base):
    __tablename__ = 'Qualification'
    QualificationID = Column(Integer, primary_key=True)
    QualificationName = Column(String(255))

class ApplicantQualification(Base):
    __tablename__ = 'ApplicantQualification'
    ApplicantID = Column(Integer, ForeignKey('Applicant.ApplicantID'), primary_key=True)
    QualificationID = Column(Integer, ForeignKey('Qualification.QualificationID'), primary_key=True)

class Reference(Base):
    __tablename__ = 'Reference'
    ApplicationID = Column(Integer, ForeignKey('Application.ApplicationID'), primary_key=True)
    RefereeName = Column(String(255), primary_key=True)
    RefereeEmail = Column(String(255))


# need to add constraints/relationships 





