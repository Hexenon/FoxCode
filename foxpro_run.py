import sublime, sublime_plugin  
import os
import re

class foxpro_run(sublime_plugin.WindowCommand):  
    def run(self):
        self.window.show_input_panel("Do ", "", self.on_done, None, None)
    	pass

    def on_done(self,user_input):
    	if user_input == "":
    		user_input = self.window.active_view().file_name()

    	path = sublime.packages_path() + "\\FoxCode\\Bats\\"
    	self.window.run_command("exec",{"cmd":["start.bat",user_input],"working_dir": path})
