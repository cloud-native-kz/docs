# Storage

Storage in the platform is managed through VM disk configuration and resource quotas. Each VM has a system disk and can have additional data disks.

---

## VM Disk Configuration

Disk sizes and types are configured when creating or editing a VM.

### Disk Settings at VM Creation

When creating a VM (**Compute** → **Virtual Machine** → **New**), configure storage in the **Storage** section:

| Field | Description |
|---|---|
| **Storage Tag** | Storage tier — e.g. **High Performance Storage** (SSD-backed) or **Performance Medium Storage** |
| **Disk Size** | System disk capacity in GB |
| **Additional Disks** | Add extra data disks with their own size and storage tag |

### Add a Disk to an Existing VM

1. In the VM list, click **More** → **Edit**.
2. Add a new disk under the storage section.
3. Click **OK**.

The new disk appears inside the guest OS as an uninitialized block device. Format and mount it before use.

**Linux:**

```bash
# Identify the new disk
lsblk

# Partition, format, and mount (example: /dev/vdb)
sudo fdisk /dev/vdb
sudo mkfs.ext4 /dev/vdb1
sudo mkdir /data && sudo mount /dev/vdb1 /data
echo '/dev/vdb1 /data ext4 defaults 0 2' | sudo tee -a /etc/fstab
```

**Windows:**

1. Open **Disk Management** (`diskmgmt.msc`).
2. Right-click the new disk → **Initialize Disk**.
3. Create a new simple volume and assign a drive letter.

---

## Storage Quota

The platform administrator allocates a storage quota to your tenant. To view your current usage and limits:

1. Click your account name in the top-right corner → **Edit Resource Quota**.
2. The **Quota Overview** shows:

| Resource | Description |
|---|---|
| **High Performance Storage** | SSD-backed storage quota and current usage |
| **Performance Medium Storage** | HDD-backed storage quota and current usage |
| **Liquid Network Storage** | Network-attached storage quota |
| **Backup Repository** | Quota available for VM backups |
| **Private Image Repository** | Quota for your private VM images |

If you need more storage quota, submit a request via **Work Orders**.

---

## Backup Storage

VM backups consume your **Backup Repository** quota. To check backup usage, go to **Edit Resource Quota** (see above) or view the backup status in the VM summary page (**Backups and DR** tab).

To configure scheduled backups, see [Virtual Machines — Scheduled Backup Policy](virtual-machines.md#backup).

---

> **Next step:** [Configure Security Services](security.md).
