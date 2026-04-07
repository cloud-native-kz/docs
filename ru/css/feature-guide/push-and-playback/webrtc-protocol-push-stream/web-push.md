# Веб-трансляция

SDK TXLivePusher используется для отправки потоков для LEB (сверхнизкозадержная прямая трансляция). Он может отправлять аудио и видео, которые браузер захватывает с камеры, экрана или локального медиафайла, на серверы прямой трансляции через WebRTC.

Вы можете использовать протокол WebRTC для прямой трансляции в Интернете. На стороне ПК вы также можете использовать инструмент OBS для прямой трансляции WebRTC. Конкретные методы операций см. в разделе [OBS WebRTC Live Streaming](/document/product/267/57042).

Преимущество использования Web для прямой трансляции WebRTC заключается в том, что не требуется установка дополнительного программного обеспечения, и вы можете работать непосредственно в браузере. В этой статье рассказывается о методе операций для прямой трансляции с помощью **Web**.

> **Примечание**При использовании WebRTC каждое доменное имя отправки по умолчанию может обслуживать до **1000 одновременных потоков**. Если вам требуется отправить больше потоков, пожалуйста, [отправьте тикет](https://console.tencentcloud.com/workorder/category).

## Основы

Ниже приведены основные сведения, которые необходимо знать перед интеграцией SDK.

### Формирование URL-адресов отправки

Для использования сервисов прямой трансляции Tencent Cloud необходимо составить URL-адреса отправки в формате, требуемом Tencent Cloud, который состоит из четырех частей.

![](https://staticintl.cloudcachetci.com/cms/backend-cms/9081715851e911ee84f2525400494e51.png)

Ключ аутентификации не требуется. Вы можете включить аутентификацию отправки, если вам требуется защита от горячих ссылок. Подробнее см. в разделе [Splicing Live Streaming URLs](https://intl.cloud.tencent.com/document/product/267/38393).

### Поддержка браузеров

Веб-трансляция основана на реализации WebRTC и зависит от поддержки операционной системой и браузером WebRTC. В настоящее время последние версии браузеров Chrome, Edge, Firefox и Safari поддерживают веб-трансляцию.

> **Примечание：**Функция захвата аудио/видео плохо поддерживается мобильными браузерами. Например, мобильные браузеры не поддерживают запись экрана, а доступ к камере можно запросить только в iOS 14.3 и более поздних версиях. Поэтому SDK отправки в основном используется на настольных браузерах. Последние версии Chrome, Firefox и Safari поддерживают отправку для LEB.

## Интеграция SDK

### Шаг 1. Подготовка страницы

Добавьте скрипт инициализации на страницу (рабочего стола), с которой будут отправляться потоки.

```
<script src="https://video.sdk.qcloudecdn.com/web/TXLivePusher-2.1.1.min.js" charset="utf-8"></script>
```

> **Примечание**Скрипт должен быть импортирован в часть `body` HTML-кода. Если он импортирован в часть `head`, будет выдана ошибка.

### Шаг 2. Добавление контейнера на страницу HTML

Добавьте контейнер проигрывателя в раздел страницы, где будет воспроизводиться локальное видео. Это достигается путем добавления div и присваивания ему имени, например `id_local_video`. Локальное видео будет отображаться в контейнере. Для изменения размера контейнера используйте CSS для стилизации div. Ниже приведен пример кода:

```
<div id="id_local_video" style="width:100%;height:500px;display:flex;align-items:center;justify-content:center;"></div>
```

### Шаг 3. Отправка потоков

1. **Создание экземпляра SDK отправки:**

Создайте экземпляр глобального объекта `TXLivePusher`. Все последующие операции будут выполняться через экземпляр.

```
const livePusher = new TXLivePusher();
```

2. **Указание контейнера локального проигрывателя видео:**
Укажите div для контейнера локального проигрывателя видео, где будет отображаться аудио и видео, захватываемые браузером.

```
livePusher.setRenderView('id_local_video');
```

> **Примечание**Элемент видео, созданный через `setRenderView`, по умолчанию не отключен. Для отключения звука видео используйте код ниже.livePusher.videoView.muted = true;=

3. **Установка качества аудио/видео:**
Качество аудио/видео должно быть установлено перед захватом. Вы можете указать параметры качества, если параметры по умолчанию не соответствуют вашим требованиям.

```
// Set video qualitylivePusher.setVideoQuality('720p');// Set audio qualitylivePusher.setAudioQuality('standard');// Set the frame rate
```

4. **Захват потоков:**
Вы можете захватывать потоки с камеры, микрофона, экрана и локальных медиафайлов. При успешном захвате контейнер проигрывателя начнет воспроизводить захватываемое аудио и видео.

```
// Turn the camera onlivePusher.startCamera();// Turn the mic onlivePusher.startMicrophone();
```

5. **Отправка потоков:**
Передайте URL-адрес отправки LEB, чтобы начать отправку потоков. Формат URL-адресов отправки см. в разделе[Splicing Live Streaming URLs](/document/product/267/57043#8a99c4e5-7eef-4a86-aa38-bb88b3701254). Необходимо заменить префикс `rtmp://` на `webrtc://`.

```
livePusher.startPush('webrtc://domain/AppName/StreamName?txSecret=xxx&txTime=xxx');
```

> **Примечание**Перед отправкой убедитесь, что потоки аудио/видео успешно захвачены, иначе вызов API отправки будет неудачным. Вы можете использовать код ниже для автоматической отправки потоков после захвата аудио/видео, то есть после получения обратного вызова для захвата первого кадра аудио или видео. Если захвачены как аудио, так и видео, отправка начинается только после получения как обратного вызова для захвата первого кадра аудио, так и обратного вызова для первого кадра видео.// Automatically push the stream after collecting the camera footagelivePusher.startCamera().then(function () { livePusher.startPush('webrtc://domain/AppName/StreamName?txSecret=xxx&txTime=xxx');}).catch(function (error) { console.log('Failed to open camera: '+ error.toString());});
> // Automatically push the stream after collecting the camera and microphonePromise.all([livePusher.startCamera(), livePusher.startMicrophone()]).then(function() { livePusher.startPush('webrtc://domain/AppName/StreamName?txSecret=xxx&txTime=xxx');});

6. **Остановка отправки:**

```
livePusher.stopPush();
```

7. **Остановка захвата аудио и видео:**

```
// Turn the camera offlivePusher.stopCamera();// Turn the mic offlivePusher.stopMicrophone();
```

## Дополнительные функции

### Совместимость

SDK предоставляет статический метод для проверки поддержки браузером WebRTC.

```
TXLivePusher.checkSupport().then(function(data) {    // Whether WebRTC is supported    if (data.isWebRTCSupported) {        console.log('WebRTC Support');    } else {        console.log('WebRTC Not Support');    }    // Whether H.264 is supported    if (data.isH264EncodeSupported) {        console.log('H264 Encode Support');    } else {        console.log('H264 Encode Not Support');    }});
```

### Обратные вызовы событий

SDK поддерживает уведомления о событиях обратного вызова. Вы можете установить наблюдателя для получения обратных вызовов статуса SDK и статистики WebRTC.

```
livePusher.setObserver({
  // Warnings for push
  onWarning: function(code, msg) {
    console.log(code, msg);
  },
  // Push status
  onPushStatusUpdate: function(status, msg) {
    console.log(status, msg);
  },
```

### Управление устройствами

Вы можете использовать экземпляр управления устройствами для получения списка устройств, переключения устройств и выполнения других операций, связанных с устройствами.

```
const deviceManager = livePusher.getDeviceManager();let cameraDeviceId = null;// Get device listdeviceManager.getDevicesList().then(function(data) {  data.forEach(function(device) {    console.log(device.type, device.deviceId, device.deviceName);    if (device.type === 'video') {      cameraDeviceId = device.deviceId;    }  });  // Switch camera device  if (cameraDeviceId) {    deviceManager.switchCamera(cameraDeviceId);  }});
```


---
*Источник: [https://www.tencentcloud.com/document/product/267/57043](https://www.tencentcloud.com/document/product/267/57043)*

---
*Источник (EN): [web-push.md](./web-push.md)*
