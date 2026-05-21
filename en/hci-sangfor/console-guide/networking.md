# Networking

The platform provides two network modes for tenants: **VPC** (Virtual Private Cloud) for logically isolated private networks, and **Classic Network** for direct communication with the physical data center environment.

---

## Network Topology

The Topology view provides a visual canvas of your entire network — VMs, subnets, routers, NFV devices, and their connections.

Go to **Networking** → **Topology**.

From the topology canvas you can:
- Add VMs to subnets using drag-and-drop
- Create subnets and connect devices visually
- View inbound/outbound traffic rates on the external network link
- Access shortcut operations on VMs (power on/off, restart, bind elastic IP, clone)
- Configure subnet settings, multi-NIC configuration, disk mounting, and more

Two network types are available in the topology selector:
- **VPC** — logically isolated private cloud network
- **Classic Network** — direct communication with the data center

---

## VPC

A Virtual Private Cloud (VPC) is a logically isolated private network within your tenant. All resources in a VPC communicate privately at Layer 3 through the VPC's internal router. Resources across different VPCs are not reachable from each other by default.

Go to **Networking** → **Network Deployment** to manage VPCs.

### Subnets

A subnet is a network segment within a VPC. VMs and NFV devices deployed in a subnet share the same network segment.

- Subnets support DHCP by default (IP and DNS are auto-configured)
- All subnets within the same VPC are intercommunicable at Layer 3
- Up to 20 subnets can be created per VPC by default

#### Create a Subnet

1. Go to **Networking** → **Network Deployment**, click your VPC name.
2. Select **Subnet** and click **New**.
3. Configure:

| Field | Description |
|---|---|
| **Name** | Subnet display name |
| **Network Segment** | e.g. `192.168.0.0/24` (supports 192.168.x.x, 10.0–253.x.x, 172.16–28.x.x) |
| **DHCP** | Enabled by default; uncheck to disable |
| **IP Range** | e.g. `192.168.0.2–192.168.0.254` |
| **Gateway** | e.g. `192.168.0.1` |

4. Click **OK**.

> Network segment and gateway cannot be modified after the subnet is created.

---

### Access Control List (ACL)

ACL rules control traffic between subnets, between the VPC and external networks. Rules are matched top-to-bottom; the first match applies.

1. In your VPC, select **ACL** and click **New**.
2. Configure:
   - **Source** and **Destination**: Any IP, Specified IP, Specified Subnet, or Specified IP Range
   - **Service**: select a predefined service (e.g. TCP 3389 for RDP) or define a custom protocol/port
   - **Action**: **Allow** or **Drop**
3. Click **OK**.

By default, all traffic is allowed. Add deny rules to restrict access.

---

### Port Mapping (Destination NAT)

Map a public elastic IP port to an internal VM port to expose services to the internet.

**Example:** map EIP TCP 80 → VM internal port 80.

1. In your VPC, select **Destination NAT** and click **New**.
2. Configure the **Original Data Packet**:
   - **Source IP**: All (any public IP) or Specified
   - **Elastic IP**: select the EIP bound to this VPC
   - **Protocol**: TCP, UDP, or ICMP
   - **Dst Port**: external port (e.g. `80`)
3. Configure the **Translated Data Packet**:
   - **Internal IP**: select the target VM
   - **Mapped Port**: internal port (e.g. `80`)
4. Click **OK**.

> The VPC must have an elastic IP associated. Go to **Network Settings** to associate one.

---

### Static Routes

Add static routes to reach external network segments.

1. In your VPC, select **Static Route** and click **New** or **New Routes**.
2. Fill in **Destination IP**, **Netmask**, and **Next-Hop IP**.
3. Click **OK**.

---

### Internal DNS

Map internal domain names to IP addresses for VMs within the VPC.

1. In your VPC, select **Internal DNS** and click **New**.
2. Enter a **Domain Name** (e.g. `www.internal.com`) and **IP Address**.
3. Click **OK**.

---

### Network Settings

Bind an elastic IP to the VPC edge and configure the DNS server.

1. In your VPC, select **Network Settings**.
2. If no EIP is associated, click **Associate Now**.
3. Click **Edit** to change the **Preferred DNS** and **Alternate DNS** servers.

> DNS changes propagate to all VMs within one day. To apply immediately, update the DNS inside the VM directly.

---

## Elastic IP

An Elastic IP (EIP) is a public IP address that can be dynamically bound to and unbound from VMs, routers, ADC devices, or SSL VPNs within your VPC.

### Add Elastic IPs

1. Go to **Networking** → **IP and Bandwidth** → **Elastic IP Pools**.
2. Click **New**.
3. Configure:
   - **VPC**: All or a specific VPC
   - **Number of EIPs**: how many IPs to add
   - **Line**: BGP or other available line types
   - **Bandwidth Type**: **Dedicated Bandwidth** (per-IP) or **Shared Bandwidth**
   - **Bandwidth**: select or enter the desired Mbps
4. Click **OK**.

### Bind / Unbind an EIP

Click **Associate** or **Disassociate** next to the EIP. Select the **Resource Type** (Virtual Machine, Router, ADC, or SSL VPN) and the specific resource.

> After associating an EIP with a VM, configure ACL rules on the VPC router to allow the desired traffic.

---

## Shared Bandwidth

Shared Bandwidth allows multiple EIPs to share a single bandwidth pool.

1. Go to **Networking** → **IP and Bandwidth** → **Shared Bandwidth**.
2. Click **New**, enter a **Name**, select the **VPC and Line**, set the **Bandwidth**, and associate EIPs.
3. Click **OK**.

---

## Classic Network

The Classic Network mode allows VMs to communicate directly with the physical data center without VPC isolation.

1. Go to **Networking** → **Topology**, and select **Classic Network** from the topology selector.
2. Use the topology editor to view and manage resources in the classic network.

> NFV devices (vNGAF, SSL VPN) cannot be created by tenants in the classic network. Contact the platform administrator if you need NFV devices deployed on the classic network.

---

## Application Delivery Controller (ADC)

The ADC (vAD) provides load balancing for applications deployed in your VPC.

1. Go to **Networking** → **ADC** and click **New**.
2. Select the **Configuration**, **Resource Pool**, **Name**, and **Subnet**.
3. Optionally bind an **Elastic IP**.
4. Click **OK**.

The vAD device supports one-click creation, deletion, and HA deployment for active/standby pairs.

---

> **Next step:** [Manage Storage](storage.md).
