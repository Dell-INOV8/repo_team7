from backend import nav
from dominate.tags import img
from flask import send_from_directory
from flask_nav.elements import Navbar, Subgroup, View, Markup, Text
from flask_security import current_user


def get_brand():
    return img(src='/static/img/dell.png')


class SearchBar(Text):
    def __init__(self):
        pass

    @property
    def text(self):
        return Markup(
            '<input type="text" class="form-control" style="width: 100%; line-height: .8;" placeholder="Search">'
        )


@nav.navigation()
def mynavbar():
    return Navbar(
        # 'Dell Team 7',
        get_brand(),
        View('Home', "index"),
        Subgroup(
            "Control Panel",
            View('Account', 'admin.index'),
            View('Log out', 'security.logout')
        )
        if current_user.is_authenticated else View('Log in', 'login'),
        SearchBar(),
    )
