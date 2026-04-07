# Учебное пособие по умному доступу к субтитрам

## Обзор

Функция умных субтитров поддерживает обработку автономных аудиофайлов, видеофайлов и потоков в реальном времени. Она может извлекать субтитры на исходном языке из видео с помощью автоматического распознавания речи (ASR) или оптического распознавания символов (OCR) и реализовывать многоязычный перевод. Функция поддерживает перевод файлов субтитров на основе LLM. Она также позволяет настраивать словари ключевых слов и терминов для повышения точности распознавания речи и перевода на основе LLM.

| Функция умных субтитров | Описание | Поддерживаемый тип входных данных |
| --- | --- | --- |
| Генерация субтитров на основе ASR | Включает преобразование диалогов на основе ASR в файлы субтитров для перевода на основе LLM. Поддерживает настройку словарей ключевых слов и терминов для повышения точности распознавания речи и перевода на основе LLM. Поддерживает встраивание и рендеринг субтитров в видеоизображения. | Аудиофайл, видеофайл, прямой поток, поток аудио в реальном времени |
| Генерация субтитров на основе OCR | Включает извлечение символов из изображений на основе OCR в виде субтитров для перевода на основе LLM. | Видеофайл (с жесткими субтитрами на изображениях) |
| Перевод файла субтитров | Поддерживает перевод входных субтитров на основе LLM на различные языки и создание новых субтитров. | Файл субтитров (в формате WebVTT или SRT) |

#### Ключевые возможности

- Комплексная поддержка платформы: предлагает возможности обработки для файлов по требованию, потоков в реальном времени и потоков RTC. Субтитрирование прямой трансляции в реальном времени поддерживает режимы устойчивого и градиентного отображения, имеет низкий барьер интеграции и не требует модификаций на стороне воспроизведения.
- Высокая точность: использует крупномасштабные модели и поддерживает базы данных ключевых слов и словарей, достигая точности, лидирующей в отрасли.
- Разнообразие языков: поддерживает сотни языков, включая различные диалекты. Способен распознавать смешанную речь, такую как комбинации китайского и английского языков.
- Настраиваемые стили: позволяет встраивать открытые субтитры в видео с настраиваемыми стилями субтитров (шрифт, размер, цвет, фон, позиция и т. д.).

#### Демонстрация

