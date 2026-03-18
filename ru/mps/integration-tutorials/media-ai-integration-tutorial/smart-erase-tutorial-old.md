# Учебное пособие по функции умного стирания (старая версия)

## Введение в функцию умного стирания

Функция умного стирания позволяет размывать, мозаиковать или беспроблемно обрабатывать такие элементы, как логотипы, субтитры, человеческие лица и номерные знаки в видеоизображениях, что облегчает распространение и совместное использование контента. Функция широко используется в различных областях, таких как платформы коротких драм, платформы коротких видео, электронная коммерция в крест-накрест и независимые медиастудии.

#### Технические преимущества

- Поддержка нескольких сценариев: может автоматически распознавать и обрабатывать более десяти распространенных логотипов. Также может удалять конфиденциальную информацию, такую как водяные знаки, субтитры, человеческие лица и номерные знаки, предлагая несколько эффектов, таких как размытие, мозаика и беспроблемная обработка для удовлетворения требований различных сценариев.
- Высокая степень кастомизации: поддерживает пользовательскую настройку параметров модели для вашего конкретного видеосценария, что улучшает точность и эффект обработки стирания, гарантируя, что окончательно отображаемое изображение более естественно и плавно.

![](https://staticintl.cloudcachetci.com/cms/backend-cms/236e697fc65511ef86f2525400bf7822.png)

#### Демонстрация

1. Перейдите в [Центр опыта](https://mps.live/demo/ai/erase), чтобы перейти на страницу опыта функции умного стирания. На правой стороне выберите либо файл видео в автономном режиме, либо прямую трансляцию, а затем нажмите **Одноклик обработки**.
2. По завершении обработки вы можете просмотреть результаты.

> **Примечание:**Функция демонстрации MPS относительно проста и предназначена только для опыта базового эффекта. Для тестирования полного эффекта используйте доступ к API.

![](https://staticintl.cloudcachetci.com/cms/backend-cms/9fc735be58b911f09c7652540044a08e.png)

## Как инициировать задачу стирания

> **Примечание:**Если задача стирания инициирована через консоль, параметр **ExtendedParameter** не может быть передан, и может быть достигнуто только базовое удаление водяного знака. Поэтому, если вам нужны другие возможности, такие как удаление субтитров или извлечение субтитров на основе OCR, см. следующий текст для инициирования задачи стирания через метод API.

Вызовите [API ProcessMedia](https://www.tencentcloud.com/document/product/1041/33640?lang=en&pg=), выберите задачу **AiAnalysisTask**, установите **Definition** на **25** (идентификатор предустановленного шаблона стирания), заполните **ExtendedParameter** дополнительными параметрами и достигните различных возможностей умного стирания, указав этот параметр. Для значений параметров см. [Примеры передачи параметров API в различных сценариях](https://www.tencentcloud.com/document/product/1041/58269#d887a911-7a40-4e37-a3cc-89a33900d2fd) ниже. JSON пример для **ProcessMedia** выглядит следующим образом:

```
{   "InputInfo":{ //Путь к входному видео. Замените его своим исходным видео.      "Type":"URL",      "UrlInputInfo":{         "Url":"https://test-1234567.cos.ap-nanjing.myqcloud.com/mps_test/myvideo.mp4"      }   },   "OutputStorage":{ //Выходное хранилище COS. Замените его.      "Type":"COS",      "CosOutputStorage":{         "Bucket":"test",         "Region":"ap-nanjing"      }   },   "OutputDir":"/mps_test/output/",//Путь к выходной папке. Замените его.   "AiAnalysisTask":{      "Definition":25, //Идентификатор предустановленного шаблона для умного стирания. Введите 25.      "ExtendedParameter":"{\\"delogo\\":{\\"cluster_id\\":\\"gpu_zhiyan\\",\\"CustomerAppId\\":\\"subtitle_erase_fast\\"}}" //Дополнительные параметры. Замените их при выборе другой возможности стирания.   },   "TaskNotifyConfig":{ //Конфигурация уведомления обратного вызова события, опционально.      "NotifyType":"URL",      "NotifyUrl":"http://www.qq.com/callback"   }}
```

Рекомендуется использовать [API Explorer](https://console.tencentcloud.com/api/explorer?Product=cvm&Version=2017-03-12&Action=DescribeRegions) для быстрой проверки. Вы можете скопировать приведенный выше JSON в режим JSON в API Explorer, переключиться на режим Form для автоматического анализа, отрегулировать необходимые параметры, такие как путь входа и выхода, и нажать **Инициировать вызов**.

В API Explorer позиции ExtendedParameter в режимах ввода Form и JSON выглядят следующим образом:

![](https://staticintl.cloudcachetci.com/cms/backend-cms/c0c8e15158ac11f09c7652540044a08e.png)

> **Примечание:**При использовании режима Form в API Explorer для заполнения ExtendedParameter необходимо передать JSON напрямую без экранирования в строку. Однако при использовании режима JSON API Explorer или прямого использования API следует передать экранированную строку. В режиме Form API Explorer передайте JSON в ExtendedParameter:![](https://staticintl.cloudcachetci.com/cms/backend-cms/f1ecc22c58ac11f09fd0525400bf7822.png)В режиме JSON API Explorer передайте экранированную строку в ExtendedParameter:{\\"delogo\\":{\\"cluster_id\\":\\"gpu_zhiyan\\",\\"CustomerAppId\\":\\"subtitle_erase_fast\\"}}

## Примеры передачи параметров API в различных сценариях

Наиболее часто используемой атомарной возможностью умного стирания является **удаление субтитров**. Для поддержки бизнеса, такого как короткие драмы, выходящие за границу, и перевод видео, он также поддерживает одновременное выполнение:

- **Извлечение и перевод субтитров на основе OCR**: извлечение субтитров и их перевод для создания файлов субтитров на целевом языке.
- **Синтез звука**: ввод видео без перерывов без субтитров и откалиброванного файла субтитров на целевом языке для создания нового видео с дублированием на целевом языке.
- **Встраивание субтитров**: встройте субтитры в видеоизображение.

Кроме того, функция умного стирания также поддерживает:

- **Удаление логотипа**: удаление логотипов на видео.
- **Обработка защиты приватности**: выполнение размытия или мозаики на человеческих лицах и номерных знаках.

Для использования различных возможностей необходимо см. следующий текст для передачи соответствующего **ExtendedParameter**.

### I. Удаление субтитров

#### Инструкции по выставлению счетов

![](https://staticintl.cloudcachetci.com/cms/backend-cms/6a4b4187832511f0ae9d5254001c06ec.png)

Передайте следующий неэкранированный JSON в ExtendedParameter (подробную информацию о полях см. в [Приложении: описание полей ExtendedParameter](/document/product/179424395149918208#1d72953b-1fb8-4cc5-b9c2-a1caf59aa176)).

```
{    "delogo": {        "cluster_id": "gpu_zhiyan",        "CustomerAppId": "subtitle_erase_fast",        "custom_objs": {            "type": 0,            "time_objs": [                {                    "objs": [                        {                            "type": 2,                            "score": 100,                            "rect": {                                "lt_x": 53,                                "lt_y": 228,                                "rb_x": 137,                                "rb_y": 644                            }                        }                    ]                }            ]        }    }}
```

При использовании функции удаления субтитров, включая автоматическое стирание, стирание указанной области и вторичную обработку пропущенных областей, будет взиматься плата за "удаление субтитров" без различия между моделями "Area Edition" и "Standard Edition". Для расценок см. [Инструкции по выставлению счетов для функции умного стирания](https://www.tencentcloud.com/document/product/1041/49204#b71b5f78-d20e-4560-8b9e-a4f02f0d75cf).

> **Примечание:**Поскольку удаление субтитров для выходного видео требует полного кодирования/декодирования видео, выставление счетов будет осуществляться на основе общей продолжительности выходного видео, а не периода стирания, указанного полями `begin_ms` и `end_ms`.

#### 1.1 Удаление субтитров (автоматическое стирание)

Удаление субтитров (автоматическое стирание) относится к автоматическому распознаванию содержимого текста субтитров в видео через модели AI, выполнению беспроблемного стирания и созданию нового видео. Помехи в изображении и специальные стили субтитров могут привести к определенным пропускам или неправильным стираниям, которые могут быть обработаны через [Удаление субтитров (стирание указанной области)](https://www.tencentcloud.com/document/product/1041/58269#subtitleerase-area).

Для использования возможности удаления субтитров (автоматическое стирание) базовая передача **ExtendedParameter** выглядит следующим образом:

Использование режима JSON API Explorer

Использование режима Form API Explorer

![](https://staticintl.cloudcachetci.com/cms/backend-cms/76bbfffc87de11f0814e525400bf7822.png)

Передайте следующую экранированную строку в ExtendedParameter (подробную информацию о полях см. в [Приложении: описание полей ExtendedParameter](https://www.tencentcloud.com/document/product/1041/58269#1d72953b-1fb8-4cc5-b9c2-a1caf59aa176)).

```
{\\"delogo\\":{\\"cluster_id\\":\\"gpu_zhiyan\\",\\"CustomerAppId\\":\\"subtitle_erase_fast\\"}}
```

Полный JSON пример для вызова ProcessMedia для инициирования задачи:

```
{   "InputInfo":{ //Путь к входному видео. Замените его своим исходным видео.      "Type":"URL",      "UrlInputInfo":{         "Url":"https://test-1234567.cos.ap-nanjing.myqcloud.com/mps_test/myvideo.mp4"      }   },   "OutputStorage":{ //Выходное хранилище COS. Замените его.      "Type":"COS",      "CosOutputStorage":{         "Bucket":"test",         "Region":"ap-nanjing"      }   },   "OutputDir":"/mps_test/output/",//Путь к выходной папке. Замените его.   "AiAnalysisTask":{      "Definition":25, //Идентификатор предустановленного шаблона для умного стирания. Введите 25.      "ExtendedParameter":"{\\"delogo\\":{\\"cluster_id\\":\\"gpu_zhiyan\\",\\"CustomerAppId\\":\\"subtitle_erase_fast\\"}}" //Дополнительные параметры. Замените их при выборе другой возможности стирания.   },   "TaskNotifyConfig":{ //Конфигурация уведомления обратного вызова события, опционально.      "NotifyType":"URL",      "NotifyUrl":"http://www.qq.com/callback"   }}
```

![](https://staticintl.cloudcachetci.com/cms/backend-cms/8059eac087de11f0974b52540044a08e.png)

Передайте следующий неэкранированный JSON в ExtendedParameter (подробную информацию о полях см. в [Приложении: описание полей ExtendedParameter](https://www.tencentcloud.com/document/product/1041/58269#1d72953b-1fb8-4cc5-b9c2-a1caf59aa176)).

```
{    "delogo": {        "cluster_id": "gpu_zhiyan",        "CustomerAppId": "subtitle_erase_fast"    }}
```

##### Указание приблизительного положения субтитров и защита видеообласти, не требующей стирания

Функция удаления субтитров автоматически распознает текстовые области в **нижней центральной** части видеоизображения по умолчанию и выполняет стирание в этих областях.

- Если ваше видео похоже на пример ниже и содержит другое текстовое содержимое в нижней центральной части, которое не требует стирания, вы можете использовать параметр `als_filter` для указания приблизительного положения субтитров, чтобы **уменьшить проблемы неправильного стирания**:

![Слева: исходное видео (субтитр "Love You at All Costs" внизу не требует стирания). В центре: использование als_filter для указания эффекта стирания на позицию субтитров. Справа: эффект стирания без указания als_filter.](https://staticintl.cloudcachetci.com/cms/backend-cms/4c4f5ca1475811f0b8185254007c27c5.png)

Использование режима JSON API Explorer

Использование режима Form API Explorer

![](https://staticintl.cloudcachetci.com/cms/backend-cms/8a4c13e487de11f0814e525400bf7822.png)

Передайте следующую экранированную строку в ExtendedParameter (подробную информацию о полях см. в [Приложении: описание полей ExtendedParameter](https://www.tencentcloud.com/document/product/1041/58269#1d72953b-1fb8-4cc5-b9c2-a1caf59aa176)).

```
als_filter:
```

Полный JSON пример для вызова ProcessMedia для инициирования задачи:

```
{   "InputInfo":{ //Путь к входному видео. Замените его своим исходным видео.      "Type":"URL",      "UrlInputInfo":{         "Url":"https://test-1234567.cos.ap-nanjing.myqcloud.com/mps_test/myvideo.mp4"      }   },   "OutputStorage":{ //Выходное хранилище COS. Замените его.      "Type":"COS",      "CosOutputStorage":{         "Bucket":"test",         "Region":"ap-nanjing"      }   },   "OutputDir":"/mps_test/output/",//Путь к выходной папке. Замените его.   "AiAnalysisTask":{      "Definition":25, //Идентификатор предустановленного шаблона для умного стирания. Введите 25.      "ExtendedParameter":"{\\"delogo\\":{\\"cluster_id\\":\\"gpu_zhiyan\\",\\"CustomerAppId\\":\\"subtitle_erase_fast\\",\\"als_filter\\":{\\"active_areas\\":[{\\"lt_x\\":0.097,\\"lt_y\\":0.626,\\"rb_x\\":0.928,\\"rb_y\\":0.705}]}}}" //Дополнительные параметры. Замените их при выборе другой возможности стирания.   },   "TaskNotifyConfig":{ //Конфигурация уведомления обратного вызова события, опционально.      "NotifyType":"URL",      "NotifyUrl":"http://www.qq.com/callback"   }}
```

![](https://staticintl.cloudcachetci.com/cms/backend-cms/93fbb00f87de11f0818a52540099c741.png)

Передайте следующий неэкранированный JSON в ExtendedParameter (подробную информацию о полях см. в [Приложении: описание полей ExtendedParameter](https://www.tencentcloud.com/document/product/1041/58269#1d72953b-1fb8-4cc5-b9c2-a1caf59aa176)).

```
{    "delogo": {        "cluster_id": "gpu_zhiyan",        "CustomerAppId": "subtitle_erase_fast",        "als_filter": {            "active_areas": [                {                    "lt_x": 0.097,                    "lt_y": 0.626,                    "rb_x": 0.928,                    "rb_y": 0.705                }            ]        }    }}
```

- Если вы хотите **автоматически стирать текстовое содержимое во весь экран**, вы можете установить размер области `als_filter` до размера видео во весь экран. См. следующий пример:

Использование режима JSON API Explorer

Использование режима Form API Explorer

![](https://staticintl.cloudcachetci.com/cms/backend-cms/9dc754d687de11f088af5254005ef0f7.png)

Передайте следующую экранированную строку в ExtendedParameter (подробную информацию о полях см. в [Приложении: описание полей ExtendedParameter](https://www.tencentcloud.com/document/product/1041/58269#1d72953b-1fb8-4cc5-b9c2-a1caf59aa176)).

```
als_filter:
```

Полный JSON пример для вызова ProcessMedia для инициирования задачи:

```
{   "InputInfo":{ //Путь к входному видео. Замените его своим исходным видео.      "Type":"URL",      "UrlInputInfo":{         "Url":"https://test-1234567.cos.ap-nanjing.myqcloud.com/mps_test/myvideo.mp4"      }   },   "OutputStorage":{ //Выходное хранилище COS. Замените его.      "Type":"COS",      "CosOutputStorage":{         "Bucket":"test",         "Region":"ap-nanjing"      }   },   "OutputDir":"/mps_test/output/",//Путь к выходной папке. Замените его.   "AiAnalysisTask":{      "Definition":25, //Идентификатор предустановленного шаблона для умного стирания. Введите 25.      "ExtendedParameter":"{\\"delogo\\":{\\"cluster_id\\":\\"gpu_zhiyan\\",\\"CustomerAppId\\":\\"subtitle_erase_fast\\",\\"als_filter\\":{\\"active_areas\\":[{\\"lt_x\\":0,\\"lt_y\\":0,\\"rb_x\\":0.9999,\\"rb_y\\":0.9999}]}}}" //Дополнительные параметры. Замените их при выборе другой возможности стирания.   },   "TaskNotifyConfig":{ //Конфигурация уведомления обратного вызова события, опционально.      "NotifyType":"URL",      "NotifyUrl":"http://www.qq.com/callback"   }}
```

![](https://staticintl.cloudcachetci.com/cms/backend-cms/a737321f87de11f0818a52540099c741.png)

Передайте следующий неэкранированный JSON в ExtendedParameter (подробную информацию о полях см. в [Приложении: описание полей ExtendedParameter](https://www.tencentcloud.com/document/product/1041/58269#1d72953b-1fb8-4cc5-b9c2-a1caf59aa176)).

```
{    "delogo": {            "cluster_id": "gpu_zhiyan",        "CustomerAppId": "subtitle_erase_fast",        "als_filter": {            "active_areas": [                {                    "lt_x": 0,                    "lt_y": 0,                    "rb_x": 0.9999,                    "rb_y": 0.9999                }            ]        }    }}
```

#### 1.2 Удаление субтитров (стирание указанной области)

Обычно удаление субтитров (автоматическое стирание) может автоматически и точно распознавать положение субтитров. Но в конкретных случаях могут возникнуть пропуски, как показано на рисунке ниже:

![Слева: субтитр в красном прямоугольнике имеет слишком низкий контраст фона. Справа: стиль субтитра является курсивом с эффектом градиента.](https://staticintl.cloudcachetci.com/cms/backend-cms/4c0651e3475811f09bd9525400454e06.png)

Поэтому, если положение вашего субтитра фиксировано, рекомендуется использовать `custom_objs` для прямого указания области стирания, чтобы максимально уменьшить пропуски.

> **Примечание:**После того, как `custom_objs` указан, система напрямую сотрет выбранную область без автоматического распознавания или стирания текста в других частях видео. Поэтому вы должны полностью передать целевую область стирания.

Пример:

![Слева: исходное видео. В центре: зеленый прямоугольник представляет область стирания, указанную custom_objs. Справа: эффект стирания.](https://staticintl.cloudcachetci.com/cms/backend-cms/4db1d87c475811f0bb6952540099c741.png)

Использование режима JSON API Explorer

Использование режима Form API Explorer

![](https://staticintl.cloudcachetci.com/cms/backend-cms/b03b8ff487de11f0b321525400e889b2.png)

Передайте следующую экранированную строку в ExtendedParameter (подробную информацию о полях см. в [Приложении: описание полей ExtendedParameter](https://www.tencentcloud.com/document/product/1041/58269#1d72953b-1fb8-4cc5-b9c2-a1caf59aa176)).

```
{\\"delogo\\":{\\"cluster_id\\":\\"gpu_zhiyan\\",\\"CustomerAppId\\":\\"subtitle_erase_fast\\",\\"custom_objs\\":{\\"type\\":0,\\"time_objs\\":[{\\"objs\\":[{\\"type\\":2,\\"score\\":100,\\"rect\\":{\\"lt_x\\":53,\\"lt_y\\":228,\\"rb_x\\":137,\\"rb_y\\":644}}]}]}}}/*Вы можете указать несколько областей стирания (не рекомендуется превышать 10 областей).(lt_x,lt_y) - координата верхней левой точки области стирания, а (rb_x,rb_y) - координата нижней правой точки. Значение координаты:            [0, 1): представляет процент ширины или высоты видео.            [1, +): представляет пиксели.*/
```

Полный JSON пример для вызова ProcessMedia для инициирования задачи:

```
{   "InputInfo":{ //Путь к входному видео. Замените его своим исходным видео.      "Type":"URL",      "UrlInputInfo":{         "Url":"https://test-1234567.cos.ap-nanjing.myqcloud.com/mps_test/myvideo.mp4"      }   },   "OutputStorage":{ //Выходное хранилище COS. Замените его.      "Type":"COS",      "CosOutputStorage":{         "Bucket":"test",         "Region":"ap-nanjing"      }   },   "OutputDir":"/mps_test/output/",//Путь к выходной папке. Замените его.   "AiAnalysisTask":{      "Definition":25, //Идентификатор предустановленного шаблона для умного стирания. Введите 25.      "ExtendedParameter":"{\\"delogo\\":{\\"cluster_id\\":\\"gpu_zhiyan\\",\\"CustomerAppId\\":\\"subtitle_erase_fast\\",\\"custom_objs\\":{\\"type\\":0,\\"time_objs\\":[{\\"objs\\":[{\\"type\\":2,\\"score\\":100,\\"rect\\":{\\"lt_x\\":53,\\"lt_y\\":228,\\"rb_x\\":137,\\"rb_y\\":644}}]}]}}}" //Дополнительные параметры. Замените их при выборе другой возможности стирания.   },   "TaskNotifyConfig":{ //Конфигурация уведомления обратного вызова события, опционально.      "NotifyType":"URL",      "NotifyUrl":"http://www.qq.com/callback"   }}
```

![](https://staticintl.cloudcachetci.com/cms/backend-cms/b961744987de11f0818a52540099c741.png)

Передайте следующий неэкранированный JSON в ExtendedParameter (подробную информацию о полях см. в [Приложении: описание полей ExtendedParameter](https://www.tencentcloud.com/document/product/1041/58269#1d72953b-1fb8-4cc5-b9c2-a1caf59aa176)).

```
{    "delogo": {        "cluster_id": "gpu_zhiyan",        "CustomerAppId": "subtitle_erase_fast",        "custom_objs": {            "type": 0,            "time_objs": [                {                    "objs": [                        {                            "type": 2,                            "score": 100,                            "rect": {                                "lt_x": 53,                                "lt_y": 228,                                "rb_x": 137,                                "rb_y": 644                            }                        }                    ]                }            ]        }    }}
```

#### 1.3 Ориентирование на субтитры специального стиля

Удаление субтитров предоставляет две редакции модели, подходящие для разных стилей субтитров:

- Standard Edition (рекомендуется): обычно рекомендуется эта редакция. Она подходит для видео со стандартными стилями субтитров с лучшей эффективностью беспроблемной обработки и превосходной восстановлением деталей.

Если `subtitle_erase_fast` передается в `CustomerAppId`, это означает использование "Standard Edition".

![Слева: исходное видео. В центре: эффект обработки редакции Area. Справа: эффект обработки редакции Standard. Если стиль субтитров в вашем видео похож на этот пример, выберите Standard Edition.](https://staticintl.cloudcachetci.com/cms/backend-cms/4dff1080475811f0a2a8525400e889b2.png)

- Area Edition: подходит для субтитров специального стиля (таких как фоновая тень, курсивные шрифты и динамические эффекты), с большей областью стирания, но менее беспроблемный эффект, чем Standard Edition.

Для указания "Area Edition" передайте `subtitle_erase_area` в `CustomerAppId`. Например:

![Слева: исходное видео. В центре: зеленый прямоугольник представляет область стирания, указанную custom_objs. Справа: эффект стирания (из-за специального стиля субтитра используется модель удаления субтитров Area Edition).](https://staticintl.cloudcachetci.com/cms/backend-cms/4cfd2178475811f0b8185254007c27c5.png)

Использование режима JSON API Explorer

Использование режима Form API Explorer

![](https://staticintl.cloudcachetci.com/cms/backend-cms/ca8ca1d587de11f0818a52540099c741.png)

Передайте следующую экранированную строку в ExtendedParameter (подробную информацию о полях см. в [Приложении: описание полей ExtendedParameter](https://www.tencentcloud.com/document/product/1041/58269#1d72953b-1fb8-4cc5-b9c2-a1caf59aa176)).

```
{\\"delogo\\":{\\"cluster_id\\":\\"gpu_zhiyan\\",\\"CustomerAppId\\":\\"subtitle_erase_area\\",\\"custom_objs\\":{\\"

```
{   "InputInfo":{ //Путь входного видео. Замените на ваше исходное видео.      "Type":"URL",      "UrlInputInfo":{         "Url":"https://test-1234567.cos.ap-nanjing.myqcloud.com/mps_test/myvideo.mp4"      }   },   "OutputStorage":{ //Бакет COS для вывода. Замените его.      "Type":"COS",      "Type":"COS",      "CosOutputStorage":{         "Bucket":"test",         "Region":"ap-nanjing"      }   },   "OutputDir":"/mps_test/output/",//Путь папки вывода. Замените его.   "AiAnalysisTask":{      "Definition":25, //ID шаблона предустановки для интеллектуального удаления. Введите 25.      "ExtendedParameter":"{\\"delogo\\":{\\"cluster_id\\":\\"gpu_zhiyan\\",\\"CustomerAppId\\":\\"subtitle_logo_erase\\",\\"als_filter\\":{\\"active_areas\\":[{\\"type\\":2,\\"lt_x\\":0.106,\\"lt_y\\":0.733,\\"rb_x\\":0.901,\\"rb_y\\":0.825},{\\"type\\":2,\\"lt_x\\":0.612,\\"lt_y\\":0.911,\\"rb_x\\":0.988,\\"rb_y\\":0.984}]}}}"  //Дополнительные параметры. Замените их при выборе другой функции удаления.   },   "TaskNotifyConfig":{ //Конфигурация уведомления обратного вызова события, опционально.      "NotifyType":"URL",      "NotifyType":"URL",      "NotifyUrl":"http://www.qq.com/callback"   }}
```

![](https://staticintl.cloudcachetci.com/cms/backend-cms/0710fce087de11f0974b52540044a08e.png)

Передайте следующий неэкранированный JSON в ExtendedParameter (подробности полей см. в [Приложение: Описание полей ExtendedParameter](https://www.tencentcloud.com/document/product/1041/58269#1d72953b-1fb8-4cc5-b9c2-a1caf59aa176)).

```
{    "delogo": {        "als_filter": {            "active_areas": [                {                    "type": 1,                    "lt_x": 527,                    "lt_y": 13,                    "rb_x": 701,                    "rb_y": 78                }            ]        }    }}{  "delogo": {    "cluster_id": "gpu_zhiyan",    "CustomerAppId": "subtitle_logo_erase",    "als_filter": {      "active_areas": [        {          "type": 2,//Для удаления субтитров установите тип 2          "lt_x": 0.106,          "lt_y": 0.733,          "rb_x": 0.901,          "rb_y": 0.824        },        {          "type": 2,//Для удаления субтитров установите тип 2          "lt_x": 0.612,          "lt_y": 0.911,          "rb_x": 0.988,          "rb_y": 0.984        }      ]    }  }}
```

- Для **немейнстримовых интернет-логотипов**, не предварительно обученных в библиотеках моделей MPS, выполняйте следующее:
  - Динамическое позиционирование логотипа: требует обучения модели для удаления, что будет влечь дополнительные комиссии за обучение.
  - Фиксированное позиционирование логотипа: укажите область удаления напрямую через `custom_objs` для удаления без дополнительных комиссий. Пример:

Использование JSON режима API Explorer

Использование режима Form API Explorer

![](https://staticintl.cloudcachetci.com/cms/backend-cms/12af0e5e87de11f0818a52540099c741.png)

Передайте следующую экранированную строку в ExtendedParameter (подробности полей см. в [Приложение: Описание полей ExtendedParameter](https://www.tencentcloud.com/document/product/1041/58269#1d72953b-1fb8-4cc5-b9c2-a1caf59aa176)).

```
{\\"delogo\\":{\\"cluster_id\\":\\"gpu_zhiyan\\",\\"CustomerAppId\\":\\"subtitle_logo_erase\\",\\"custom_objs\\":{\\"type\\":0,\\"time_objs\\":[{\\"objs\\":[{\\"type\\":1,\\"value\\":\\"customobjs\\",\\"score\\":100,\\"rect\\":{\\"lt_x\\":0.024,\\"lt_y\\":0.027,\\"rb_x\\":0.14,\\"rb_y\\":0.198}}]}]}}}
```

Полный пример JSON для вызова ProcessMedia для запуска задачи:

```
{   "InputInfo":{ //Путь входного видео. Замените на ваше исходное видео.      "Type":"URL",      "UrlInputInfo":{         "Url":"https://test-1234567.cos.ap-nanjing.myqcloud.com/mps_test/myvideo.mp4"      }   },   "OutputStorage":{ //Бакет COS для вывода. Замените его.      "Type":"COS",      "CosOutputStorage":{         "Bucket":"test",         "Region":"ap-nanjing"      }   },   "OutputDir":"/mps_test/output/",//Путь папки вывода. Замените его.   "AiAnalysisTask":{      "Definition":25, //ID шаблона предустановки для интеллектуального удаления. Введите 25.      "ExtendedParameter":"{\\"delogo\\":{\\"cluster_id\\":\\"gpu_zhiyan\\",\\"CustomerAppId\\":\\"subtitle_logo_erase\\",\\"custom_objs\\":{\\"type\\":0,\\"time_objs\\":[{\\"objs\\":[{\\"type\\":1,\\"value\\":\\"customobjs\\",\\"score\\":100,\\"rect\\":{\\"lt_x\\":0.024,\\"lt_y\\":0.027,\\"rb_x\\":0.14,\\"rb_y\\":0.198}}]}]}}}"  //Дополнительные параметры. Замените их при выборе другой функции удаления.   },   "TaskNotifyConfig":{ //Конфигурация уведомления обратного вызова события, опционально.      "NotifyType":"URL",      "NotifyUrl":"http://www.qq.com/callback"   }}
```

![](https://staticintl.cloudcachetci.com/cms/backend-cms/2042859487de11f0814e525400bf7822.png)

Передайте следующий неэкранированный JSON в ExtendedParameter (подробности полей см. в [Приложение: Описание полей ExtendedParameter](https://www.tencentcloud.com/document/product/1041/58269#1d72953b-1fb8-4cc5-b9c2-a1caf59aa176)).

```
{  "delogo": {    "cluster_id": "gpu_zhiyan",    "CustomerAppId": "subtitle_logo_erase",    "custom_objs": {      "type": 0,      "time_objs": [        {          "objs": [            {              "type": 1,//Для удаления водяного знака установите тип 1              "value": "customobjs",              "score": 100,              "rect": {                "lt_x": 0.024,                "lt_y": 0.027,                "rb_x": 0.14,                "rb_y": 0.198              }            }          ]        }      ]    }  }}
```

### VII. Обработка защиты конфиденциальности (лица и номерные знаки)

#### Инструкции по выставлению счетов

Если вы используете функцию обработки защиты конфиденциальности, взимается плата за "Обработку защиты конфиденциальности (лица и номерные знаки)". Для получения прайс-листа см. инструкции по выставлению счетов в [Интеллектуальное удаление](https://www.tencentcloud.com/document/product/1041/49204?lang=zh&pg=#b71b5f78-d20e-4560-8b9e-a4f02f0d75cf).

#### 7.1 Обработка человеческих лиц

Выполняет размытие или мозаичную обработку и создает новое видео после распознавания человеческих лиц в видеоизображении.

##### Эффект размытия

![Левый рисунок: исходное видеоизображение. Правый рисунок: размытие лица.](https://staticintl.cloudcachetci.com/cms/backend-cms/4de65d36475811f0afa1525400bf7822.png)

Использование JSON режима API Explorer

Использование режима Form API Explorer

![](https://staticintl.cloudcachetci.com/cms/backend-cms/310b315b87de11f0818a52540099c741.png)

Передайте следующую экранированную строку в ExtendedParameter (подробности полей см. в [Приложение: Описание полей ExtendedParameter](https://www.tencentcloud.com/document/product/1041/58269#1d72953b-1fb8-4cc5-b9c2-a1caf59aa176)).

```
{\\"delogo\\":{\\"CustomerAppId\\":\\"facial_blur\\"}}
```

Полный пример JSON для вызова ProcessMedia для запуска задачи:

```
{   "InputInfo":{ //Путь входного видео. Замените на ваше исходное видео.      "Type":"URL",      "UrlInputInfo":{         "Url":"https://test-1234567.cos.ap-nanjing.myqcloud.com/mps_test/myvideo.mp4"      }   },   "OutputStorage":{ //Бакет COS для вывода. Замените его.      "Type":"COS",      "CosOutputStorage":{         "Bucket":"test",         "Region":"ap-nanjing"      }   },   "OutputDir":"/mps_test/output/",//Путь папки вывода. Замените его.   "AiAnalysisTask":{      "Definition":25, //ID шаблона предустановки для интеллектуального удаления. Введите 25.      "ExtendedParameter":"{\\"delogo\\":{\\"CustomerAppId\\":\\"facial_blur\\"}" //Дополнительные параметры. Замените их при выборе другой функции удаления.   },   "TaskNotifyConfig":{ //Конфигурация уведомления обратного вызова события, опционально.      "NotifyType":"URL",      "NotifyUrl":"http://www.qq.com/callback"   }}
```

![](https://staticintl.cloudcachetci.com/cms/backend-cms/3d7880c487de11f0b321525400e889b2.png)

Передайте следующий неэкранированный JSON в ExtendedParameter (подробности полей см. в [Приложение: Описание полей ExtendedParameter](https://www.tencentcloud.com/document/product/1041/58269#1d72953b-1fb8-4cc5-b9c2-a1caf59aa176)).

```
{    "delogo": {        "CustomerAppId": "facial_blur"    }}
```

##### Мозаичный эффект

![Левый рисунок: исходное видеоизображение. Правый рисунок: обработанные человеческие лица с мозаикой.](https://staticintl.cloudcachetci.com/cms/backend-cms/4d171792475811f0a5a752540044a08e.png)

Использование JSON режима API Explorer

Использование режима Form API Explorer

![](https://staticintl.cloudcachetci.com/cms/backend-cms/4829ad4587de11f0b321525400e889b2.png)

Передайте следующую экранированную строку в ExtendedParameter (подробности полей см. в [Приложение: Описание полей ExtendedParameter](https://www.tencentcloud.com/document/product/1041/58269#1d72953b-1fb8-4cc5-b9c2-a1caf59aa176)).

```
{\\"delogo\\":{\\"CustomerAppId\\":\\"facial_mosaic\\"}}
```

Полный пример JSON для вызова ProcessMedia для запуска задачи:

```
{   "InputInfo":{ //Путь входного видео. Замените на ваше исходное видео.      "Type":"URL",      "UrlInputInfo":{         "Url":"https://test-1234567.cos.ap-nanjing.myqcloud.com/mps_test/myvideo.mp4"      }   },   "OutputStorage":{ //Бакет COS для вывода. Замените его.      "Type":"COS",      "CosOutputStorage":{         "Bucket":"test",         "Region":"ap-nanjing"      }   },   "OutputDir":"/mps_test/output/",//Путь папки вывода. Замените его.   "AiAnalysisTask":{      "Definition":25, //ID шаблона предустановки для интеллектуального удаления. Введите 25.      "ExtendedParameter":"{\\"delogo\\":{\\"CustomerAppId\\":\\"facial_mosaic\\"}}" //Дополнительные параметры. Замените их при выборе другой функции удаления.   },   "TaskNotifyConfig":{ //Конфигурация уведомления обратного вызова события, опционально.      "NotifyType":"URL",      "NotifyUrl":"http://www.qq.com/callback"   }}
```

![](https://staticintl.cloudcachetci.com/cms/backend-cms/52c5de9f87de11f0974b52540044a08e.png)

Передайте следующий неэкранированный JSON в ExtendedParameter (подробности полей см. в [Приложение: Описание полей ExtendedParameter](https://www.tencentcloud.com/document/product/1041/58269#1d72953b-1fb8-4cc5-b9c2-a1caf59aa176)).

```
{    "delogo": {        "CustomerAppId": "facial_mosaic"    }}
```

#### 7.2 Одновременная обработка лиц и номерных знаков

Одновременно выполняет размытие или мозаичную обработку и создает новое видео после распознавания человеческих лиц и номерных знаков в видеоизображении.

##### Эффект размытия

Функция находится на этапе бета-тестирования. Свяжитесь с нами для получения поддержки, если вам нужно протестировать опыт.

##### Мозаичный эффект

![Левый рисунок: исходное видеоизображение. Правый рисунок: человеческие лица и номерные знаки с мозаикой.](https://staticintl.cloudcachetci.com/cms/backend-cms/4d621de0475811f09bd9525400454e06.png)

Использование JSON режима API Explorer

Использование режима Form API Explorer

![](https://staticintl.cloudcachetci.com/cms/backend-cms/5ce55dfd87de11f0ae9d5254001c06ec.png)

Передайте следующую экранированную строку в ExtendedParameter (подробности полей см. в [Приложение: Описание полей ExtendedParameter](https://www.tencentcloud.com/document/product/1041/58269#1d72953b-1fb8-4cc5-b9c2-a1caf59aa176)).

```
{\\"delogo\\":{\\"CustomerAppId\\":\\"facial_and_numberplate_mosaic_v2\\"}}
```

Полный пример JSON для вызова ProcessMedia для запуска задачи:

```
{   "InputInfo":{ //Путь входного видео. Замените на ваше исходное видео.      "Type":"URL",      "UrlInputInfo":{         "Url":"https://test-1234567.cos.ap-nanjing.myqcloud.com/mps_test/myvideo.mp4"      }   },   "OutputStorage":{ //Бакет COS для вывода. Замените его.      "Type":"COS",      "CosOutputStorage":{         "Bucket":"test",         "Region":"ap-nanjing"      }   },   "OutputDir":"/mps_test/output/",//Путь папки вывода. Замените его.   "AiAnalysisTask":{      "Definition":25, //ID шаблона предустановки для интеллектуального удаления. Введите 25.      "ExtendedParameter":"{\\"delogo\\":{\\"CustomerAppId\\":\\"facial_and_numberplate_mosaic_v2\\"}}" //Дополнительные параметры. Замените их при выборе другой функции удаления.   },   "TaskNotifyConfig":{ //Конфигурация уведомления обратного вызова события, опционально.      "NotifyType":"URL",      "NotifyUrl":"http://www.qq.com/callback"   }}
```

![](https://staticintl.cloudcachetci.com/cms/backend-cms/69243ea887de11f084bd5254007c27c5.png)

Передайте следующий неэкранированный JSON в ExtendedParameter (подробности полей см. в [Приложение: Описание полей ExtendedParameter](https://www.tencentcloud.com/document/product/1041/58269#1d72953b-1fb8-4cc5-b9c2-a1caf59aa176)).

```
{    "delogo": {        "CustomerAppId": "facial_and_numberplate_mosaic_v2"    }}
```

### Приложение: Описание полей ExtendedParameter

Все поля, поддерживаемые **ExtendedParameter**, и их описания следующие:

```
"delogo":{    "CustomerAppId": "subtitle_extract",  # String, параметр предустановленного сценария. Различные сценарии могут использовать только некоторые параметры ниже. Обычно требуется внутреннее подтверждение для изменения параметров.    "cluster_id": "",             # String, зарезервированное поле, используемое для планирования кластера по политикам. Конкретная задача должна выполняться на конкретном кластере, поэтому ее нельзя изменять небрежно.    "output_patten": "{task_type}-{session_id}",   # String, имя файла вывода, без специальных символов. Длина должна быть меньше 200, идентификатор — {}, а заполнитель может быть task_type и session_id.    "als_filter": {            # JSON объект, целевая проверка и фильтр анализа.            "min_ocr_height": 10,   # Float, действительно, если больше или равно 0. Для распознавания символов: минимальный размер текста. Примечание: значение меньше или равно 1 представляет отношение высоты видео, а значение больше 1 представляет пиксели.            "max_ocr_height": 0.06, # Float, действительно, если больше или равно 0. Для распознавания символов: максимальный размер текста.            "active_areas": [       # JSON массив. Результат распознавания принимается только, если его центральная точка находится в этой области через фильтрацию области.                {                    "lt_x": 0.1,  # Float, действительно, если больше или равно 0. X-координата верхнего левого угла области. Примечание: значение меньше или равно 1 представляет отношение, а значение больше 1 представляет пиксели.                    "lt_y": 0.6,  # Float, действительно, если больше или равно 0. Y-координата верхнего левого угла области.                    "rb_x": 0.9,  # Float, действительно, если больше или равно 0. X-координата нижнего правого угла области.                    "rb_y": 0.95  # Float, действительно, если больше или равно 0. Y-координата нижнего правого угла области.                }            ]        },     "custom_objs": { # JSON объект, пользовательская область.            "type": 0,   # Int, введите 0. Указанный тип.         "time_objs": [# JSON массив, информация о временной области.                {                    "begin_ms": 0,  # Int, начальное время в миллисекундах. Если оставить пусто, то же самое, что и начало видео.                    "end_ms": 100,  # Int, конечное время в миллисекундах. Если оставить пусто, то же самое, что и конец видео.                    "objs": [ # JSON массив, информация области.                        {                            "rect": { # JSON объект, целевая область.                                "lt_x": 55,  # Float, действительно, если больше или равно 0. X-координата верхнего левого угла области. Примечание: значение меньше 1 представляет отношение, а значение больше или равно 1 представляет пиксели.                                "lt_y": 143, # Float, действительно, если больше или равно 0. Y-координата верхнего левого угла области.                                "rb_x": 327, # Float, действительно, если больше или равно 0. X-координата нижнего правого угла области.                                "rb_y": 192  # Float, действительно, если больше или равно 0. Y-координата нижнего правого угла области.                            },                            "score": 100,  # Int, введите 100 здесь. Целевая оценка значимости.                            "type": 2,     # Int, целевой тип. 1 представляет такие целевые объекты как логотипы, а 2 представляет текст.                            "value": "LUSN" # String, целевое значение. Например, введите соответствующий текст для распознавания символов.                        }                    ]                }            ]           }    "subtitle_param" : {   # JSON объект, параметры, связанные с субтитрами.        "margin_bottom": 0.2,  # Float, действительно, если больше или равно 0. Используется для отрисовки файла субтитров. Расстояние субтитра от дна: меньше или равно 1 представляет отношение высоты видео, а больше 1 представляет пиксели.        "font_size": 50,       # Float, действительно, если больше или равно 0. Используется для отрисовки файла субтитров. Размер шрифта отрисовки субтитров: меньше или равно 1 представляет отношение высоты видео, а больше 1 представляет пиксели.        "font_type": "simkai", # String. Шрифт отрисовки субтитров: simkai представляет KaiTi, hei представляет SimHei, и song представляет SimSun.        "translate_dst_language": "en"  # String, используется для перевода субтитров. Если установлено значение пусто, перевод не будет выполнен, и будут выведены только исходные субтитры. Соответствующие отношения для других значений: en-английский, zh-китайский, ja-японский, ko-корейский, de-немецкий, pt-португальский, id-индонезийский, th-тайский и ms-малайский. Вышеуказанное — это просто список часто используемых языков. Мы поддерживаем перевод на сотни языков. Свяжитесь с нами, чтобы получить полный список.    }}
```

## Часто задаваемые вопросы

### Могут ли субтитры быть созданы на основе ASR?

Да. Вы можете использовать функцию интеллектуальных субтитров для достижения этой цели. Подробнее см. [Tutorial on Smart Subtitle Access](https://www.tencentcloud.com/document/product/1041/54517).

В сценарии удаления исходное видео обычно поставляется с исходными субтитрами. Использование OCR для извлечения субтитров дает лучшие и более точные результаты. Поэтому функция интеллектуального удаления интегрирует только возможности OCR.

### Могут ли функции встроенных субтитров и внешних субтитров использоваться отдельно?

Встроение субтитров или использование внешних субтитров без удаления можно реализовать через функцию транскодирования аудио/видео. Подробнее см. [Subtitle Embedding](https://www.tencentcloud.com/document/product/1041/70464#8aad65a1-9588-4230-94fe-e352f675b27a) и [External Subtitles](https://www.tencentcloud.com/document/product/1041/70464#7680e1c7-6c55-4ef2-bd27-70fa21d5efb3) в разделе Audio/Video Transcoding Integration.

### Как объединить существующий аудиофайл с видеофайлом для создания нового видео?

##### Бизнес-сценарий:

Файл с синтезированным речью AI был создан другими методами. Требуется разделить голос и фоновый звук в видео, затем объединить синтезированную речь AI с фоновым звуком и заменить аудио исходного видео.

##### Решение:

Для разделения голоса и фонового звука вы можете создать задачу улучшения аудио/видео в консоли и включить функцию разделения аудио. После инициирования задачи вы получите файл фонового звука.

![](https://staticintl.cloudcachetci.com/cms/backend-cms/ca5d29785bd711f095485254005ef0f7.png)

Затем вызовите API [Video Editing](https://www.tencentcloud.com/document/product/1041/37460) и выберите задачу синтеза для объединения синтезированной речи AI и фонового звука с видео и создания нового видео. Пример JSON приведен ниже:

```
POST / HTTP/1.1Host: mps.tencentcloudapi.comContent-Type: application/jsonX-TC-Action: EditMedia<Common request parameters>{    "FileInfos": [//Input the information of the file that requires synthesis.        {            "InputInfo": {//Input video path.                "Type": "URL",                "UrlInputInfo": {                    "Url": "https://test.cos.ap-nanjing.myqcloud.com/MPS/sourcevideo.mp4"                }            },            "Id": "SOURCE_VIDEO"        },        {            "InputInfo": {//Input voice path.                "Type": "URL",                "UrlInputInfo": {                    "Url": "https://test.cos.ap-nanjing.myqcloud.com/MPS/voices.mp3"                }            },            "Id": "AUDIO_VOICES"        },        {            "InputInfo": {//Input background sound path.                "Type": "URL",                "UrlInputInfo": {                    "Url": "https://test.cos.ap-nanjing.myqcloud.com/MPS/background.mp3"                }            },            "Id": "AUDIO_BACKGROUND"        }    ],    "OutputStorage": { //Output COS directory.        "Type": "COS",        "CosOutputStorage": {            "Bucket": "test",            "Region": "ap-nanjing"        }    },    "OutputObjectPath": "/editmedia/compose/final_video.{format}",//Output folder path and filename definition.    "ComposeConfig": {        "TargetInfo": {//Output video parameters.            "Container": "mp4",            "RemoveVideo": 0,            "RemoveAudio": 0,            "VideoStream": {                "Codec": "H.264",                "Fps": 18            },            "AudioStream": {                "Codec": "AAC",                "SampleRate": 32000,                "AudioChannel": 1            }        },        "Tracks": [//Track information.            {                "Type": "Video",//Track 1, video.                "Items": [                    {                        "Type": "Video",                        "Video": {                            "SourceMedia": {                                "FileId": "SOURCE_VIDEO"                            },                            "AudioOperations": [                                {                                    "Type": "Volume",                                    "Volume": 0 //Mute the original audio in the video.                                }                            ]                        }                    }                ]            },            {                "Type": "Audio",//Track 2, voice.                "Items": [                    {                        "Type": "Audio",                        "Audio": {                            "SourceMedia": {                                "FileId": "AUDIO_VOICES"                            },                            "TrackTime": {                                "Duration": "10s" //Track duration, same as the SourceMedia duration if left blank.                            },                            "AudioOperations": [                                {                                    "Type": "Volume",                                    "Volume": 5 //Volume configuration.                                }                            ]                        }                    }                ]            },            {                "Type": "Audio",//Track 3, background sound.                "Items": [                    {                        "Type": "Audio",                        "Audio": {                            "SourceMedia": {                                "FileId": "AUDIO_BACKGROUND"                            },                            "TrackTime": {                                "Duration": "10s" //Track duration, same as the SourceMedia duration if left blank.                            },                            "AudioOperations": [                                {                                    "Type": "Volume",                                    "Volume": 5 //Volume configuration.                                }                            ]                        }                    }                ]            }        ]    }}
```

### Какие логотипы поддерживаются функцией удаления логотипа?

В настоящее время мы поддерживаем автоматическое распознавание и удаление более десяти логотипов. Для логотипов, не входящих в поддерживаемый диапазон, мы также предлагаем услуги индивидуального обучения модели, которые взимаются отдельно в виде платы за обучение модели.

Если позиция логотипа фиксирована, вы также можете обработать его, указав область удаления без дополнительной платы за обучение модели.

### Взимаются ли сборы за видео без логотипа?

Да. Служба по-прежнему выполняет распознавание, даже если в видео нет логотипа, что также потребляет вычислительные ресурсы.

### Поддерживается ли потоковая трансляция?

В настоящее время внешние API поддерживают только файлы VOD. Если у вас есть потребность в обработке потоковой трансляции, свяжитесь с разработчиками.

### Как указать имя файла удаления вывода?

Вы можете указать имя файла вывода с помощью параметра **output_patten** в дополнительных параметрах.

Идентификатор заполнителя — это `{}`, и заполнитель может быть `task_type` и `session_id`. Вывод по умолчанию — `{task_type}-{session_id}`.

Пример использования:

```

```

### Поддерживает ли Smart Erase автоматическое срабатывание COS?

Шаблон smart erase находится в разработке и планируется запуск в консоли к июлю 2025 года. В этот момент вы сможете настроить оркестровку и включить автоматическое срабатывание через консоль.

В настоящее время, если у вас есть требование автоматического срабатывания, свяжитесь с нами для автономной конфигурации. Благодарим вас за понимание.


---
*Источник: [https://www.tencentcloud.com/document/product/1041/58269](https://www.tencentcloud.com/document/product/1041/58269)*

---
*Источник (EN): [smart-erase-tutorial-old.md](./smart-erase-tutorial-old.md)*
