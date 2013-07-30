import sublime, sublime_plugin
import os
import re

class foxpro_compile(sublime_plugin.WindowCommand):  
    def run(self):
        fname = self.window.active_view().file_name()
        path = sublime.packages_path() + "\\Foxpro\\Bats\\"
        self.window.run_command("exec",{"cmd":["start.bat",path+"compile.fxp",fname],"working_dir": path})
