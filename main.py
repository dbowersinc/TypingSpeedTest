from .gui import App


def create_app():
    app = App()

    return app


myapp = create_app()
myapp.mainloop()
