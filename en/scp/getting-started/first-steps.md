# First Steps — SCP

After logging in for the first time, complete these steps to get your workspace up and running.

---

## Step 1 — Request Your First Virtual Machine

Go to **Compute → Virtual Machines** in the mega-menu, then click **+ Request**.

<!-- screenshot: SCP Virtual Machines page — + Request button -->

This opens the **Apply for VM** form. Fill in all sections from top to bottom, then click **OK** at the bottom to submit.

<!-- screenshot: SCP Apply for VM form — full page -->

### Resource Pool

Select the resource pool your VM will be created in.

<!-- screenshot: SCP Apply for VM — Resource Pool section -->

In this deployment, the available pool is **HCI**. Click it to select it.

### Image

Select an operating system image for your VM. Use the **All OSes** and **All Types** dropdowns or the search field to filter the list.

<!-- screenshot: SCP Apply for VM — Image section -->

Available images in this deployment:

| Image | OS | Type |
|---|---|---|
| openEuler-24.03-LTS-SP3 | openEuler | ISO |
| ubuntu-26.04 | Ubuntu | ISO |
| ubuntu-24.04.4 | Ubuntu | ISO |

> **Important — ISO images require manual OS installation.** All images are ISO type, meaning the VM will boot from the installation disc. After the VM is created, you must connect via VNC console and complete the OS installation manually before the VM is usable. See [Step 2](#step-2--connect-to-your-vm-and-install-the-os) below.

> **Don't see the image you need?** Contact your administrator to request it be added to the image library.

### VM Count

In the **Number of VMs** field, enter how many VMs to create from this request. For a first-time setup, enter **1**.

<!-- screenshot: SCP Apply for VM — VM Count section -->

### Compute

Set the CPU and memory for your VM.

<!-- screenshot: SCP Apply for VM — Compute section -->

**CPU:** click a preset button — **1 core**, **2 cores**, **4 cores**, **6 cores**, **8 cores**, **12 cores**, **16 cores** — or type a value in the input field to the right.

**Memory Size:** click a preset button — **1 GB**, **2 GB**, **4 GB**, **6 GB**, **8 GB**, **12 GB**, **16 GB**, **32 GB**, **48 GB**, **64 GB** — or type a value in the input field.

Click **Show More** to reveal additional compute options.

### Storage

Configure the storage for your VM.

<!-- screenshot: SCP Apply for VM — Storage section -->

| Field | Description |
|---|---|
| **Storage Tag** | The storage tier to use. In this deployment, **High Performance Storage** is available. |
| **Storage Policy** | Choose **Default Policy** or **HA Policy** (high availability, mirrors data across nodes). |
| **Disk** | Click **+ Add** to add a data disk. Up to 3 disks can be added per VM. |

> **Note about data disks:** After the VM is created, any data disks you add here will appear as unformatted block devices inside the OS. You must **format and mount** them from within the VM console before they can be used.

### Networking

Select the network type for your VM.

<!-- screenshot: SCP Apply for VM — Networking section -->

In this deployment, the available network type is **Classic Network**. Click it to select it.

> **Note:** There is no option to assign a static IP or choose a specific subnet from this form. IP address assignment is handled by the infrastructure. If you need specific network configuration, contact your administrator.

### Submit the Request

When all sections are complete, click **OK** at the bottom of the form (or **Cancel** to discard).

<!-- screenshot: SCP Apply for VM — OK and Cancel buttons -->

After submitting, the request enters an **approval queue**. To check its status, click the **Work Orders** button in the top-right corner of the Virtual Machines page. Once approved by your administrator, the VM will be provisioned and appear in the list.

---

## Step 2 — Connect to Your VM and Install the OS

Because all images are ISO type, your VM will boot into the OS installer on first start. You must complete the installation via the VNC console before the VM is accessible over SSH or RDP.

### Open the VNC Console

1. In the **Virtual Machines** list, find your VM.
2. Click the **Console** button in the **Operation** column.
3. A VNC session opens in a new browser tab.

<!-- screenshot: SCP VM VNC console — OS installer screen -->

The console toolbar provides: **Power On**, **Suspend**, **Shut Down**, **Power Off**, **Restart**, **Reset**, **Hot Keys**, **Reset Password**, **Paste Command**, **Full Screen**, and a refresh button.

> **Note:** You may see a yellow banner — "vmTools is not installed on this virtual machine" — at the top of the console. This is expected on a fresh VM and can be addressed after OS installation. See the vmTools entry in the [FAQ](./faq.md).

4. Complete the OS installation as prompted. Set a root or administrator password during installation — you will need it to log in.

> **Tip:** Keep the VNC console open throughout installation. Duration varies depending on the OS.

### After Installation — Connect via SSH (Linux)

Once the OS is installed and the VM has rebooted:

1. Note the **IP** address shown in the VM list. If it still shows "-", install vmTools first — the VNC console has an **Install Now** link in the yellow banner. After vmTools is running, the IP will appear.
2. Connect from a terminal: `ssh <username>@<VM-IP>`
3. Use the credentials you set during OS installation.

> **Can't reach the IP from your workstation?** VM networking is on a private internal network. External access requires your administrator to configure routing. Contact your administrator if you cannot reach your VM's IP.

### After Installation — Connect via RDP (Windows)

1. Note the **IP** address shown in the VM list.
2. Open **Remote Desktop Connection** and enter the VM's IP address.
3. Log in with the credentials you set during OS installation.

---

## Step 3 — Monitor Your VM

To view detailed metrics for a running VM, click its **Name** in the Virtual Machines list to open the **VM Summary** page.

<!-- screenshot: VM Summary page -->

The Summary page shows:
- **Status gauges** — real-time CPU usage, memory (used vs. remaining), and disk space (used vs. remaining)
- **Running Status graphs** — time-series charts for CPU, memory, network throughput (inbound/outbound), and disk IO speed/IOPS. The time range is configurable and data can be exported.

The left sidebar of the VM detail page also provides:
- **Snapshots** — create and manage VM snapshots
- **Tasks** — operation history for this specific VM
- **Alerts** — alerts triggered for this VM

For platform-wide alerts, go to **Monitor Center → Alerts** in the mega-menu.

**System → Tasks** (in the mega-menu) shows the status of all background operations across your tenant — useful for tracking VM creation and other provisioning tasks.

---

> **Need help?** Email [cns-support@fcd.kz](mailto:cns-support@fcd.kz).
