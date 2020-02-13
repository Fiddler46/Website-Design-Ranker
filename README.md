# Website Design Ranker

Website Design Ranker is a program that takes URLs as input and ranks the website's designs against each other.
Each website is scrapped through to find the number of colours contained in the elements of the website, which is then used as a rank parameter to rank them against each other.
Currently, this program is only supported on Linux and any Ubuntu based distros. A Windows/OS X release is not considered at this time.

**Prerequisites**

Before running the program, there are a few Python packages that the system must contain in order for it to function properly. All of these require Python3 to be installed on the system beforehand:
    
    `$ sudo apt-get install python3.6`

*  **Beautiful Soup**

Beautiful Soup is a Python package for parsing HTML and XML documents. It creates a parse tree for parsed pages that can be used to extract data from HTML, which is useful for web scraping. 

Installation code:
    `pip3 install beautifulsoup4`
    
* **Requests**

The requests library is the de facto standard for making HTTP requests in Python. It abstracts the complexities of making requests behind a beautiful, simple API so that a user can focus on interacting with services and consuming data in an application.
Requests allows you to send HTTP/1.1 requests extremely easily. There’s no need to manually add query strings to your URLs, or to form-encode your POST data. 

Installation code:
    `pip3 install requests`
    
* **PyQt**

PyQt is a Python binding of the cross-platform GUI toolkit Qt, implemented as a Python plug-in. PyQt is a blend of Python programming language and the Qt library.

Installation code:
    `pip3 install PyQt5`
    
**Running the Program**

Once all the above packages have been installed, run *wederan.py* file from within the ui folder of the main program folder.

    `python3 wederan.py`
    
Now, insert any number of URLs into the "Input" text box and press the "Rank" button.
The output ranks should be visible within the "Output" text box for the corresponding website.