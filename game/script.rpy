init -999 python:
    def newest_slot_tuple():
        newest = renpy.newest_slot()

        if newest is not None:
            page, name = newest.split("-")
            return (page, name)

    class Continue(Action):
        def __call__(self):
            if not self.get_sensitive():
                return
            newest_page, newest_name = newest_slot_tuple()
            FileLoad(newest_name, confirm=False, page=newest_page, newest=True)()

        def get_sensitive(self):
            if not main_menu or _in_replay:
                return False
            newest = newest_slot_tuple()
            if newest is None:
                return False
            newest_page, newest_name = newest
            if newest_page == '_reload':
                return False
            return FileLoadable(newest_name, page=newest_page)