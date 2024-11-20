# services.py

import csv

def write_to_file(data):
    with open('database.txt', mode='a') as database:
        email = data["Email"]
        subject = data["Subject"]
        message = data["Message"]
        database.write(f'\nemail = {email}, subject = {subject}, message = {message}')

def write_to_csv(data):
    with open('database.csv', mode='a', newline='') as database2:
        email = data["Email"]
        subject = data["Subject"]
        message = data["Message"]
        csv_writer = csv.writer(database2, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email, subject, message])
