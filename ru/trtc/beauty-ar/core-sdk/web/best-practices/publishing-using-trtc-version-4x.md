# Публикация с использованием TRTC (версия 4.x)

> **Примечание:** Это руководство основано на веб-SDK TRTC версии 4.x. Если вы используете версию 5.x SDK, обратитесь к [этому руководству](https://www.tencentcloud.com/document/product/1143/67329#).

## Перед началом

- Прочитайте [руководство по интеграции](https://www.tencentcloud.com/document/product/1143/50099) для Beauty AR Web.
- Выполните шаги из раздела [Интеграция (без пользовательского интерфейса)](https://www.tencentcloud.com/document/product/647/35096) для интеграции веб-SDK TRTC.
- Попробуйте [запустить демонстрацию TRTC Web](https://www.tencentcloud.com/document/product/647/35607) в своем локальном проекте.

## Инструкции

### Шаг 1. Импорт SDK Beauty AR Web

```
<script charset="utf-8" src="https://webar-static.tencent-cloud.com/ar-sdk/resources/latest/webar-sdk.umd.js"></script>
```

> **Примечание:** В приведенном выше примере используется тег script для импорта SDK. Вы также можете [импортировать его с помощью пакета npm](https://www.tencentcloud.com/document/product/1143/50099).

### Шаг 2. Ознакомьтесь с логикой инициализации потока TRTC

```
// Capture audio and video from the mic and camera for the local streamconst localStream = TRTC.createStream({ userId, audio: true, video: true });localStream.initialize().then(() => { console.log('initialize localStream success'); // The local stream was initialized successfully. You can call `Client.publish(localStream)` to publish the local stream..catch(error => { console.error('failed initialize localStream ' + error);});
```

Это наиболее распространенный способ инициализации локального потока.

2. `TRTC.createStream` также позволяет использовать внешний источник аудио/видео для локального потока, что дает вам возможность применять собственную обработку потока (такую как применение эффектов красоты к видео). Ниже приведен пример:

```
// Get the custom streamconst stream = await this.ar.getOutput();// Use the audio/video source to create a local stream objectconst audioTrack = stream.getAudioTracks()[0];const videoTrack = stream.getVideoTracks()[0];const localStream = TRTC.createStream({ userId, audioSource: audioTrack, videoSource: videoTrack });localStream.initialize().then(() => { console.log('initialize localStream success'); // The local stream was initialized successfully. You can call `Client.publish(localStream)` to publish the local stream..catch(error => { console.error('failed initialize localStream ' + error);});
```

Подробное описание использования `createStream` см. в [документации SDK TRTC](https://web.sdk.qcloud.com/trtc/webrtc/doc/zh-cn/TRTC.html#createStream).

3. Для обработки локального потока с использованием Tencent Effect необходимо использовать второй способ выше. Перед вызовом `getMyStream` [инициализируйте SDK Beauty AR Web](#step3) предварительно.

### Шаг 3. Инициализация SDK Beauty AR Web

```
const { ArSdk } = window.AR/** ----- Authentication configuration ----- *//** * The APPID of your Tencent Cloud account. *  * You can view your APPID in the [Account Center](https://console.cloud.tencent.com/developer). */const APPID = ''; // Set it to your Tencent Cloud account APPID./** * Web LicenseKey *  * Log in to the RT-Cube console and click [Web Licenses](https://console.cloud.tencent.com/vcube/web) on the left sidebar. A license key will be automatically generated after you create a license. */const LICENSE_KEY = ''; // Set it to your license key./** * The token used to calculate the signature. *  * Note: This method is only suitable for debugging. In a production environment, you should store the token and calculate the signature on your server. The front end can get the signature by calling an API. For details, see * [Signature](https://cloud.tencent.com/document/product/616/71370#.E7.AD.BE.E5.90.8D.E6.96.B9.E6.B3.95) */const token = ''; // Set it to your token./** ----------------------- *//** * Get the signature * * Note: This method is only suitable for debugging. In a production environment, you should calculate the signature on your server. The front end can get the signature by calling an API. ** Example: * async function () { *  return fetch('http://xxx.com/get-ar-sign').then(res => res.json()); * }; */const getSignature = function () {    const timestamp = Math.round(new Date().getTime() / 1000);    const signature = sha256(timestamp + token + APPID + timestamp).toUpperCase();    return { signature, timestamp };};let w = 1280;let h = 720;// The basic settings for the Tencent Effect SDKconst config = {    camera: { //This indicates that the SDK will capture streams from the camera.        width: 1280,        height:720    },    auth: {        licenseKey: LICENSE_KEY,        appId: APPID,        authFunc: getSignature    },    // Configure the initial effects (optional)    beautify: {        whiten: 0.1, // The brightening effect. Value range: 0-1.        dermabrasion: 0.5, // The smooth skin effect. Value range: 0-1.        lift: 0.3, // The slim face effect. Value range: 0-1.        shave: 0, // The V shape effect. Value range: 0-1.        eye: 0, // The big eyes effect. Value range: 0-1.        chin: 0, // The chin effect. Value range: 0-1.    },    language: 'en',    …}// Pass `config` to the Tencent Effect SDKconst ar = new ArSdk(config);// You can display the effect and filter list in the `created` callback.ar.on('created', () => {    // Get the built-in makeup effects and stickers    ar.getEffectList({        Type: 'Preset'    }).then((res) => {        const list = res.map(item => ({            name: item.Name,            id: item.EffectId,            cover: item.CoverUrl,            url: item.Url,            label: item.Label,            type: item.PresetType,        }));        const makeupList = list.filter(item=>item.label.indexOf('Makeup')>=0)        const stickerList = list.filter(item=>item.label.indexOf('Sticker')>=0)        // Show the makeup and sticker lists        renderMakeupList(makeupList);        renderStickerList(stickerList);    }).catch((e) => {        console.log(e);    });    // Get the built-in filters    ar.getCommonFilter().then((res) => {        const list = res.map(item => ({            name: item.Name,            id: item.EffectId,            cover: item.CoverUrl,            url: item.Url,            label: item.Label,            type: item.PresetType,        }));        // Show the filter list        renderFilterList(list);    }).catch((e) => {        console.log(e);    });});ar.on('ready', (e) => {    // After receiving the `ready` callback, you can call `setBeautify`, `setEffect`, or `setFilter` to configure effects.    //  For example, you can use `range input` to set the smooth skin effect:    $('#dermabrasion_range_input').change((e) => {        ar.setBeautify({            dermabrasion: e.target.value, // The smooth skin effect. Value range: 0-1.        });    });    // In the `created` callback, apply the effects based on user interactions with the makeup effect and sticker lists. The `setEffect` API supports three types of request parameters. For details, see the SDK integration guide.    $('#makeup_list li').click(() => {        ar.setEffect([{id: effect.id, intensity: 1}]);    });    $('#sticker_list li').click(() => {        ar.setEffect([{id: effect.id, intensity: 1}]);    });    // In the `created` callback, apply the filter based on user interactions with the filter list. The value `1` for the second parameter of `setFilter` indicates the filter strength. For details, see the SDK integration guide.    ar.setFilter(filterList[0].id, 1);    $('#filter_list li').click(() => {        ar.setFilter(filter.id, 1);    });});ar.on('error', (e) => {    console.log(e);});
```

Приведенный выше код показывает, как инициализировать SDK Beauty AR Web, а также как реагировать на взаимодействие пользователя в обратном вызове `ready`. Чтобы узнать больше о взаимодействии с пользовательским интерфейсом, вы можете загрузить пакет кода в конце этого документа.

### Шаг 4. Инициализация потока TRTC

```
// Get the output stream of the Tencent Effect SDKconst arStream = await this.ar.getOutput();const audioSource = arStream.getAudioTracks()[0];const videoSource = arStream.getVideoTracks()[0];// create a local stream with audio/video from custom sourcethis.localStream_ = TRTC.createStream({    audioSource,    videoSource});
```

### Шаг 5. Воспроизведение потока

> **Примечание:** Для примера проекта необходимо запустить веб-сервис вашего устройства и убедиться, что доступ к файлу HTML возможен через указанный порт.

После входа в комнату вы сможете просмотреть поток с применными эффектами (файл `index_AR.html` в образце кода). После этого вы можете открыть новую вкладку браузера и войти в комнату, чтобы имитировать вход нового пользователя.

### Шаг 6. Управление устройствами

```
const cameraApi = this.ar.camera;// Get the device listconst devices = await cameraApi.getDevices()console.log(devices)// Switch to a different camera// await cameraApi.switchDevice('video', 'your-video-device-id')// Disable the video track// cameraApi.muteVideo()// Enable the video track// cameraApi.unmuteVideo()// Disable the audio track// cameraApi.muteAudio()// Enable the audio track// cameraApi.unmuteAudio()// Stop the camera// cameraApi.stop()// Restart the camera// await cameraApi.restart()
```

### Шаг 7. Локальный предпросмотр эффектов

```
// Use the built-in player of the SDK. `my-dom-id` is the ID of the playerâs container.const player = await sdk.initLocalPlayer('my-dom-id')// Play the videoawait player.play()// Pause the videoplayer.pause()
```

## Пакет примеров кода

Вы можете загрузить пакет примеров кода [здесь](https://github.com/tencentcloud-webar/web-demo-en). Пример кода находится в папке **TRTC_Web(4.x)**. Основные изменения находятся в файлах `index_AR.html` и `rtc-client-with-webar.js`. Код логики взаимодействия Tencent Effect находится в файле `base-js/js/ar_interact.js`. Конфигурация ключевой информации TRTC находится в файле `base-js/js/debug/GenerateTestUserSig.js`.


---
*Источник: [https://trtc.io/document/53885](https://trtc.io/document/53885)*

---
*Источник (EN): [publishing-using-trtc-version-4x.md](./publishing-using-trtc-version-4x.md)*
