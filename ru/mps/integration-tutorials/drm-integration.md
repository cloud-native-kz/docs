# Интеграция DRM

## Обзор

Digital Rights Management (DRM) — это система, предназначенная для защиты авторских прав на цифровой контент путем применения техник шифрования и проверки авторизации. Её основные функции включают:

- Шифрование контента: Шифрование аудио, видео и другого цифрового контента для предотвращения несанкционированного распространения;
- Управление разрешениями: Реализация детализированного управления разрешениями через управление лицензиями, включая контроль над частотой воспроизведения и привязкой к устройству;
- Безопасная передача: Обеспечение целостности контента во время процесса распространения.

Media Processing Services (MPS) предоставляет услуги шифрования видео по запросу на основе протоколов шифрования DRM, таких как Widevine, FairPlay и PlayReady. Путем глубокой интеграции стандартизированной технологии шифрования с системами управления ключами третьих сторон (например, SDMC, DRMtoday и т.д.) достигается разделение шифрования контента и управления ключами, комплексно обеспечивая безопасность пользовательского контента. Услуги шифрования DRM, предоставляемые Media Processing, сосредоточены на обработке безопасности контента, в то время как генерация, хранение, распространение ключей и управление лицензиями обеспечиваются поставщиками услуг DRM третьих сторон.

Ниже будет показан процесс интеграции услуг шифрования DRM Media Processing с использованием DRMtoday в качестве примера.

## Процесс интеграции

### Подготовка

Активируйте и настройте сервис DRM третьей стороны, используя DRMtoday в качестве примера.

#### Шаг первый: Регистрация услуги

