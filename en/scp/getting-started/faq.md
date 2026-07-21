# Frequently Asked Questions — SCP

Answers to common questions at each stage of using the portal.

---

## Access & Login

**I haven't received my login credentials**

Credentials are provided by your administrator, not sent automatically by the system. Contact your account manager or email [cns-support@fcd.kz](mailto:cns-support@fcd.kz).

---

**I get an "Invalid username or password" error**

Check that:
- You are entering the correct value in the **Username/Email** field (your email address, or a username assigned by your admin).
- Caps Lock is not on.
- You are typing the password exactly as provided.

If the problem persists, ask your administrator to confirm your account is active, or contact [cns-support@fcd.kz](mailto:cns-support@fcd.kz) to have your password reset.

---

**I forgot my password**

On the login page, click **Forgot Password?** to the right of the Password field and follow the on-screen instructions to reset it. If the reset email does not arrive, check your Spam folder or contact [cns-support@fcd.kz](mailto:cns-support@fcd.kz).

---

**The portal doesn't load or I see a connection error**

Make sure you are using the exact URL provided by your administrator (format: `https://<SCP-address>/login`). Try a different browser or disable browser extensions. If the problem persists, contact [cns-support@fcd.kz](mailto:cns-support@fcd.kz).

---

**After logging in I get sent back to the login page**

Try clearing your browser cache and cookies, then log in again. If that does not help, try an incognito/private browsing window. If the issue persists, contact [cns-support@fcd.kz](mailto:cns-support@fcd.kz).

---

## Resources

**My VM request was rejected or never provisioned**

VM requests go through administrator approval. If your request was not approved, contact your administrator to discuss available resources or adjust the request.

---

## Virtual Machines

**My VM is stuck in "Creating" or shows an "Error" status**

Provisioning takes some time after the request is submitted. If the status does not change after an extended wait, try refreshing the page. You can also check **System → Tasks** for details on the operation. If the VM shows Error, contact [cns-support@fcd.kz](mailto:cns-support@fcd.kz) with the VM name and the time the error appeared.

---

**I submitted an "Apply for VM" request but nothing happened**

All VM requests go through an **approval step** before provisioning begins. After submitting, the request waits for administrator approval. To check its status, click the **Work Orders** button in the top-right corner of the Virtual Machines page. Once the request is approved, the VM will be provisioned and appear in the list.

---

**I created a VM but I can't connect to it — I just see an OS installer screen**

