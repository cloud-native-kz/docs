# Glossary — SCP

| Term | Definition |
|---|---|
| **SCP** | Self-Service Cloud Portal — the web portal (accessed at `https://<SCP-address>/login`) that tenants use to manage virtual resources on the HCI platform. |
| **Tenant** | An isolated organizational unit on the HCI platform with its own VMs and storage. Each tenant corresponds to one customer or team. |
| **Apply for VM** | The name of the VM creation form in the SCP. Accessed via the **+ Request** button on the Virtual Machines page. |
| **Work Orders** | A queue of pending VM requests awaiting administrator approval. Accessible via the Work Orders button in the top-right corner of the Virtual Machines page. |
| **Virtual Machine (VM)** | A software-based computer running on the HCI infrastructure. Each VM is allocated vCPU, RAM, and storage. |
| **vCPU / Core** | Virtual CPU core — a virtual processor unit assigned to a VM. Referred to as "cores" in the Apply for VM form. |
| **Resource Pool** | A logical grouping of physical compute and storage resources on the HCI platform. Selected when requesting a VM. In this deployment the pool is named **HCI**. |
| **ISO Image** | A disc image of an OS installer (e.g., Ubuntu, openEuler). VMs created from ISO images boot into the OS installation wizard — you must complete installation via VNC console before the VM is usable. |
| **System Disk** | The boot disk of a VM. Contains the operating system after installation. Added automatically as part of VM creation. |
| **Data Disk** | An additional storage volume added to a VM. Up to 3 data disks can be added during VM creation. Must be formatted and mounted inside the OS before use. |
| **Storage Tag** | A label identifying the storage tier for a disk. In this deployment the available tag is **High Performance Storage**. |
| **Storage Policy** | The data redundancy policy for a disk. **Default Policy** stores a single copy; **HA Policy** mirrors data across nodes for high availability. |
| **Classic Network** | The network type available to tenants in this deployment. Connects VMs to the infrastructure's internal network. |
| **Elastic IP** | A public IP address that can be assigned to a VM by the administrator to allow external access. Visible in the VM list but not assignable by tenants directly. |
| **VNC Console** | A browser-based remote display that lets you access a VM directly from the portal. Opened via the **Console** button in the Operation column. Used to complete OS installation and for emergency access when SSH/RDP is not available. |
| **vmTools** | A guest agent installed inside the VM after OS installation. Required for the portal to display the VM's IP address, and for Reset Password, Bind Key Pair, and automatic fault recovery to function. The VNC console shows an Install Now link when vmTools is missing. |
| **VM Summary** | The VM detail page, opened by clicking a VM's name in the list. Shows real-time CPU, memory, and disk gauges, plus time-series graphs for CPU, memory, network, and disk IO. |
| **Change configuration** | A per-VM action (in the More dropdown) that allows modifying the VM's vCPU and memory allocation. |
| **Snapshot** | A saved state of a VM at a specific point in time (disk and memory). Allows rolling back the VM to that state — for example, after a failed update or for debugging. Not a backup: the snapshot is stored on the same infrastructure as the VM. Created via More → **Take Snapshot**. Managed via More → **Snapshots** or the VM detail page sidebar. |
| **Validity Period** | The expiration setting for a VM, configured in the Apply for VM form. Defaults to **Unlimited** (no expiration). Select **Specified** only if you need a temporary VM with an automatic end date. If a VM reaches its expiration date, it may be automatically stopped or released. Extensions are handled by your administrator. |
| **Tasks** | Found under **System → Tasks**. A log of background operations (VM creation, deletion, power changes) and their completion status. |
| **Key Pairs** | SSH key pairs managed under **System → Key Pairs**. Use **+ Create Key Pair** to auto-generate a key pair (download the private key immediately — shown only once) or to import an existing public key (Base64-encoded). After creation, bind the key pair to a running Linux VM via More → **Bind Key Pair** (requires vmTools). |
| **Monitor Center** | The monitoring section of the SCP mega-menu. Contains **Alerts** about resource health and status events. |
| **HCI** | Hyper-Converged Infrastructure — the underlying platform that combines compute, storage, and networking in a unified system. The SCP runs on top of HCI. |