1. Перейдите на официальный веб-сайт [DRMtoday Provider](https://castlabs.com/drmtoday). DRMtoday предоставляет инструкции по бесплатному пробному использованию и покупке коммерческих услуг на своем веб-сайте.
2. Нажмите **Get your FREE trial today** для пробного использования.

![](https://staticintl.cloudcachetci.com/cms/backend-cms/bd54bea9fe4411ef9f695254007c27c5.png)

3. Пользователи должны зарегистрироваться с корпоративным адресом электронной почты и создать организацию для доступа на следующую страницу.

![](https://staticintl.cloudcachetci.com/cms/backend-cms/bd51d9c1fe4411efa17e525400454e06.png)

#### Шаг второй: Конфигурация услуги

(1) Настройка API-аккаунта

1. Выберите **Members/Users** из левой боковой панели.

![](https://staticintl.cloudcachetci.com/cms/backend-cms/bce99c24fe4411efa17e525400454e06.png)

2. Нажмите **Add API account**, выберите необходимые опции, убедитесь в корректности и нажмите **Add member** для подтверждения.

> **Примечание:**После успешного сохранения появится запрос пароля. Рекомендуется безопасно сохранить этот пароль для дальнейшего использования.

![](https://staticintl.cloudcachetci.com/cms/backend-cms/bd604e15fe4411efaf3d52540099c741.png)

##### （2）Настройка сертификатов FairPlay

Перейдите на левую боковую панель, выберите **DRM settings**, введите информацию о сертификате FairPlay и нажмите **Save Settings**.

![](https://staticintl.cloudcachetci.com/cms/backend-cms/bd7b03b5fe4411efbf88525400e889b2.png)

##### （3）Настройка секретного ключа "seed".

1. Выберите **Key Seeds** из левой боковой панели.

![](https://staticintl.cloudcachetci.com/cms/backend-cms/bd3f335bfe4411efa49152540044a08e.png)

2. Нажмите **Add seed**, вы можете сгенерировать случайный seed, нажав **Random**. Необходимо сгенерировать два seed: один для ключевого seed и другой для IV seed.

![](https://staticintl.cloudcachetci.com/cms/backend-cms/bd0577e5fe4411efa17e525400454e06.png)

##### (4) Настройка CPIX

> **Примечание:**Поскольку бэкэнд сервиса обработки медиа взаимодействует с поставщиками DRM для получения информации о ключах через [CPIX протокол](https://dashif.org/docs/CPIX2.2/Cpix.pdf), необходимо настроить CPIX.

1. Выберите **Ingest Settings** из левой боковой панели.

![](https://staticintl.cloudcachetci.com/cms/backend-cms/bd4be4a1fe4411efbf88525400e889b2.png)

2. Нажмите **Add CPIX config**, где Key seed и Initialization vector (IV) seed — это seed, настроенные на предыдущем шаге (3). Сопоставление типов потока и четыре опции ниже могут быть выбраны в соответствии с потребностями бизнеса для определения соответствующих правил генерации ключей.

![](https://staticintl.cloudcachetci.com/cms/backend-cms/bcf526e1fe4411ef8c825254001c06ec.png)

##### (5) Настройка аутентификации сертификата

Перейдите на **License Delivery Authorization** на левой боковой панели, где пользователи могут выбрать соответствующий метод аутентификации сертификата в соответствии с требованиями.

![](https://staticintl.cloudcachetci.com/cms/backend-cms/bd1cf445fe4411efa49152540044a08e.png)

#### Шаг третий: Генерирование URL запроса ключа

Для получения информации о ключах пользователи должны установить URL запроса ключа для сервиса обработки медиа. Этот URL позволяет сервису запрашивать ключи у поставщика DRM. После аутентификации запроса поставщиком DRM он отправляет ключи в формате CPIX. Сервис медиа использует эти ключи для расшифровки медиа. Инструкции по созданию URL запроса ключа см. в [документации DRMtoday](https://fe.drmtoday.com/documentation/integration/). Сценарий для генерирования этого URL предоставляется для справки.

```
#!/bin/bash# First request to get ticketTICKET_RESPONSE=$(curl 'https://auth.drmtoday.com/cas/v1/tickets' \\  -d "username=<API account>&password=<API account password>" \\  -s -D -)# Extract location header if status is 201if echo "$TICKET_RESPONSE" | grep -q "HTTP.*201"; then    TICKET_URL=$(echo "$TICKET_RESPONSE" | grep -i "Location:" | cut -d' ' -f2 | tr -d '\\r')        # Second request using the ticket URL    TICKET=$(curl "$TICKET_URL" \\      -d 'service=https://fe.drmtoday.com/frontend/cpix/v1/<Organization UUID>/ingest/<CPIX ID>')else    echo "Failed to get ticket. Status code was not 201"    echo "$TICKET_RESPONSE"    exit 1fi# Concatenate the service URL with the ticketSERVICE_URL="https://fe.drmtoday.com/frontend/cpix/v1/<Organization UUID>/ingest/<CPIX ID>?ticket=$TICKET"echo $SERVICE_URL
```

##### （1）API-аккаунт

Выберите **Members/Users** из левой боковой панели. API-аккаунт, упомянутый в сценарии, относится к API-аккаунту, настроенному на шаге 2, а "пароль API-аккаунта" соответствует его пароли.

![](https://staticintl.cloudcachetci.com/cms/backend-cms/fe101ef7fe4611ef9f695254007c27c5.png)

##### （2）Organization UUID

Выберите **API endpoints** на левой боковой панели. Organization UUID отображается в правом верхнем углу страницы.

![](https://staticintl.cloudcachetci.com/cms/backend-cms/0d7a4046fe4711efaf3d52540099c741.png)

##### （3）CPIX ID

Выберите **Ingest Settings** из левой боковой панели, где вы можете просмотреть информацию о CPIX, созданную на шаге 2. ID конфигурации CPIX — это CPIX ID, требуемый в сценарии.

![](https://staticintl.cloudcachetci.com/cms/backend-cms/0d8fc99ffe4711efa49152540044a08e.png)

После правильной установки сценария вы можете начать запрос для получения URL секретного ключа.

> **Примечание:**Помните: URL истекает, поэтому рекомендуется периодически его регенерировать.

### Инициирование задач шифрования через API

Для инициирования задач обработки медиа-файлов, находящихся по URL-ссылкам видео или в COS, обратитесь к документации API [Инициирование обработки медиа](https://www.tencentcloud.com/document/product/1041/33627).

```
POST / HTTP/1.1Host: mps.tencentcloudapi.comContent-Type: application/jsonX-TC-Action: ProcessMedia
```

```
{    "InputInfo": {        "Type": "URL",        "UrlInputInfo": {            "Url": "https://test-<appid>.cos.ap-nanjing.myqcloud.com/mps_input/test.mp4"        }    },    "OutputStorage": {        "Type": "COS",        "CosOutputStorage": {            "Region": "ap-nanjing",            "Bucket": "test-<appid>"        }    },    "OutputDir": "/mps_output/drm/",    "MediaProcessTask": {        "AdaptiveDynamicStreamingTaskSet": [            {                "Definition": <definition id>,                "DrmInfo": {                    "Type": "widevine",                    "SpekeDrm": {                        "ResourceId": "test123",                        "KeyServerUrl": "<DRM key server url>",                        "Vector": "<IV>",                        "EncryptionMethod": "cbcs",                        "EncryptionPreset": "preset0"                    }                }            }        ]    },    "TaskNotifyConfig": {        "NotifyType": "URL",        "NotifyUrl": "<notify url>"    }}
```

Пример ответа:

```
{    "Response": {        "TaskId": "24000035-WorkflowTask-cf405e365e75efb2a7bfdef514cc17dbtt195964",        "RequestId": "a7ba06b6-6810-4343-b55d-3afcc3dac64c"    }}
```

Описание примера: TaskId служит уникальным идентификатором задачи, который может быть использован для запроса и управления задачами.

#### Type

Типы шифрования, допустимые значения включают:

- **simpleaes**: Шифрование AES-128, исключительно совместимо с HLS. Поддерживаемые форматы сегментов включают TS и MP4. Допускается только сегментированный режим; режим одного файла не поддерживается.
- **fairplay**: Применимо только к HLS. Формат сегмента ограничен MP4 с поддержкой как сегментированного, так и режима одного файла.
- **widevine**: Совместимо с HLS и DASH. Формат сегмента ограничен MP4 (для выходных данных HLS доступны сегментированный или режим одного файла; для выходных данных DASH поддерживается только режим одного файла).
- **playready**: Поддерживает HLS и DASH. Формат сегмента ограничен MP4 (для выходных данных HLS поддерживается сегментированный или режим одного файла; для выходных данных DASH поддерживается только режим одного файла).

#### SpekeDrm

##### （1）ResourceId

Маркировка ресурса поддерживает 1-128 символов, включая цифры, буквы, подчеркивание (_) и дефис (-). ResourceId можно рассматривать как ID для набора криптографических ключей, который может использоваться для шифрования нескольких различных медиа-потоков. Мы можем просмотреть все созданные ResourceId на консоли DRMtoday.

![](https://staticintl.cloudcachetci.com/cms/backend-cms/96e45612fe4711efa21c525400bf7822.png)

##### （2）KeyServerUrl

URL запроса ключа создается на шаге три подготовительной фазы.

> **Примечание:**Различные поставщики DRM имеют различные ограничения на количество подпотоков, Pallycon позволяет до 5, а DRMtoday — до 9.

##### （3）Vector

Вектор инициализации шифрования (32-байтовая строка).

##### （4）EncryptionMethod

Метод шифрования: По умолчанию FairPlay использует cbcs, в то время как PlayReady и Widevine по умолчанию используют cenc.

Обратите внимание, что различные стандарты DRM поддерживают различные методы шифрования:

- cbcs: Поддерживается PlayReady, Widevine и FairPlay.
- cenc: Поддерживается PlayReady и Widevine.

##### (5) EncryptionPreset

Правила шифрования подпотоков со значением по умолчанию preset0.

- preset0: Все подпотоки шифруются одинаковым ключом.
- preset1: Каждый подпоток шифруется различным ключом.

### Проверка воспроизведения

Воспроизведение может быть использовано со ссылкой на [Официальную документацию DRMtoday Player](https://fe.drmtoday.com/documentation/integration/player_integration.html). Ниже мы иллюстрируем способ воспроизведения зашифрованных потоков с использованием [Официального DRMtoday Player](https://demo.castlabs.com/#/player/) в качестве примера.

1. Нажмите **Try Your Stream**.

![](https://staticintl.cloudcachetci.com/cms/backend-cms/275cd33bfe4811ef83195254005ef0f7.png)

2. Заполните информацию конфигурации.
  2.1. Сначала введите URL потока для воспроизведения в поле "Content URL". Если это поток HLS, выберите "HLS" для типа; если это поток DASH, выберите "MPEG-DASH".

![](https://staticintl.cloudcachetci.com/cms/backend-cms/275d21e6fe4811efbf88525400e889b2.png)

  2.2. Далее настройте информацию об аутентификации клиента. Для DRM Environment выберите DRMtoday PRODUCTION. Merchant должен быть Organization UUID, найденным в API endpoints, а User ID должен быть Members ID из Members/Users. Session ID может быть любым значением, в то время как Asset ID должен быть ResourceId, указанным при инициировании задачи шифрования. После настройки плеера нажмите **Load** для нормального воспроизведения зашифрованного потока.

![](https://staticintl.cloudcachetci.com/cms/backend-cms/7143e220fe4811efa49152540044a08e.png)

![](https://staticintl.cloudcachetci.com/cms/backend-cms/7aa025b8fe4811efbf88525400e889b2.png)


---
*Источник: [https://www.tencentcloud.com/document/product/1041/68547](https://www.tencentcloud.com/document/product/1041/68547)*

---
*Источник (EN): [drm-integration.md](./drm-integration.md)*
