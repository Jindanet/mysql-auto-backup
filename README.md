# MySQL Auto Backup

## 📌 Overview
This script automates the backup process for a MySQL database by running every 6 hours. It saves the backup as a `.sql` file, compresses it into a `.zip` file, and maintains a log file.

## 🚀 Features
- Automatically organizes backups into daily folders.
- Uses `mysqldump` to export the database.
- Compresses the backup into a `.zip` file.
- Logs backup success and failure events.
- Runs continuously, creating backups every 6 hours.

## 🛠️ Setup & Usage
### 1️⃣ Prerequisites
- Install **Python 3**  
- MySQL must be installed and `mysqldump` must be available in the system path.

### 2️⃣ Install Dependencies
This script does not require additional dependencies beyond Python's standard library.

### 3️⃣ Configure Database Settings
Edit the following variables in `backup.py`:
```python
DB_HOST = "your_host"
DB_USER = "your_username"
DB_PASSWORD = "your_password"
DB_NAME = "your_database"
BACKUP_BASE_DIR = "C:\\path\\to\\backup\\directory"
```
### 4️⃣ Run the Script
Run the script manually or set it to start automatically:

python backup.py

### ⚠️ Troubleshooting
Ensure mysqldump is accessible from the command line.
If backups fail, check backup_log.txt for error details.
