# Отправить сообщение

## Чат

## Отображение пользовательского интерфейса

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/dc0473afcbdd11ef8c8a525400454e06.png)

## Создание сообщения

### Создание текстового сообщения

Этот API используется для создания текстового сообщения. Он возвращает экземпляр сообщения, который можно отправить, вызвав API `sendMessage` когда требуется отправить текстовое сообщение.

**API**

```
chat.createTextMessage(options);
```

**Параметры**

Параметр `options` имеет тип `Object`. Он содержит следующие значения атрибутов:

| Название | Тип | Описание |
| --- | --- | --- |
| to | String | `userID` или `groupID` получателя сообщения |
| conversationType | String | Тип диалога. Допустимые значения: `TencentCloudChat.TYPES.CONV_C2C` (личный диалог) `TencentCloudChat.TYPES.CONV_GROUP` (групповой диалог) |
| priority | String | Приоритет сообщения. Если количество сообщений в группе превышает предел частоты, бэкэнд сначала доставляет сообщения с высоким приоритетом. Поддерживаемые перечисляемые значения: `TencentCloudChat.TYPES.MSG_PRIORITY_HIGH` `TencentCloudChat.TYPES.MSG_PRIORITY_NORMAL (по умолчанию)` `TencentCloudChat.TYPES.MSG_PRIORITY_LOW` `TencentCloudChat.TYPES.MSG_PRIORITY_LOWEST` |
| payload | Object | Контейнер содержимого сообщения |
| cloudCustomData | String | Пользовательские данные сообщения, которые сохраняются в облаке, отправляются получателю и могут быть получены даже после удаления и переустановки приложения. Этот атрибут поддерживается в v2.10.2 и выше |
| receiverList | Array \| undefined | Список членов группы, которые могут получать адресованные сообщения (не применимо к сообществам и аудио-видео группам) |
| isSupportExtension | Boolean | Поддерживаются ли расширения сообщений: `true` (поддерживается) или `false` (не поддерживается) (требуется приобретение премиум-пакета) |

`payload` описывается следующим образом:

| Название | Тип | Описание |
| --- | --- | --- |
| text | String | Текстовое содержимое сообщения |

##### **Возвращаемое значение**

`Message`

##### **Примеры**

```
// 1. Создайте экземпляр сообщения. Возвращаемый экземпляр может быть отображен на экране.let message = chat.createTextMessage({  to: 'user1',  conversationType: TencentCloudChat.TYPES.CONV_C2C,  // priority: TencentCloudChat.TYPES.MSG_PRIORITY_NORMAL,  payload: {    text: 'Hello world!'  },  // Для использования функции квитанции о прочтении необходимо приобрести выпуск Pro, Pro Plus или Enterprise  // и установить `needReadReceipt` на `true` при создании сообщения.  needReadReceipt: true  // cloudCustomData: 'your cloud custom data'});// 2. Отправьте сообщение.let promise = chat.sendMessage(message);promise.then(function(imResponse) {  // Сообщение отправлено успешно  console.log(imResponse);}).catch(function(imError) {  // Ошибка при отправке сообщения  console.warn('sendMessage error:', imError);});
```

```
// Отправить адресованное групповое сообщение// адресованные групповые сообщения не учитываются в unreadCount разговора// и receiverList поддерживает до 50 получателей.let message = chat.createTextMessage({  to: 'group1',  conversationType: TencentCloudChat.TYPES.CONV_GROUP,  payload: {    text: 'Hello world!'  },  receiverList: ['user0', 'user1']});let promise = chat.sendMessage(message);promise.then(function(imResponse) {  console.log(imResponse);}).catch(function(imError) {  console.warn('sendMessage error:', imError);});
```

### Создание сообщения с упоминанием (@mention)

Этот API используется для создания текстового сообщения с упоминанием (@mention). Он возвращает экземпляр сообщения, который можно отправить, вызвав API `sendMessage` когда требуется отправить текстовое сообщение.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/f58f060acbdd11efa2ff52540044a08e.png)

