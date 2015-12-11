import socket, time, urllib2, json
channel = '#' + 'tryhard_clan'
sockets = []
sockets2 = []
def login(channel, user, pw, sock):
    sock.send('PASS {}\r\n'.format(pw))
    sock.send('NICK {}\r\n'.format(user))
    sock.send('JOIN {}\r\n'.format(channel))
def main():
    with open('accounts', 'r') as accts:
        for act in accts:
            acct = act.split(':', 1)
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.connect(('irc.twitch.tv', 6667))
            sock2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock2.connect(('192.16.64.212', 443))
            sockets.append(sock)
            sockets2.append(sock2)
            login(channel, acct[0], acct[1], sock)
            login('#jtv', acct[0], acct[1], sock2)
def console():
    global channel
    while True:
        line = raw_input()
        cmd = line.split(' ')        
        if cmd[0] == 'global':
            for x in range(len(sockets)):
                sockets[x].send('PRIVMSG {} :{}\r\n'.format(channel, cmd[1]))
        elif cmd[0] == 'globalw':
            for x in range(len(sockets2)):
                data = json.load(urllib2.urlopen('http://tmi.twitch.tv/group/user/{}/chatters'.format(channel.split('#')[1])))
                users = data['chatters']['viewers']
                for usr in users:
                    sockets2[x].send('PRIVMSG #jtv :/w {} {}\r\n'.format(usr, cmd[1]))
                    time.sleep(.2)
        elif cmd[0] == 'sing':
            lyrics = open(cmd[1])
            for line in lyrics:
                for x in range(len(sockets)):
                    sockets[x].send('PRIVMSG {} :{}\r\n'.format(channel, line))
                    time.sleep(2)
        elif cmd[0] == 'join':
            for x in range(len(sockets)):
                sockets[x].send('PART {}\r\n'.format(channel))
                sockets[x].send('JOIN {}\r\n'.format(cmd[1]))
                channel = cmd[1]
main()
console()
