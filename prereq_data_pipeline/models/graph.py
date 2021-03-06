import datetime
from prereq_data_pipeline.models.base import Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Text, ForeignKey, Integer, DateTime


class Graph(Base):
    course_id = Column(Integer, ForeignKey('course.id'))
    course = relationship("Course", back_populates="graph")
    graph_json = Column(Text())
    create_date = Column(DateTime, default=datetime.datetime.utcnow)
