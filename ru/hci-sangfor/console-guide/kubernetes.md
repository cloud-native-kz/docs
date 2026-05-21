# Интеграция Kubernetes с хранилищем

HCI предоставляет CSI-плагин (Container Storage Interface), который позволяет существующему Kubernetes-кластеру использовать блочное хранилище HCI для постоянных томов. Плагин подключает Kubernetes к распределённому хранилищу HCI через iSCSI, что позволяет создавать и монтировать PersistentVolumeClaim, обеспеченные хранилищем HCI.

> Данное руководство описывает подключение **самостоятельно управляемого Kubernetes-кластера** к хранилищу HCI. Kubernetes не является управляемым сервисом на этой платформе — вы используете собственный кластер.

---

## Предварительные условия

**На стороне HCI (выполняется администратором платформы):**
- Порт HCI 4433 должен быть включён (Управление системой → Управление портами)
- Виртуальное хранилище iSCSI должно быть настроено на HCI с доступным целевым IP и пулом IP, доступным с узлов Kubernetes

**На стороне Kubernetes (ваша ответственность):**
- Работающий Kubernetes-кластер (рекомендуется v1.18 или новее)
- `kubectl` и `helm` v3 доступны на мастер-узле
- `iscsiadm` установлен на **каждом** узле кластера
- Пакет CSI-плагина (`asan-csi-provisioner.tar.gz`) и образ (`sangfor-asan-csi.tar.gz`), предоставленные администратором

---

## Шаг 1 — Установка необходимых инструментов

### Helm

Проверьте наличие Helm:

```bash
helm version
```

Если не установлен:

```bash
# Скачать и установить Helm v3
tar zxvf helm-v3.x.x-linux-amd64.tar.gz
cp linux-amd64/helm /usr/bin/helm
helm version
```

### iscsiadm

Проверьте на каждом узле:

```bash
iscsiadm --version
```

Если не установлен (CentOS):

```bash
yum install iscsi-initiator-utils.x86_64
mkdir -p /var/lock/iscsi
touch /var/lock/iscsi/lock
iscsiadm --version
```

> `iscsiadm` должен быть установлен на **каждом узле** кластера, включая рабочие узлы.

---

## Шаг 2 — Загрузка образа CSI-плагина

На **каждом узле** кластера загрузите и установите образ:

```bash
docker load -i sangfor-asan-csi.tar.gz
```

---

## Шаг 3 — Распаковка и настройка плагина

На **мастер-узле**:

```bash
tar -zxvf asan-csi-provisioner.tar.gz
```

Это создаёт директорию `sangfor-block-csi-provisioner/`.

### Настройка values.yaml

Отредактируйте `sangfor-block-csi-provisioner/values.yaml`. Поля, указанные ниже, должны соответствовать вашей среде HCI:

```yaml
aSAN:
  storageLabel: "astorage1"        # Имя хранилища aSAN (уточните у администратора)
  iqn: iqn.2015-08.5e82de89.com.sangfor.asan   # Виртуальный iSCSI IQN (уточните у администратора)
  restfulusername: admin            # Имя суперадминистратора HCI
  restfulpassword: <encrypted-pwd>  # Зашифруйте командой: ./encrypt_pwd encrypt <password>
  chapUserName: admin               # Имя пользователя CHAP для iSCSI
  chapPassword: <encrypted-pwd>     # Зашифрованный пароль CHAP
  domain: https://<HCI_IP>:4433    # Адрес кластера HCI
  targetPortal: <iSCSI-target-IP>:3260  # Целевой IP iSCSI, настроенный администратором

hcistorageClass:
  name: sangfor-csi-asan-provisioner  # Имя StorageClass (оставьте как есть)
  fsType: ext4
  storageLabel: "storage1"
  lunGroup: "k8s"
```

Для шифрования паролей:

```bash
./sangfor-block-csi-provisioner/encrypt_pwd encrypt <ваш-пароль>
```

---

## Шаг 4 — Установка плагина

```bash
helm install sangfor-block-csi-provisioner sangfor-block-csi-provisioner/
```

Проверьте, что поды запущены:

```bash
kubectl --namespace=default get pods -l "app=sangfor-asan-csi,release=sangfor-block-csi-provisioner"
```

Все поды должны иметь `STATUS: Running`. Если какой-либо под не запускается, проверьте логи:

```bash
kubectl logs <имя-пода> -c iscsi
```

---

## Шаг 5 — Использование хранилища HCI в рабочих нагрузках

### Создание PersistentVolumeClaim

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

Статус PVC должен стать `Bound` после создания тома.

### Монтирование в поде

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

### Расширение PVC (онлайн)

Для увеличения хранилища PVC без остановки пода отредактируйте PVC и увеличьте значение `storage`:

```bash
kubectl edit pvc my-data
```

Измените значение `storage` на новый размер. Расширение применяется без перезапуска пода.

### Удаление PVC

Сначала удалите под для отмонтирования тома, затем удалите PVC:

```bash
kubectl delete pod my-app
kubectl delete pvc my-data
```

---

## Удаление плагина

```bash
helm uninstall sangfor-block-csi-provisioner
```

---

> **Следующий шаг:** [Управляемые базы данных (DMP)](databases.md).
