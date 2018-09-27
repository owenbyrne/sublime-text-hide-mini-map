import sublime
import sublime_plugin

def plugin_loaded():
  sublime.active_window().run_command("hide_mini_map")

class HideMiniMapCommand(sublime_plugin.WindowCommand):
  def run(self):
    self.window.set_minimap_visible(False)
