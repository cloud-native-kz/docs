# Monitoring & Alerts

The platform provides a monitoring dashboard for tracking VM and network performance, an alert center for viewing platform events, and a quota overview for tracking resource usage.

---

## Monitoring Dashboard

The monitoring dashboard displays real-time and historical performance charts for your VMs and elastic IPs.

### Create a Monitoring Panel

1. Go to **Monitor Center** → **Monitoring Dashboard**.
2. Click **New Panel**.
3. Select the **Object Type**:
   - **Virtual Machine** — monitor CPU, memory, disk, network throughput, IOPS, and IO speed
   - **Elastic IP** — monitor inbound/outbound traffic
   - **Shared Bandwidth** — monitor shared bandwidth usage
4. Select the specific resource(s) from the list.
5. Check the metrics to display.
6. Click **OK**.

The panel appears on the dashboard and updates in real time.

### VM Performance Metrics

When monitoring a virtual machine, the following metrics are available:

| Metric | Description |
|---|---|
| **CPU Usage** | vCPU utilization (%) |
| **Memory Usage** | RAM used vs. total |
| **IOPS** | Disk read/write operations per second |
| **IO Speed** | Disk read/write speed |
| **Throughput** | Inbound/outbound network throughput |
| **Throughput (pps)** | Packets per second |
| **Disk Usage** | Disk space used |

### VM-Level Performance Charts

To view detailed performance data for a single VM:

1. Go to **Compute** → **Virtual Machine**, click the VM name.
2. The **Summary** tab shows CPU and memory gauges and time-series charts.
3. Use the time range selector (Last hour, custom range) to adjust the view.
4. Click **Export** on a chart to download it as PNG, JPEG, SVG, or CSV.

---

## Alerts

The alerts view shows all platform events affecting your resources.

1. Go to **Monitor Center** → **Alert**.
2. The alert list shows:

| Column | Description |
|---|---|
| **Severity** | Critical, Warning, or Info |
| **Timestamp** | When the alert was generated |
| **Object Type** | Type of affected resource |
| **Object** | Specific resource name |
| **Resource Pool** | The cluster where the resource lives |
| **Event** | Alert type description |

Use the filter controls to narrow alerts by time range, severity, or object type.

> VM-level alerts (e.g. expiration warnings, backup failures) are also visible in the **Alerts** tab within each VM's summary page.

---

## Resource Quota

Track your current resource usage against the quota allocated by the platform administrator.

1. Click your account name in the top-right corner → **Edit Resource Quota**.
2. The **Quota Overview** shows all resource categories:

**Compute:**

| Resource | Description |
|---|---|
| **Virtual Machines** | Number of VMs allowed vs. used |
| **CPU** | Total vCPU cores allocated |
| **Memory** | Total RAM allocated |

**Storage:**

| Resource | Description |
|---|---|
| **High Performance Storage** | SSD-backed storage quota |
| **Performance Medium Storage** | HDD-backed storage quota |
| **Backup Repository** | Storage quota for VM backups |
| **Private Image Repository** | Storage quota for private images |

**Networking:**

| Resource | Description |
|---|---|
| **Elastic IPs** | Number of public IPs allocated |
| **Bandwidth** | Bandwidth quota per line |

**NFV Devices:**

| Resource | Description |
|---|---|
| **vAD** | Application Delivery Controller instances |
| **vNGAF** | Virtual next-generation firewall instances |
| **SSL VPN** | SSL VPN instances |

If you need more resources, submit a request via **Work Orders**.

---

> **Also see:** [Kubernetes Storage Integration](kubernetes.md) · [Managed Databases (DMP)](databases.md)
