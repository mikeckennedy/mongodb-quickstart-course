active_account = None


def reload_account():
    global active_account
    if not active_account:
        return

    # TODO: pull owner account from the database.
    pass
