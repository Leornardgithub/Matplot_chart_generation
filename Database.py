import sqlite3

def setup_database():
    connection = sqlite3.connect('database.db')
    cursor = connection.cursor()
    
    # Line Plot
    cursor.execute('CREATE TABLE IF NOT EXISTS lineplot (xvalue INTEGER, yvalue INTEGER)')
    
    # scatterplot
    cursor.execute('CREATE TABLE IF NOT EXISTS scatterplot (xvalue INTEGER, yvalue INTEGER)')

    # Bar Charts
    cursor.execute('CREATE TABLE IF NOT EXISTS barchart (category TEXT, value INTEGER)')
    
    # Horizontal Bar Chart
    cursor.execute('CREATE TABLE IF NOT EXISTS barchart_horizontal (category TEXT, value INTEGER)')

    # Histogram
    cursor.execute('CREATE TABLE IF NOT EXISTS histogram (value INTEGER)')

    # Box Plot
    cursor.execute('CREATE TABLE IF NOT EXISTS boxplot (category TEXT, value INTEGER)')

    # Pie Chart
    cursor.execute('CREATE TABLE IF NOT EXISTS piechart (category TEXT, value INTEGER)')

    # Area Plot
    cursor.execute('CREATE TABLE IF NOT EXISTS areaplot (xvalue INTEGER, yvalue INTEGER)')

    # Stacked Bar Chart
    cursor.execute('CREATE TABLE IF NOT EXISTS stackedbarchart (category TEXT, value1 INTEGER, value2 INTEGER)')

    # Heatmap 
    cursor.execute('CREATE TABLE IF NOT EXISTS heatmap (x INTEGER, y INTEGER, value INTEGER)')
    
    # Contour Plot
    cursor.execute('CREATE TABLE IF NOT EXISTS contourplot (x INTEGER, y INTEGER, z INTEGER)')

    # 3D Plot
    cursor.execute('CREATE TABLE IF NOT EXISTS three_d_plot (x INTEGER, y INTEGER, z INTEGER)')

    connection.commit()
    connection.close()
 
def clear_data_from_table2():
    connection = sqlite3.connect('database.db')
    cursor = connection.cursor()
    cursor.execute('DELETE FROM lineplot')  # This line clears all data from the table
    connection.commit()
    connection.close()
    
def clear_data_from_table():
    connection = sqlite3.connect('database.db')
    cursor = connection.cursor()

    # Retrieve a list of all table names in the database
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()

    # Drop each table
    for table in tables:
        table_name = table[0]  # table name is in the first column
        cursor.execute(f"DELETE FROM {table_name}")

    connection.commit()
    connection.close()
