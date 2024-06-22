import sqlite3

# Step 2: Connect to a database (creates a new database file if it doesn't exist)
conn = sqlite3.connect('spotify.db')

# Step 3: Create a cursor object
cursor = conn.cursor()

# Step 4: Create a table for songs with file_name, title, audio_file, and cover_image fields
cursor.execute('''
CREATE TABLE IF NOT EXISTS songs (
    id INTEGER PRIMARY KEY,
    file_name TEXT NOT NULL,
    title TEXT,
    audio_file TEXT,
    cover_image TEXT
)
''')

# Step 5: Insert sample data into the table
# Note: The title 'Song One' is corrected from your original script

# Sample data including audio_file and cover_image
cursor.execute('''
INSERT INTO songs (file_name, title, audio_file, cover_image)
VALUES ('song1.mp3', 'Song One', 'audio/song1.mp3', 'images/cover1.jpg')
''')

# Insert another sample song
cursor.execute('''
INSERT INTO songs (file_name, title, audio_file, cover_image)
VALUES ('song2.mp3', 'Song Two', 'audio/song2.mp3', 'images/cover2.jpg')
''')

# Step 6: Commit the changes
conn.commit()

# Step 7: Query the database
cursor.execute('SELECT * FROM songs')
rows = cursor.fetchall()

# Print the retrieved rows
for row in rows:
    print(row)

# Step 8: Close the connection
conn.close()
