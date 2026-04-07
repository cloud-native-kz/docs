# Авторизация CSS для сохранения скриншотов в бакет COS

В этом документе описано, как сохранять скриншоты или данные обнаружения порнографии в бакет COS. Необходимо создать бакет COS, авторизировать CSS для сохранения данных в нём, а затем настроить параметры живого захвата экрана и обнаружения порнографии в консоли CSS. После этого скриншоты и данные обнаружения порнографии смогут сохраняться в бакет. Эта функция доступна в новой консоли.

### Создание бакета COS

1. Войдите в консоль COS и выберите [Bucket List](https://console.tencentcloud.com/cos5/bucket) на левой боковой панели.
2. Нажмите **Create Bucket**. В появившемся окне введите основную информацию, выберите разрешение для бакета и нажмите **Next**.

![](https://staticintl.cloudcachetci.com/cms/backend-cms/dface17c8f7911ef95ae525400fdb830.png)

3. Завершите расширенную конфигурацию (опционально) и нажмите **Next**.

![](https://staticintl.cloudcachetci.com/cms/backend-cms/363b1f458f7a11ef9ba5525400f69702.png)

4. Подтвердите информацию конфигурации и нажмите **Create**.

![](https://staticintl.cloudcachetci.com/cms/backend-cms/566258088f7a11efa11a525400a9236a.png)

> **Примечание:** В примере выше имя бакета — `test02` (`-130****051` не является частью имени). Выполните описанные выше параметры в соответствии с вашими фактическими потребностями.

5. Для включения ускорения CDN.
  5.1. Нажмите на имя вашего бакета или нажмите **Configure**.

![](https://staticintl.cloudcachetci.com/cms/backend-cms/e6886b278f9311ef9ed652540075b605.png)

  5.2. В списке бакетов выберите **Domains and Transfer** > **Custom CDN Acceleration Domain** на левой боковой панели. Нажмите **Edit** в элементе конфигурации Global Acceleration.

![](https://staticintl.cloudcachetci.com/cms/backend-cms/37759c898f9611efa11a525400a9236a.png)

  5.3. Включите переключатель **status** и завершите настройку. Подробные инструкции см. в разделе [Enabling Custom CDN Acceleration Domain Name](https://www.tencentcloud.com/document/product/436/31505?lang=zh&pg=). После конфигурации нажмите **Save**.

![](https://staticintl.cloudcachetci.com/cms/backend-cms/595a78668f9611ef9ba5525400f69702.png)

### Авторизация CSS для сохранения скриншотов в COS

1. Предоставьте корневому аккаунту `3508645126` **права на запись** и **права на чтение** для бакета COS.
  1.1. В [Bucket List](https://console.tencentcloud.com/cos5/bucket) найдите созданный вами бакет и нажмите **Configure**.

![](https://staticintl.cloudcachetci.com/cms/backend-cms/8c3cb1ac8f9611ef95ae525400fdb830.png)

  1.2. На странице конфигурации бакета выберите **Permission Management** > [**Bucket ACL (Access Control List)**](https://console.tencentcloud.com/cos5/bucket/setting?type=aclconfig&anchorType=accessPermission&bucketName=text-1258968577&projectId=&path=%2F®ion=ap-guangzhou). Затем нажмите **Add User**.

![](https://staticintl.cloudcachetci.com/cms/backend-cms/d2fafd488f9611ef9ba5525400f69702.png)

  1.3. Выберите **Root account** в качестве типа пользователя и **введите ID корневого аккаунта 3508645126**.

![](https://staticintl.cloudcachetci.com/cms/backend-cms/0de7d7d98f9711efa22452540055f650.png)

  1.4. Нажмите **save**.

![](https://staticintl.cloudcachetci.com/cms/backend-cms/237bf06d8f9711ef9897525400d5f8ef.png)

  - Кроме того, в списке бакетов нажмите **Manage Permissions**.

![](https://staticintl.cloudcachetci.com/cms/backend-cms/7d743c448f9711ef95ae525400fdb830.png)

    - Выберите созданный вами бакет. Затем нажмите **Add User**, выберите **Root account** в качестве типа пользователя, введите ID корневого аккаунта `3508645126`, нажмите **Save** для сохранения конфигурации и нажмите **OK**.

![](https://staticintl.cloudcachetci.com/cms/backend-cms/edd681bb8f9711ef9ba5525400f69702.png)

> **Примечание:** `3508645126` — это **`APPID`** CSS. Для успешной авторизации необходимо ввести этот ID.

  1.5. Для получения информации о том, как использовать API для установки доступа к бакету, см. [PUT Bucket acl](https://intl.cloud.tencent.com/document/product/436/7737).
2. Получите информацию о бакете COS, к которому была предоставлена доступность CSS.
  2.1. Выберите авторизованный бакет в **Bucket list** и нажмите на **Bucket Name** слева для входа в Overview.

![](https://staticintl.cloudcachetci.com/cms/backend-cms/1d2739b08f9811ef9ed652540075b605.png)

  2.2. Всю информацию COS можно просмотреть в [Overview](https://console.intl.cloud.tencent.com/cos/bucket) бакета. В endpoint вы можете найти имя бакета, COS APPID и регион бакета.

![](https://staticintl.cloudcachetci.com/cms/backend-cms/7e0e5e4b8f9811efac345254002693fd.png)

  - Имя бакета: `test02`
  - COS appid: `130****051`
  - Регион бакета: `ap-guangzhou`
  2.3. Предоставьте вышеуказанную информацию в CSS, и система будет сохранять живые скриншоты в созданный вами бакет COS.


---
*Источник: [https://www.tencentcloud.com/document/product/267/33384](https://www.tencentcloud.com/document/product/267/33384)*

---
*Источник (EN): [authorizing-css-to-store-screenshots-in-a-cos-bucket.md](./authorizing-css-to-store-screenshots-in-a-cos-bucket.md)*
