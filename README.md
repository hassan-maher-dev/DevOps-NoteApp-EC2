📘 Deploy a Note-Taking Website on AWS EC2 with Backup Strategy

## 🎯 Project Objective
Deploying a dynamic Python (Flask) web application on an AWS EC2 instance (RHEL 10), connected to a MariaDB database, with an automated backup strategy using a separate EBS volume managed by LVM.

## 🛠️ Infrastructure & Technologies
- **Cloud Provider:** AWS (EC2, EBS)
- **OS:** Red Hat Enterprise Linux (RHEL)
- **Programming Language:** Python (Flask)
- **Database:** MariaDB
- **Storage Management:** LVM (Logical Volume Manager)



## 🚀 Setup Steps



### 1. Environment Setup
Updated the system and installed necessary packages:
```bash
sudo dnf update -y
sudo dnf install python3 python3-pip git mariadb-server -y
pip3 install flask mysql-connector-python
2. Database Configuration (MariaDB)
Created the database and user:

SQL
CREATE DATABASE notes_db;
CREATE TABLE notes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    content TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
CREATE USER 'app_user'@'localhost' IDENTIFIED BY 'password';
GRANT ALL PRIVILEGES ON notes_db.* TO 'app_user'@'localhost';
3. Backup Storage Configuration (LVM)
Attached a new EBS volume and configured it using LVM for flexibility:

Created Physical Volume (PV).

Created Volume Group (VG).

Created Logical Volume (LV) and mounted it to /backup.

Verification:


df -h /backup
4. Backup Strategy
Performed a database dump to the mounted volume:


mysqldump -u app_user -p notes_db > /backup/notes_backup_$(date +%F).sql


✅ Usage
The application is running on port 80. Users can submit notes which are saved to the database and displayed with timestamps.


```mermaid
graph TD;
    User((👤 User)) -->|HTTP:80| EC2[AWS EC2 Instance<br/>RHEL 10];
    subgraph EC2 [AWS EC2 Instance]
        App[🐍 Python Flask App] -->|Reads/Writes| DB[(🐬 MariaDB)];
    end
    DB -->|mysqldump| BackupVol[(💽 EBS Backup Volume<br/>/backup)];
    RootVol[(💽 Root EBS Volume<br/>/)] -.-> EC2;
    BackupVol -.->|Mounted| EC2;

    style EC2 fill:#f9f2f4,stroke:#333,stroke-width:2px;
    style BackupVol fill:#ffaaaa,stroke:#333,stroke-width:2px;
    style DB fill:#e1f5fe,stroke:#333;```
