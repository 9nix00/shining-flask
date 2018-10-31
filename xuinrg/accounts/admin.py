"""
=============
Admin
=============


"""

import flask_admin as admin


class AccountAdminView(admin.BaseView):
    @admin.expose('/')
    def index(self):
        return self.render('admin.html')

    @admin.expose('/test/')
    def test(self):
        return self.render('test.html')
