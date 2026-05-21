# Managed Databases (DMP)

Sangfor DMP (Database Management Platform) is a separate web console for deploying and managing relational database instances on top of HCI and SCP. It handles provisioning, high availability, backups, and lifecycle management.

**Supported engines and architectures:**

| Engine | Versions | Architectures |
|---|---|---|
| **MySQL** | 5.7, 8.0 | Single Instance, One-Primary-One-Replica, One-Primary-Two-Replicas |
| **Oracle** | 11g, 12c, 19c | Single Instance, RAC |
| **SQL Server** | 2012, 2016, 2019 | Single Instance, Always On (2 or 3 nodes) |
| **PostgreSQL** | 13 | Single Instance, Active-Standby |

---

## Access DMP

DMP has its own web console separate from the SCP tenant portal. Open the DMP URL provided by your administrator and log in with your SCP account credentials.

The DMP console has the following sections: **Databases**, **Data Protection**, **Monitoring**, **System**.

---

## Create a Database Instance

1. Go to **Databases** → **Database List** → **New**.
2. Select the **engine** (MySQL, Oracle, SQL Server, or PostgreSQL) and the **deployment architecture** (Single Instance, Primary-Replica, etc.), then click **Go to Deployment Wizard**.
3. Configure the instance:

| Field | Description |
|---|---|
| **Name** | Display name shown in the Database List |
| **Resource Pool** | The cluster resource pool to deploy into |
| **Image** | Select the base version and configuration method |
| **Specifications** | Number of vCPUs and memory (GB) |
| **Storage Tag** | Storage tier: High Performance Storage, Performance Sensitive, or Capacity Sensitive |
| **Storage Location** | Datastore where the database VM will be created |
| **System Disk Capacity** | Boot disk — stores OS and database software (fixed size) |
| **Data Disk Capacity** | Stores database data files |
| **Log Disk Capacity** | Stores transaction logs |
| **NIC** | For VPC deployment: select the VPC subnet. For Classic Network: specify IP, netmask, and gateway |
| **Listener** | Database service port (default: 3306 for MySQL, 1521 for Oracle, 1433 for SQL Server, 5432 for PostgreSQL) |

4. Click **Next** to configure database settings: **Database Name**, **Character Set**, **Password**, and optional parameter templates.
5. Click **Next** to configure backup (optional at this stage — can be set up after deployment).
6. Click **Next** to review, then confirm deployment.

Monitor progress under **System** → **Tasks**. Status changes to **Running** when the database is ready.

> Only images provided by DMP can be used to deploy database instances.

---

## Connect to a Database

### SQL DMC (Browser-Based)

DMP includes a built-in SQL console for running queries directly from the browser.

1. Go to **Databases** → **Database List**.
2. Click **More** next to the database → **SQL DMC**.
3. Select the node and enter the database password, then click **Log In**.

### Standard Client

Connect using any compatible database client. The connection endpoint is the IP address of the database VM (visible in the database topology or detail page).

**MySQL:**
```bash
mysql -h <db-ip> -P 3306 -u root -p
```

**PostgreSQL:**
```bash
psql -h <db-ip> -p 5432 -U postgres
```

**SQL Server:**
```bash
sqlcmd -S <db-ip>,1433 -U sa -P '<password>'
```

**Oracle:**
```bash
sqlplus sys/<password>@//<db-ip>:1521/<db-name> as sysdba
```

> If the database is deployed in a VPC, ensure the VPC ACL rules allow inbound traffic on the database port from your client's subnet.

---

## Manage Database Accounts

1. Go to **Databases** → **Database List** and click the database name.
2. Navigate to the **Accounts** tab → **New Account**.
3. Specify **Username**, **System Permissions**, **Password**, and click **OK**.
4. To set object-level permissions, click **Set Object Permissions** for the account.

---

## Backups

### Step 1 — Configure a Backup Repository

Before taking any backup, you must configure a backup repository for the database.

1. In **Database List**, click the database name to open its detail page.
2. Go to **Data Protection** → **Backup Repository** → **Configure Now**.
3. Select the storage type (**iSCSI** or **NFS**) and fill in the connection details provided by your administrator.
4. Click **OK**.

### Create a Manual Backup

1. In the database detail page, go to **Data Protection** → **Backup Repository**.
2. Click **Manual Backup**, enter a description, and click **OK**.

### Configure a Scheduled Backup Policy

1. In the database detail page, go to **Data Protection** → **Scheduled Backup Policy** → **Configure Now**.
2. Select or create a backup policy (schedule and retention period).
3. Click **OK**.

### Restore from Backup

1. In the DMP console, go to **Data Protection** → **Database Backup** → **Backups**.
2. Locate the backup point and click **Recover from Backup**.
3. Select the target database and confirm.

### Continuous Data Protection (CDP)

CDP captures incremental transaction logs so you can restore to any point in time.

> CDP is supported for **Oracle** (11g, 12c, 19c) and **MySQL 5.7** only. A Scheduled Backup Policy must be enabled before CDP can be activated.

1. In the database detail page, go to **Data Protection** → **CDP Policy**.
2. Enable CDP.
3. To recover: go to **Data Protection** → **Database Backup** → **Backups**, select a CDP recovery point, and click **Recover from Backup**.

---

## Database Lifecycle Management

From **Databases** → **Database List**, click **More** next to a database to access:

| Action | Description |
|---|---|
| **Restart** | Restart the database service |
| **Shut Down** | Stop the database |
| **Start** | Start a stopped database |
| **Delete** | Remove the database instance (must be in Shutdown state first; the underlying VM moves to the SCP Recycle Bin) |
| **SQL DMC** | Open the browser-based SQL console |
| **Edit Settings** | Modify name, CPU/memory, disk sizes, and network configuration |

To view runtime metrics (connections, queries, replication lag), click the database name → **Database Details** → **Running Overview**.

---

> **Next step:** [Monitor your resources](monitoring.md).
