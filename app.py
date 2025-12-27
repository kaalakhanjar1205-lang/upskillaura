from flask import Flask, jsonify, render_template
from config import Config
from database import db
from models import Certificate
from sqlalchemy import func


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)

    # ==========================
    # Home Page
    # ==========================
    @app.route("/")
    def home():
        return render_template("home.html")

    # ==========================
    # Verification Page
    # ==========================
    @app.route("/verify")
    def verify_page():
        return render_template("index.html")

    # ==========================
    # Certificate Verification API
    # ==========================
    @app.route("/verify-certificate/<string:serial_number>", methods=["GET"])
    def verify_certificate(serial_number):

        clean_serial = serial_number.strip().upper()

        certificate = Certificate.query.filter(
            func.upper(Certificate.serial_number) == clean_serial
        ).first()

        if not certificate:
            return jsonify({
                "success": False,
                "message": "Invalid certificate serial number"
            }), 404

        if certificate.status != "VALID":
            return jsonify({
                "success": False,
                "message": "Certificate has been revoked"
            }), 400

        return jsonify({
            "success": True,
            "data": certificate.to_dict()
        }), 200

    return app


app = create_app()

# 🔥 THIS LINE CREATES TABLES ON RENDER
with app.app_context():
    db.create_all()
# # 🔥 THIS LINE CREATES TABLES ON RENDER

# from flask import Flask, jsonify, render_template
# from config import Config
# from database import db
# from models import Certificate
# from sqlalchemy import func

# ⚠️ DO NOT use app.run() for Render


# def create_app():
#     app = Flask(__name__)
#     app.config.from_object(Config)

#     db.init_app(app)

#     # ==========================
#     # Home Page
#     # ==========================
#     @app.route("/")
#     def home():
#         return render_template("home.html")

#     # ==========================
#     # Verification Page
#     # ==========================
#     @app.route("/verify")
#     def verify_page():
#         return render_template("index.html")

#     # ==========================
#     # Certificate Verification API
#     # ==========================
#     @app.route("/verify-certificate/<string:serial_number>", methods=["GET"])
#     def verify_certificate(serial_number):

#         clean_serial = serial_number.strip().upper()

#         certificate = Certificate.query.filter(
#             func.upper(Certificate.serial_number) == clean_serial
#         ).first()

#         if not certificate:
#             return jsonify({
#                 "success": False,
#                 "message": "Invalid certificate serial number"
#             }), 404

#         if certificate.status != "VALID":
#             return jsonify({
#                 "success": False,
#                 "message": "Certificate has been revoked"
#             }), 400

#         return jsonify({
#             "success": True,
#             "data": certificate.to_dict()
#         }), 200

#     return app
# app = create_app()

if __name__ == "__main__":
    with app.app_context():
        db.create_all()

    app.run(debug=False)

