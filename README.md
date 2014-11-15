#Sublime HTML5 Minifier

This is a Sublime Text 3 Plugin for reducing the code size of HTML5, CSS3 and Javascript files. 

##Installation

This plugin can be installed by searching for HTML Minifier on Package Control in Sublime Text 3. 

You can install Package Control by following these steps: [https://sublime.wbond.net/installation](https://sublime.wbond.net/installation)

##Usage

In order to minify code, Click on the HTML5 Minifier option and click Minify Current File. A .min file be added onto the current directory where you are working. 

Alternatively, Right Click on the Editor area or the sidebar and click 'Minify HTML5 File'.

For example, if you are working on a file 'main.css' in the location 'C:\Projects\' then a minified file will be created at 'C:\Projects\' with the name main.min.css making the full path 'C:\Projects\main.min.css'.

This is done to keep two versions of the codebase, one minified and the other development version

##What's new in Version 1.1?

Version 1.1 contains the following changes in the plugin:

- Minifying Process runs in a separate thread

- Source has been streamlined on the principles of OOP

- Already Minified versions of the file will open up in the Sublime Window, instead of no output being shown.

- Performance Improvements

- Javascript Not Opening Bug Fixed 

Version 1.1.1

- Changed HTML minify module from HTML Minfier to htmlmin

- Improved performance and reliability thanks to htmlmin

- File Auto Open if exists not working bug fixed


##A Request to OSX and Linux Users

If you have installed this package, and you are finding issues with the Plugin on OSX and Linux (I can't test the plugin on these platforms), Please open a Issue Thread on GitHub and I'll try to solve it.

##About 

This Plugin uses Closure Compiler for Javascript compilation, CSS Minifier for CSS and HTML5Minifier for HTML.

Created By Pradipta aka GeekPradd