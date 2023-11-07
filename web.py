from http.server import HTTPServer, BaseHTTPRequestHandler
content = """
<!DOCTYPE html>
<html>
<title> image map </title>

 <body>

   <table border="4" cellspacing-"8" cellspacing="7"> 

<caption> Top Five Generating Software Companies </caption>

<tr>

<th>S.No</th>

<th>Company</th>

<th>Revenue</th>

</tr>
<tr>

<th>1</th>

<td>Microsoft</td>

<td>65 Billion</td>

</tr>

<tr>

<th>2</th>

><td>Oracle</td>

<td>29.6 Billlion</td>

</tr>

<tr>

<th>3</th>

<td>IBM</td>

<td>29.1 Billon</td>

</tr>

<tr>

<th>4</th>

<td>SAP</td>

<td>6.4 Billion</td>

</tr>

<tr>

<th>5</th>

<td>Symantec</td>

<td>5.6 Billon</td>

</tr>

   </table border>

 </body>

</html>
"""
class myhandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print("request received")
        self.send_response(200)
        self.send_header('content-type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(content.encode())
server_address = ('',8000)
httpd = HTTPServer(server_address,myhandler)
print("my webserver is running...")
httpd.serve_forever()