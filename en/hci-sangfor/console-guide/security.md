# Security Services

The platform provides tenant-level network security through the Distributed Firewall and NFV security devices (vNGAF and SSL VPN) deployed within your VPC.

---

## Distributed Firewall

The Distributed Firewall lets you create traffic control policies that apply to all networks within your tenant — VPC and classic networks alike. Policies are organized into named groups, and rules within each group are matched in priority order.

### Create a Firewall Policy

1. Go to **Security Services** → **Distributed Firewall**.
2. Select the tenant network from the left panel.
3. Click **Create Policy**.
4. Fill in:

| Field | Description |
|---|---|
| **Name** | Policy group name |
| **Scope** | The network this policy applies to |
| **Priority** | Higher-priority policies match before the platform default policy |

5. Click **OK**.

### Add Rules to a Policy

1. Click **Configure Rules** next to the policy.
2. Click **New** to add a rule.
3. Configure:

| Field | Description |
|---|---|
| **Name** | Rule name |
| **Source** | Any IP address, IP Group, IP Range, Virtual Machine, or VM Group |
| **Destination** | Same options as Source |
| **Service** | Select a predefined service or define a custom TCP/UDP/ICMP protocol and port |
| **Action** | **Allow** or **Drop** |

4. Click **OK**.

To reorder rules, select a rule and click **Move Up**, **Move Down**, or **Move to** to place it in a different policy group.

### IP Groups

IP Groups let you define a named set of IP ranges that can be reused across multiple rules.

1. Click **IP Groups** in the Distributed Firewall toolbar.
2. Click **New**, enter a **Name** and **IP Range**, then click **OK**.

> Rules using virtual machine sources require VM Tools to be installed in the guest OS. Without VM Tools, the platform cannot automatically resolve the VM's IP address, making the rule ineffective.

---

## vNGAF (Virtual Next-Generation Firewall)

The vNGAF is a virtual firewall appliance deployed inside your VPC. It provides full life-cycle traffic inspection and protection for your tenant workloads.

**Prerequisites:**
- Sufficient NFV quota allocated to your tenant (check via **Edit Resource Quota**)
- vNGAF device image available in your resource pool

### Create a vNGAF

1. Go to **Security Services** → **NFV Features** → **NGAF**.
2. Click **New**.
3. Configure:

| Field | Description |
|---|---|
| **Name** | Display name for the vNGAF instance |
| **Resource Pool** | The cluster to deploy into |
| **VPC** | VPC where the vNGAF will be placed |
| **Configuration** | CPU/memory/bandwidth tier (e.g. 2 CPU cores, 4 GB, 100 Mbps) |
| **Branch VPN Sites** | Optional: number of branch VPN site licenses |
| **SSL VPN Users** | Optional: number of SSL VPN user licenses |

4. Click **OK**.

After creation, click **More** to access the vNGAF management console and enable protection. Protection is enabled by default after creation.

To disable protection: click **Disable Protection** in the vNGAF console.

---

## SSL VPN

SSL VPN provides secure remote access for users connecting to your VPC from outside the network.

**Prerequisites:**
- Sufficient NFV quota allocated to your tenant
- SSL VPN device image available in your resource pool

### Create an SSL VPN

1. Go to **Security Services** → **NFV Features** → **SSL VPN**.
2. Click **New**.
3. Configure:

| Field | Description |
|---|---|
| **Name** | Display name |
| **Resource Pool** | The cluster to deploy into |
| **VPC** | VPC where the SSL VPN will be placed |
| **Subnet** | Subnet for the SSL VPN device |
| **Elastic IP** | Skip, create new, or choose an existing EIP |
| **Configuration** | CPU/memory/bandwidth tier |
| **Total Mobile Users** | Number of remote user licenses |
| **Total Remote Users** | Number of concurrent remote connections |

4. Click **OK**.

After creation, click **More** to open the SSL VPN management console for detailed configuration (authentication methods, access policies, client profiles).

---

> **Next step:** [Monitor your resources](monitoring.md).
