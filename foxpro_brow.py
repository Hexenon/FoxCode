import sublime, sublime_plugin  
import os
import re
class foxpro_brow(sublime_plugin.WindowCommand):  
    def run(self):
        self.window.show_input_panel("Browse:", "", self.on_done, None, None)
    	pass

    def on_done(self,user_input):
    	if user_input == "":
    		user_input = "?"

    	path = sublime.packages_path() + "\\FoxCode\\Bats\\"
    	self.window.run_command("exec",{"cmd":["start.bat",path + "brow.fxp",user_input],"working_dir": path})
    	pass
