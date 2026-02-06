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

```markdown
![Architecture Diagram](https://kroki.io/mermaid/svg/eNqVVF1v2jAU_SuWnypS2g_QPlSp2gdt1aZp0j5MchsTw01sZzsMivrvc0ICZR-2Pljiufee-3F8fQ6UEg4C-Wv0Y4SiH7zXEAy9r_5Hrz_wB4PucDDo9_3u0O_3-4O_o_4H7z8_P9-O4v0n9B5eS6V0hFIIqXQG1wpaYSkEwzXWylAIGx3ACuM05FppWOC10jA3N7f6YgMrrRQK-iilYgVzM2_0Kj4f6c4dFkIKpXQGMy0Fw7nWiudawT8I3mCprYIZNgrGmCsF3369m2_rN57nE4Z203eM50rCDEvtFMx13qj4fKQ791gIKZTSGcx1oWEGjXZawe94Y_2j5w2uFHz75W4e_d_59H_i3x-sVfDt17v5tn7jeT5haDd9x_id79j6jef5hKHd9B3jRyVhhm2tFMx13qj4fKQ791gIKZTSGcy10jDHUlsFc2wUzLHVTsEcW-01zLHRTsEcW-00zLHVXo_nm53_G8-zCUNX03eM51rBDCv9N6xW8O3Xu_m2fuN5PmFoN33H-J0vmPqN5_mEod30HeN3vmLqN57nE4Z203eM3_mOqd94nk8Y2k3fMX7nB6Z-43k-YWg3fcf4gW-Y-o3n-YSh3fQd4we-Yeo3nucThnbTd4w_8BNTv_E8nzC0m75j_MGv2PqN5_mEod30HeM5rTXMsdIwx0p7DXOstFMwx0p7DXOstM_x_N-P8z81_QdD21Qn)
