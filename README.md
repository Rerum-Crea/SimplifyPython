&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[![GitHub issues](https://img.shields.io/github/issues/Necrownyx/SimplifyPython)](https://github.com/Necrownyx/SimplifyPython/issues) [![GitHub forks](https://img.shields.io/github/forks/Necrownyx/SimplifyPython)](https://github.com/Necrownyx/SimplifyPython/network) [![GitHub stars](https://img.shields.io/github/stars/Necrownyx/SimplifyPython)](https://github.com/Necrownyx/SimplifyPython/stargazers) [![GitHub license](https://img.shields.io/github/license/Necrownyx/SimplifyPython)](https://github.com/Necrownyx/SimplifyPython/blob/main/LICENSE) [![Python](https://img.shields.io/badge/Made%20with-Python-%2300AEFF)](https://python.org) [![Python](https://img.shields.io/badge/Available%20on-PyPi-%2300AEFF)](https://pypi.org/project/SimplifyPython/) [![Hits](https://hits.seeyoufarm.com/api/count/incr/badge.svg?url=https%3A%2F%2Fgithub.com%2FNecrownyx%2FSimplifyPython&count_bg=%2300AEFF&title_bg=%23555555&icon=&icon_color=%23E7E7E7&title=hits&edge_flat=false)](https://hits.seeyoufarm.com)  
<pre align="center">  
███████╗██╗███╗   ███╗██████╗ ██╗     ██╗███████╗██╗   ██╗  
██╔════╝██║████╗ ████║██╔══██╗██║     ██║██╔════╝╚██╗ ██╔╝  
███████╗██║██╔████╔██║██████╔╝██║     ██║█████╗   ╚████╔╝   
╚════██║██║██║╚██╔╝██║██╔═══╝ ██║     ██║██╔══╝    ╚██╔╝    
███████║██║██║ ╚═╝ ██║██║     ███████╗██║██║        ██║     
╚══════╝╚═╝╚═╝     ╚═╝╚═╝     ╚══════╝╚═╝╚═╝        ╚═╝     
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;built by @Necrownyx</pre>  
  
# Simplify Python  
This is a python package designed to reduce the need for code to be over-complex by providing one-line solutions to problems.  
  
## Features list  
1. Json: Json is a package widely used for data storage.  
2. print: print is used to print to the terminal.
  
More coming soon.  
  
# Documentation  
  
This is a section for the documentation for all of the modules in the package.  
<br>  
## Json  
  
#### First import the Json branch of the package with:  
  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`from SimplifyPython import sjson`  
  
#### Then you can choose to create a file with:  
  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`sjson.new(filename)`  
  
where filename is either the name of a `json` file without the `.json` or a filename with an extension for example `data.app.json`.  
  
#### Or if you already have a file you can read it with:  
  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`data = sjson.open(filename)`  
  
where filename is either the name of a file. This will set the data variable to be the contents of the json file.  
  
#### Then when you are finished editing the data you can run:  
  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`sjson.save(data, filename)`  
  
where data is the edited data to be put in the `json` file and filename is either the name of a file.

## Print

#### First import the print branch with:

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`from SimplifyPython import sprint`

#### Then to use the package type:

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`sprint.{color}(message)

Where color is a color from the below list and treat message like a normal print command arguments.

1. red
2. pink
3. purple
4. blue
5. lightblue
6. brightblue
7. green
8. lightgreen
9. yellow
10. orange

This will print in the color of your choice.

## Flask

First import the package with:

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`pip install PingServer`

Then import it with:

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`import PingServer`

Then add this one line to start the server:

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`PingServer.start()`

The `start()` command has an optional parameter for a message on the web page to be pinged.

#### How to run on a thread.
If you want to run the server on its own thread you can put this in your code:

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`PingServer.thread().start()`

This module of the package can also take a custom message for example:

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`PingServer.thread("hello, world!").start()`

Will output "hello, world!" on the webpage.

#### How to serve multiple pages.
If you want to serve multiple different pages first create the page use either:

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`PingServer.create_page(route, message)`

with `route` being the route of the site for example: `'/'`  and `message` being the message to be served to users or a html file name for example `index.html` this file must be in the templates directory of your project.

You can loop through this as many times as you want.

Then when you have defined all of the pages for your site run:

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`PingServer.launch_pages().start()`

To run all the sites on a thread or:

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`PingServer.launch_pages_nothread()`

To run the sites on the main thread.