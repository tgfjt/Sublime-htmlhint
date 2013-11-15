import os, sublime, sublime_plugin

package = "Htmlhint"

class HtmlhintCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        filepath = self.view.file_name()
        packages = sublime.packages_path()
        pluginpath = packages + "/Sublime-htmlhint"
        htmlhintpath = pluginpath + "/HTMLHint"

        args = {
            "cmd": [
                htmlhintpath + "/bin/htmlhint",
                filepath,
                "-f",
                "nocolor",
                "-c",
                pluginpath + "/.htmlhintrc"
            ]
        }

        if sublime.platform() == "windows":
            args['cmd'][0] += ".cmd"
        elif sublime.platform() == "osx":
            args['path'] = "/usr/local/share/npm/bin:/usr/local/bin:/opt/local/bin:$HOME/.nodebrew/current/bin:$PATH"

        self.view.window().run_command('exec', args)
