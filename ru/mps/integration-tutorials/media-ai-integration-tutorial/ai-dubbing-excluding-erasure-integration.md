# Интеграция AI дубляжа (без удаления)

## Обзор функции AI дубляжа

Функция AI дубляжа позволяет заменить исходный дубляж видео на AI-генерируемый дубляж на целевом языке и встроить переведённые субтитры в изображение видео. Для инициирования задачи AI дубляжа необходимо использовать следующие два файла в качестве входных данных:

1. Чистый видеофайл без субтитров исходного языка на изображении видео.
2. Файл субтитров и тегов говорящих (файл Speaker).

Вы также можете напрямую вызвать функцию [Перевод видео на уровне дубляжа](https://www.tencentcloud.com/document/product/1041/74090), ввести видео с исходными субтитрами и выполнить перевод субтитров и дубляжа в один этап, чтобы получить переведённое видео.

> **Примечание:** Подробные сведения о получении чистых видео и файла Speaker см. в [Часто задаваемые вопросы](#QA).

![](https://staticintl.cloudcachetci.com/cms/backend-cms/341b3f15cc3a11f093295254001c06ec.png)

## Инструкции по биллингу

Когда вы инициируете задачу AI дубляжа, вам выставляются счета за AI дубляж (клонированный тембр) и встраивание субтитров. При этом встраивание субтитров является опциональным.

> **Примечание:** Функция AI дубляжа по умолчанию использует клонированный тембр. Возможность стандартного тембра в настоящее время обновляется и доступна только для бета-тестирования. Если вам требуется использовать стандартный тембр, вы можете связаться с отделом продаж для получения поддержки. При использовании стандартного тембра вам выставляются счета за AI дубляж (стандартный тембр) и встраивание субтитров. При этом встраивание субтитров является опциональным.

## Инициирование задачи перевода видео

### Предварительные требования для интеграции

Перед интеграцией AI дубляжа необходимо выполнить следующие предварительные требования для использования Media Processing Service (MPS): зарегистрироваться и войти в учётную запись Tencent Cloud, активировать MPS и предоставить разрешения ролям сервиса.

Для получения подробного руководства см. [Быстрый старт](https://www.tencentcloud.com/document/product/1041/33482). По вопросам авторизации учётной записи см. [Авторизация учётной записи](https://www.tencentcloud.com/document/product/1041/69220).

### Способ 1: Инициирование задачи в консоли

1. Перейдите на страницу [Создание задачи](https://console.tencentcloud.com/mps/tasks/create/vod) в консоли, последовательно укажите путь входного файла, рабочий процесс оркестрирования и выходной путь.
2. В конфигурации оркестрирования выберите узел Media AI - Интеллектуальный анализ.
3. На открывшейся справа странице выберите предустановленный шаблон **32**, включите **Расширенные параметры** в разделе Дополнительные параметры, а затем введите требуемые параметры в ExtendedParameter на основе [Описание ExtendedParameter](#extendedpara) в следующем разделе.

> **Примечание:** Для инициирования задачи AI дубляжа необходимо ввести путь файла субтитров или путь файла Speaker в ExtendedParameter; в противном случае задача не будет выполнена. Консоль MPS автоматически экранирует данные JSON. Вводите данные напрямую и не вводите экранированные строки. В противном случае задача не будет выполнена.

![](https://staticintl.cloudcachetci.com/cms/backend-cms/9e1dc29ccf5911f093295254001c06ec.png)

### Способ 2: Инициирование задачи путём вызова API

Вызовите [API ProcessMedia](https://www.tencentcloud.com/document/product/1041/33640), выберите задачу AiAnalysisTask, установите Definition на **32** (ID предустановленного шаблона) и заполните ExtendedParameter, который является параметром, включающим возможность AI дубляжа. Для значений параметров см. [Описание ExtendedParameter](#extendedpara) в следующем разделе. JSON пример для ProcessMedia выглядит следующим образом:

```
{   "InputInfo":{ //Input video path. Replace it with the path of your original video.      "Type":"URL",      "UrlInputInfo":{         "Url":"https://test-1234567.cos.ap-nanjing.myqcloud.com/mps_test/myvideo.mp4"      }   },   "OutputStorage":{ //Output Cloud Object Storage (COS) bucket. Replace it.      "Type":"COS",      "CosOutputStorage":{         "Bucket":"test",         "Region":"ap-nanjing"      }   },   "OutputDir":"/mps_test/output/",//Output folder path. Replace it.   "AiAnalysisTask":{      "Definition":32, //Preset template ID. Enter 32.      "ExtendedParameter":"{\\"dubbing\\":{\\"speakerUrl\\":\\"https://mycloud.com/path/to/file.json\\"}}" //Required extension parameter. It is used to specify the speaker file path, subtitle style, and other parameters.   },   "TaskNotifyConfig":{ //Event callback notification configuration, which is optional.      "NotifyType":"URL",      "NotifyUrl":"http://www.qq.com/callback"   }}
```

Рекомендуется использовать [API Explorer](https://console.tencentcloud.com/api/explorer?Product=mps&Version=2019-06-12&Action=ProcessMedia) для быстрой проверки. Вы можете скопировать приведённые выше данные JSON в режим JSON в API Explorer, переключиться на режим Form для автоматического анализа, отрегулировать требуемые параметры, такие как пути входа и выхода, а затем нажать **Инициировать вызов**.

В API Explorer позиции ExtendedParameter в режимах ввода Form и JSON выглядят следующим образом:

![](https://staticintl.cloudcachetci.com/cms/backend-cms/35ef669fcea711f084a45254005ef0f7.png)

> **Примечание:** При заполнении значений в поле ExtendedParameter в режиме Form API Explorer необходимо напрямую ввести данные JSON вместо экранирования их в строку. Однако при использовании режима JSON API Explorer или прямого использования API следует ввести экранированную строку. В режиме Form API Explorer введите данные JSON в ExtendedParameter:![](https://staticintl.cloudcachetci.com/cms/backend-cms/4e461e5bcf6111f0b638525400e889b2.png)В режиме JSON API Explorer введите экранированную строку в поле ExtendedParameter. Пример:{\\"dubbing\\":{\\"speakerUrl\\":\\"https://mycloud.com/path/to/file.json\\"}}

## Дополнительные примечания

### Описание ExtendedParameter

`ExtendedParameter` используется для настройки параметров задач AI дубляжа. Все опциональные параметры и их описания указаны ниже:

| Параметр | Тип | Требуется | Описание |
| --- | --- | --- | --- |
| speakerUrl | string | Нет | Необходимо указать либо URL файла Speaker, либо URL субтитров. Подробнее см. в [Формат данных Speaker](#12433bbd-bad0-4b1a-89b6-bfb4ba58bdbb). |
| srcLang | string | Нет | Исходный язык. Опционален при использовании режима speakerUrl. |
| dstLangs | list<string> | Нет | Целевые языки дубляжа. Опционален при использовании режима speakerUrl. |
| subtitleUrls | json | Нет | URL входных субтитров. Необходимо указать это или speakerUrl. |
| subtitleUrls.srcSubtitleUrl | string | Нет | URL исходного субтитра. |
| subtitleUrls.dstSubtitleUrls | json | Нет | URL целевых субтитров, где ключ — язык, значение — URL субтитра. |
| subtitle | json | Нет | Параметры, связанные с выходными субтитрами. |
| subtitle.embed | bool | Нет | Встраивать ли субтитры. Включено по умолчанию. |
| subtitle.style | json | Нет | Стиль субтитров. Действует при включённом встраивании субтитров. |
| subtitle.style.font | string | Нет | Семейство шрифтов. Использует шрифт по умолчанию при пустом значении или "auto". Поддерживаемые шрифты см. в [Структура данных SubtitleTemplate](https://cloud.tencent.com/document/api/862/37615#SubtitleTemplate). |
| subtitle.style.fontSize | float | Нет | Размер шрифта. По умолчанию: 50 px. |
| subtitle.style.marginV | float | Нет | Нижний отступ. По умолчанию: 50 px. |
| outputPattern | string | Нет | Префикс имени выходного файла. Если не указано, по умолчанию "dub", полное имя файла — `dub_{unixtime}.{format}`. |

Пример параметров запроса с использованием speakerUrl:

```
{  	"dubbing": {       "speakerUrl": "https://mycloud.com/path/to/file.json",	// Required. The Speaker file URL.       "subtitle": {          "embed": true,	 // Specify whether to embed subtitles. true by default.          "style": {     // The subtitle style. This parameter is valid only when subtitle embedding is enabled.            "font": "kai.ttf",    // The font. Default value: "kai.tff".            "fontSize": 50,    // The font size. Default value: 50px.            "marginV": 50    // The bottom margin. Default value: 50.          }       },       "outputPattern": "filename" // Optional. The prefix of the output file name.    }}
```

Пример параметров запроса с использованием subtitleUrls:

```
{  	"dubbing": {       "srcLang": "zh",       "dstLangs": ["ja"],       "subtitleUrls": {          "srcSubtitleUrl": "https://test/zh.vtt", // Original-language subtitle URL.          "dstSubtitleUrls": {            "ja": "https://test/ja.vtt" // Target-language subtitle URL.          }       },       "subtitle": {          "embed": true,	// Specify whether to embed subtitles. true by default.          "style": {     // The subtitle style. This parameter is valid only when subtitle embedding is enabled.            "font": "auto", // The font. auto means automatic matching based on subtitle language.            "fontSize": 0.04, // The font size. A value less than 1 represents a percentage.            "marginV": 0.15 // The bottom margin. A value less than 1 represents a percentage.          }       },       "outputPattern": "filename" // Optional. The prefix of the output file name.    }}
```

> **Примечание:** **Длительность одного субтитра в файле Speaker или файле субтитров должна быть не менее 0,15 секунды.**

### Описание файлов Speaker

#### Формат данных

Файл Speaker — это JSON-форматированный файл, содержащий субтитры и соответствующую информацию о говорящих. Его формат данных выглядит следующим образом:

```
{  	"SrcLang": "zh",    "DstLangs": ["en"],    "Speakers": [        {          "Id": "speaker_0",          "Gender": "male"        },        {          "Id": "speaker_1",          "Gender": "female"        }    ],    "Clips": [        {          "TextStartTime": "00:00:00.100",          "TextEndTime": "00:00:00.600",          "SpeakerId": "speaker_0",          "SrcText": "没谁",          "DstTexts": {            "en": "No one"          }        },        {          "TextStartTime": "00:00:01.0",          "TextEndTime": "00:00:01.200",          "SpeakerId": "speaker_1",          "SrcText": "早上好"          "DstTexts": {            "en": "Morning"          }        }    ]}
```

| Параметр | Требуется | Тип | Описание |
| --- | --- | --- | --- |
| SrcLang | Да | string | Исходный язык видео. Подробнее см. в [Поддерживаемые языки](#language). |
| DstLangs | Да | list<string> | Целевой язык для перевода. В настоящее время можно выбрать только один язык. Подробнее см. в [Поддерживаемые языки](#language). |
| Speakers[i].Id | Да | string | ID говорящего. |
| Speakers[i].Gender | Да | string | Пол говорящего. Допустимые значения: male и female. |
| Clips[i].TextStartTime | Да | string | Начальная временная метка фрагмента субтитра. Формат: hh:mm:ss.ms. |
| Clips[i].TextEndTime | Да | string | Конечная временная метка фрагмента субтитра. Формат: hh:mm:ss.ms. |
| Clips[i].SpeakerId | Да | string | ID говорящего, соответствующий фрагменту субтитра. |
| Clips[i].SrcText | Да | string | Исходный язык фрагмента субтитра. |
| Clips[i].DstTexts | Да | map<string,string> | Целевой язык фрагмента субтитра. В настоящее время можно выбрать только один язык. |

#### Примеры изменения файла Speaker

##### Измените неверные теги говорящих (SpeakerId), чтобы избежать перекрытия речи.

![](https://staticintl.cloudcachetci.com/cms/backend-cms/7237be87d98311f0929b525400bf7822.png)

##### Измените слишком короткие временные метки, чтобы избежать чрезмерно быстрой речи при дубляже.

![](https://staticintl.cloudcachetci.com/cms/backend-cms/78ef9185d98311f08250525400454e06.png)

##### Измените перевод, чтобы сделать его более идиоматичным и разговорным.

![](https://staticintl.cloudcachetci.com/cms/backend-cms/7dc23f34d98311f0ab505254001c06ec.png)

### Поддерживаемые языки AI дубляжа

> **Примечание:** Функция AI дубляжа **по умолчанию использует клонированный тембр**. **Возможность стандартного тембра в настоящее время обновляется и доступна только для бета-тестирования**. Если вам требуется использовать стандартный тембр, вы можете связаться с отделом продаж для получения поддержки.

При выборе **AI дубляжа с клонированным тембром** поддерживаются следующие языки.

| Язык | Код | Поддерживается в качестве исходного языка (SrcLang) | Поддерживается в качестве целевого языка (DstLangs) |
| --- | --- | --- | --- |
| Китайский | zh | ✓ | ✓ |
| Английский | en | ✓ | ✓ |
| Японский | ja | ✓ | ✓ |
| Немецкий | de | ✓ | ✓ |
| Французский | fr | ✓ | ✓ |
| Корейский | ko | ✓ | ✓ |
| Русский | ru | ✓ | ✓ |
| Украинский | uk | ✓ | ✓ |
| Португальский | pt | ✓ | ✓ |
| Итальянский | it | ✓ | ✓ |
| Испанский | es | ✓ | ✓ |
| Индонезийский | id | ✓ | ✓ |
| Голландский | nl | ✓ | ✓ |
| Турецкий | tr | ✓ | ✓ |
| Филиппинский | fil | ✓ | ✓ |
| Малайский | ms | ✓ | ✓ |
| Греческий | el | ✓ | ✓ |
| Финский | fi | ✓ | ✓ |
| Хорватский | hr | ✓ | ✓ |
| Словацкий | sk | ✓ | ✓ |
| Польский | pl | ✓ | ✓ |
| Шведский | sv | ✓ | ✓ |
| Хинди | hi | ✓ | ✓ |
| Болгарский | bg | ✓ | ✓ |
| Румынский | ro | ✓ | ✓ |
| Арабский | ar | ✓ | ✓ |
| Чешский | cs | ✓ | ✓ |
| Датский | da | ✓ | ✓ |
| Тамильский | ta | ✓ | ✓ |
| Венгерский | hun | ✓ | ✓ |
| Вьетнамский | vi | ✓ | ✓ |

## Запрос результата задачи

После завершения задачи AI дубляжа в настроенный выходной путь сохраняются и выводятся два типа файлов: обработанный видеофайл и уточненный файл Speaker. Во время дубляжа перевод в исходном файле Speaker упрощается, чтобы обеспечить нормальную скорость дубляжа и предотвратить слишком быстрое звучание речи, что приводит к созданию нового файла Speaker.

### Запрос результата в консоли

1. Вы можете проверить статус задачи на странице [Управление задачами](https://console.tencentcloud.com/mps/tasks/vod-list) в консоли. Когда статус подзадачи — "Успешно", нажмите **Callback JSON**.

![](https://staticintl.cloudcachetci.com/cms/backend-cms/7bf7e991cf6111f0b638525400e889b2.png)

2. Путь выходного файла можно найти в выходном сообщении.

![](https://staticintl.cloudcachetci.com/cms/backend-cms/91ad4a2acf6111f093295254001c06ec.png)

Если в качестве выходного пути используется COS, вы можете найти выходной файл на странице **Управление оркестрированием** > **Bucket COS** > **Выходной bucket** в консоли MPS. Файлы с именами, похожими на "dub-xxx.mp4" или "dub-xxx.json", — это обработанный видеофайл и файл Speaker, созданные после AI дубляжа.

![](https://staticintl.cloudcachetci.com/cms/backend-cms/0d6dd062cf3511f08e5c52540044a08e.png)

### Обратный вызов уведомления о событии

При использовании [ProcessMedia](https://www.tencentcloud.com/document/product/1041/33640) для инициирования задачи обработки мультимедиа вы можете настроить обратный вызов события через параметр TaskNotifyConfig. После завершения обработки задачи результат задачи будет вызван обратно через настроенную информацию обратного вызова. Вы можете анализировать результат уведомления о событии с помощью [ParseNotification](https://www.tencentcloud.com/document/product/1041/33679). Соответствующие структуры данных приведены ниже для справки.

### Запрос результата задачи путём вызова API

После использования [ProcessMedia](https://www.tencentcloud.com/document/product/1041/33640) для инициирования задачи обработки мультимедиа будет возвращён ID задачи (TaskId), например 24000022-WorkflowTask-b20a8exxxxxxx1tt110253 и 24000022-ScheduleTask-774f101xxxxxxx1tt110253. Вызовите API [DescribeTaskDetail](https://www.tencentcloud.com/document/product/1041/33644) и введите ID задачи, чтобы получить результат задачи. Вам необходимо проанализировать поле WorkflowTask ->AiAnalysisResultSet > DubbingTask > Output, чтобы получить результат задачи. Соответствующие структуры данных приведены ниже для справки.

#### Соответствующие структуры данных

- [AiAnalysisTaskDubbingResult](https://www.tencentcloud.com/document/product/1041/33690#aianalysistaskdubbingresult)
- [AiAnalysisTaskDubbingInput](https://www.tencentcloud.com/document/product/1041/33690#AiAnalysisTaskDubbingInput)
- [AiAnalysisTaskDubbingOutput](https://www.tencentcloud.com/document/product/1041/33690#AiAnalysisTaskDubbingOutput)

## Часто задаваемые вопросы

### **Как получить чистые видео?**

Вы можете использовать функцию [Интеллектуальное стирание](https://www.tencentcloud.com/document/product/1041/73595) для удаления субтитров и водяных знаков из видео и получения чистых видео.

### Поддерживается ли ввод видео и выполнение одностадийной обработки, включая удаление субтитров, перевод субтитров, встраивание субтитров и AI дубляж?

Да, это поддерживается. Подробнее см. в [Интеграция перевода видео на уровне дубляжа](https://www.tencentcloud.com/document/product/1041/74090).

### Как создать файл Speaker из файла субтитров SRT/VTT?

MPS предоставляет сценарий [subtitle2speaker.py](https://ie-mps-1258344699.cos-internal.ap-nanjing.tencentcos.cn/common/lauriehuang/dubbing/scripts/subtitle2speaker.py) для преобразования файлов субтитров в файлы Speaker.

Поддерживаются файлы субтитров SRT или VTT. Примеры использования:

- Предоставьте двуязычные файлы субтитров (исходный язык и переведённые субтитры в одном файле).

```
python3 subtitle2speaker.py input.srt output.json --src_lang "zh" --dst_langs "en"
```

- Предоставьте два одноязычных файла субтитров (исходный язык и переведённые субтитры в отдельных файлах).

```
python3 subtitle2speaker.py input_src.vtt input_dst.vtt output.json --src_lang "zh" --dst_langs "en"
```

> **Примечание:** Файлы Speaker, созданные из файлов субтитров SRT/VTT, используют ID говорящего по умолчанию для всех говорящих. Вам необходимо вручную изменить информацию о говорящих; в противном случае качество дубляжа может не соответствовать ожиданиям.

---
*Источник: [https://www.tencentcloud.com/document/product/1041/74378](https://www.tencentcloud.com/document/product/1041/74378)*

---
*Источник (EN): [ai-dubbing-excluding-erasure-integration.md](./ai-dubbing-excluding-erasure-integration.md)*
