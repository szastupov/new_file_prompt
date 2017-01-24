import sublime_plugin
import functools
import os


class NewFileAtCommand(sublime_plugin.WindowCommand):
    def run(self, dirs):
        self.window.show_input_panel(
            "File Name:", "", functools.partial(self.on_done, dirs[0]),
            None, None
        )

    def on_done(self, dir, name):
        self.window.open_file(os.path.join(dir, name))

    def is_visible(self, dirs):
        return len(dirs) == 1
