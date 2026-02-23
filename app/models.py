from sqlmodel import SQLModel,Field,Relationship
from typing import Optional,List
from pydantic import EmailStr
from datetime import datetime
from enum import Enum



class AuthProvider(str,Enum):
    LOCAL = "local"
    GOOGLE = "google"
    APPLE = "apple"


class Status(str,Enum):
    PENDING = "pending"
    WORKING = "working"
    FINISHED = "finished"

class ProjectMember(SQLModel,table=True):
    UserId : int = Field(...,foreign_key="user.id",primary_key="True")
    projectId : int = Field(...,foreign_key="user.id",primary_key=True)

class User(SQLModel,table=True):
    id :int = Field(...,nullable=False, primary_key=True)
    name :str = Field(...,nullable=False,max_length=50)
    email : EmailStr = Field(...,nullable=False,unique=True)
    passwordHash : str
    provider: AuthProvider = Field(default="local")
    createdAT = datetime = Field(default_factory=datetime.utcnow)

    owned_project : List["Project"] = Relationship(back_populate="owner")
    tasks: List["Task"] = Relationship(back_populate="asignee")




class Project(SQLModel, table=True):
    id : int = Field(...,primary_key=True)
    name : str = Field(...,nullable=False,max_length=50)
    description: Optional[str] = Field(nullable=True,max_length=500)
    owner :int =Field(...,foreign_key="user.id")
    createdat = datetime.now = Field(nullable=False)

    owner: User = Relationship(back_populates="owned_projects")
    tasks: List["Task"] = Relationship(back_populates="project")


class Task(SQLModel,table=True):
    id :int = Field(primary_key=True)
    name: str = Field(...,nullable=False,max_length=50)
    description: str = Field(max_length=500,nullable=False)
    projectId : int = Field(...,foreign_key="project.id")
    assignto : int = Field(...,foreign_key="user.id")
    status : Status = Field(...,default="pending",nullable=False)
    createdAt : datetime.now = Field(nullabe=False)

    # Relationships
    project: Project = Relationship(back_populates="tasks")
    assignee: User = Relationship(back_populates="tasks")



   



   