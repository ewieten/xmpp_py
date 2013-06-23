import dns
from xmpp import *
import urllib2
import ConfigParser
import time
import sys
import os
import pyglet
print('Imported succesfully.')

config = ConfigParser.ConfigParser()
config.read('bot.conf')
user=config.get('logondata','user')
passw=config.get('logondata','password')
server=config.get('logondata','server')
msg=config.get('botdata','spammessage')
target=config.get('botdata','spamtarget')
target=target+"@"+server
debug=config.get('botdata','debug')
print('Config loaded succesfully.')

if debug=1:
    client=Client('xmpp.evolvehq.com',debug=['always'])
else:
    client=Client('xmpp.evolvehq.com')

client.connect()
print('Connected')

if client.auth(user,passw):
    print('Authenticated.')
else:
    print('Invalid credentials')
    exit

def messageHandler(conn,mess_node): pass

client.RegisterHandler('message',messageHandler)
print('Handlers Registered')

while True:
    client.send(Message(target,msg))