> **Примечание:** Применимо только к групповым чатам, и упоминание (@) всех членов не поддерживается для сообщества и его темы. Создание группового сообщения @ не поддерживает указание `receiverList`.

##### **API**

```
chat.createTextAtMessage(options);
```

##### **Параметры**

Параметр `options` имеет тип `Object`. Он содержит следующие значения атрибутов:

| Название | Тип | Описание |
| --- | --- | --- |
| to | String | `userID` или `groupID` получателя сообщения |
| conversationType | String | Тип диалога. Допустимые значения: `TencentCloudChat.TYPES.CONV_GROUP` (групповой диалог) |
| priority | String | Приоритет сообщения. Если количество сообщений в группе превышает предел частоты, бэкэнд сначала доставляет сообщения с высоким приоритетом. Поддерживаемые перечисляемые значения: `TencentCloudChat.TYPES.MSG_PRIORITY_HIGH` `TencentCloudChat.TYPES.MSG_PRIORITY_NORMAL (по умолчанию)` `TencentCloudChat.TYPES.MSG_PRIORITY_LOW` `TencentCloudChat.TYPES.MSG_PRIORITY_LOWEST` |
| payload | Object | Контейнер содержимого сообщения |
| cloudCustomData | String | Пользовательские данные сообщения, которые сохраняются в облаке, отправляются получателю и могут быть получены даже после удаления и переустановки приложения. |

`payload` описывается следующим образом:

| Название | Тип | Описание |
| --- | --- | --- |
| text | String | Текстовое содержимое |
| atUserList | Array | Список пользователей, которых необходимо упомянуть (@). Чтобы упомянуть (@) всех, передайте `TencentCloudChat.TYPES.MSG_AT_ALL`. Например, чтобы упомянуть (@) `denny` и `lucy`, а также всех членов, передайте `['denny', 'lucy', TencentCloudChat.TYPES.MSG_AT_ALL]` для `atUserList`. |

##### **Возвращаемое значение**

`Message`

##### **Примеры**

```
// 1. Создайте экземпляр сообщения. Возвращаемый экземпляр может быть отображен на экране.let message = chat.createTextAtMessage({  to: 'group1',  conversationType: TencentCloudChat.TYPES.CONV_GROUP,  // priority: TencentCloudChat.TYPES.MSG_PRIORITY_NORMAL,  payload: {    text: '@denny @lucy @all Dinner tonight. Reply 1 if you receive this message',    // 'denny' и 'lucy' - это значения `userID`, а не прозвища    atUserList: ['denny', 'lucy', TencentCloudChat.TYPES.MSG_AT_ALL]  },  // cloudCustomData: 'your cloud custom data'});// 2. Отправьте сообщение.let promise = chat.sendMessage(message);promise.then(function(imResponse) {  // Сообщение отправлено успешно  console.log(imResponse);}).catch(function(imError) {  // Ошибка при отправке сообщения  console.warn('sendMessage error:', imError);});
```

### Создание сообщения с изображением

Этот API используется для создания сообщения с изображением. Он возвращает экземпляр сообщения, который можно отправить, вызвав API `sendMessage` когда требуется отправить сообщение с изображением.

##### **API**

```
chat.createImageMessage(options);
```

##### **Параметры**

Параметр `options` имеет тип `Object`. Он содержит следующие значения атрибутов:

| Название | Тип | Описание |
| --- | --- | --- |
| to | String | Получатель сообщения |
| conversationType | String | Тип диалога. Допустимые значения: `TencentCloudChat.TYPES.CONV_C2C`, `TencentCloudChat.TYPES.CONV_GROUP`. |
| priority | String | Приоритет сообщения. Если количество сообщений в группе превышает предел частоты, бэкэнд сначала доставляет сообщения с высоким приоритетом. Поддерживаемые перечисляемые значения: `TencentCloudChat.TYPES.MSG_PRIORITY_HIGH` `TencentCloudChat.TYPES.MSG_PRIORITY_NORMAL (по умолчанию)` `TencentCloudChat.TYPES.MSG_PRIORITY_LOW` `TencentCloudChat.TYPES.MSG_PRIORITY_LOWEST` |
| payload | Object | Контейнер содержимого сообщения |
| onProgress | function | Функция обратного вызова для получения хода загрузки |
| cloudCustomData | String | Пользовательские данные сообщения, которые сохраняются в облаке, отправляются получателю и могут быть получены даже после удаления и переустановки приложения. |

