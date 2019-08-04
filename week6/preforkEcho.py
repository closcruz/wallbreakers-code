import os
import socket
import sys
# import socketserver

# class ForkHandler(socketserver.StreamRequestHandler):
#     def handle(self):
#         self.wfile.write("Child {} ECHO".format(os.getpid()))
#         self.wfile.flush()
#         msg = self.rfile.readline()
#         self.wfile.write(msg)
#         print("Child {} ECHO'D: {}".format(os.getpid(), msg))

# if __name__ == "__main__":    
#     srv = socketserver.ForkingTCPServer(('localhost', 4242), ForkHandler)
#     print('Server listening on localhost:4242...')
#     try:
#         srv.serve_forever()
#     except KeyboardInterrupt:
#         print('\nStopping')
SERVER_ADDR = ('localhost', 4242)

sock = socket.socket()
sock.bind(SERVER_ADDR)
sock.listen(10)

for _ in range(3):
    pid = os.fork()

    if pid == 0:
        cpid = os.getpid()
        print("Child {} listening on localhost:4242".format(cpid))

        try:
            while True:
                con, adr = sock.accept()

                fl = con.makefile()
                fl.write("Child {} echo".format(cpid))
                fl.flush()
                msg = fl.readline()
                fl.write(msg)
                con.close()
                print("Child {} echo'd: {}".format(cpid, msg.strip()))
        except KeyboardInterrupt:
            sys.exit()