from server import app, register_blueprints

register_blueprints(app)

if __name__ == "__main__":
    application.run()  # noqa: F821
