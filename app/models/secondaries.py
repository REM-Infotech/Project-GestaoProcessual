from app import db

admins = db.Table(
    "admins",
    db.Column("users_id", db.Integer, db.ForeignKey("users.id")),
    db.Column("license_user_id", db.Integer, db.ForeignKey("licenses_users.id")),
)
