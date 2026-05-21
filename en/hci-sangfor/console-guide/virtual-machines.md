# Virtual Machines

Virtual machines (VMs) are the core compute resource in the platform. This guide covers creating, connecting to, and managing VMs.

---

## Create a Virtual Machine

1. Go to **Compute** → **Virtual Machine**.
2. Click **New**.
3. Select the **Resource Pool** and **Image** for the VM.
4. Configure **Compute** (CPU and memory), **Storage** (disk size and type), and **Networking** (VPC/subnet or classic network), then click **Next**.
5. Fill in the VM details:

| Field | Description |
|---|---|
| **Name** | Display name for the VM |
| **Description** | Optional description |
| **Group** | Organizational group (optional) |
| **Administrator Password** | Password for the OS administrator account |
| **Hostname** | Hostname assigned to the OS (optional) |
| **Expiration Date** | Set a validity period or leave as **Unlimited** |

6. Confirm the summary and click **OK** to create the VM.

Once created, click **Console** to connect to the VM, or use **More** for additional actions.

---

## VM Actions

After a VM is created, click **More** in the VM list to access the following actions:

| Action | Description |
|---|---|
| **Console** | Open a browser-based VNC console |
| **Shut Down** | Gracefully shut down the guest OS |
| **Suspend** | Pause the VM (saves state to memory) |
| **Restart** | Reboot the guest OS |
| **Power Off** | Force stop the VM immediately |
| **Bind Key Pair** | Attach an SSH key pair for login |
| **Snapshots/Backups Management** | Manage snapshots and backup policies |
| **Clone** | Clone the VM |
| **Create Image** | Create a built-in image from this VM |
| **Export** | Export the VM to OVA, VMA, OVF, MF, or VMDK |
| **Delete** | Delete the VM (moves to Recycle Bin) |

---

## Connect to a VM

### Console (Browser)

Click **Console** in the VM list or VM summary. A browser-based VNC session opens without requiring network connectivity to the VM.

> Use Console to access VMs during OS installation or when the VM is not reachable over the network.

### SSH (Linux)

Ensure the VM has a reachable IP address, then:

```bash
ssh <username>@<vm-ip>
```

### RDP (Windows)

1. Open **Remote Desktop Connection** on your local machine.
2. Enter the VM's IP address.
3. Log in with the administrator credentials set at VM creation.

---

## View VM Details

Click a VM name to open the **VM Summary** page. The left panel provides:

| Tab | What's here |
|---|---|
| **Summary** | CPU, memory, disk usage gauges and performance charts |
| **Snapshots** | Create and manage snapshots |
| **Backups and DR** | Backup history, backup policies, and disaster recovery |
| **Tasks** | Ongoing task status |
| **Alerts** | VM-specific alert events |

The **Summary** tab shows configuration details including Guest OS, Run Location, Datastore, Storage Policy, hostname, Tags, CPU Clock Speed, Logical Space Used, Used Memory, and Uptime.

---

## Snapshots

Snapshots capture the disk state of a VM at a point in time.

### Take a Snapshot

1. Click the VM name → **Snapshots** → **Take Snapshot**.
2. Optionally enable **Quiesce Guest File System** for application-consistent snapshots (requires VM Tools installed in the guest OS).
3. Click **OK**.

New VMs use **External Disk Based Snapshots** by default, which free space when deleted without impacting VM performance. VMs with existing internal snapshots retain the internal type.

### Restore from a Snapshot

1. In the **Snapshots** view, click **Recover** on the snapshot.
2. Select **All** disks or **Specified** disks.
3. Optionally check **Power on the VM after recovery** and **Take a snapshot before recovery**.
4. Click **OK**.

> Restoring a snapshot rolls the VM's disk back to the captured state. Any data written after the snapshot was taken will be lost. Use **Take a snapshot before recovery** to preserve the current state first.

---

## Backup

### Manual Backup

1. Click the VM name → **Backups and DR**.
2. Click **Backup** to back up the VM immediately.

Monitor progress in **Tasks**.

### Scheduled Backup Policy

1. Click the VM name → **Backups and DR** → **Setting**.
2. Click **Create Backup Policy**.
3. Select the VMs to include, configure the **Schedule** (Weekly/Daily/Hourly), **Backup Point Retention Method**, and **Policy Name**.
4. Click **OK**.

### File Recovery

If a file is accidentally deleted, you can recover individual files from a backup:

1. Click the VM name → **Backups and DR** → **Browse Files**.
2. Navigate to the file in the backup, select it, and click **Download File**.

> File recovery supports Windows NTFS/FAT32 and Linux ext3/ext4/xfs. Files over 5 GB cannot be browsed.

---

## Export a VM

The VM must be powered off before export.

1. In the VM list, click **More** → **Export**.
2. Select the file format: **OVA**, **VMA**, **OVF**, **MF**, or **VMDK**.
3. For OVA, select the target VMware Workstation software version.
4. Click **Export** and wait for the download link.

---

## Clone a VM

1. In the VM list, click **More** → **Clone**.
2. Configure the cloned VM name and settings.
3. Click **OK**.

---

## Delete a VM

1. In the VM list, click **More** → **Delete**.
2. Confirm the deletion.

Deleted VMs move to the **Recycle Bin** (under **Management**) and can be restored within 30 days.

---

> **Next step:** [Configure Networking](networking.md).
