import os
import tarfile
import datetime
import smtplib
from email.mime.text import MIMEText

# === Configuration ===
SOURCE_DIRS = [r"C:\Users\DELL\OneDrive\Documents\KNUST FILES\AUTOTRONICS LAB"]  # Only Windows paths
BACKUP_DIR = r"C:\Users\DELL\OneDrive\Documents\Project Backups"        # Use raw string
EMAIL_REPORT = True
EMAIL_TO = "charlesagana14@gmail.com"
EMAIL_FROM = "charlesagana14@gmail.com"
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
EMAIL_USER = "charlesagana14@gmail.com"
EMAIL_PASS = "ivpf msfr ofpq jxmc"  # <-- paste your app password here

# === Create Backup ===
def create_backup():
    if not os.path.exists(BACKUP_DIR):
        os.makedirs(BACKUP_DIR)
    date_str = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    backup_filename = f"backup_{date_str}.tar.gz"
    backup_path = os.path.join(BACKUP_DIR, backup_filename)
    
    try:
        with tarfile.open(backup_path, "w:gz") as tar:
            for directory in SOURCE_DIRS:
                tar.add(directory, arcname=os.path.basename(directory))
        message = f"Backup successful: {backup_path}"
        success = True
    except Exception as e:
        message = f"Backup failed: {e}"
        success = False

    print(message)
    if EMAIL_REPORT:
        send_email(success, message)

# === Send Notification Email ===
def send_email(success, message):
    subject = "Backup Success" if success else "Backup Failure"
    msg = MIMEText(message)
    msg["Subject"] = subject
    msg["From"] = EMAIL_FROM
    msg["To"] = EMAIL_TO

    try:
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()
            server.login(EMAIL_USER, EMAIL_PASS)
            server.send_message(msg)
    except Exception as e:
        print(f"Failed to send email: {e}")

if __name__ == "__main__":
    create_backup()
