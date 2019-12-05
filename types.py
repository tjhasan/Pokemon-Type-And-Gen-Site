import mysql.connector
import json
import simplejson
from pprint import pprint;
from string import Template
from cgi import parse_qs
import codecs;

def application(env, start_response):
    start_response('200 OK', [('Content-Type', 'application/json')])
    x = 'GENERATIONS'

    creds = { 'user': 'pokemon',
              'password':'Pa$$w0rd',
              'database':'Pokemon',
              'auth_plugin':'mysql_native_password'}

    cnx = mysql.connector.connect(**creds)
    cursor = cnx.cursor(dictionary = True)

    cursor.execute('SELECT * FROM Pokemon_Type;')
    x = cursor.fetchall()

    x = simplejson.dumps(x)

    return x.encode()





