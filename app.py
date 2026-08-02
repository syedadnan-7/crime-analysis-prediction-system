import os
import flask
from flask import render_template, request, jsonify, session
from flask import jsonify
from flask_mysqldb import MySQL
import MySQLdb.cursors
from flask_session import Session
import numpy as np
import random
import matplotlib.pyplot as plt
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from collections import defaultdict
from datetime import datetime, timedelta
from wordcloud import WordCloud
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import OneHotEncoder, LabelEncoder
from sklearn.metrics import accuracy_score
import pandas as pd

app = flask.Flask(__name__, template_folder='Templates')
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

UPLOAD_FOLDER = 'static/incidents'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


#code for connection
app.config['MYSQL_HOST'] = 'localhost'#hostname
app.config['MYSQL_USER'] = 'root'#username
app.config['MYSQL_PASSWORD'] = ''#password
app.config['MYSQL_DB'] = 'crimeanalysis'#database name

mysql = MySQL(app)
@app.route('/')

@app.route('/main', methods=['GET', 'POST'])
def main():
    if flask.request.method == 'GET':
            return(flask.render_template('index.html'))

@app.route('/joinus', methods=['GET', 'POST'])
def joinus():
    if flask.request.method == 'GET':
            return(flask.render_template('joinus.html'))
        

        
@app.route('/about', methods=['GET', 'POST'])
def about():
    if flask.request.method == 'GET':
        return(flask.render_template('about.html'))
    
@app.route('/service', methods=['GET', 'POST'])
def service():
    if flask.request.method == 'GET':
        return(flask.render_template('service.html'))
    
@app.route('/aboutus', methods=['GET', 'POST'])
def aboutus():
    if flask.request.method == 'GET':
        return(flask.render_template('aboutus.html'))
    
@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if flask.request.method == 'GET':
        return(flask.render_template('contact.html'))
    
@app.route('/admin', methods=['GET', 'POST'])
def admin():
    if flask.request.method == 'GET':
        return(flask.render_template('admin.html'))
    
@app.route('/userhome', methods=['GET', 'POST'])
def userhome():
    if flask.request.method == 'GET':
        return(flask.render_template('userhome.html'))
    
@app.route('/analysispage', methods=['GET', 'POST'])
def analysispage():
    if flask.request.method == 'GET':
        return(flask.render_template('analysispage.html'))
    
@app.route('/futureanalysis', methods=['GET', 'POST'])
def futureanalysis():
    if flask.request.method == 'GET':
        return(flask.render_template('futureanalysis.html'))
    
@app.route('/adminhome', methods=['GET', 'POST'])
def adminhome():
    if flask.request.method == 'GET':
        return(flask.render_template('adminhome.html'))
    
@app.route('/complainthistory', methods=['GET', 'POST'])
def complainthistory():
    if flask.request.method == 'GET':
        return(flask.render_template('complainthistory.html'))
    

@app.route('/getrecords', methods=['GET', 'POST'])
def getrecords():        
    if flask.request.method == 'POST':
        userid = session.get("userid")
        con = mysql.connect
        con.autocommit(True)
        cursor = con.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM history WHERE userid="'+str(userid)+'"')
        result = cursor.fetchall();
    return jsonify(result)



@app.route('/login', methods=['GET', 'POST'])
def login():
    if flask.request.method == 'POST':
        phone           = request.form['signphone']
        password        = request.form['signpassword']
        msg = 0
        con = mysql.connect
        con.autocommit(True)
        cursor = con.cursor(MySQLdb.cursors.DictCursor)
        
        qry = 'SELECT * FROM userdetails WHERE phone="'+phone+'" AND password="'+password+'"'
        result = cursor.execute(qry)
        result = cursor.fetchone()
        
        if result is not None:
            msg = "1"
            session["userid"]   = result["userid"]
            session["username"]   = result["name"]
            session["usermail"]   = result["email"]
            session["userrole"]   = "user"
        else:
           msg = "0"           
    return jsonify(msg)


@app.route('/adminlogin', methods=['GET', 'POST'])
def adminlogin():
    if flask.request.method == 'POST':
        phone           = request.form['signphone']
        password        = request.form['signpassword']
        
        if phone == "admin" and password == "adminpassword":
            msg = "1"
            session["userrole"]   = "admin"
        else:
           msg = "0"           
    return jsonify(msg)
    