`payload` описывается следующим образом:

| Название | Тип | Описание |
| --- | --- | --- |
| file | HTMLInputElement \| Object | Используется для выбора узла DOM (веб) или объекта `File` (веб) изображения. SDK читает данные, содержащиеся в этом параметре, и загружает изображение. |

##### **Возвращаемое значение**

`Message`

##### **Примеры**

```
// Пример 1: Отправка сообщения с изображением на веб - передача узла DOM// 1. Создайте экземпляр сообщения. Возвращаемый экземпляр может быть отображен на экране.let message = chat.createImageMessage({  to: 'user1',  conversationType: TencentCloudChat.TYPES.CONV_C2C,  // priority: TencentCloudChat.TYPES.MSG_PRIORITY_NORMAL,  payload: {    file: document.getElementById('imagePicker'),  },  // cloudCustomData: 'your cloud custom data'  onProgress: function(event) { console.log('file uploading:', event) }});// 2. Отправьте сообщение.let promise = chat.sendMessage(message);promise.then(function(imResponse) {  // Сообщение отправлено успешно  console.log(imResponse);}).catch(function(imError) {  // Ошибка при отправке сообщения  console.warn('sendMessage error:', imError);});
```

```
// Пример 2: Отправка сообщения с изображением на веб - передача объекта File// Добавьте поле ввода сообщения с ID `testPasteInput`document.getElementById('testPasteInput').addEventListener('paste', function(e) {  let clipboardData = e.clipboardData;  let file;  let fileCopy;  if (clipboardData && clipboardData.files && clipboardData.files.length > 0) {    file = clipboardData.files[0];    // После успешной отправки сообщения с изображением    // содержимое, на которое указывает `file`, может быть очищено браузером.    // Если у вас есть дополнительные потребности в отображении, вы можете заранее скопировать данные.    fileCopy = file.slice();  }  if (typeof file === 'undefined') {    console.warn('The `file` is `undefined`. Check for the compatibility of the code or browser.');    return;  }  // 1. Создайте экземпляр сообщения. Возвращаемый экземпляр может быть отображен на экране.  let message = chat.createImageMessage({    to: 'user1',    conversationType: TencentCloudChat.TYPES.CONV_C2C,    payload: {      file: file    },    onProgress: function(event) { console.log('file uploading:', event) }  });  // 2. Отправьте сообщение.  let promise = chat.sendMessage(message);  promise.then(function(imResponse) {    // Сообщение отправлено успешно    console.log(imResponse);  }).catch(function(imError) {    // Ошибка при отправке сообщения    console.warn('sendMessage error:', imError);  });});
```

```
// Отправка изображения в мини-программе wxwx.chooseImage({  sourceType: ['album'],  count: 1,  success: function (res) {    let message = chat.createImageMessage({      to: 'user1',      conversationType: TencentCloudChat.TYPES.CONV_C2C,      payload: { file: res },      onProgress: function(event) { console.log('file uploading:', event) }    });     let promise = chat.sendMessage(message);    promise.then(function(imResponse) {      console.log(imResponse);    }).catch(function(imError) {      console.warn('sendMessage error:', imError);    });  }})
```

```
// Отправка изображения в uni-appuni.chooseMedia({  count: 1,  mediaType: ['image'],  sizeType: ['original', 'compressed'],  sourceType: ['album'],  success: function(res) {    let message = chat.createImageMessage({      to: 'user1',      conversationType: TencentCloudChat.TYPES.CONV_C2C,      payload: { file: res },      onProgress: function(event) { console.log('file uploading:', event) }    });     let promise = chat.sendMessage(message);    promise.then(function(imResponse) {      console.log(imResponse);    }).catch(function(imError) {      console.warn('sendMessage error:', imError);    });  }});
```

