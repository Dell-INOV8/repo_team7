from backend import nav
from flask import url_for
from flask_nav.elements import Navbar, View


@nav.navigation()
def mynavbar():
    return Navbar(
        'Dell Team 7',
        View('Home', "index"),
    )
