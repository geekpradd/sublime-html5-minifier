#Sublime HTML5 Minifier

<a href="https://packagecontrol.io/packages/HTML%20Minifier"><img src="https://packagecontrol.herokuapp.com/downloads/HTML%20Minifier.svg"></a>

This is a Sublime Text 3 Plugin for reducing the code size of HTML5, CSS3 and Javascript files. 

##Installation

This plugin can be installed by searching for HTML Minifier on Package Control in Sublime Text 3. 

You can install Package Control by following these steps: [https://sublime.wbond.net/installation](https://sublime.wbond.net/installation)

##Usage

In order to minify code, Click on the Tools menu and click Minify Current File. A .min file be added onto the current directory where you are working. 

Alternatively, Right Click on the Editor area or the sidebar and click 'Minify HTML5 File'.

For example, if you are working on a file 'main.css' in the location 'C:\Projects\' then a minified file will be created at 'C:\Projects\' with the name main.min.css making the full path 'C:\Projects\main.min.css'.

This is done to keep two versions of the codebase, one minified and the other development version.

If you want to overwrite your file, such that the minified version of say `main.html` should be written to `main.html` inplace of `main.min.html`, click on Tools - Minify HTML5 File (modify existing)

####Command Palllete

Press Ctrl+Shift+P and then type `Minify File`. You have two options:
If you want to create a new file, then click on "HTML Minfier: Minify File (create new)" or if you want to write to the current file, then click on "HTML Minfier: Minify File (modify existing)"

##Change Log

Version 1.1 contains the following changes in the plugin:

- Minifying Process runs in a separate thread

- Source has been streamlined on the principles of OOP

- Already Minified versions of the file will open up in the Sublime Window, instead of no output being shown.

- Performance Improvements

- Javascript Not Opening Bug Fixed 


Version 1.2

- Performance Optimisations
- Bug Fixing
- Module changing for better support

Version 1.3 

- Mac OS X Bug fixes 
- Code uses PEP8 
- Better Linux Support

Version 1.4 

- Ability to Minify Files in the same file instead of creating a new file 
- Commands for Command Pallete 
- Switch Menu to Tools 

##About 

This Plugin uses Closure Compiler for Javascript compilation, CSS Minifier for CSS and HTML5Minifier for HTML.

Created By Pradipta aka GeekPradd