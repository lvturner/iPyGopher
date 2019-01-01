import socket
import console
import urllib
from gopher_item import GopherItem


class GopherClient(object):
    def parse_content(self, data):
        lines = data.split('\r\n')
        arr = []
        for x in range(len(lines)):
            arr.append(self.build_item(lines[x]))
            
        data = self.build_html(arr)
        
        return data
    
    def build_item(self, data):
        #print("Building from: " + data)
        item = GopherItem()
        if not data or data == '.':
            return
        item.type = data[0]
        data = data[1:]
        sp = data.split('\t')
        item.name = sp[0].replace(' ', '&nbsp')
        item.selector = sp[1]
        item.host = sp[2]
        item.port = sp[3]
        print("Selector: " + item.selector)      
        return item
    
    def build_html(self, data):
        ret = ''
        for i in range(len(data)):
            item = data[i]
            if not item:
                break
            if item.type == 'h':
                ret += "<a href='file://" + item.selector + "'>" + item.name + "</a>"
            elif item.type == 'i':
                ret += item.name
            else:
                ret += "<a href='file://" + item.type + "_" + item.host + ":" + item.port + item.selector + "'>" + item.name + "</a>"
            ret += "<br />"
        return ret
                
    def get(self, type, host, port, selector):
        print(type)
            
        self.curr_host = host
        self.curr_port = port
        HOST = host    # The remote host
        PORT = int(port)              # The same port as used by the server
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((HOST, PORT))
            s.sendall(str(urllib.parse.unquote(selector) + '\r\n').encode())
            data = b''
            while True:
                temp = s.recv(1024)
                if not temp:
                    break
                data += temp
        #print(str(data).replace('\\r\\n', '\r\n'))
        #Getting too tired and stupid now...
        try:
            content = self.parse_content(str(data.decode('UTF-8', errors="ignore")))
        except:
            content = "<pre>" + str(data.decode('UTF-8')) + "</pre>"
        
        return content

        
    
