import mysql.connector

def get_database_connection():
    cnx = mysql.connector.connect(
        host='localhost',
        user='root',
        password='mperor',
        database='chatbot'
    )
    return cnx

def close_database_connection(cnx):
    cnx.close()

def insert_chat(user_msg, bot_msg):
    cnx = get_database_connection()
    cursor = cnx.cursor()
    query = "INSERT INTO chats (user_msg, bot_msg) VALUES (%s, %s)"
    values = (user_msg, bot_msg)
    
    try:
        cursor.execute(query, values)
        cnx.commit()
        cursor.close()
        close_database_connection(cnx)
        
        return True
    except Exception as e:
        cursor.close()
        close_database_connection(cnx)        
        return False
