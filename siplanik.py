#    Copyright 2014 Philippe THIRION
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.

#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.

#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.

import sipfullproxy
from sipfullproxy import UDPHandler
import logging
import socketserver
import socket
import logging


HOST = '192.168.0.181'
PORT = 5060

logging.basicConfig(format='%(asctime)s:%(message)s',filename='dennik_hovorov.log',level=logging.INFO)

hostname = socket.gethostname()
sipfullproxy.ipaddress = socket.gethostbyname(hostname)

sipfullproxy.recordroute = "Record-Route: <sip:%s:%d;lr>" % (HOST,PORT)
sipfullproxy.topvia = "Via: SIP/2.0/UDP %s:%d" % (HOST,PORT)

server = socketserver.UDPServer((HOST, PORT), UDPHandler)
print("HOST:" + str(HOST) +"    PORT:" +str(PORT))
server.serve_forever()