import sublime, sublime_plugin  
import re

class foxconsole(sublime_plugin.WindowCommand):  
    def run(self):
      path = sublime.packages_path() + "\\FoxCode\\Bats\\"
    	self.window.run_command("exec",{"cmd":["start.bat"],"working_dir": path})
