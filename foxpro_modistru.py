import sublime, sublime_plugin  
import os
import re

class foxpro_modistru(sublime_plugin.WindowCommand):  
    def run(self):
        self.window.show_input_panel("Modify Structure:", "", self.on_done, None, None)
        pass

    def on_done(self,user_input):
      if user_input == "":
    		user_input ="?"

        path = sublime.packages_path() + "\\Foxpro\\Bats\\"
    	self.window.run_command("exec",{"cmd":["modistru.bat",path+"modistru.fxp",user_input],"working_dir": path})
    	pass