### Создание сообщения с аудио

Этот API используется для создания сообщения с аудио. Он возвращает экземпляр сообщения, который можно отправить, вызвав API `sendMessage` когда требуется отправить сообщение с аудио.

##### **API**

```
chat.createAudioMessage(options);
```

##### **Параметры**

Параметр `options` имеет тип `Object`. Он содержит следующие значения атрибутов:

| Название | Тип | Описание |
| --- | --- | --- |
| to | String | Получатель сообщения |
| conversationType | String | Тип диалога. Допустимые значения: `TencentCloudChat.TYPES.CONV_C2C` `TencentCloudChat.TYPES.CONV_GROUP` |
| priority | String | Приоритет сообщения. Если количество сообщений в группе превышает предел частоты, бэкэнд сначала доставляет сообщения с высоким приоритетом. Поддерживаемые перечисляемые значения: `TencentCloudChat.TYPES.MSG_PRIORITY_HIGH` `TencentCloudChat.TYPES.MSG_PRIORITY_NORMAL (по умолчанию)` `TencentCloudChat.TYPES.MSG_PRIORITY_LOW` `TencentCloudChat.TYPES.MSG_PRIORITY_LOWEST` |
| payload | Object | Контейнер содержимого сообщения |
| cloudCustomData | String | Пользовательские данные сообщения, которые сохраняются в облаке, отправляются получателю и могут быть получены даже после удаления и переустановки приложения. |

`payload` описывается следующим образом:

| Название | Тип | Описание |
| --- | --- | --- |
| file | Object | Аудиофайл, полученный после записи |

##### **Возвращаемое значение**

`Message`

##### **Примеры**

```
// Отправка аудио в мини-программе wxconst recorderManager = wx.getRecorderManager();const recordOptions = {  duration: 60000,   sampleRate: 44100,  numberOfChannels: 1,  encodeBitRate: 192000,  format: 'aac'};recorderManager.onError(function(errMsg) {  console.warn('recorder error:', errMsg);});recorderManager.onStop(function(res) {  console.log('recorder stop', res);  const message = chat.createAudioMessage({    to: 'user1',    conversationType: TencentCloudChat.TYPES.CONV_C2C,    payload: {      file: res    },  });  let promise = chat.sendMessage(message);  promise.then(function(imResponse) {    console.log(imResponse);  }).catch(function(imError) {    console.warn('sendMessage error:', imError);  });});recorderManager.start(recordOptions);
```

```
// Отправка аудио на веб-сайтеlet recorder = new Recorder({  sampleBits: 16,  sampleRate: 16000,  numChannels: 1,});let startTs;recorder.start().then(() => {  startTs = Date.now();}, (error) => {  console.log(`${error.name} : ${error.message}`);});recorder.stop();let duration = Date.now() - startTs; // единица: мсlet wavBlob = recorder.getWAVBlob();// blob -> Filelet audioFile = new File([wavBlob], 'hello.wav', { type: 'wav' });audioFile.duration = duration;let message = chat.createAudioMessage({  to: 'user1',  conversationType: 'C2C',  payload: {    file: audioFile  }});let promise = chat.sendMessage(message);promise.then(function(imResponse) {  console.log(imResponse);}).catch(function(imError) {  console.warn('sendMessage error:', imError);});
```

### Создание видеосообщения

Этот API используется для создания видеосообщения. Он возвращает экземпляр сообщения, который можно отправить, вызвав API `sendMessage` когда требуется отправить видеосообщение.

##### **API**

```
chat.createVideoMessage(options);
```

##### **Параметры**

Параметр `options` имеет тип `Object`. Он содержит следующие значения атрибутов:

