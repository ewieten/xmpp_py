import dns
from xmpp import *
import urllib2
import ConfigParser
import time
import sys
import os
import pyglet
print('Imported succesfully.')

group = 'group-738@muc.xmpp.evolvehq.com'

config = ConfigParser.ConfigParser()
config.read('bot.conf')
user=config.get('logondata','user')
passw=config.get('logondata','password')
server=config.get('logondata','server')
msg=config.get('botdata','spammessage')
target=config.get('botdata','spamtarget')
print('Config loaded succesfully.')

group = group+"/"+user
print(group)
client=Client('xmpp.evolvehq.com')
client.connect()

if client.auth(user,passw):
    print('Connected!')
else:
    print('Invalid credentials')

def messageHandler(conn,mess_node): pass

client.RegisterHandler('message',messageHandler)
print('Handlers Registered')

client.send(Presence(to=epic))

while True:
    client.send(Message(group,msg))
