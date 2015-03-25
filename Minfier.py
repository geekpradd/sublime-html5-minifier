import threading
import os
import sys
import platform
import sublime
import sublime_plugin
sys.path.append(os.path.join(os.path.dirname(__file__), "modules"))
from htmlmin import minify as htmlminify
from jsmin import jsmin as jsminify
from csscompressor import compress as cssminify

extensions = ['js', 'css', 'html', 'htm']
IS_WINDOWS = platform.system() == "Windows"


def return_minified(data, extension):
    if extension == 'css':
        return cssminify(data)
    elif extension == 'js':
        return jsminify(data)
    else:
        return htmlminify(data)


class MinifierCommand(sublime_plugin.TextCommand):

    def get_content(self):
        allcontent = sublime.Region(0, self.view.size())
        content = self.view.substr(allcontent)
        return content

    def location_params(self):
        self.location = self.view.file_name()
        if IS_WINDOWS:
            self.name = self.location.split('\\')[-1]
        else:
            self.name = self.location.split('/')[-1]

        self.folder = self.location.replace(self.name, '')
        self.extension = self.name.split('.')[-1]
        self.n = self.name.replace(self.extension, '')
        self.path = self.folder + self.n + 'min.' + self.extension

        return [self.location, self.name, self.folder, self.extension, self.n, self.path]

    def run(self, edit):
        td = threading.Thread(target=self.main)
        td.start()

    def main(self):
        self.content = self.get_content()
        self.locations = self.location_params()
        self.minifiedLocation = self.locations[-1]
        self.minifiedExtension = self.locations[3]
        t = threading.Thread(target=self.write_minified)
        t.start()

    def write_minified(self):
        if self.minifiedExtension in extensions:
            if os.path.isfile(self.minifiedLocation):
                content = return_minified(self.content, self.minifiedExtension)
                with open(self.minifiedLocation, 'w') as file:
                    file.write(content)
            else:
                content = return_minified(self.content, self.minifiedExtension)
                open(self.minifiedLocation, 'w').close()
                with open(self.minifiedLocation, 'w') as file:
                    file.write(content)

            window = sublime.active_window()
            self.view.window().open_file(self.minifiedLocation)
