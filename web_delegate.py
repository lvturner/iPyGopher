import console

class WebViewDelegate (object):    
    def webview_should_start_load(self, webview, url, nav_type):
        return True
        
    def webview_did_start_load(self, webview):
        pass
        
    def webview_did_finish_load(self, webview):
        pass
        
    def webview_did_fail_load(self, webview, error_code, error_msg):
        pass
        
    def load_gopher(self, uri):
        console.alert(uri)
