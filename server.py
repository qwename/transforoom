# Copyright 2015 Yixin Zhang
# 
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# 
#     http://www.apache.org/licenses/LICENSE-2.0
# 
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import __main__
import logging
import sys
import sqlite3
from twisted.internet import reactor, protocol

logging.basicConfig(filename='server_log.txt', level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")


class Global():
    server = None
    online = False
    VERSION = 35
    VERBOSE = True
    LOGVERBOSE = True
    SERVERS = dict(enumerate(['EN', 'FR', 'RU', 'BR', 'ES', 'CN', 'TR', 'VK', '*']))

world = Global()

class TransforoomProtocol(protocol.Protocol)
    
    recvd = ""
    structFormat = "!I"

    def dataReceived(self, data):
        if data == '<policy-file-request/>\x00' or data == 'SuperBelette\x00':
            self.flashPolicyRequest(data)
        else:
            self.recvd += data
        while not self.recvd == '':
            datalength = len(self.recvd)
            if datalength>=4:
                packetlength = int((struct.unpack('%sL' % '!', self.recvd[:4]))[0])
                if datalength == packetlength:
                    self.stringReceived(self.recvd[4:])
                    self.recvd = ''
                elif datalength < packetlength:
                    break
                else:
                    self.stringReceived(self.recvd[4:packetlength])
                    self.recvd = self.recvd[packetlength:]
            else:
                break

    def sendString(self, string, utf = True):
        if len(string) >= 2 ** (8 * 4):
            raise StringTooLongError(
                'Try to send %s bytes whereas maximum is %s' % (
                len(string), 2 ** (8 * 4)))
        if utf:
            self.transport.write(
            struct.pack(self.structFormat, len(string)) + string)
        else:
            self.transport.write(string)

class TransforoomClient(TransforoomProtocol):

    def __init__(client):
        client.policy = False
        client.correctVersion = False
        client.sentMDT = False
        client.Langue = ''
        client.loginned = False

        client.wrongPassAttempts = 0
        client.username = ''
        client.playerCode = -1
        #-1 - Invalid, 0 - Guest, 1 - Normal, 2 - PlayerBot, 3 - Arbitre, 4 - Modbot, 5 - Moderator, 6 - Manager/Supermod, 10 - Admin
        client.privilegeLevel = -1
        client.isGuest = True
        client.isBot = False
        client.newAccount = False

        client.ATEC_Time = None
        client.ping_Time = None
        client.pingTimer = None
        clieng.ping = -1

    def log(client, message):
        if world.LOGVERBOSE:
            logging.info(message)
        if world.VERBOSE:
            print str(datetime.today()) + ' ' + message

    def connectionMade(client):
        #Get IP Address
        if sys.platform.startswith('win'):
            #Windows
            client.address = self.transport.getPeer()[1:]
        else:
            client.address = self.transport.getHandle().getpeername()

        log('Connection received from IP: ' + self.address[0] + ' from Port: ' + str(self.address[1]))
        log(self.transport.getHost())

        #Ban Check - coming soon
        
        #Link client to server
        #client.server = client.factory

        #Rejects players when server is offline for testing
        if !world.online and self.address[0] != '127.0.0.1':
            self.transport.loseConnection()
            log('Disconnected: ' + self.address[0] + ' Reason: Server Offline')
        #Rejects players when server is full
        elif world.server

def execute(query, list = None):
    if list not None:
        world.curse.execute(query, list)
    else:
        world.curse.execute(query)
    if query[:6] in ('CREATE', 'UPDATE', 'DELETE', 'INSERT'):
        world.db.commit()

def initiateDatabase():
    world.db = sqlite3.connect('data.sqlite')
    world.curse = world.db.cursor()
    execute(

def main():
    world.server = TFMooseServer()
    initiateDatabase()
    initiatePorts(world.server)
    log("[Server] Closed.")
    
if __name__ == '__main__':
    main()
