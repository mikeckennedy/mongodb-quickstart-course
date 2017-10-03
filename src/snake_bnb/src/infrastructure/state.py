from data.owners import Owner

active_account: Owner = None


def reload_account():
    global active_account
    if not active_account:
        return

    # TODO: pull owner account from the database.
    pass