| Название | Тип | Описание |
| --- | --- | --- |
| to | String | Получатель сообщения |
| conversationType | String | Тип диалога. Допустимые значения: `TencentCloudChat.TYPES.CONV_C2C` `TencentCloudChat.TYPES.CONV_GROUP` |
| priority | String | Приоритет сообщения. Если количество сообщений в группе превышает предел частоты, бэкэнд сначала доставляет сообщения с высоким приоритетом. Поддерживаемые перечисляемые значения: `TencentCloudChat.TYPES.MSG_PRIORITY_HIGH` `TencentCloudChat.TYPES.MSG_PRIORITY_NORMAL (по умолчанию)` `TencentCloudChat.TYPES.MSG_PRIORITY_LOW` `TencentCloudChat.TYPES.MSG_PRIORITY_LOWEST` |
| payload | Object | Контейнер содержимого сообщения |
| cloudCustomData | String | Пользовательские данные сообщения, которые сохраняются в облаке, отправляются получателю и могут быть получены даже после удаления и переустановки приложения. |

`payload` описывается следующим образом:

| Название | Тип | Описание |
| --- | --- | --- |
| file | HTMLInputElement \| File \| Object | Видеофайл, полученный после записи. |

##### **Возвращаемое значение**

`Message`

##### **Примеры**

```
// Отправка видеосообщения в мини-программе wxwx.chooseVideo({  sourceType: ['album', 'camera'],  maxDuration: 60,  camera: 'back',  success (res) {    let message = chat.createVideoMessage({      to: 'user1',      conversationType: TencentCloudChat.TYPES.CONV_C2C,      payload: {        file: res      },      // cloudCustomData: 'your cloud custom data'      onProgress: function(event) { console.log('file uploading:', event) }    })       let promise = chat.sendMessage(message);    promise.then(function(imResponse) {      console.log(imResponse);    }).catch(function(imError) {      console.warn('sendMessage error:', imError);    });  }})
```

```
// Пример: Отправка видеосообщения на веб// 1. Получите видеофайл, передав узел DOM.// 2. Создайте экземпляр сообщения.const message = chat.createVideoMessage({  to: 'user1',  conversationType: TencentCloudChat.TYPES.CONV_C2C,  payload: {    file: document.getElementById('videoPicker') // Или используйте `event.target`  },  onProgress: function(event) { console.log('file uploading:', event) }});// 3. Отправьте сообщение.let promise = chat.sendMessage(message);promise.then(function(imResponse) {  // Сообщение отправлено успешно  console.log(imResponse);}).catch(function(imError) {  // Ошибка при отправке сообщения  console.warn('sendMessage error:', imError);});
```

```
// Отправка видеосообщения в uni-appuni.chooseVideo({  count: 1,  sourceType: ['camera', 'album'],  maxDuration: 60,  camera: 'back',  success: function(res) {    let message = chat.createVideoMessage({      to: 'user1',      conversationType: TencentCloudChat.TYPES.CONV_C2C,      payload: { file: res },      onProgress: function(event) { console.log('file uploading:', event) }    });       let promise = chat.sendMessage(message);    promise.then(function(imResponse) {      console.log(imResponse);    }).catch(function(imError) {      console.warn('sendMessage error:', imError);    });  }})
```

### Создание пользовательского сообщения

Этот API используется для создания пользовательского сообщения. Он возвращает экземпляр сообщения, который можно отправить, вызвав API `sendMessage` когда требуется отправить пользовательское сообщение. Когда текущие возможности SDK не удовлетворяют вашим потребностям, вы можете создать пользовательское сообщение.

##### **API**

```
chat.createCustomMessage(options);
```

##### **Параметры**

Параметр `options` имеет тип `Object`. Он содержит следующие значения атрибутов:

| Название | Тип | Описание |
| --- | --- | --- |
| to | String | `userID` или `groupID` получателя сообщения |
| conversationType | String | Тип диалога. Допустимые значения: `TencentCloudChat.TYPES.CONV_C2C` (личный диалог) `TencentCloudChat.TYPES.CONV_GROUP` (групповой диалог) |
| priority | String | Приоритет сообщения. Если количество сообщений в группе превышает предел частоты, бэкэнд сначала доставляет сообщения с высоким приоритетом. Поддерживаемые перечисляемые значения: `TencentCloudChat.TYPES.MSG_PRIORITY_HIGH` `TencentCloudChat.TYPES.MSG_PRIORITY_NORMAL (по умолчанию)` `TencentCloudChat.TYPES.MSG_PRIORITY_LOW` `TencentCloudChat.TYPES.MSG_PRIORITY_LOWEST` |
| payload | Object | Контейнер содержимого сообщения |
| cloudCustomData | String | Пользовательские данные сообщения, которые сохраняются в облаке, отправляются получателю и могут быть получены даже после удаления и переустановки приложения. |

