# Kubernetes Storage Integration

HCI provides a Container Storage Interface (CSI) plugin that lets your existing Kubernetes cluster use HCI block storage for persistent volumes. The plugin connects Kubernetes to HCI's distributed storage via iSCSI, so you can provision and mount PersistentVolumeClaims backed by HCI storage.

> This guide covers connecting a **self-managed Kubernetes cluster** to HCI storage. Kubernetes itself is not a managed service on this platform — you bring your own cluster.

---

## Prerequisites

**On the HCI side (handled by your platform administrator):**
- HCI port 4433 must be enabled (System Management → Port Management)
- iSCSI Virtual Storage must be configured on HCI with an accessible target IP and IP pool reachable from the Kubernetes nodes

**On the Kubernetes side (your responsibility):**
- A running Kubernetes cluster (v1.18 or later recommended)
- `kubectl` and `helm` v3 available on the master node
- `iscsiadm` installed on **every** node in the cluster
- The CSI plugin package (`asan-csi-provisioner.tar.gz`) and image (`sangfor-asan-csi.tar.gz`) provided by your administrator

---

## Step 1 — Install Required Tools

### Helm

Check if Helm is installed:

```bash
helm version
```

If not installed:

```bash
# Download and install Helm v3
tar zxvf helm-v3.x.x-linux-amd64.tar.gz
cp linux-amd64/helm /usr/bin/helm
helm version
```

### iscsiadm

Check on each node:

```bash
iscsiadm --version
```

If not installed (CentOS):

```bash
yum install iscsi-initiator-utils.x86_64
mkdir -p /var/lock/iscsi
touch /var/lock/iscsi/lock
iscsiadm --version
```

> `iscsiadm` must be installed on **every node** in the cluster, including worker nodes.

---

## Step 2 — Load the CSI Plugin Image

On **every node** in the cluster, upload and load the image:

```bash
docker load -i sangfor-asan-csi.tar.gz
```

---

## Step 3 — Extract and Configure the Plugin

On the **master node**:

```bash
tar -zxvf asan-csi-provisioner.tar.gz
```

This creates the `sangfor-block-csi-provisioner/` directory.

### Configure values.yaml

Edit `sangfor-block-csi-provisioner/values.yaml`. The fields marked below must match your HCI environment:

```yaml
aSAN:
  storageLabel: "astorage1"        # aSAN storage name (ask your admin)
  iqn: iqn.2015-08.5e82de89.com.sangfor.asan   # virtual iSCSI IQN (ask your admin)
  restfulusername: admin            # HCI super administrator username
  restfulpassword: <encrypted-pwd>  # Encrypt using: ./encrypt_pwd encrypt <password>
  chapUserName: admin               # iSCSI CHAP username
  chapPassword: <encrypted-pwd>     # Encrypted CHAP password
  domain: https://<HCI_IP>:4433    # HCI cluster address
  targetPortal: <iSCSI-target-IP>:3260  # iSCSI target IP configured by admin

hcistorageClass:
  name: sangfor-csi-asan-provisioner  # StorageClass name (use as-is)
  fsType: ext4
  storageLabel: "storage1"
  lunGroup: "k8s"
```

To encrypt passwords:

```bash
./sangfor-block-csi-provisioner/encrypt_pwd encrypt <your-password>
```

---

## Step 4 — Install the Plugin

```bash
helm install sangfor-block-csi-provisioner sangfor-block-csi-provisioner/
```

Verify the pods are running:

```bash
kubectl --namespace=default get pods -l "app=sangfor-asan-csi,release=sangfor-block-csi-provisioner"
```

All pods should show `STATUS: Running`. If any pod is not running, check the logs:

```bash
kubectl logs <pod-name> -c iscsi
```

---

## Step 5 — Use HCI Storage in Your Workloads

### Create a PersistentVolumeClaim

```yaml
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: my-data
spec:
  accessModes:
    - ReadWriteOnce
  storageClassName: sangfor-csi-asan-provisioner
  resources:
    requests:
      storage: 50Gi
```

```bash
kubectl apply -f pvc.yaml
kubectl get pvc my-data
```

The PVC status should become `Bound` once the volume is provisioned.

### Mount in a Pod

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: my-app
spec:
  containers:
    - name: my-app
      image: nginx:1.25
      volumeMounts:
        - mountPath: /data
          name: storage
  volumes:
    - name: storage
      persistentVolumeClaim:
        claimName: my-data
```

```bash
kubectl apply -f pod.yaml
kubectl get pods my-app
```

### Expand a PVC (Online)

To increase PVC storage while the pod is running, edit the PVC and increase the `storage` request:

```bash
kubectl edit pvc my-data
```

Change the `storage` value to the new size. The expansion takes effect without restarting the pod.

### Delete a PVC

Delete the pod first to unmount the volume, then delete the PVC:

```bash
kubectl delete pod my-app
kubectl delete pvc my-data
```

---

## Uninstall the Plugin

```bash
helm uninstall sangfor-block-csi-provisioner
```

---

> **Next step:** [Provision Managed Databases with DMP](databases.md).
