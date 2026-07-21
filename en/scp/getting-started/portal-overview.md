# Portal Overview — SCP

This section describes the layout and main areas of the Self-Service Cloud Portal.

---

## Navigation

The SCP uses a **top navigation bar**. To move between sections, click the **hamburger menu (☰)** in the top-left corner. This opens a mega-menu panel with a search bar and the following sections:

<!-- screenshot: SCP mega-menu open -->

**Compute**
- Virtual Machines
- Physical Machines

**Hybrid Cloud**
- Third-Party Public Cloud

**IDaaS**
- Service Provider Management

**Monitor Center**
- Alerts

**System**
- Tasks
- Key Pairs

The left side of the mega-menu also shows a **Resources / My Favorites** panel for quick access to pages you have pinned.

In the **top-right corner** of the screen you will see your account displayed as **Username / Role** (for example, *Zhanat / Member*). The top bar also shows a **language switcher** (English / other), notification icons, and a **Work Orders** button for tracking pending VM requests.

<!-- screenshot: SCP top bar — account indicator and language switcher -->

---

## Landing Page

After logging in you land on the **Virtual Machines** page directly. There is no separate dashboard or resource overview page. To see resource usage for a specific VM, click its name to open its **VM Summary** page.

---

## Virtual Machines

**Compute → Virtual Machines** is the main working area of the portal. It lists all VMs in your tenant.

<!-- screenshot: SCP Virtual Machines list — empty state -->

The table shows the following columns:

| Column | Description |
|---|---|
| **Name** | The display name of the VM |
| **Status** | Current power state. Possible values include: Running, Stopped, Error, Alerting, and others. |
| **Resource Pools** | The resource pool the VM belongs to |
| **Guest OS** | The operating system installed on the VM |
| **IP** | The VM's internal IP address. Shows **-** if vmTools is not installed on the VM. |
| **Elastic IP** | A public IP address assigned to the VM by the administrator (if any) |
| **CPU** | Number of virtual CPUs assigned |
| **Memory** | RAM assigned |
| **Memory Usage** | Real-time memory consumption |
| **Storage** | Total disk size |
| **Storage Usage** | Real-time disk usage |
| **Operation** | Per-VM action buttons: **Console** and **More** |

**Toolbar actions** (apply to selected VMs):

| Button | Description |
|---|---|
| **+ Request** | Open the Apply for VM form to request a new VM |
| **Power On** | Start the selected VM(s) |
| **Shut Down** | Gracefully shut down the selected VM(s) |
| **Columns** | Show or hide table columns |
| **More** | Additional bulk actions |

**Per-VM actions** — click **Console** to open the VNC console, or click **More** to open the action dropdown:

| Action | Description |
|---|---|
| **Power On** | Start the VM |
| **Shut Down** | Gracefully shut down the VM |
| **Suspend** | Pause the VM and save its state to memory |
| **Reset Password** | Reset the OS user password (requires vmTools) |
| **Bind Key Pair** | Associate an SSH key pair with the VM (requires vmTools) |
| **Reboot** | Gracefully restart the VM |
| **Reset** | Force-restart the VM without graceful shutdown |
| **Power Off** | Force-stop the VM immediately |
| **Edit** | Rename the VM or update its description |
| **Change configuration** | Modify the VM's vCPU and memory allocation |
| **Take Snapshot** | Create a snapshot of the current VM state |
| **Snapshots** | View and manage existing snapshots for the VM |

### VM Summary page

Click on a VM's **Name** to open its **VM Summary** page. This page shows:

<!-- screenshot: VM Summary page -->

**Status section** — three gauges showing real-time consumption:
- **Total CPU** — current CPU usage percentage and clock speed
- **Total Memory** — used vs. remaining RAM
- **Total Disk Space** — used vs. remaining storage

**Running Status section** — time-series graphs with configurable time range and export:
- **CPU** — CPU usage over time
- **Memory** — memory usage over time
- **Network** — inbound/outbound throughput (bps and pps)
- **Disk** — IO speed and IOPS

**Configuration panel** (right side) — displays all VM properties: name, status, OS, resource pool, network type, storage policy, uptime, boot order, and vmTools status. Scrolling down in this panel also shows the attached disks (name, size, storage tag, disk file) and network interfaces (NIC1, NIC2, etc.).

**Left sidebar** — sub-sections for the selected VM:
- **Summary** — the main metrics page described above
- **Snapshots** — manage VM snapshots
- **Tasks** — operation history for this VM
- **Alerts** — alerts triggered for this VM

---

## Physical Machines

**Compute → Physical Machines** lists bare-metal servers allocated to your tenant. In this deployment no physical machines are currently allocated to tenants, so the page shows "No data available".

---

## Hybrid Cloud

**Hybrid Cloud → Third-Party Public Cloud** shows connections to external public cloud providers configured by your administrator.

<!-- screenshot: SCP Hybrid Cloud page -->

---

## IDaaS

**IDaaS → Service Provider Management** (titled **Service Providers** in the portal) allows you to configure SSO (Single Sign-On) access for your users. Once a service provider is set up, local users can be authorized to access it through SSO, reducing the overhead of managing multiple accounts.

If no service providers have been created yet, the page displays "No service provider available now." Contact your administrator to set one up.

---

## Monitor Center

**Monitor Center → Alerts** shows notifications about the health and status of your resources.

<!-- screenshot: SCP Monitor Center — Alerts page -->

Per-VM metrics (CPU, memory, network, disk graphs) are also available directly from the **VM Summary** page — click any VM name in the Virtual Machines list to open it.

---

## System

| Item | Description |
|---|---|
| **Tasks** | Log of background operations (VM creation, deletion, etc.) and their status |
| **Key Pairs** | SSH key pairs for passwordless authentication on Linux VMs. Use **+ Create Key Pair** to auto-generate a key pair (download the private key immediately — it is shown only once) or to import an existing public key. After creation, bind a key pair to a running VM via More → **Bind Key Pair** (requires vmTools). |

---

> **Need help?** Email [cns-support@fcd.kz](mailto:cns-support@fcd.kz).
