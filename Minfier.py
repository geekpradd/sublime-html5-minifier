import sublime, sublime_plugin, urllib.request,urllib.parse,os,sys
sys.path.append(os.path.join(os.path.dirname(__file__), "modules"))
from HTMLMinifier import minify




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

      data={'js_code':content,'compilation_level':'WHITESPACE_ONLY','output_format':'text','output_info':'compiled_code'}
      d=urllib.parse.urlencode(data)
      d=d.encode('utf-8')
      req=urllib.request.urlopen('http://closure-compiler.appspot.com/compile',d)
      code=str(req.read())[2:-3:]

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
      data={'input':content}
      d=urllib.parse.urlencode(data)
      d=d.encode('utf-8')
      req=urllib.request.urlopen('http://cssminifier.com/raw',d)
      code=str(req.read())[2:-1:]
      file=open(self.path,'w')
      file.write(code)
      file.close()
      self.view.window().open_file(self.path)


