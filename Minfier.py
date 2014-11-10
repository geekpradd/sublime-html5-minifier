import sublime, sublime_plugin, urllib.request,urllib.parse,os,sys
sys.path.append(os.path.join(os.path.dirname(__file__), "modules"))
from HTMLMinifier import minify
from jsmin import jsmin
import cssmin



class MinifierCommand(sublime_plugin.TextCommand):
  def run(self, edit):

    allcontent=sublime.Region(0,self.view.size())
    content=self.view.substr(allcontent)


    self.location=self.view.file_name()
    self.name=self.location.split('\\')[-1]
    self.folder=self.location.replace(self.name,'')
    self.extension=self.name.split('.')[-1]
    self.n=self.name.replace(self.extension,'')
    self.path=self.folder+self.n+'min.'+self.extension

    if  self.extension == 'js':


      code=jsmin(content)

      file=open(self.path,'w')
      file.write(code)
      file.close()
      self.view.window().open_file(self.path)
    elif self.extension=='html' or self.extension=='htm':
      code=minify(content)

      file=open(self.path,'w')
      file.write(code)
      file.close()
      self.view.window().open_file(self.path)
    elif self.extension=='css':

      code=cssmin.cssmin(content)
      file=open(self.path,'w')
      file.write(code)
      file.close()
      window=sublime.active_window()
      self.view.window().open_file(self.path)


