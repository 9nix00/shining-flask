"""
=============
Models
=============
"""

from account.models import Account, db

_ = Account


class AccountUsername(db.Model):
    username = db.Column(db.String(32), primary_key=True)
    account_id = db.Column('account_id', db.Integer(),
                           db.ForeignKey('account.id'),
                           unique=True)

    account = db.relationship("Account", backref=db.backref('username',
                                                            uselist=False))
    pass
