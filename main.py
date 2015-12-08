# If you use this code please read the LICENSE included
# Created by @lifestealrxx on Twitter :)

import socket, time

channel = '#twitchuser'

sockets = []

class irc:
    @staticmethod
    def main(channel, user, pw, sock):
        sock.send('PASS %s\r\n' %pw)
        sock.send('NICK %s\r\n' %user)
        sock.send('JOIN %s\r\n' %channel)
		
def main():
    with open('accounts', 'r') as accts:
        for act in accts:
            acct = act.split(':', 1)

            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.connect(('irc.twitch.tv', 6667))

            sockets.append(sock)
            
            irc.main(channel,
                    acct[0],
                    acct[1],
                    sock)

main()

exit()
