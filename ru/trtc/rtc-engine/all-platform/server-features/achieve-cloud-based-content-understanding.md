# Реализация облачного анализа контента

## Описание сценария

В сценариях, таких как дистанционное образование, трансляция из выставочного зала, видеоконференции, удаленная оценка убытков, финансовая аудиовизуальная запись и онлайн-консультации врача, требования к сбору доказательств, проверке качества, рецензированию, архивированию и повторному воспроизведению часто требуют, чтобы весь процесс видеозвонка или прямой трансляции прошел анализ контента третьей стороной через облачное нарезание.

## Обзор выставления счетов

Для функции облачного анализа контента, инициированной через TRTC, TRTC взимает плату только за аудионарезание и снимки экрана видео. В то же время поставщик услуг третьей стороны взимает плату за облачный анализ контента в соответствии с их собственными правилами выставления счетов. Подробную информацию о стоимости аудионарезания и снимков экрана видео см. в разделе [Описание выставления счетов за аудионарезание и снимки экрана видео](https://www.tencentcloud.com/document/product/647/64803).

## Описание функции

С помощью функции облачного анализа контента TRTC вы можете выполнять облачное нарезание медиапотока каждого пользователя в комнате и отправлять его поставщику услуг третьей стороны для анализа контента без необходимости обработки на стороне клиента.

## Определения

**Облачная модерация:** отправка аудио и видеоконтента третьей стороне через облачное нарезание, получение результатов и их возврат в бэкэнд через обратный вызов.

**Облачное нарезание:** включает сценарии как аудионарезания, так и снимков экрана видео.

**Аудионарезание:** нарезание аудиопотока пользователя в комнате с заданными интервалами времени, в результате чего получаются аудиосегменты.

**Снимок экрана видео:** захват снимков видеопотока пользователя в комнате с заданными интервалами времени, в результате чего получаются изображения.

**Хранилище файлов:** поддержка сохранения файлов облачного нарезания в COS, AWS S3 или Alibaba Cloud OSS.

**Уведомление об обратном вызове:** поддерживается уведомление об обратном вызове. Путем настройки домена обратного вызова статус события облачной модерации уведомит ваш сервер обратного вызова.

## Процесс облачного анализа контента

На основе инициированного вами запроса на облачный анализ контента и информации поставщика услуг третьей стороны в запросе (вам необходимо заранее включить или приобрести услугу третьей стороны), аудио и видеоконтент в задаче облачного анализа контента будут отправлены поставщику услуг обработки контента третьей стороны через API облачного анализа контента для обработки.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/611e0996832011f0992e52540044a08e.png)

Как показано выше, это сценарий записи одного потока. В комнате 1234 якорь 1 и якорь 2 загрузили как аудио, так и видеопотоки. Если вы подписываетесь на их медиапотоки и устанавливаете одновременные снимки экрана видео и проверку аудионарезания, бэкэнд будет отдельно вытягивать их потоки и нарезать их на независимые файлы снимков экрана и аудиофайлы для внешних поставщиков услуг анализа контента.

**Поддерживаемые в настоящее время поставщики услуг модерации:** Tencent TIANYU, Shumei, NetEase Yidun.

## Интерфейс API и ограничение параллелизма вызовов модерации

