import sublime, sublime_plugin, urllib.request,urllib.parse,os,sys, threading

sys.path.append(os.path.join(os.path.dirname(__file__), "modules"))

from htmlmin import minify
from jsmin import jsmin
import cssmin



class MinifierCommand(sublime_plugin.TextCommand):
  def getContent(self):
    allcontent=sublime.Region(0,self.view.size())
    content=self.view.substr(allcontent)
    return content
  def locationParams(self):
    self.location=self.view.file_name()
    self.name=self.location.split('\\')[-1]
    self.folder=self.location.replace(self.name,'')
    self.extension=self.name.split('.')[-1]
    self.n=self.name.replace(self.extension,'')
    self.path=self.folder+self.n+'min.'+self.extension

    return [self.location,self.name,self.folder,self.extension,self.n,self.path]
  def run(self, edit):


    td=threading.Thread(target=self.exists)
    td.start()



  def exists(self):
    self.content=self.getContent()
    self.locations=self.locationParams()
    t=threading.Thread(target=self.writeMinified)
    t.start()


  def writeMinified(self):
    if  self.locations[3] == 'js':


        code=jsmin(self.content)

        with open(self.locations[-1],'w') as file:
            file.write(code)

        self.view.window().open_file(self.locations[-1])
    elif self.locations[3]=='html' or self.locations[3]=='htm':
        code=minify(self.content)

        with open(self.locations[-1],'w') as file:
            file.write(code)

        self.view.window().open_file(self.locations[-1])
    elif self.locations[3]=='css':

        code=cssmin.cssmin(self.content)
        with open(self.locations[-1],'w') as file:
            file.write(code)
        window=sublime.active_window()
        self.view.window().open_file(self.locations[-1])


