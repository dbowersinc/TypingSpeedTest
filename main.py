from gui import App


def create_app():
    app = App()

    return app

if __name__ == '__main__':
    myapp = create_app()
    myapp.mainloop()
