# Использование корзин Amazon S3 с MPS

### Шаг 1. Создание корзины S3 для входных/выходных файлов

1. Нажмите **Create bucket** (Создать корзину).

![](https://staticintl.cloudcachetci.com/cms/backend-cms/d9dd91cefeea11ef8c825254001c06ec.png)

2. **Введите имя корзины и выберите регион.**

Введите имя корзины и выберите регион для корзины. В примере ниже выбран Сингапур.

![](https://staticintl.cloudcachetci.com/cms/backend-cms/d8ef0b2bfeea11efa17e525400454e06.png)

3. Нажмите **Create bucket** (Создать корзину).
4. Повторите описанные выше шаги, чтобы создать корзину для выходных файлов трансляции (необязательно).

> **Примечание:** Вы также можете выводить файлы трансляции в новый каталог входной корзины.

![](https://staticintl.cloudcachetci.com/cms/backend-cms/d977e2ccfeea11ef8c825254001c06ec.png)

### Шаг 2. Создание очереди SQS для уведомлений корзины

1. Выберите регион очереди.

Выберите Сингапур (ap-southeast-1).

![](https://staticintl.cloudcachetci.com/cms/backend-cms/d9de76bdfeea11efa49152540044a08e.png)

> **Примечание:** Чтобы привязать очередь к корзине, убедитесь, что регион очереди совпадает с регионом корзины.

2. Введите имя очереди.

![](https://staticintl.cloudcachetci.com/cms/backend-cms/d95cdce1feea11efa49152540044a08e.png)

3. Отключите шифрование.

![](https://staticintl.cloudcachetci.com/cms/backend-cms/d95c6827feea11efa17e525400454e06.png)

4. Измените политику доступа.

Выберите **Advanced** (Дополнительно), введите ARN SQS, ARN корзины S3 и ID учетной записи в указанных местах ниже (сведения о том, как получить эту информацию, см. в конце этого документа) и вставьте код на вкладку политики доступа в консоли AWS.

```
        {    "Version": "2012-10-17",    "Id": "__default_policy_ID",    "Statement": [        {            "Sid": "__owner_statement",            "Effect": "Allow",            "Principal": {                "Service": "s3.amazonaws.com"            },            "Action": [                "SQS:SendMessage"            ],            "Resource": "Your SQS ARN",            "Condition": {                "ArnLike": {                    "aws:SourceArn": "Your bucket ARN"                },                "StringEquals": {                    "aws:SourceAccount": "Your account ID"                }            }        }    ]}
```

5. Нажмите **Create queue** (Создать очередь).

### Шаг 3. Создание очереди SQS для обратных вызовов трансляции

> **Примечание:** Это требуется только если вы используете обратные вызовы AWS SQS.

1. Выберите регион очереди.

Выберите Сингапур.

![](https://staticintl.cloudcachetci.com/cms/backend-cms/d9ed13f5feea11efbf88525400e889b2.png)

> **Примечание:** Регион очереди должен совпадать с регионом вашей корзины.

2. Введите имя очереди.

![](https://staticintl.cloudcachetci.com/cms/backend-cms/d9b0f3b7feea11efa21c525400bf7822.png)

3. Отключите шифрование.

![](https://staticintl.cloudcachetci.com/cms/backend-cms/d95c82e4feea11efa49152540044a08e.png)

4. Нажмите **Create queue** (Создать очередь).

### Шаг 4. Привязка входной корзины к очереди SQS

1. **Перейдите на страницу сведений о входной корзине.**

Вернитесь в консоль Amazon S3. Найдите созданную корзину и нажмите на имя корзины, чтобы перейти на страницу сведений.

![](https://staticintl.cloudcachetci.com/cms/backend-cms/d9ffd838feea11ef9f695254007c27c5.png)

2. Привяжите корзину к очереди SQS.
  2.1. Выберите **Properties** (Свойства).

![](https://staticintl.cloudcachetci.com/cms/backend-cms/d9fee4cefeea11ef9f695254007c27c5.png)

  2.2. Прокрутите вниз до раздела **Event notifications** (Уведомления о событиях). Нажмите **Create event notification** (Создать уведомление о событии).

![](https://staticintl.cloudcachetci.com/cms/backend-cms/d9e65297feea11efa17e525400454e06.png)

  2.3. Введите имя события.

![](https://staticintl.cloudcachetci.com/cms/backend-cms/d8ae4287feea11efaf3d52540099c741.png)

  2.4. Выберите **All object create events** (Все события создания объектов) в разделе **Event types** (Типы событий).

![](https://staticintl.cloudcachetci.com/cms/backend-cms/d9f5c8d1feea11efaf3d52540099c741.png)

  2.5. Для параметра **Destination** (Назначение) выберите **SQS queue** (Очередь SQS) и выберите созданную очередь для получения уведомлений о корзине. Нажмите **Save changes** (Сохранить изменения).

![](https://staticintl.cloudcachetci.com/cms/backend-cms/d8fb8731feea11efbf88525400e889b2.png)

  2.6. Проверьте, содержит ли ваша очередь SQS доступные сообщения. Если **Messages available** (Доступные сообщения) изменилось с 0 на 1, привязка выполнена успешно.

![](https://staticintl.cloudcachetci.com/cms/backend-cms/d8d6ba08feea11ef8c825254001c06ec.png)

### Шаг 5. Создание пользователя IAM и предоставление ему разрешений

#### **5.1 Создайте политику.**

1. Перейдите в **Identity and Access Management** (Управление идентификацией и доступом), нажмите **Policies** (Политики) и нажмите **Create policy** (Создать политику).

![](https://staticintl.cloudcachetci.com/cms/backend-cms/da040af7feea11ef9f695254007c27c5.png)

2. Выберите вкладку JSON, введите ARN SQS и ARN корзины в политику JSON ниже, вставьте код на вкладку JSON и нажмите **Next** (Далее) дважды.

Политика для обратных вызовов Amazon SQS

Политика для обратных вызовов HTTP

![](https://staticintl.cloudcachetci.com/cms/backend-cms/d9b0a4affeea11efbf88525400e889b2.png)

```
{    "Version": "2012-10-17",    "Statement": [        {            "Sid": "VisualEditor0",            "Effect": "Allow",            "Action": [                "sqs:DeleteMessage",                "s3:GetObject",                "sqs:GetQueueUrl",                "sqs:ReceiveMessage",                "s3:GetObjectAttributes",                "sqs:GetQueueAttributes",                "sqs:ListQueueTags"            ],            "Resource": [                "The ARN of the SQS queue for bucket notifications",                "The input bucket ARN + /*"            ]        },        {            "Sid": "VisualEditor1",            "Effect": "Allow",            "Action": [                "s3:PutObject",                "sqs:GetQueueUrl",                "sqs:SendMessage"            ],            "Resource": [                "The ARN of the SQS queue for transcoding callbacks",                "The output bucket ARN + /*"            ]        }    ]}
```

![](https://staticintl.cloudcachetci.com/cms/backend-cms/d8a8cc89feea11ef9f695254007c27c5.png)

```
{    "Version": "2012-10-17",    "Statement": [        {            "Sid": "VisualEditor0",            "Effect": "Allow",            "Action": [                "sqs:DeleteMessage",                "s3:GetObject",                "sqs:GetQueueUrl",                "sqs:ReceiveMessage",                "s3:GetObjectAttributes",                "sqs:GetQueueAttributes",                "sqs:ListQueueTags"            ],            "Resource": [                "The ARN of the SQS queue for bucket notifications",                "The input bucket ARN + /*"            ]        },        {            "Sid": "VisualEditor1",            "Effect": "Allow",            "Action": [                "s3:PutObject"            ],            "Resource": [                "The output bucket ARN + /*"            ]        }    ]}
```

> **Примечание:** В разделе `Resources` документа JSON убедитесь, что вы добавили `/*` к ARN корзины. Например, если ARN вашей корзины — `arn:aws:s3:::tencentbucket`, введите `arn:aws:s3:::tencentbucket/*`.

3. Введите имя политики и нажмите **Create policy** (Создать политику).

![](https://staticintl.cloudcachetci.com/cms/backend-cms/d9c4de1ffeea11ef83195254005ef0f7.png)

#### 5.2 Создайте пользователя IAM.

1. Перейдите на страницу IAM, нажмите **Users** (Пользователи) и нажмите **Add users** (Добавить пользователей).

![](https://staticintl.cloudcachetci.com/cms/backend-cms/d9ef953bfeea11efa21c525400bf7822.png)

2. Введите имя пользователя и нажмите **Next** (Далее) в нижней правой части.

![](https://staticintl.cloudcachetci.com/cms/backend-cms/d91ff8cdfeea11efaf3d52540099c741.png)

Нажмите **Attach existing policies directly** (Непосредственно подключить существующие политики), введите в поле поиска имя только что созданной политики и выберите политику.

Нажмите **Next** (Далее) и затем нажмите **Create user** (Создать пользователя).

3. Нажмите на имя созданного пользователя.

![](https://staticintl.cloudcachetci.com/cms/backend-cms/d9974a66feea11efa17e525400454e06.png)

4. Нажмите **Security credentials** (Учетные данные безопасности) > **Access keys** (Ключи доступа) > **Create access key** (Создать ключ доступа).

![](https://staticintl.cloudcachetci.com/cms/backend-cms/d9d9c7e6feea11efa17e525400454e06.png)

5. Выберите **Other** (Другое) и нажмите **Next** (Далее). Запишите ID ключа доступа и секретный ключ доступа.

![](https://staticintl.cloudcachetci.com/cms/backend-cms/d9ecce7afeea11ef83195254005ef0f7.png)

### Приложение

- Вы можете просмотреть ID своей учетной записи, нажав на имя пользователя в правом верхнем углу домашней страницы консоли.

![](https://staticintl.cloudcachetci.com/cms/backend-cms/d9dfc7ebfeea11ef9f695254007c27c5.png)

- Чтобы просмотреть ARN корзины S3, перейдите на страницу **Buckets** (Корзины) и нажмите **Properties** (Свойства).

![](https://staticintl.cloudcachetci.com/cms/backend-cms/d8c20984feea11efaf3d52540099c741.png)

- Чтобы найти ARN вашей очереди SQS, на странице **Create queue** (Создать очередь) найдите раздел **Access policy** (Политика доступа), нажмите **Advanced** (Дополнительно), и `Resource` указывает ARN вашей очереди.

![](https://staticintl.cloudcachetci.com/cms/backend-cms/d9b5a6b3feea11efa21c525400bf7822.png)

- Если вы не знаете, что ввести в поле региона в консоли Tencent Cloud, перейдите на страницу [Amazon S3 Buckets](https://s3.console.aws.amazon.com/s3/buckets), найдите свою корзину, вторая половина **AWS Region** (без пробелов) — это значение, которое вы должны предоставить в Tencent Cloud. Согласно снимку экрана ниже, регион, который следует ввести для корзины `tencentbucket`, — `ap-southeast-1`.

![](https://staticintl.cloudcachetci.com/cms/backend-cms/d9ff6837feea11ef83195254005ef0f7.png)


---
*Источник: [https://www.tencentcloud.com/document/product/1041/54516](https://www.tencentcloud.com/document/product/1041/54516)*

---
*Источник (EN): [using-amazon-s3-buckets-with-mps.md](./using-amazon-s3-buckets-with-mps.md)*
