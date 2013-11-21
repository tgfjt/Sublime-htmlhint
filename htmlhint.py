import os, sublime, sublime_plugin
import subprocess

try:
    import commands
except ImportError:
    pass

PACKAGE = 'Sublime-htmlhint'
SETTINGS_FILE = PACKAGE + '.sublime-settings'
HTMLHINTRC = '/.htmlhintrc'
HTMLHINT_ERROR = 'htmlhint_errors'

class HtmlhintCommand(sublime_plugin.TextCommand):
    def run(self, edit, show_regions=True, show_panel=True):
        view = self.view
        view.erase_regions(HTMLHINT_ERROR)
        filepath = view.file_name()
        packagespath = sublime.packages_path()
        pluginpath = packagespath + '/' + PACKAGE
        htmlhintpath = pluginpath + '/HTMLHint'

        settings = sublime.load_settings(SETTINGS_FILE)

        htmlhintrc = settings.get('htmlhintrc')

        if htmlhintrc == None:
            htmlhintrc = htmlhintpath + HTMLHINTRC

        nodepath = settings.get('node_path')

        cmd = [nodepath, htmlhintpath + '/bin/htmlhint', filepath, '-f', 'sublime', '-c', htmlhintrc]

        output = get_output(cmd)

        regions = []
        menuitems = []

        for line in output.decode().splitlines():
            try:
                lineNo, columnNo, description = line.split(':: ')
                text_point = view.text_point(int(lineNo) - 1, int(columnNo))
                region = view.word(text_point)
                menuitems.append('L' + lineNo + ':C' + columnNo + ' ' + description)
                regions.append(region)
            except:
                pass

        self.add_regions(regions)
        self.view.window().show_quick_panel(menuitems, self.on_chosen)

    def on_chosen(self, index):
        if index == -1:
          return

        region = self.view.get_regions(HTMLHINT_ERROR)[index]
        selection = self.view.sel()
        selection.clear()
        selection.add(region)
        self.view.show(region)

    def add_regions(self, regions):
        view = self.view
        if int(sublime.version()) >= 3000:
          icon = 'Packages/' + PACKAGE + '/icon/warn.png'
          view.add_regions(HTMLHINT_ERROR, regions, 'keyword', icon,
            sublime.DRAW_EMPTY |
            sublime.DRAW_NO_FILL |
            sublime.DRAW_NO_OUTLINE |
            sublime.DRAW_SQUIGGLY_UNDERLINE |
            sublime.HIDE_ON_MINIMAP)
        else:
          icon = '../' + PACKAGE + '/icon/warn'
          view.add_regions(HTMLHINT_ERROR, regions, 'keyword', icon,
            sublime.DRAW_EMPTY |
            sublime.DRAW_OUTLINED |
            sublime.HIDE_ON_MINIMAP)

def get_output(cmd):
    if int(sublime.version()) < 3000:
        if sublime.platform() != 'windows':
            # Linux and OSX(Python2
            run = '"' + '" "'.join(cmd) + '"'
            return commands.getoutput(run)
        else:
            # Windows(Python2

            # http://stackoverflow.com/questions/1813872/running-a-process-in-pythonw-with-popen-without-a-console
            startupinfo = subprocess.STARTUPINFO()
            startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW

            return subprocess.Popen(cmd, stdout=subprocess.PIPE, startupinfo=startupinfo).communicate()[0]
    else:
        # Python3
        return subprocess.check_output(cmd, stderr=subprocess.PIPE)

