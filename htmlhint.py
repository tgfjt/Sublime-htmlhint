import os, sublime, sublime_plugin

package = "Sublime-htmlhint"
SETTINGS_FILE = package + ".sublime-settings"

class HtmlhintCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        filepath = self.view.file_name()
        packages = sublime.packages_path()
        pluginpath = packages + "/Sublime-htmlhint"
        htmlhintpath = pluginpath + "/HTMLHint"

        settings = sublime.load_settings(SETTINGS_FILE)

        htmlhintrc = settings.get("htmlhintrc")[0]

        if htmlhintrc == None:
            htmlhintrc = htmlhintpath + ".htmlhintrc"

        args = {
            "cmd": [
                htmlhintpath + "/bin/htmlhint",
                filepath,
                "-f",
                "nocolor",
                "-c",
                htmlhintrc
            ]
        }
        

        if sublime.platform() == "windows":
            args['cmd'][0] += ".cmd"
        elif sublime.platform() == "osx":
            args['path'] = "/usr/local/share/npm/bin:/usr/local/bin:/opt/local/bin:$HOME/.nodebrew/current/bin:$PATH"

        self.view.window().run_command('exec', args)
