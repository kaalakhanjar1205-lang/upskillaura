from database import db
from datetime import datetime
import uuid

class Certificate(db.Model):
    __tablename__ = "certificates"

    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    serial_number = db.Column(db.String(50), unique=True, nullable=False, index=True)
    student_name = db.Column(db.String(100), nullable=False)
    course = db.Column(db.String(100), nullable=False)
    year = db.Column(db.Integer, nullable=False)
    status = db.Column(db.String(20), default="VALID")
    issued_date = db.Column(db.Date, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    # ✅ THIS METHOD MUST BE INSIDE THE CLASS
    def to_dict(self):
        return {
            "serial_number": self.serial_number,
            "student_name": self.student_name,
            "course": self.course,
            "year": self.year,
            "status": self.status,
            "issued_date": self.issued_date.isoformat()
        }
