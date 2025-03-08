import os
import time
import zipfile
import subprocess

# ตั้งค่าการเชื่อมต่อ MySQL
DB_HOST = "your_host"
DB_USER = "your_username"
DB_PASSWORD = "your_password"
DB_NAME = "your_database"
BACKUP_BASE_DIR = "C:\\path\\to\\backup\\directory"

while True:
    # กำหนดโฟลเดอร์ของแต่ละวัน
    date_folder = time.strftime("%Y-%m-%d")
    backup_dir = os.path.join(BACKUP_BASE_DIR, date_folder)
    
    # ตรวจสอบว่ามีโฟลเดอร์หรือไม่ ถ้าไม่มีให้สร้าง
    if not os.path.exists(backup_dir):
        os.makedirs(backup_dir)
    
    # ตั้งชื่อไฟล์สำรองข้อมูล
    timestamp = time.strftime("%H%M%S")
    backup_sql_file = os.path.join(backup_dir, f"{DB_NAME}_{timestamp}.sql")
    backup_zip_file = os.path.join(backup_dir, f"{DB_NAME}_{timestamp}.zip")
    log_file = os.path.join(backup_dir, "backup_log.txt")
    
    # คำสั่ง mysqldump
    dump_command = f"mysqldump -h {DB_HOST} -u {DB_USER} -p{DB_PASSWORD} {DB_NAME} > {backup_sql_file}"
    
    try:
        # รันคำสั่งเพื่อสำรองข้อมูล
        result = subprocess.run(dump_command, shell=True, check=True, stderr=subprocess.PIPE, text=True)
        
        # บีบอัดไฟล์เป็น ZIP
        with zipfile.ZipFile(backup_zip_file, 'w', zipfile.ZIP_DEFLATED) as zipf:
            zipf.write(backup_sql_file, os.path.basename(backup_sql_file))
        
        # ลบไฟล์ .sql หลังจากบีบอัด
        os.remove(backup_sql_file)
        
        # บันทึกเวลา backup
        with open(log_file, "a") as log:
            log.write(f"Backup completed: {backup_zip_file} at {time.strftime('%Y-%m-%d %H:%M:%S')}\n")
        
        print(f"Backup completed: {backup_zip_file}")
    except subprocess.CalledProcessError as e:
        error_message = e.stderr if e.stderr else "Unknown error"
        with open(log_file, "a") as log:
            log.write(f"Backup failed at {time.strftime('%Y-%m-%d %H:%M:%S')}: {error_message}\n")
        print(f"Backup failed: {error_message}")
    
    # รอ 6 ชั่วโมงก่อนทำ backup ครั้งต่อไป
    time.sleep(6 * 60 * 60)
