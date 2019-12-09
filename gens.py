import mysql.connector
import json
import simplejson
from pprint import pprint;
from string import Template
from cgi import parse_qs
import codecs;

def application(env, start_response):
    """Returns the Pokemon games for the selected generation in the query string or the full list of games if no generation is specified"""
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
        #Query string contains the number of the generation user is looking up
        types = env['QUERY_STRING']
        types = types.split('=')
        types = types[1]
        
        cursor.execute('SELECT * FROM Pokemon_Games WHERE GenNumber = '+ types +';')    
        x = cursor.fetchall()
        x = simplejson.dumps(x)

        return x.encode()

    #Otherwise the entire table is returned if there the query string is empty
    else:
        cursor.execute('SELECT * FROM Pokemon_Games;')
        x = cursor.fetchall()
        x = simplejson.dumps(x)

        return x.encode()
    