Ограничение скорости вызовов для API облачного анализа контента составляет 20 qps (при необходимости [отправьте заявку](https://console.tencentcloud.com/workorder/category) для увеличения qps).

Время ожидания API составляет 6 секунд.

Одно приложение поддерживает по умолчанию 500 одновременных потоков передачи. Задачи, превышающие лимит параллелизма, будут неудачными. Если вам нужно больше одновременных потоков передачи, пожалуйста [отправьте заявку](https://console.tencentcloud.com/workorder/category).

Одна задача поддерживает до 25 подписанных хостов в комнате. Хосты, занимающие восходящий аудиопоток, также считаются отдельным потоком передачи.

## Процесс выполнения задачи облачного анализа контента

### Запуск облачного анализа контента ([CreateCloudModeration](https://trtc.io/document/72648?product=rtcengine&menulabel=core%20sdk&platform=flutter))

Для запуска задачи облачного анализа контента вызовите REST API ([CreateCloudModeration](https://trtc.io/document/72648?product=rtcengine&menulabel=core%20sdk&platform=flutter)) через ваш бэкэнд-сервис. Особое внимание обратите на параметр ID задачи (TaskId); этот параметр является уникальным идентификатором задачи. Вам необходимо сохранить этот ID задачи, так как он потребуется для последующих операций, нацеленных на интерфейс этой задачи.

1. API для инициации задач облачного анализа контента ([CreateCloudModeration](https://trtc.io/document/72648?product=rtcengine&menulabel=core%20sdk&platform=flutter))

В API вам необходимо указать параметры входа в комнату UserId и UserSig для назначения робота передачи ([Как получить UserSig](https://www.tencentcloud.com/document/product/647/35166?from_search=1&lang=en&pg=)). Убедитесь, что UserId не дублирует идентификаторы обычных якорей или зрителей в вашей комнате и не совпадает с UserId робота передачи, уже назначенного комнате в процессе передачи; в противном случае это приведет к отказу задачи записи.

2. Назначение пользователей потока ([SubscribeModerationUserIds](https://trtc.io/document/36760?product=rtcengine&menulabel=core%20sdk&platform=flutter#subscribemoderationuserids))

Вы также можете указать информацию черного списка и белого списка пользователей якорей для передачи или исключения через параметр [SubscribeModerationUserIds](https://trtc.io/document/36760?product=rtcengine&menulabel=core%20sdk&platform=flutter#subscribemoderationuserids). Конечно, мы также поддерживаем операции обновления во время процесса задачи.

3. Указание места передачи хранилища ([ModerationStorageParams](https://trtc.io/document/36760?product=rtcengine&menulabel=core%20sdk&platform=flutter#moderationstorageparams))

Место хранения: поддерживаются хранилища AWS S3 или COS. Укажите параметры хранилища в параметре [ModerationStorageParams](https://trtc.io/document/36760?product=rtcengine&menulabel=core%20sdk&platform=flutter#moderationstorageparams).

Файлы нарезаемых изображений имеют формат png, файлы аудионарезания — формат ogg.

4. Указание поставщика услуг анализа контента ([ModerationSupplierParam](https://trtc.io/document/36760?product=rtcengine&menulabel=core%20sdk&platform=flutter#moderationsupplierparam))

### Запрос статуса задачи облачного анализа контента ([DescribeCloudModeration](https://trtc.io/document/72646?product=rtcengine&menulabel=core%20sdk&platform=flutter))

При необходимости вы можете вызвать этот API для запроса статуса задачи облачного анализа контента.

### Изменение статуса задачи облачного анализа контента ([ModifyCloudModeration](https://trtc.io/document/72645?product=rtcengine&menulabel=core%20sdk&platform=flutter))

При необходимости вы можете вызвать этот API для изменения параметров задачи, например для подписки на черный список/белый список [SubscribeModerationUserIds](https://trtc.io/document/36760?product=rtcengine&menulabel=core%20sdk&platform=flutter#subscribemoderationuserids)

### Отключение задачи облачного анализа контента ([DeleteCloudModeration](https://trtc.io/document/72647?product=rtcengine&menulabel=core%20sdk&platform=flutter))

После успешной активации задачи облачного анализа контента вы можете использовать этот API для ее остановки.

## Обратный вызов облачного анализа контента

Мы предоставляем несколько событий обратного вызова для функции облачного анализа контента, чтобы помочь вам своевременно узнать о статусе обработки и завершения задач анализа контента.

### Конфигурация адреса обратного вызова облачного анализа контента

Консоль Tencent Real-Time Communication (TRTC) поддерживает самостоятельную конфигурацию информации об обратном вызове. После конфигурации вы сможете получать уведомления об обратном вызове событий. Подробное руководство см. в разделе [Конфигурация обратного вызова](https://trtc.io/document/39559?product=rtcengine&menulabel=core%20sdk&platform=flutter).

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/d5e5667182f511f0a8ae5254005ef0f7.png)

### API обратного вызова

Вы можете предоставить шлюз службы HTTP/HTTPS для получения обратных вызовов и подписки на сообщения обратного вызова. При возникновении связанных событий система облачного анализа контента отправит уведомления о событиях обратного вызова на ваш сервер получения сообщений.

Формат сообщения обратного вызова события: HTTPS POST-запрос, отправляемый на ваш сервер. При этом:

Формат кодирования символов: UTF-8.

Запрос: формат body — JSON.

Ответ: HTTP STATUS CODE = 200. Сервер игнорирует содержимое пакета ответа. Для дружественности протокола рекомендуется, чтобы содержимое вашего ответа содержало JSON: {"code":0}.

## Событие обратного вызова облачного анализа контента

### Описание параметров

Заголовок сообщения обратного вызова события содержит следующие поля:

| Имя поля | Значение |
| --- | --- |
| Content-Type | application/json |
| Sign | значение подписи |
| SdkAppId | значение ID приложения SDK |

Тело сообщения обратного вызова события содержит следующие поля:

| Имя поля | Тип | Описание |
| --- | --- | --- |
| EventGroupId | Number | ID группы событий. Группа событий облачного анализа контента фиксирована как 11. |
| EventType | Number | Тип события уведомления об обратном вызове. |
| CallbackTs | Number | Временная метка Unix отправки запроса обратного вызова сервером событий на ваш сервер в миллисекундах. |
| EventInfo | JSON Object | Информация о событии. |

### Описание типа события

| Имя поля | Тип | Описание |
| --- | --- | --- |
| EVENT_TYPE_CLOUD_Moderation_START | 1101 | Запуск модуля облачного анализа контента. |
| EVENT_TYPE_CLOUD_Moderation_STOP | 1102 | Выход из модуля облачного анализа контента. |
| EVENT_TYPE_CLOUD_Moderation_SEND_START | 1103 | Запуск задачи облачного анализа контента. |
| EVENT_TYPE_CLOUD_Moderation_TASK_INFO | 1104 | Обратный вызов результата облачного анализа контента. |
| EVENT_TYPE_CLOUD_Moderation_SEND_STOP | 1105 | Отправка облачного анализа контента на рецензирование. |
| EVENT_TYPE_CLOUD_Moderation_UPLOAD_ERROR | 1106 | Возникла ошибка модуля доставки облачного анализа контента. |

### Описание информации о событии

| Имя поля | Тип | Описание |
| --- | --- | --- |
| RoomId | String/Number | Имя комнаты (тип совпадает с типом ID комнаты клиента). |
| EventTs | Number | Временная метка Unix возникновения события в секундах (не рекомендуется к использованию, рекомендуется использовать EventMsTs). |
| EventMsTs | Number | Временная метка Unix возникновения события в миллисекундах. |
| UserId | String | ID пользователя робота извлечения потока. |
| TaskId | String | ID задачи, уникальный идентификатор задачи облачного анализа контента, работающей только один раз. |
| Payload | JsonObject | Определение различных типов событий. |

**Определение Payload для события типа 1101** при EVENT_TYPE_CLOUD_Moderation_START:

| Имя поля | Тип | Описание |
| --- | --- | --- |
| Status | Number | 0: представляет успешный запуск модуля. 1: представляет неудачный запуск модуля. |

```
{    "EventGroupId": 11,    "EventType": 1101,    "CallbackTs": 1726125338219,    "EventInfo": {        "RoomId": "960025",        "EventTs": 1726125338,        "EventMsTs": 1726125338219,        "UserId": "inspect",        "TaskId": "-npVqpdU7sBobiK1iskE3BwlLIebCMrbKUbnL4K-rO+8oZWQndib9uvO4Deq9P1Na+sXGNGNuAE."	    "Payload": {            "Status": 0        }    }}
```

**Определение Payload для события типа 1102** при EVENT_TYPE_CLOUD_Moderation_STOP:

| Имя поля | Тип | Описание |
| --- | --- | --- |
| LeaveCode | Number | 0: представляет нормальный вызов модуля облачного анализа контента для выхода из журнала рецензирования. 1: робот передачи был выбит из комнаты клиентом. 2: клиент закрыл комнату. 3: сервер выбил робота передачи. 4: сервер закрыл комнату. 99: в комнате нет других потоков пользователей, кроме робота передачи, выход после превышения указанного времени. 100: выход по истечении времени ожидания комнаты. 101: повторный вход того же пользователя в одну и ту же комнату приводит к выходу робота. |

```
{        "EventGroupId": 11,        "EventType":    1102,        "CallbackTs":   1729601782073,        "EventInfo":    {                "RoomId":       "975626",                "EventTs":      "1729601782",                "EventMsTs":    1729601782073,                "UserId":       "SliceTaskDuration1-partner-robot",                "TaskId":       "-nHRjqhU7gTG0UIL-MquzG8D0Q+wehTbVTeeIIK-rO+8oZWQndibtueIpQ8A0F3n9PEVRk0rngE.",                "Payload":      {                        "LeaveCode":    99                }        }}
```

**Определение Payload для события типа 1103** при EVENT_TYPE_CLOUD_Moderation_SEND_START:

| Имя поля | Тип | Описание |
| --- | --- | --- |
| Status | Number | 0: представляет начало отправки файла нарезанного фрагмента. |

```
{    "EventGroupId": 11,    "EventType": 1103,    "CallbackTs": 1726750023538,    "EventInfo": {        "RoomId": "295210",        "EventTs": 1726750023,        "EventMsTs": 1726750023538,        "UserId": "inspect",        "TaskId": "-nHwXIdU7mJvL22pFsXZ-v7OgEzq1OzbNXe9L4K-4pycoZWQndib3ZfzqN7Wq+AdiPLMBLxd0gE.",        "Payload": {            "Status": 0        }    }}
```

### Результат рецензирования

**Определение Payload для события типа 1104** при EVENT_TYPE_CLOUD_Moderation_FILE_INFO:

| Имя поля | Тип | Описание |
| --- | --- | --- |
| DataId | String | ID задачи облачного анализа контента. |
| RequestId | String | ID запроса поставщика услуг анализа контента третьей стороны. |
| MediaType | Number | speech2: изображение. |
| Suggest | Number | 0: рекомендуется пройти. 1: рекомендуется ручное рецензирование. 2: рекомендуется блокировка. |
| Label | String | Normal Ad: RecommendationPorn: PornographyAbuse: InsultIllegal: ProhibitedPolity: Political contentTerror: Violence and terrorSexy: Sexy imageQRCode: QR codeCustom |
| Image | String | Путь к изображению в корзине пользователя. |
| Audio | String | Путь к аудиофайлу в корзине пользователя. |
| AudioText | String | Текст распознавания аудио. |
| CheckDetail | Object | Подробные результаты облачного анализа контента. |
| Keywords | []String | Ключевое слово (слова) |
| Score | Number | Оценка достоверности. |
| AudioSegments | Object | Информация о местоположении аудиосегмента. |
| ImageLocation | Object | Информация о координатах попадания изображения. |

**Пример результата рецензирования услуги аудиомодерации:**

```
{    "EventGroupId": 11,    "EventType": 1104,    "CallbackTs": 1726750309161,    "EventInfo": {        "RoomId": "963239",        "EventTs": 1735872251,        "EventMsTs": 1735872251524,        "UserId": "TRTCModerationCase2-user0",        "StreamerUserId": "SliceCustomUploadCase6-user0",        "TaskId": "-m9lm+lU7tOlL2mFgsPuzHeyNThbhZzbJlKQI4K-raO8oZWQndibARGYcSDohF0Zfgo7RNCuGQE.",        "Payload": {            "DataId": "547512114953106866",            "RequestId": "",            "MediaType": 1,            "Suggest": 2,            "Label": "Polity",            "Image": "",            "Rate": 100,            "Audio": "https://x.xx.com/-m9lm+lU7tOlL2mFgsPuzHeyNThbhZzbJlKQI4K-raO8oZWQndibARGYcSDohF0Zfgo7RNCuGQE./547512114835666354.ogg",            "AudioText": "xxxxxx.",            "CheckDetail": [                {                    "Label": "Polity",                    "Suggest": 2,                    "Keywords": [                        "XXX"                    ],                    "Score": 100,                    "Desc": "",                    "AudioSegments": {},                    "ImageLocation": {}                }            ]        }    }}
```

**Пример результата рецензирования изображения:**

```
{    "EventGroupId": 11,    "EventType": 1104,    "CallbackTs": 1726750309161,    "EventInfo": {        "RoomId": "963239",        "EventTs": 1735872251,        "EventMsTs": 1735872251524,        "UserId": "TRTCModerationCase2-user0",        "StreamerUserId": "SliceCustomUploadCase6-user0",        "TaskId": "-m9lm+lU7tOlL2mFgsPuzHeyNThbhZzbJlKQI4K-raO8oZWQndibARGYcSDohF0Zfgo7RNCuGQE.",        "Payload": {            "DataId": "554678038156038407",            "RequestId": "a82e0175-65ed-46b5-a656-45814aea1c60",            "MediaType": 2,            "Suggest": 2,            "Label": "Ad",            "Image": "https://trtcauto-sg-1311572968.cos.ap-singapore.myqcloud.com/prefix1/prefix2/-nHlf1xU7tsdRVBjLsog0ZX9T62DtVjbNguMJYK-58aNM6KipeDPAfrKt1aejC8ipMaphfYxAQ../TianyuModerationCase3-user1/images/20005067_963715_TianyuModerationCase3-user1_20250221211113.png",            "ImageOcr": "Movable Type Culture Moveable TVo The pain of never being able to go home again;"            "Rate": 90,            "Audio": "",            "AudioText": "",            "CheckDetail": [                {                    "Scene": "Ad",                    "Label": "Normal",                    "Suggest": 2,                    "Keywords": [],                    "Score": 90,                    "AudioSegments": {},                    "ImageLocation": {}                }            ]        }    }}
```

**Определение Payload для события типа 1105** при EVENT_TYPE_CLOUD_Moderation_SEND_STOP:

| Имя поля | Тип | Описание |
| --- | --- | --- |
| Status | Number | Завершить задачу. |

```
{    "EventGroupId": 11,    "EventType": 1105,    "CallbackTs": 1726751347072,    "EventInfo": {        "RoomId": "295211",        "EventTs": 1726751347,        "EventMsTs": 1726751347072,        "UserId": "inspect",        "TaskId": "-nHwXIdU7jx6C00Nt8Vr+3h4GwYdP7zbeHi9L4K-4pycoZWQndibqFeEaV4LvjFqSuQvaAkrNQE.",        "Payload": {            "Status": 0        }    }}
```

**Определение Payload для события типа 1106** при EVENT_TYPE_CLOUD_Moderation_SEND_ERROR:

| Имя поля | Тип | Описание |
| --- | --- | --- |
| Code | Number | Код ошибки COS или хранилища третьей стороны. |
| Message | String | Сообщение об ошибке COS или хранилища третьей стороны. |

```
{    "EventGroupId": 11,    "EventType": 1106,    "CallbackTs": 1726751347072,    "EventInfo": {        "RoomId": "295211",        "EventTs": 1726751347,        "EventMsTs": 1726751347072,        "UserId": "inspect",        "TaskId": "-nHwXIdU7jx6C00Nt8Vr+3h4GwYdP7zbeHi9L4K-4pycoZWQndibqFeEaV4LvjFqSuQvaAkrNQE.",        "Payload": {            "Code": 10002,            "Message": "BadRequest"        }    }}
```

### Управление файлами модерации

При инициации запроса TencentCloud API для облачной модерации вы можете настроить, передавать ли файлы совпадений через параметр [ModerationParams](https://trtc.io/document/36760?product=rtcengine&menulabel=core%20sdk&platform=flutter#moderationparams).SaveModerationFile. Бэкэнд назначит загрузку необходимых файлов совпадений на выбранную вами платформу облачного хранилища (COS, AWS S3 или Alibaba Cloud OSS).

### **Спецификация именования файлов совпадений**

**Имя по умолчанию для аудиосегментов:**

{bucket name}/{taskId}/{userId}/audios/{sdkappid}_{roomId}_{userid}_{UTC time}.ogg

**Имя по умолчанию для снимков экрана видео:**

{bucket name}/{taskId}/{userId}/images/{sdkappid}_{roomId}_{userid}_{UTC time}.png

#### Описание значения поля

| **Поле** | **Значение** |
| --- | --- |
| <taskId> | ID задачи облачного анализа контента. |
| <sdkappid> | SdkAppId задачи облачного анализа контента. |
| <roomId> | Номер комнаты для облачного анализа контента. |
| <userid> | ID пользователя якоря |
| UTC time | строка текущего времени, например: 20250106143143 |


---
*Источник: [https://trtc.io/document/73394](https://trtc.io/document/73394)*

---
*Источник (EN): [achieve-cloud-based-content-understanding.md](./achieve-cloud-based-content-understanding.md)*