@app.route('/getadmincrimehistory', methods=['GET', 'POST'])
def getadmincrimehistory():
    if request.method == 'POST':
        search        = request.form['search']
        
        con = mysql.connect
        con.autocommit(True)
        cursor = con.cursor(MySQLdb.cursors.DictCursor)

        if search != "":
            query = "SELECT * FROM crimedetails WHERE category LIKE %s OR description LIKE %s OR datetime LIKE %s"
            cursor.execute(query, ('%' + search + '%', '%' + search + '%', '%' + search + '%'))

        else:
            # Fetch all crime details for the user
            query = "SELECT * FROM crimedetails"
            cursor.execute(query)

        result = cursor.fetchall()
        cursor.close()

        return jsonify(result)
    
    
@app.route('/futureprediction', methods=['GET', 'POST'])
def futureprediction():
    if request.method == 'POST':
        con = mysql.connect
        con.autocommit(True)
        cursor = con.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM crimedetails')
        result = cursor.fetchall()

        if not result:
            return jsonify({"message": "No historical crime records available.", "predictions": []})

        df = pd.DataFrame(result)
        df['datetime_parsed'] = pd.to_datetime(df['datetime'], errors='coerce')
        df['address'] = df['address'].fillna('').astype(str).str.strip()
        df = df.dropna(subset=['datetime_parsed'])

        # Get distinct addresses directly from the database (no filtering)
        cursor.execute('SELECT DISTINCT address FROM crimedetails')
        distinct_rows = cursor.fetchall()
        all_addresses = [row.get('address') if row.get('address') is not None else '' for row in distinct_rows]
        # Ensure at least one placeholder exists
        if not all_addresses:
            all_addresses = ['Unknown Location']

        if df.empty:
            return jsonify({"message": "No valid historical datetime records found.", "predictions": []})

        grouped = df.groupby(['category', 'address'])
        entries = []

        for (category, address), group in grouped:
            count = int(group.shape[0])
            hour_mode = group['datetime_parsed'].dt.hour.mode()
            expected_hour = int(hour_mode.iloc[0]) if not hour_mode.empty else 20
            entries.append({
                'category': category,
                'address': address,
                'count': count,
                'hour': expected_hour
            })

        entries.sort(key=lambda item: item['count'], reverse=True)

        prediction_count = random.randint(5, 10)
        selected_entries = random.sample(entries, min(prediction_count, len(entries))) if entries else []
        if len(selected_entries) < prediction_count and entries:
            selected_entries += random.choices(entries, k=prediction_count - len(selected_entries))

        max_count = max(item['count'] for item in selected_entries) if selected_entries else 1
        start_date = datetime.now().date() + timedelta(days=1)
        future_dates = [start_date + timedelta(days=i) for i in range(7)]

        def security_suggestion(category_text):
            normalized = category_text.strip().upper()
            if 'THEFT' in normalized:
                return 'Increase lighting, secure valuables, and strengthen CCTV coverage.'
            if 'ASSAULT' in normalized or 'VIOLENCE' in normalized:
                return 'Add patrols, emergency alarms, and visible security presence.'
            if 'BURGLARY' in normalized or 'BREAK' in normalized:
                return 'Secure doors/windows, add motion sensors, and organize neighborhood watch.'
            if 'ROBBERY' in normalized or 'SNATCH' in normalized:
                return 'Install cameras, keep areas well-lit, and avoid isolated spots.'
            return 'Deploy targeted patrols and improve surveillance for this area.'

        predictions = []
        for entry in selected_entries:
            prediction_date = random.choice(future_dates)
            hour_variation = random.choice([-1, 0, 1])
            predicted_hour = max(0, min(23, entry['hour'] + hour_variation))
            expected_datetime = datetime(
                prediction_date.year,
                prediction_date.month,
                prediction_date.day,
                predicted_hour,
                0,
                0
            )
            chosen_location = random.choice(all_addresses)
            probability = min(98, max(55, int((entry['count'] / max_count) * 100)))
            predictions.append({
                'crime_type': entry['category'],
                'location': chosen_location,
                'expected_datetime': expected_datetime.strftime('%Y-%m-%d %H:%M:%S'),
                'probability': f"{probability}%",
                'security_suggestion': security_suggestion(entry['category'])
            })

        return jsonify({"message": "Future prediction generated successfully.", "predictions": predictions})


