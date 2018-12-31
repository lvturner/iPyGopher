import ui
from web_delegate import WebViewDelegate
from gopher_client import GopherClient


class MainApp(object):
    def __init__(self):
        self.v = ui.load_view()
        self.v['webview'].delegate = WebViewDelegate()
        self.wv = self.v['webview']
        self.ab = self.v['addressBar']
        self.v.present('fullscreen')
        self.v['goBtn'].action = self.go_tapped
        self.wv.load_url('file://sdf.org:70/phlogs')
        
    @ui.in_background
    def go_tapped(self, sender):
        self.wv.load_url('sdf.org:70/phlogs')
MainApp()
