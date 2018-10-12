from backend import nav
from flask_nav.elements import Navbar, Subgroup, View
from flask_security import current_user


@nav.navigation()
def mynavbar():
    return Navbar(
        'Dell Team 7',
        View('Home', "index"),
        Subgroup(
            "Control Panel",
            View('Account', 'admin.index'),
            View('Log out', 'security.logout')
        )
        if current_user.is_authenticated else View('Log in', 'login')
    )
