import mysql.connector
import json
import simplejson
from pprint import pprint;
from string import Template
from cgi import parse_qs
import codecs;

def application(env, start_response):
    start_response('200 OK', [('Content-Type', 'application/json')])

    creds = { 'user': 'pokemon',
              'password':'Pa$$w0rd',
              'database':'Pokemon',
              'auth_plugin':'mysql_native_password'}

    cnx = mysql.connector.connect(**creds)
    cursor = cnx.cursor(dictionary = True)
    if(env['QUERY_STRING'] != ''):
        types = env['QUERY_STRING']
        types = types.split('=')
        types = types[1]
        print(types)
        command = 'SELECT * FROM Pokemon_Type WHERE Types = \'' +str(types)+ '\';'
        cursor.execute(command)
        x = cursor.fetchall()
        
        x = simplejson.dumps(x)
    else:
        cursor.execute('SELECT * FROM Pokemon_Type;')
        x = cursor.fetchall()
        x = simplejson.dumps(x)
        
    return x.encode()