All images in this deployment are ISO type. This means the VM boots into the OS installation wizard on first start, not a ready-to-use system. You must open the **VNC console** and complete the OS installation before the VM is accessible over SSH or RDP. See [First Steps — Step 2](./first-steps.md#step-2--connect-to-your-vm-and-install-the-os) for instructions.

---

**The IP column shows "-" for my VM**

The IP address is reported by **vmTools**, the guest agent that must be installed inside the VM after OS installation. If vmTools is not installed, the IP column shows a dash. To get the IP to appear, install vmTools — the VNC console shows a banner with an **Install Now** link when vmTools is missing. You can also find the IP by opening the VNC console and checking the OS network configuration directly (e.g., `ip addr` on Linux).

---

**I created a VM but I can't connect to it over SSH or RDP**

Check the following in order:

1. The OS installation has been completed via VNC console (all images require manual installation).
2. The VM status is not Error.
3. The **IP** column shows an address (not a dash). If it shows "-", vmTools is not installed — see the entry above.
4. For SSH: confirm port 22 is not blocked by a network policy in your deployment.
5. For RDP: confirm port 3389 is accessible.

VM networking is on a private internal network. If you cannot reach the VM's IP from your workstation, contact your administrator — external access is configured at the infrastructure level, not in the tenant portal.

---

**The VNC console opens but shows a blank or frozen screen**

This is common when vmTools is not installed — you will see a yellow banner at the top of the console saying "vmTools is not installed on this virtual machine." The screen can appear black even when the VM is running. Try pressing a key or clicking inside the console to wake the display. If the OS has been installed, the screen should respond. If the VM is completely unresponsive, use the **Reset** action from the **More** dropdown in the VM list to force-restart it.

---

**My VM is approaching its expiration date (Validity Period)**

VMs are created without an expiration date by default (**Unlimited**). An expiration date is only set if **Specified** was selected in the Apply for VM form — this is an optional field for temporary VMs. If your VM has an expiration date and it is approaching, contact your administrator to request an extension before the VM is automatically stopped or released.

---

**I need to resize my VM (change vCPU or RAM)**

Click **More** in the **Operation** column for the VM and select **Change configuration**. This allows you to modify the VM's vCPU and memory allocation. The VM may need to be powered off first — follow the on-screen instructions.

---

**Can I take a snapshot of my VM?**

Yes. Click **More** in the **Operation** column and select **Take Snapshot** to create a snapshot. To view and manage existing snapshots, select **Snapshots** from the same menu, or open the VM's detail page and click **Snapshots** in the left sidebar.

A snapshot saves the VM's disk and memory state at that point in time and lets you roll back to it — useful before risky changes like OS updates. Snapshots are not backups: they are stored on the same infrastructure as the VM.

---

**How do I set up SSH key authentication for my VM?**

1. Go to **System → Key Pairs** in the mega-menu and click **+ Create Key Pair**.
2. Give the key pair a name, then choose a type:
   - **Auto-create** — the portal generates a key pair. Download the private key immediately after creation — it is shown only once.
   - **Import** — paste your existing public key (Base64-encoded) into the Public Key field.
3. After the key pair is created, make sure vmTools is installed on the target VM (required for Bind Key Pair to be available).
4. In the **Virtual Machines** list, click **More** for the VM and select **Bind Key Pair**.

SSH key injection is not available at VM creation time — keys can only be bound to VMs that are already running and have vmTools installed.

---

## Networking

**I only see one network type option when creating a VM**

This is expected. In this deployment, **Classic Network** is the only available network type. If you need a different network configuration, contact your administrator.

---

**My VM has an IP address but I can't reach it from outside the platform**

VMs are on private internal networks by default. Public or external access requires your administrator to configure routing or an external IP. Contact your administrator to request external connectivity for your VM.

---

**Can I assign a static IP or Elastic IP to my VM?**

IP assignment is not available in the tenant portal. Internal IPs are assigned automatically by the infrastructure. **Elastic IPs** (public IPs) are assigned to VMs by your administrator — you can see whether your VM has one in the **Elastic IP** column of the VM list, but you cannot assign or remove them yourself. Contact your administrator to request an Elastic IP for your VM.

---

**Can I create or modify virtual networks?**

No. There is no network management section in the tenant portal. Virtual networks are managed entirely by your administrator. When creating a VM, you select a network type (**Classic Network**) but cannot configure subnets, IP ranges, or routing.

---

**What is vmTools and do I need it?**

**vmTools** is a guest agent that runs inside the VM and enables deeper integration with the HCI platform. Without it:
- The **IP** column in the VM list shows "-" (IP is not reported to the portal)
- **Reset Password** and **Bind Key Pair** in the More dropdown are grayed out and unavailable
- **Reboot If Fault Occurs** (automatic recovery) does not function

The VNC console shows a yellow banner — "vmTools is not installed on this virtual machine" — with an **Install Now** link that opens installation instructions. Installing vmTools is strongly recommended after OS installation.

---

## Images & Operating Systems

**The OS image I need isn't in the list**

Available images are managed by your administrator. Contact your administrator to request a specific OS image.

---

**What username and password should I use to log into a new VM?**

All images in this deployment are ISO type — there are no pre-set credentials because you set them yourself during OS installation. When the OS installer prompts you to create a root or administrator account, that is the password you will use to log in afterwards. If you did not record the password during installation, you will need to rebuild the VM.

---

**The OS installation finished but the VM is still booting from the ISO — it shows the installer again**

After completing the installation, the installer typically prompts you to reboot. If the VM boots back into the installer instead of the installed OS, the boot order may still point to the ISO. Contact your administrator to detach the ISO from the VM so it boots from the disk.

---

> Didn't find your answer? Email [cns-support@fcd.kz](mailto:cns-support@fcd.kz).
