import ui
import console
from web_delegate import WebViewDelegate
from gopher_client import GopherClient


class MainApp(object):
    def __init__(self):
        self.v = ui.load_view()
        self.wvd = WebViewDelegate(self)
        self.v['webview'].delegate = self.wvd
        self.wv = self.v['webview']
        self.ab = self.v['addressBar']
        self.v.present('fullscreen')
        self.v['goBtn'].action = self.go_tapped
        self.v['back_button'].action = self.wvd.go_back
        self.wv.load_url('file://1_gopherproject.org:70/')
        
    @ui.in_background
    def go_tapped(self, sender):
        if "://" in self.ab.text:
            console.alert("Please don't use gopher:// or similar, just use host:port/selector")
        else:
            self.wv.load_url("file://1_" + self.ab.text)
    
    def go_back(self, sender):
        print("Go back called in main")
        self.wv.delegate.go_back()
MainApp()
