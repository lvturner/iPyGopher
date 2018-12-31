import ui
from web_delegate import WebViewDelegate

class MainApp(object):
    def __init__(self):
        self.v = ui.load_view()
        self.wv = WebViewDelegate()
        self.v['webview'].delegate = self.wv
        self.ab = self.v['addressBar']
        self.v.present('fullscreen')
        self.v['goBtn'].action = self.go_tapped
        
    @ui.in_background
    def go_tapped(self, sender):
        self.wv.load_gopher(self.ab.text)

MainApp()