from flask import Flask

def create_app(): 
    app = Flask(__name__) 
    # Cria a instância da aplicação Flask.
    
    app.config["SECRET_KEY"] = "123123" # need to private the key

    from .views import views
    from .auth import auths
    # Importa os blueprints definidos em outros módulos.

    app.register_blueprint(views, url_prefix="/")
    app.register_blueprint(auths, url_prefix="/")

    return app