1. Получите доступ к [Experience Center](https://mps.live/demo/ai/captions) и перейдите на страницу опыта умных субтитров. На правой стороне выберите автономный видеофайл или прямой поток, укажите исходный язык и тип субтитров, затем нажмите **Обработка в один клик**.
2. После завершения обработки вы сможете просмотреть результаты.

> **Примечание:** Функция демонстрации MPS относительно проста и предназначена только для экспериментирования с базовым эффектом. Используйте доступ через API для тестирования полного эффекта.

![](https://staticintl.cloudcachetci.com/cms/backend-cms/b143845e563011f0bf84525400454e06.png)

## Сценарий 1: Обработка автономных файлов

### Способ 1: Инициирование задачи без кода из консоли

#### Инициирование задачи вручную

Войдите в консоль Media Processing Service (MPS) и нажмите **Создать задачу >** [Создать задачу обработки VOD](https://console.tencentcloud.com/mps/tasks/create).

![](https://staticintl.cloudcachetci.com/cms/backend-cms/73006ff9a63c11efbd5752540055f650.png)

1. **Укажите входной файл.**

Вы можете выбрать видеофайл из хранилища объектов Tencent Cloud (COS) или предоставить URL загрузки видео. Текущая функция генерации и перевода субтитров не поддерживает использование AWS S3 в качестве источника входного файла.

2. **Обработайте входной файл.**

Выберите **Создать оркестрацию** и вставьте узел "Умные субтитры".

![](https://staticintl.cloudcachetci.com/cms/backend-cms/64dace9418f811f09240525400bf7822.png)

Вы можете выбрать предустановленный шаблон или использовать пользовательские параметры. Для подробного руководства по конфигурации шаблона см. [Шаблон умных субтитров](https://www.tencentcloud.com/document/product/1041/68175).

![](https://staticintl.cloudcachetci.com/cms/backend-cms/4057ae28cb7211f0afdc52540044a08e.png)

3. **Укажите выходной путь.**

Укажите путь хранилища выходного файла.

4. **Инициируйте задачу.**

Нажмите **Создать** для инициирования задачи.

#### Автоматическое запуск задачи через оркестрацию (опционально)

Если вы хотите загрузить видеофайл в корзину COS и достичь автоматического создания умных субтитров в соответствии с предустановленными параметрами, вы можете:

1. Перейдите в **Оркестрация по требованию** в меню, нажмите **Создать оркестрацию VDD**, выберите узел умных субтитров в конфигурации задачи и настройте параметры, такие как корзина и директория для запуска.

![](https://staticintl.cloudcachetci.com/cms/backend-cms/b0d03373cc3911f08658525400454e06.png)

2. Перейдите в список **Оркестрация по требованию**, найдите новую оркестрацию и включите переключатель в **Включение**. После этого любые новые видеофайлы, добавленные в директорию запуска, автоматически инициируют задачи в соответствии с предустановленным процессом и параметрами оркестрации, а обработанные видеофайлы сохраняются по выходному пути, настроенному в оркестрации.

> **Примечание:** Оркестрации требуется 3-5 минут для вступления в силу после включения.

![](https://staticintl.cloudcachetci.com/cms/backend-cms/1915ec3818f911f0b5c65254001c06ec.png)

### Способ 2: Вызов API

#### **Способ 1**

Вызовите API [ProcessMedia](https://www.tencentcloud.com/document/product/1041/33640) и инициируйте задачу, указав **ID шаблона**. Пример:

```
{    "InputInfo": {        "Type": "URL",        "UrlInputInfo": {            "Url": "https://test-1234567.cos.ap-guangzhou.myqcloud.com/video/test.mp4" // Замените на URL обрабатываемого видео.        }    },    "SmartSubtitlesTask": {        "Definition": 122 //122 — это ID предустановленного шаблона "видео источник на китайском — создать субтитры на китайском и английском", который можно заменить на ID пользовательского шаблона умных субтитров.    },    "OutputStorage": {        "CosOutputStorage": {            "Bucket": "test-1234567",            "Region": "ap-guangzhou"        },        "Type": "COS"    },    "OutputDir": "/output/",    "Action": "ProcessMedia",    "Version": "2019-06-12"}
```

#### **Способ 2**

Вызовите API [ProcessMedia](https://www.tencentcloud.com/document/product/1041/33640) и инициируйте задачу, указав **ID оркестрации**. Пример:

```
{    "InputInfo": {        "Type": "COS",         "CosInputInfo": {            "Bucket": "facedetectioncos-125*****11",             "Region": "ap-guangzhou",             "Object": "/video/123.mp4"        }    },     "ScheduleId": 12345, //Замените на ID пользовательской оркестрации. 12345 — это пример кода и не имеет практического значения.    "Action": "ProcessMedia",     "Version": "2019-06-12"}
```

> **Примечание:** Если установлен адрес обратного вызова, см. документ [ParseNotification](https://www.tencentcloud.com/document/product/1041/33679) для пакетов ответов.

### Применение субтитров к видео (дополнительная возможность)

Вызовите API [ProcessMedia](https://www.tencentcloud.com/document/product/1041/33640), инициируйте **задачу перекодирования**, укажите путь к файлу vtt для субтитров и укажите стили применения субтитров через поле [SubtitleTemplate](https://www.tencentcloud.com/document/product/1041/33690#subtitletemplate).

Пример:

```
{    "MediaProcessTask": {        "TranscodeTaskSet": [            {                "Definition": 100040, //ID шаблона перекодирования. Должно быть заменено на нужный вам шаблон перекодирования.                "OverrideParameter": { //Параметры переопределения, используемые для гибкого переопределения некоторых параметров в шаблоне перекодирования.                    "SubtitleTemplate": { //Конфигурация применения субтитров.                        "Path": "https://test-1234567.cos.ap-nanjing.myqcloud.com/mps_autotest/subtitle/1.vtt",                         "StreamIndex": 2,                         "FontType": "simkai.ttf",                         "FontSize": "10px",                         "FontColor": "0xFFFFFF",                         "FontAlpha": 0.9                    }                }            }        ]    },     "InputInfo": { //Информация о входе.        "Type": "URL",         "UrlInputInfo": {            "Url": "https://test-1234567.cos.ap-nanjing.myqcloud.com/mps_autotest/subtitle/123.mkv"        }    },     "OutputStorage": { //Выходная корзина.        "Type": "COS",         "CosOutputStorage": {            "Bucket": "test-1234567",             "Region": "ap-nanjing"        }    },     "OutputDir": "/mps_autotest/output2/", //Выходной путь.    "Action": "ProcessMedia",     "Version": "2019-06-12"}
```

### Запрос результатов задачи

#### Через консоль

1. Перейдите в [Управление автономными задачами](https://console.tencentcloud.com/mps/tasks/vod-list) в консоли, где список отображает только что инициированные задачи.

![](https://staticintl.cloudcachetci.com/cms/backend-cms/4782ad07cc3a11f08e74525400bf7822.png)

2. Когда статус подзадачи — "Успешно", нажатие на **Просмотр результата** позволяет просмотреть субтитры.

![](https://staticintl.cloudcachetci.com/cms/backend-cms/5c1ceb7ecc3a11f0afdc52540044a08e.png)

3. Созданный файл субтитров VTT можно найти в **Оркестрация > Корзина COS > Выходная корзина**.

![](https://staticintl.cloudcachetci.com/cms/backend-cms/2dde588719ca11f0b5c65254001c06ec.png)

Пример китайско-английских субтитров:

![](https://staticintl.cloudcachetci.com/cms/backend-cms/2dea220f19ca11f091eb525400454e06.png)

#### Обратные вызовы уведомлений о событиях

При инициировании задачи обработки медиа с помощью [ProcessMedia](https://www.tencentcloud.com/document/product/1041/33640) вы можете настроить обратные вызовы событий через параметр `TaskNotifyConfig`. По завершении задачи результаты будут переданы вам через настроенную информацию обратного вызова, которую вы можете расшифровать с помощью [ParseNotification](https://www.tencentcloud.com/document/product/1041/33679).

#### Запрос результатов задачи путем вызова API

Вызовите API [DescribeTaskDetail](https://www.tencentcloud.com/document/product/1041/33640) и заполните ID задачи (например, 24000022-WorkflowTask-b20a8exxxxxxx1tt110253 или 24000022-ScheduleTask-774f101xxxxxxx1tt110253) для запроса результатов задачи. Пример:

![](https://staticintl.cloudcachetci.com/cms/backend-cms/aa2482efb92b11f0a6c652540044a08e.png)

## Сценарий 2: Потоки в реальном времени

В настоящее время существует 2 решения для использования субтитров и переводов в потоках в реальном времени: включение функции субтитров через консоль Cloud Streaming Services (CSS) или использование MPS для обратного вызова текста и его встраивания в потоки в реальном времени. Рекомендуется включить функцию субтитров через консоль CSS. Решение описано следующим образом:

### Способ 1: Включение функции субтитров в консоли CSS

1. **Настройте функцию прямого субтитрирования.**
  1.1. Включите [CSS](https://console.tencentcloud.com/live/livestat) и [MPS](https://console.tencentcloud.com/mps/index).
  1.2. Войдите в [консоль CSS](https://console.tencentcloud.com/live/livestat), [создайте шаблон субтитров](https://console.tencentcloud.com/live/config/subtitle) и привяжите шаблон перекодирования.
2. **Получите потоки субтитров.**

Когда получен поток перекодирования (добавьте имя шаблона перекодирования `_имя_шаблона_перекодирования` связанное с шаблоном субтитров к соответствующему StreamName прямого потока для создания адреса потока перекодирования), субтитры будут отображаться. Для подробных правил объединения адресов для получения потоков см. [Объединение URL-адресов для воспроизведения](https://www.tencentcloud.com/document/product/267/38393?lang=en&pg=#splicing-push-urls).

> **Примечание:** В настоящее время существует 2 форма отображения субтитров: субтитры в реальном времени и отложенные субтитры в устойчивом состоянии. Для субтитров в реальном времени субтитры в прямой трансляции динамически корректируют содержание слово за словом на основе содержания речи, и выходные субтитры изменяются в реальном времени. Для отложенных субтитров в устойчивом состоянии система отображает прямую трансляцию с задержкой в соответствии с установленным временем, но опыт просмотра режима полных субтитров лучше.

### Способ 2: Обратный вызов текста через MPS

В настоящее время не поддерживается использование консоли MPS для инициирования задач умных субтитров потока в реальном времени. Вы можете инициировать их через API.

Ниже приведены примеры использования. Для подробной документации по API см. [ProcessLiveStream](https://www.tencentcloud.com/document/product/1041/33641). Для пакета обратного вызова в реальном времени см. [ParseLiveStreamProcessNotification](https://www.tencentcloud.com/document/product/1041/33680).

> **Примечание:** В настоящее время обработка потоков в реальном времени с помощью MPS требует использования шаблона **Intelligent Identification**. Это достигается с помощью автоматического распознавания речи или перевода речи.

```
{    "Url": "http://5000-wenzhen.liveplay.myqcloud.com/live/123.flv",     "AiRecognitionTask": {        "Definition": 10101 //10101 — это ID предустановленного шаблона китайских субтитров, который можно заменить на ID пользовательского шаблона интеллектуальной идентификации.    },     "OutputStorage": {        "CosOutputStorage": {            "Bucket": "6c0f30dfvodgzp*****0800-10****53",             "Region": "ap-guangzhou"        },         "Type": "COS"    },     "OutputDir": "/6c0f30dfvodgzp*****0800/0d1409d3456551**********652/",     "TaskNotifyConfig": {        "NotifyType": "URL",         "NotifyUrl": "http://****.qq.com/callback/qtatest/?token=*****"    },     "Action": "ProcessLiveStream",     "Version": "2019-06-12"}
```

## Сценарий 3: Обработка частных потоков аудио через WebSocket

В сценариях, таких как видеоконференции и двусторонняя голосовая связь, аудио может передаваться в услуги распознавания и перевода через WebSocket, и результаты могут быть возвращены через тот же протокол. Поддерживается распознавание, распознавание и перевод, а также одновременное распознавание и перевод нескольких потоков аудио в реальном времени. Субтитры в реальном времени могут выводиться в режиме устойчивого состояния или градиента. Для деталей протокола см. [Протокол WebSocket для распознавания](https://www.tencentcloud.com/document/product/1041/72106).

Пример кода:

```
#!/usr/bin/env python3# -*- coding: utf-8 -*-import argparseimport structimport timeimport osimport signalimport sysimport hashlibimport hmacimport randomfrom urllib.parse import urlencode, urlunsplit, quoteimport websocketsimport asyncioimport loggingimport json# Setup logginglogging.basicConfig(level=logging.INFO)logger = logging.getLogger(__name__)class AudioPacket:    def __init__(self, format=1, is_end=False, timestamp=0, audio_src_id="123456", ext_data=b'', data=b''):        self.format = format        self.is_end = is_end        self.timestamp = timestamp        self.audio_src_id = audio_src_id        self.ext_data = ext_data        self.data = data    def marshal(self):        """Serialize audio packet to binary format"""        header = struct.pack(            '>BBQH',             self.format,             1 if self.is_end else 0,            self.timestamp,            len(self.audio_src_id)        )        audio_src_bytes = self.audio_src_id.encode('utf-8')        ext_len = struct.pack('>H', len(self.ext_data))        return header + audio_src_bytes + ext_len + self.ext_data + self.datadef sha256hex(s):    """Calculate SHA256 hex digest"""    if isinstance(s, str):        s = s.encode('utf-8')    return hashlib.sha256(s).hexdigest()def hmacsha256(s, key):    """Calculate HMAC-SHA256"""    if isinstance(s, str):        s = s.encode('utf-8')    if isinstance(key, str):        key = key.encode('utf-8')    return hmac.new(key, s, hashlib.sha256).digest()def generate_random_number(digits):    """Generate random number with specified digits"""    low = 10 ** (digits - 1)    high = (10 ** digits) - 1    return random.randint(low, high)def generate_url_v3(args):    """Generate WebSocket URL with TC3-HMAC-SHA256 signature"""    query_params = {}    if args.dstLang:        query_params["transSrc"] = args.lang        query_params["transDst"] = args.dstLang    else:        query_params["asrDst"] = args.lang        query_params["fragmentNotify"] = "1" if args.frame else "0"    query_params["timeoutSec"] = str(args.timeout)        timestamp = int(time.time())    expire_timestamp = timestamp + 3600        query_params["timeStamp"] = str(timestamp)    query_params["expired"] = str(expire_timestamp)    query_params["secretId"] = args.secretId    query_params["nonce"] = str(generate_random_number(10))        # Sort keys and build canonical query string    sorted_keys = sorted(query_params.keys())    canonical_query = "&".join(        ["{}={}".format(k, quote(query_params[k], safe=''))          for k in sorted_keys]    )        # Build canonical request    path = "/wss/v1/{}".format(args.appid)    http_method = "post"    canonical_uri = path    canonical_headers = "content-type:application/json; charset=utf-8\\nhost:{}\\n".format(args.addr)    signed_headers = "content-type;host"        canonical_request = "{}\\n{}\\n{}\\n{}\\n{}\\n".format(        http_method,        canonical_uri,        canonical_query,        canonical_headers,        signed_headers,    )        # Build string to sign    date = time.strftime("%Y-%m-%d", time.gmtime(timestamp))    credential_scope = "{}/mps/tc3_request".format(date)    hashed_canonical = sha256hex(canonical_request)        algorithm = "TC3-HMAC-SHA256"    string_to_sign = "{}\\n{}\\n{}\\n{}".format(        algorithm,        timestamp,        credential_scope,        hashed_canonical    )        # Calculate signature    secret_date = hmacsha256(date, "TC3" + args.secretKey)    secret_service = hmacsha256("mps", secret_date)    secret_signing = hmacsha256("tc3_request", secret_service)    signature = hmac.new(        secret_signing,         string_to_sign.encode('utf-8'),         hashlib.sha256    ).hexdigest()        # Add signature to query params    query_params["signature"] = signature        # Build final URL    scheme = "wss" if args.ssl else "ws"    url = urlunsplit((        scheme,        args.addr,        path,        urlencode(query_params),        ""    ))    return urlasync def receive_messages(websocket, stop_event):    """Handle incoming WebSocket messages"""    try:        while not stop_event.is_set():            message = await websocket.recv()            if isinstance(message, bytes):                try:                    message = message.decode('utf-8')                except UnicodeDecodeError:                    message = str(message)            logger.info("Received: %s", message)    except Exception as e:        logger.info("Connection closed: %s", e)async def run_client():    parser = argparse.ArgumentParser()    parser.add_argument("--addr", default="mps.cloud.tencent.com", help="websocket service address")    parser.add_argument("--file", default="./wx_voice.pcm", help="pcm file path")    parser.add_argument("--appid", default="121313131", help="app id")    parser.add_argument("--lang", default="zh", help="language")    parser.add_argument("--dstLang", default="", help="destination language")    parser.add_argument("--frame", action="store_true", help="enable frame notify")    parser.add_argument("--secretId", default="123456", help="secret id")    parser.add_argument("--secretKey", default="123456", help="secret key")    parser.add_argument("--ssl", action="store_true", help="use SSL")    parser.add_argument("--timeout", type=int, default=10, help="timeout seconds")    parser.add_argument("--wait", type=int, default=700, help="wait seconds after end")    args = parser.parse_args()    url = generate_url_v3(args)    logger.info("Connecting to %s", url)    try:        # Python 3.6 compatible websockets connection        websocket = await websockets.connect(url, ping_timeout=5)        # Handle initial response        initial_msg = await websocket.recv()        try:            result = json.loads(initial_msg)            if result.get("Code", 0) != 0:                logger.error("Handshake failed: %s", result.get("Message", ""))                return            logger.info("TaskId %s handshake success", result.get("TaskId", ""))        except ValueError:  # json.JSONDecodeError not available in 3.6            logger.error("Invalid initial message")            return        # Setup signal handler        loop = asyncio.get_event_loop()        stop_event = asyncio.Event()        loop.add_signal_handler(signal.SIGINT, stop_event.set)        # Start receiver        receiver_task = asyncio.ensure_future(receive_messages(websocket, stop_event))        # Audio processing        try:            with open(args.file, "rb") as fd:                PCM_DUR_MS = 40                pcm = bytearray(PCM_DUR_MS * 32)                pkt = AudioPacket(data=pcm)                is_end = False                wait_until = 0                while not stop_event.is_set():                    if is_end:                        if time.time() > wait_until:                            logger.info("Finish")                            break                        await asyncio.sleep(0.1)                        continue                    # Read PCM data                    n = fd.readinto(pkt.data)                    if n < len(pkt.data):                        pkt.is_end = True                        is_end = True                        wait_until = time.time() + args.wait                    # Send audio packet                    await websocket.send(pkt.marshal())                    logger.info("Sent ts %d", pkt.timestamp)                    pkt.timestamp += n // 32                    await asyncio.sleep(PCM_DUR_MS / 1000)        except IOError:  # FileNotFoundError not available in 3.6            logger.error("Open file error: %s", args.file)            return        # Cleanup        await asyncio.wait_for(receiver_task, timeout=1)        await websocket.close()    except Exception as e:        logger.error("Connection error: %s", e)        returnif __name__ == "__main__":    # Python 3.6 compatible asyncio runner    loop = asyncio.get_event_loop()    try:        loop.run_until_complete(run_client())    finally:        loop.close()
```

## Часто задаваемые вопросы

### Какие языки поддерживают умные субтитры

##### Исходные и целевые языки, поддерживаемые типом обработки "Генерация субтитров на основе ASR"

Исходный язык

| № | Язык (исходный язык) | Код |
| --- | --- | --- |
| 1 | Африкаанс (Южная Африка) | af-ZA |
| 2 | Албанский (Албания) | sq-AL |
| 3 | Амхарский (Эфиопия) | am-ET |
| 4 | Арабский (Алжир) | ar-DZ |
| 5 | Арабский (Бахрейн) | ar-BH |
| 6 | Арабский (Египет) | ar-EG |
| 7 | Арабский (Ирак) | ar-IQ |
| 8 | Арабский (Израиль) | ar-IL |
| 9 | Арабский (Иордания) | ar-JO |
| 10 | Арабский (Кувейт) | ar-KW |
| 11 | Арабский (Ливан) | ar-LB |
| 12 | Арабский (Мавритания) | ar-MR |
| 13 | Арабский (Марокко) | ar-MA |
| 14 | Арабский (Оман) | ar-OM |
| 15 | Арабский (Катар) | ar-QA |
| 16 | Арабский (Саудовская Аравия) | ar-SA |
| 17 | Арабский (Государство Палестина) | ar-PS |
| 18 | Арабский (Сирия) | ar-SY |
| 19 | Арабский (Тунис) | ar-TN |
| 20 | Арабский (Объединенные Арабские Эмираты) | ar-AE |
| 21 |

---
*Источник (EN): [smart-subtitle-access-tutorial.md](./smart-subtitle-access-tutorial.md)*
