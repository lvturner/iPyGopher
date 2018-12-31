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
        #print("webview failed")
        #print(error_code)
        #print(error_msg)
        pass
    
    def print_welcome(self, webview):
        print("print_welcome")
        webview.load_html("<center><h1>Welcome to iPyGopher</h1></center>")
        return True
        
    def parse_url(self, url):
        item = GopherItem()
        host_port = url.split('/')[2].split(":")
        
        item.host = host_port[0]
        if not host_port[1]:
            item.port = 70
        else:
            item.port = host_port[1]
        
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
            self.history.append(url)
            self.main.ab.text = url[7:]
            #lazy hack
            self.wv = webview
            print("Loading gophers")
            item = self.parse_url(url)
            #item = GopherItem()
            #item.host = 'sdf.org'
            #item.port = 70
            #item.selector = '/phlogs'
            g = GopherClient()
            txt = g.get(item.host, item.port, item.selector)
            webview.load_html(self.header + txt + self.footer)
            
            return True
        return False
        
    def go_back(self, sender):
        print("Go back called")
        for x in range(len(self.history)):
            print(self.history[x])
        print(len(self.history))
        # get rid of the current url... this feels wrong, probably is
        if len(self.history) > 1:
            self.history.pop()
            self.wv.load_url(self.history.pop())
