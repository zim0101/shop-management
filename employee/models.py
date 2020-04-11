from app import db, marshmallow


# ------------------------------------------- Employee Model ------------------------------------------

class Employee(db.Model):

    __tablename__ = 'employees'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100))
    salary = db.Column(db.Float, nullable=False)
    started_at = db.Column(db.DateTime, nullable=False)
    end_at = db.Column(db.DateTime, nullable=False)
    still_working = db.Column(db.Boolean, nullable=True)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, server_default=db.func.now(), server_onupdate=db.func.now())

    def __init__(self, name: str, salary: float, started_at: str, end_at: str, still_working: bool):
        """
        @param name:
        @param salary:
        @param started_at:
        @param end_at:
        @param still_working:
        """
        self.name = name
        self.salary = salary
        self.started_at = started_at
        self.end_at = end_at
        self.still_working = still_working


# ------------------------------------------- Employee Schema -----------------------------------------

class EmployeeSchema(marshmallow.Schema):
    class Meta:
        fields = ("id", "name", "salary", "started_at", "end_at", "still_working", "created_at")