`payload` описывается следующим образом:

| Название | Тип | Описание |
| --- | --- | --- |
| data | String | Данные пользовательского сообщения |
| description | String | Описание пользовательского сообщения |
| extension | String | Расширение пользовательского сообщения |

##### **Возвращаемое значение**

`Message`

##### **Примеры**

```
// Пример: Использование пользовательского сообщения для реализации броска кубика// 1. Определите функцию случайного числа.function random(min, max) {  return Math.floor(Math.random() * (max - min + 1) + min);}// 2. Создайте экземпляр сообщения. Возвращаемый экземпляр может быть отображен на экране.let message = chat.createCustomMessage({  to: 'user1',  conversationType: TencentCloudChat.TYPES.CONV_C2C,  payload: {    data: 'dice', // Используется для идентификации сообщения как сообщения кубика    description: String(random(1,6)), // Получите результат    extension: ''  }});// 3. Отправьте сообщение.let promise = chat.sendMessage(message);promise.then(function(imResponse) {  // Сообщение отправлено успешно  console.log(imResponse);}).catch(function(imError) {  // Ошибка при отправке сообщения  console.warn('sendMessage error:', imError);});
```

### Создание сообщения с эмодзи

Этот API используется для создания сообщения с эмодзи. Он возвращает экземпляр сообщения, который можно отправить, вызвав API `sendMessage` когда требуется отправить сообщение с эмодзи.

##### **API**

```
chat.createFaceMessage(options);
```

##### **Параметры**

Параметр `options` имеет тип `Object`. Он содержит следующие значения атрибутов:

| Название | Тип | Описание |
| --- | --- | --- |
| to | String | `userID` или `groupID` получателя сообщения |
| conversationType | String | Тип диалога. Допустимые значения: `TencentCloudChat.TYPES.CONV_C2C` (личный диалог) `TencentCloudChat.TYPES.CONV_GROUP` (групповой диалог) |
| priority | String | Приоритет сообщения. Если количество сообщений в группе превышает предел частоты, бэкэнд сначала доставляет сообщения с высоким приоритетом. Поддерживаемые перечисляемые значения: `TencentCloudChat.TYPES.MSG_PRIORITY_HIGH` `TencentCloudChat.TYPES.MSG_PRIORITY_NORMAL (по умолчанию)` `TencentCloudChat.TYPES.MSG_PRIORITY_LOW` `TencentCloudChat.TYPES.MSG_PRIORITY_LOWEST` |
| payload | Object | Контейнер содержимого сообщения |
| cloudCustomData | String | Пользовательские данные сообщения, которые сохраняются в облаке, отправляются получателю и могут быть получены даже после удаления и переустановки приложения. |

`payload` описывается следующим образом:

| Название | Тип | Описание |
| --- | --- | --- |
| index | Number | Индекс эмодзи, который определяется пользователем |
| data | String | Дополнительные данные |

##### **Возвращаемое значение**

`Message`

##### **Примеры**

```
// Отправка сообщения с эмодзи на веб// 1. Создайте экземпляр сообщения. Возвращаемый экземпляр может быть отображен на экране.let message = chat.createFaceMessage({  to: 'user1',  conversationType: TencentCloudChat.TYPES.CONV_C2C,  payload: {    index: 1, // Число. Индекс эмодзи, который определяется пользователем    data: 'tt00' // Строка. Дополнительные данные  },  // cloudCustomData: 'your cloud custom data'});// 2. Отправьте сообщение.let promise = chat.sendMessage(message);promise.then(function(imResponse) {  // Сообщение отправлено успешно  console.log(imResponse);}).catch(function(im

---
*Источник (EN): [send-a-message.md](./send-a-message.md)*
