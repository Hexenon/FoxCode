import sublime, sublime_plugin  
import re

class FoxConsoleCommand(sublime_plugin.WindowCommand):  
    def run(self):
        path = sublime.packages_path() + "\\FoxCode\\Bats\\"
        self.window.run_command("exec",{"cmd":["start.bat"],"working_dir": path})

import sublime, sublime_plugin  
import os
import re
class FoxproBrowCommand(sublime_plugin.WindowCommand):  
    def run(self):
        self.window.show_input_panel("Browse:", "", self.on_done, None, None)
    	pass

    def on_done(self,user_input):
    	if user_input == "":
    		user_input = "?"

    	path = sublime.packages_path() + "\\FoxCode\\Bats\\"
    	self.window.run_command("exec",{"cmd":["start.bat",path + "brow.fxp",user_input],"working_dir": path})
    	pass

import sublime, sublime_plugin
import os
import re

class FoxproCompileCommand(sublime_plugin.WindowCommand):  
    def run(self):
        fname = self.window.active_view().file_name()
    	path = sublime.packages_path() + "\\FoxCode\\Bats\\"
    	self.window.run_command("exec",{"cmd":["start.bat",path+"compile.fxp",fname],"working_dir": path})

import sublime, sublime_plugin  
import os
import re

class FoxproModistruCommand(sublime_plugin.WindowCommand):  
    def run(self):
        self.window.show_input_panel("Modify Structure:", "", self.on_done, None, None)
    	pass

    def on_done(self,user_input):
    	if user_input == "":
    		user_input = "?"

        path = sublime.packages_path() + "\\FoxCode\\Bats\\"
    	self.window.run_command("exec",{"cmd":["start.bat",path+"modistru.fxp",user_input],"working_dir": path})
    	pass 

import sublime, sublime_plugin  
import os
import re

class FoxproRunCommand(sublime_plugin.WindowCommand):  
    def run(self):
        self.window.show_input_panel("Do ", "", self.on_done, None, None)
    	pass

    def on_done(self,user_input):
    	if user_input == "":
    		user_input = self.window.active_view().file_name()

    	path = sublime.packages_path() + "\\FoxCode\\Bats\\"
    	self.window.run_command("exec",{"cmd":["start.bat",user_input],"working_dir": path})    	
