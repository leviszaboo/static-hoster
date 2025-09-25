# wsgi.py
from . import create_app
from .config import ProdConfig

app = create_app(config_class=ProdConfig())

if __name__ == "__main__":
    app.run()
