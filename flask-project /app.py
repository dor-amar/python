from flask import Flask, request, jsonify, render_template
from discord_webhook import DiscordWebhook
import sqlite3
from datetime import datetime, timedelta

# Initialize the Flask app
app = Flask(__name__)

# ====================
# DATABASE SETUP
# ====================
# Function to initialize the SQLite database and create the 'messages' table
def init_db():
    # Connect to the SQLite database (or create it if it doesn't exist)
    conn = sqlite3.connect('messages.db')
    cursor = conn.cursor()
    
    # Create a table for storing messages if it doesn't already exist
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS messages (
            id INTEGER PRIMARY KEY,        
            content TEXT,                 
            timestamp DATETIME             
        )
    ''')
    
    # Commit the changes and close the connection to the database
    conn.commit()
    conn.close()

# ====================
# DISCORD SETUP
# ====================
# Discord webhook URL to send messages to the Discord server (replace with your own)
discord_webhook_url = 'https://discordapp.com/api/webhooks/1283887694186807307/ucN04vSXggXLlqqPGTr1meDdAwizGR0rpmKETt5sa6IKl-aLBdHA1VNWYS6l9CFXuAo1'

# ====================
# ROUTES
# ====================

# Route to render the home page (index.html)
@app.route('/')
def index():
    return render_template('index.html')

# ====================
# INPUT TEXT ROUTE
# ====================
# This route allows users to submit a message, which will be sent to Discord and stored in the SQLite database.
@app.route('/input_text', methods=['POST'])
def input_text():
    try:
        # Check if the request contains JSON data
        if request.is_json:
            # Extract the text from the JSON request
            data = request.get_json()
            text = data['text']
        else:
            # If the data is from an HTML form, extract the text from the form submission
            text = request.form['text']
        
        # Send the extracted text to the Discord server
        send_to_discord(text)
        
        # Save the message to the SQLite database
        save_to_database(text)
        
        # Return a success response in JSON format
        return jsonify({"status": "success"})
    
    # If something goes wrong, catch the exception and return an error response
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)})

# ====================
# HELPER FUNCTIONS
# ====================

# Function to send a message to the Discord server via the webhook
def send_to_discord(text):
    # Create a webhook object using the provided webhook URL and message content
    webhook = DiscordWebhook(url=discord_webhook_url, content=text)
    
    # Execute the webhook to send the message to Discord
    webhook.execute()

# Function to save the message to the SQLite database
def save_to_database(text):
    # Connect to the SQLite database
    conn = sqlite3.connect('messages.db')
    cursor = conn.cursor()
    
    # Insert the message content along with the current timestamp into the database
    cursor.execute('INSERT INTO messages (content, timestamp) VALUES (?, ?)', (text, datetime.now()))
    
    # Commit the transaction and close the database connection
    conn.commit()
    conn.close()

# ====================
# RETRIEVE MESSAGES ROUTE
# ====================
# This route retrieves messages from the database that were submitted within the last 30 minutes.
@app.route('/get_messages', methods=['GET'])
def get_messages():
    try:
        # Connect to the SQLite database
        conn = sqlite3.connect('messages.db')
        cursor = conn.cursor()
        
        # Calculate the cutoff time (30 minutes ago)
        cutoff_time = datetime.now() - timedelta(minutes=30)
        
        # Query the database for messages with a timestamp greater than the cutoff time
        cursor.execute('SELECT content, timestamp FROM messages WHERE timestamp > ?', (cutoff_time,))
        messages = cursor.fetchall()
        
        # Close the database connection
        conn.close()
        
        # Return the retrieved messages in JSON format
        return jsonify({"status": "success", "messages": messages})
    
    # Handle any errors that occur and return an error response
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)})

# ====================
# MAIN FUNCTION
# ====================
# The main function that runs the Flask app
if __name__ == '__main__':
    # Initialize the SQLite database (create the table if it doesn't exist)
    init_db()
    
    # Run the Flask app in debug mode (useful for development)
    app.run(debug=True)
