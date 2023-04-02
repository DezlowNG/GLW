define config.name = _("Последнее желание девочки")
define gui.show_name = False
define config.version = "1.0"

define build.name = "glw"

define config.has_sound = True
define config.has_music = True
define config.has_voice = False

define config.main_menu_music = "audio/music/main_menu.mp3"

define config.enter_transition = dissolve
define config.exit_transition = dissolve
define config.intra_transition = dissolve
define config.after_load_transition = dissolve
define config.end_game_transition = dissolve
define config.window = "auto"
define config.window_show_transition = Dissolve(.2)
define config.window_hide_transition = Dissolve(.2)
default preferences.text_cps = 0
default preferences.afm_time = 15
define config.save_directory = "glw-1680229233"
define config.window_icon = "gui/window_icon.png"

init python:
    build.classify('**~', None)
    build.classify('**.bak', None)
    build.classify('**/.**', None)
    build.classify('**/#**', None)
    build.classify('**/thumbs.db', None)
    build.classify('**.code-workspace', None)