@app.route('/getcrimehistory', methods=['GET', 'POST'])
def gethistory():
    if request.method == 'POST':
        userid = session.get("userid")
        con = mysql.connect
        con.autocommit(True)
        cursor = con.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM crimedetails WHERE userid='+str(userid))
        result = cursor.fetchall()
        
        return jsonify(result)

@app.route('/logout', methods=['GET', 'POST'])
def logout():
    if flask.request.method == 'GET':
        session.pop('userid', None)
        session.pop('username', None)
        session.pop('usermail', None)
        
        return(flask.render_template('index.html'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    if flask.request.method == 'POST':
        username  = request.form['regusername']
        phone        = request.form['regphone']
        email        = request.form['regemail']
        usedfor      = request.form['usingfor']
        password     = request.form['regpassword']
        address     = request.form['regaddress']
        
        con = mysql.connect
        con.autocommit(True)
        cursor = con.cursor(MySQLdb.cursors.DictCursor)
        
        qry = 'SELECT * FROM userdetails WHERE phone="'+phone+'" AND password="'+password+'"'
        result = cursor.execute(qry)
        result = cursor.fetchone()
        
        if result:
            msg = '2'
        else:
            cursor.execute('INSERT INTO userdetails VALUES (NULL, %s, %s, %s, %s, %s, %s, NULL)', (username, email, phone, password, usedfor, address, ))
            mysql.connect.commit()
            msg = '1'
            
            subject = "Register at Crime Detecteion Portal Reg"
            body = f"Hi {username},\n\nThank you for choosing our crime analysis portal for registration. We're thrilled to welcome you to our community dedicated to leveraging advanced technology for crime prevention and analysis. At Crime Analysis Hub, we empower law enforcement agencies with cutting-edge AI algorithms and data-driven insights to enhance community safety and strategic decision-making.\n\nWe look forward to supporting you in your efforts to make a meaningful impact in crime analysis and prevention.\n\nWelcome aboard!\n\nBest regards,\nThe Crime Analysis Hub Team"

            sendmail(email, subject, body)
        
        return msg
    
@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return 'No file part'

    file = request.files['file']

    if file.filename == '':
        return 'No selected file'

    if file:
        filename = file.filename
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        return filename
    
@app.route('/addcomplaint', methods=['GET', 'POST'])
def addcomplaint():
    if flask.request.method == 'POST':
        category  = request.form['category']
        officer        = request.form['officer']
        datetime        = request.form['datetime']
        address      = request.form['address']
        description     = request.form['description']
        
        userid = session.get("userid")
        username = session.get("username")
        email=session.get("usermail")
        
        con = mysql.connect
        con.autocommit(True)
        cursor = con.cursor(MySQLdb.cursors.DictCursor)
        
        cursor.execute('INSERT INTO crimedetails VALUES (NULL, %s, %s, %s, %s, %s, %s)', (userid, category, officer, datetime, address, description, ))
        mysql.connect.commit()
        msg = '1'
        
        last_id = cursor.lastrowid
        crime_id = "CR-"+str(last_id)
        
        # Email subject and body
        subject = "Complaint Registered at Crime Detection Portal"
        
        body = f"Hi {username},\n\nThank you for your complaint. Your complaint with ID {crime_id} has been registered successfully.\n\n"\
          "Here are the next steps:\n"\
          "1. Our team will review your complaint and investigate further.\n"\
          "2. You will receive updates on the progress of your complaint via email.\n"\
          "3. If you have any additional information or questions, please reply to this email or contact our support team.\n\n"\
          "We appreciate your cooperation and patience as we work towards resolving this matter.\n\n"\
          "Best regards,\nThe Crime Analysis Hub Team"
          
        sendmail(email, subject, body)
    
    return msg
    
def sendmail(receiver, subject, body):
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login("thirstolearn@gmail.com", "mutk ukoz jvxc pjhn")

    # Email details
    sender_email_id = "thirstolearn@gmail.com"
    
    # Create a MIMEMultipart object
    msg = MIMEMultipart()
    msg['From'] = sender_email_id
    msg['To'] = receiver
    msg['Subject'] = subject
    
    text = MIMEText(body, 'plain')
    msg.attach(text)

    # Send the email
    s.sendmail(sender_email_id, receiver, msg.as_string())
    s.quit()
    
    
@app.route('/getanalysis', methods=['GET', 'POST'])
def getanalysis():
    if flask.request.method == 'POST':
        con = mysql.connect
        con.autocommit(True)
        cursor = con.cursor(MySQLdb.cursors.DictCursor)
        
        cursor.execute('SELECT * FROM crimedetails')
        result = cursor.fetchall()
        
        category_counts = defaultdict(int)
        address_counts = defaultdict(int)
        datetime_counts = defaultdict(int)
        word_frequency = defaultdict(int)
    
        # Iterate through each entry in the result
        for entry in result:
            category_counts[entry['category']] += 1
            address_counts[entry['address']] += 1
            
            # Convert datetime string to datetime object for better analysis
            crime_datetime = datetime.fromisoformat(entry['datetime'])
            # Use date part for counts
            date_key = crime_datetime.date()
            datetime_counts[date_key] += 1
            
            # Process description for word frequency analysis (assuming description is a text field)
            description = entry['description']
            words = description.split()
            for word in words:
                word_frequency[word.lower()] += 1
    
        # Generate crime analysis by category bar chart
        plt.figure(figsize=(10, 6))
        categories = list(category_counts.keys())
        counts = list(category_counts.values())
        colors = plt.cm.Set2(range(len(categories)))  # Generate colors from Set2 colormap
        plt.bar(categories, counts, color=colors)
        plt.xlabel('Crime Category')
        plt.ylabel('Number of Incidents')
        plt.title('Crime Incidents by Category')
        plt.xticks(rotation=45)
        category_chart_name = 'category.png'
        category_chart_path = save_chart(plt, category_chart_name)
    
        # Generate crime analysis by address bar chart
        plt.figure(figsize=(12, 6))
        addresses = list(address_counts.keys())
        counts = list(address_counts.values())
        colors = plt.cm.Paired(range(len(addresses)))  # Generate colors from Paired colormap
        plt.bar(addresses, counts, color=colors)
        plt.xlabel('Crime Address')
        plt.ylabel('Number of Incidents')
        plt.title('Crime Incidents by Address')
        plt.xticks(rotation=45)
        address_chart_name = 'address.png'
        address_chart_path = save_chart(plt, address_chart_name)
    
        # Generate crime analysis over time (datetime) line chart
        plt.figure(figsize=(12, 6))
        dates = list(datetime_counts.keys())
        dates.sort()  # Sort dates chronologically
        counts = [datetime_counts[date] for date in dates]
        plt.plot(dates, counts, marker='o', linestyle='-', color='b')  # Blue color for line chart
        plt.xlabel('Date')
        plt.ylabel('Number of Incidents')
        plt.title('Crime Incidents Over Time')
        plt.xticks(rotation=45)
        datetime_chart_name = 'datetime.png'
        datetime_chart_path = save_chart(plt, datetime_chart_name)
    
        # Generate word cloud for descriptions
        plt.figure(figsize=(10, 6))
        wordcloud = WordCloud(width=800, height=400, background_color='white').generate_from_frequencies(word_frequency)
        plt.imshow(wordcloud, interpolation='bilinear')
        plt.axis('off')
        plt.title('Word Cloud of Crime Descriptions')
        description_wordcloud_name = 'wordcloud.png'
        description_wordcloud_path = save_chart(plt, description_wordcloud_name)
    
        # Return filenames of saved images as response
        response = {
            'category_chart': category_chart_name,
            'address_chart': address_chart_name,
            'datetime_chart': datetime_chart_name,
            'description_wordcloud': description_wordcloud_name
        }
        return jsonify(response)

def save_chart(plt, filename):
    output_dir = os.path.join(app.static_folder, 'output')
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    chart_path = os.path.join(output_dir, filename)
    plt.savefig(chart_path)
    plt.close()
    return chart_path
    

if __name__ == '__main__':
    app.run(debug=True)