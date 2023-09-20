from flask import Flask
from views import main_bp


def create_app() -> Flask:
    """Initialize Flasc app"""
    app = Flask(__name__)
    app.register_blueprint(main_bp)
    return app

# app = Flask(__name__)
#
# BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# DATA_DIR = os.path.join(BASE_DIR, "data")
#
#
# @app.route("/perform_query")
# def perform_query():
#     # получить параметры query и file_name из request.args, при ошибке вернуть ошибку 400
#     # проверить, что файла file_name существует в папке DATA_DIR, при ошибке вернуть ошибку 400
#     # с помощью функционального программирования (функций filter, map), итераторов/генераторов сконструировать запрос
#     # вернуть пользователю сформированный результат
#     return app.response_class('', content_type="text/plain")
