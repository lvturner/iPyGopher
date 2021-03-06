import console
import webbrowser
import urllib
from gopher_client import GopherClient
from gopher_item import GopherItem

class WebViewDelegate (object):
    header = """
    <html>
        <head>
        <style>
            body {
                font-family: "Courier New", Courier, monospace;
            }
            a {
                text-decoration: none;
            }
            pre {
            	font-family: "Courier New", Courier, monospace;
            }
        </style>
        </head>
            <body>
    """
    
    footer = """
        </body>
    </html>
    """
    history = []
    
    def __init__(self, main):
        self.main = main
    
    def webview_should_start_load(self, webview, url, nav_type):
        print(url)
        if "file://URL:" in url:
            if "URL:http" in url:
                url = url.replace("file://URL:", 'safari-')
            else:
                url = url.replace("file://URL:", '')
            webbrowser.open(url)
            return False
        self.url = url
        return True
        
    def webview_did_start_load(self, webview):
        print("Webview start load with " + self.url)
        if self.url == 'about:blank':
            return False
        elif self.url == 'about:welcome':
            return self.print_welcome(webview)
        else:
            return self.load_gopher(webview, self.url)
        
        return True
        
    def webview_did_finish_load(self, webview):
        #print("Webview finished loading")
        pass
        
    def webview_did_fail_load(self, webview, error_code, error_msg):
        print("webview failed")
        #print(error_code)
        #print(error_msg)
        pass
    
    def print_welcome(self, webview):
        print("print_welcome")
        webview.load_html("<center><h1>Welcome to iPyGopher</h1></center>")
        return True
        
    def parse_url(self, url):
        item = GopherItem()
        print("Using url: " + url)
        item.url = url
        type_host_port = url.split('/')[2].split(":")
        print(type_host_port)
        
        item.type = type_host_port[0].split("_")[0]
        item.host = type_host_port[0].split("_")[1]
        if not type_host_port[1]:
            item.port = 70
        else:
            item.port = type_host_port[1]
        
        selectors = url.split('/')[3:]
        item.selector = ''
        for x in range(len(selectors)):
            item.selector += "/" + selectors[x]
        print("Parsed selector: " + item.selector)
        
        return item
        
    def load_gopher(self, webview, url):
        print("load_gopher")
        print(url)
        if url.startswith('file://'):
            #lazy hack
            self.wv = webview
            print("Loading gophers")
            item = self.parse_url(url)
            if item.type == '7' and not "?" in item.selector:
                # only prompt if the selector doesn't have a search term
                print("Type is search")
                search = console.input_alert("Enter search term")
                item.selector += "?" + search
                url += "?" + search #laaazzzy
            elif item.type == '9' or item.type == 'g' or item.type == '4' or item.type == '5':
                print("Unsupported link: " + url)
                console.alert("Binary file download currently not supported")
                return
            elif item.type == 'h':
                print(url)
                console.alert("H")
                return
            self.history.append(url)
            self.main.ab.text = urllib.parse.unquote(url[9:])

            g = GopherClient()
            
            txt = g.get(item.type, item.host, item.port, item.selector)
            webview.load_html(self.header + txt + self.footer)
        return True
        
    def go_back(self, sender):
        print("Go back called")
        for x in range(len(self.history)):
            print(self.history[x])
        print(len(self.history))
        # get rid of the current url... this feels wrong, probably is
        if len(self.history) > 1:
            self.history.pop()
            load_url = self.history.pop()
            print("Loading url: " + load_url)
            self.wv.load_url(load_url)
