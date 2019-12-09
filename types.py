import mysql.connector
import json
import simplejson
from pprint import pprint;
from string import Template
from cgi import parse_qs
import codecs;

def application(env, start_response):
    """Returns the type match-up for the selected type in QUERY_STRING or the full type chart if no type is specified"""
    start_response('200 OK', [('Content-Type', 'application/json')])

    #set up connection credentials
    creds = { 'user': 'pokemon',
              'password':'Pa$$w0rd',
              'database':'Pokemon',
              'auth_plugin':'mysql_native_password'}

    #begin connection
    cnx = mysql.connector.connect(**creds)
    cursor = cnx.cursor(dictionary = True)

    #If the query string isn't empty then we do a seperate SQL Query for that specific value
    if(env['QUERY_STRING'] != ''):
        #Query string contains the selected type (
        types = env['QUERY_STRING']
        types = types.split('=')
        types = types[1]
        print(types)
        command = 'SELECT * FROM Pokemon_Type WHERE Types = \'' +str(types)+ '\';'
        cursor.execute(command)
        x = cursor.fetchall()
        
        x = simplejson.dumps(x)
    #Otherwise the entire database is returned if the query string is empty
    else:
        cursor.execute('SELECT * FROM Pokemon_Type;')
        x = cursor.fetchall()
        x = simplejson.dumps(x)
        
    return x.encode()





