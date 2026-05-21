# Images & Templates

Images are the base for creating virtual machines. The platform provides **Public VM Images** (pre-configured OS images maintained by the platform) and **Private VM Images** (images you upload or create yourself).

---

## Public VM Images

Public images are provided and maintained by the platform administrator. They include pre-installed operating systems (Windows Server, CentOS, Ubuntu, and others).

To use a public image, select it in the **Image** field when creating a VM (**Compute** → **Virtual Machine** → **New** → step 2).

---

## Private VM Images

Private images are stored in your tenant's **Private Image Repository**. You can create private images by uploading an ISO file or by converting an existing VM into a reusable built-in image.

Go to **Compute** → **Image** → **Private VM Images** to manage your private images.

---

## Upload an ISO

Upload an OS installation ISO to use it when creating a VM from scratch.

1. Go to **Compute** → **Image** → **Private VM Images**.
2. Click **Upload**.
3. Select the local ISO file, choose the **Operating System** type, and select the **Resource Pool**.
4. Click **Upload** to begin.
5. After the upload completes, click **Finish** to close or **Close** to continue uploading additional files.

---

## Create a Built-in Image from a VM

A built-in image captures the full state of a configured VM so you can deploy identical copies quickly.

**Prerequisites:**
- The VM must have VM Tools installed.
- It is recommended to enable CPU hot add and memory hot add in the VM's **Advanced** settings before creating the image.

**Steps:**

1. Go to **Compute** → **Virtual Machine**, select the VM.
2. Click **More** → **Edit**. In the **Advanced** tab, enable CPU hot add and memory hot add, then click **OK**.
3. Click **More** → **Create Image**.
4. Enter a **Name** and **Description** for the image.
5. Select the **Operating System** type and the **Resource Pool**.
6. Click **OK** to start image creation.

The image appears in **Private VM Images** once creation is complete.

---

## Use a Private Image to Create a VM

1. Go to **Compute** → **Virtual Machine** → **New**.
2. In the Image selection step, switch to **Private VM Images** and select your image.
3. Continue with the VM creation wizard.

---

## Export a VM

You can export a VM as an OVA, VMA, OVF, MF, or VMDK file for use on other platforms or as an offline archive.

See [Export a VM](virtual-machines.md#export-a-vm) for steps.

---

> **Next step:** [Manage Storage](storage.md).
