# Публикация с использованием TRTC (Версия 5.x)

> **Примечание:** Это руководство основано на Web SDK TRTC версии 5.x. Если вы используете SDK версии 4.x, обратитесь к [этому руководству](https://www.tencentcloud.com/document/product/1143/53885).

## Перед началом работы

- Прочитайте [руководство по интеграции](https://www.tencentcloud.com/document/product/1143/50099) для Beauty AR Web.
- Следуйте инструкциям в разделе [Интеграция (без пользовательского интерфейса)](https://www.tencentcloud.com/document/product/647/35096) для интеграции Web SDK TRTC.
- Попробуйте [запустить веб-демонстрацию TRTC](https://www.tencentcloud.com/document/product/647/35607) в своём локальном проекте.

## Инструкции

### Шаг 1. Импортируйте Web SDK Beauty AR

**Вы можете импортировать Web SDK Beauty AR, внеся незначительные изменения в метод импорта в веб-демонстрации TRTC.**

Добавьте следующий скрипт JavaScript на вашу веб-страницу (для рабочего стола):

```
<script charset="utf-8" src="https://webar-static.tencent-cloud.com/ar-sdk/resources/latest/webar-sdk.umd.js"></script>
```

> **Примечание:** Приведённый выше пример использует тег script для импорта SDK. Вы также можете [импортировать его с помощью пакета npm](https://www.tencentcloud.com/document/product/1143/50099).

### Шаг 2. Разберитесь в логике инициализации потока TRTC

1. В демонстрационном проекте TRTC вы можете наблюдать процесс присоединения к комнате TRTC. После входа в комнату TRTC захватывает локальный ввод устройства, используя методы [startLocalVideo](https://web.sdk.qcloud.com/trtc/webrtc/v5/doc/en/TRTC.html#startLocalVideo) и [startLocalAudio](https://web.sdk.qcloud.com/trtc/webrtc/v5/doc/en/TRTC.html#startLocalAudio), создавая объекты потока и публикуя их в комнату:

```
const trtc = TRTC.create();await trtc.enterRoom({ roomId: 8888, sdkAppId, userId, userSig });// Collect the default microphone and publishawait trtc.startLocalAudio();// Collect the default camera and publishawait trtc.startLocalVideo({  view: document.getElementById("localVideo"), // Preview the video on the element with the DOM elementId of localVideo.});
```

Приведённый выше код описывает наиболее базовый метод захвата локальных аудио- и видеопотоков и их публикации в указанную комнату.

2. TRTC предоставляет интерфейс [updateLocalVideo](https://web.sdk.qcloud.com/trtc/webrtc/v5/doc/en/TRTC.html#updateLocalVideo) для обновления видеопотоков. Мы можем использовать пользовательские методы захвата для получения потоков с улучшенной красотой и передачи их этому интерфейсу для использования.

```
// Get the custom streamconst stream = await ar.getOutput();// update trtc video trackawait trtc.updateLocalVideo({  option: { videoTrack: mediaStream.getVideoTracks()[0] },});
```

3. Для обработки локального потока с использованием Tencent Effect необходимо сначала [инициализировать Web SDK Beauty AR](#step3).

### Шаг 3. Инициализируйте Web SDK Beauty AR

Пример кода:

```
const { ArSdk } = window.AR/** ----- Authentication configuration ----- *//** * The APPID of your Tencent Cloud account. *  * You can view your APPID in the [Account Center](https://console.cloud.tencent.com/developer). */const APPID = ''; // Set it to your Tencent Cloud account APPID./** * Web LicenseKey *  * Log in to the RT-Cube console and click [Web Licenses](https://console.cloud.tencent.com/vcube/web) on the left sidebar. A license key will be automatically generated after you create a license. */const LICENSE_KEY = ''; // Set it to your license key./** * The token used to calculate the signature. *  * Note: This method is only suitable for debugging. In a production environment, you should store the token and calculate the signature on your server. The front end can get the signature by calling an API. For details, see * [Signature](https://cloud.tencent.com/document/product/616/71370#.E7.AD.BE.E5.90.8D.E6.96.B9.E6.B3.95) */const token = ''; // Set it to your token./** ----------------------- *//** * Get the signature * * Note: This method is only suitable for debugging. In a production environment, you should calculate the signature on your server. The front end can get the signature by calling an API. ** Example: * async function () { *  return fetch('http://xxx.com/get-ar-sign').then(res => res.json()); * }; */const getSignature = function () {    const timestamp = Math.round(new Date().getTime() / 1000);    const signature = sha256(timestamp + token + APPID + timestamp).toUpperCase();    return { signature, timestamp };};// get trtc video track(original)const arInputStream = new MediaStream([trtc.getVideoTrack()]);// The basic settings for the Tencent Effect SDKconst config = {    input: arInputStream,    auth: {        licenseKey: LICENSE_KEY,        appId: APPID,        authFunc: getSignature    },    // Configure the initial effects (optional)    beautify: {        whiten: 0.1, // The brightening effect. Value range: 0-1.        dermabrasion: 0.5, // The smooth skin effect. Value range: 0-1.        lift: 0.3, // The slim face effect. Value range: 0-1.        shave: 0, // The V shape effect. Value range: 0-1.        eye: 0, // The big eyes effect. Value range: 0-1.        chin: 0, // The chin effect. Value range: 0-1.    },    language: 'en',    …}// Pass `config` to the Tencent Effect SDKconst ar = new ArSdk(config);// You can display the effect and filter list in the `created` callback.ar.on('created', () => {    // Get the built-in makeup effects and stickers    ar.getEffectList({        Type: 'Preset'    }).then((res) => {        const list = res.map(item => ({            name: item.Name,            id: item.EffectId,            cover: item.CoverUrl,            url: item.Url,            label: item.Label,            type: item.PresetType,        }));        const makeupList = list.filter(item=>item.label.indexOf('Makeup')>=0)        const stickerList = list.filter(item=>item.label.indexOf('Sticker')>=0)        // Show the makeup and sticker lists    }).catch((e) => {        console.log(e);    });    // Get the built-in filters    ar.getCommonFilter().then((res) => {        const filterList = res.map(item => ({            name: item.Name,            id: item.EffectId,            cover: item.CoverUrl,            url: item.Url,            label: item.Label,            type: item.PresetType,        }));        // Show the filter list    }).catch((e) => {        console.log(e);    });});ar.on('ready', (e) => {    // After receiving the `ready` callback, you can call `setBeautify`, `setEffect`, or `setFilter` to configure effects.    // ar.setBeautify()    // ar.setEffect()    // ar.setFilter()        // update trtc video track (with AR effect)    const mediaStream = await ar.getOutput();    await trtc.updateLocalVideo({      option: { videoTrack: mediaStream.getVideoTracks()[0] },    });});ar.on('error', (e) => {    console.log(e);});
```

Приведённый выше код инициализирует конфигурацию для Web SDK эффектов красоты. Входными данными для SDK красоты является необработанный видеопоток, полученный от интерфейса getVideoTrack объекта TRTC.

### Шаг 4. Обновите поток TRTC

После инициализации Web SDK эффектов красоты вы можете использовать метод getOutput для получения выходного потока. Затем вызовите интерфейс updateLocalVideo экземпляра TRTC для обновления локального потока и его публикации в комнату.

```
const mediaStream = await ar.getOutput();// update trtc video track (with AR effect)await trtc.updateLocalVideo({  option: { videoTrack: mediaStream.getVideoTracks()[0] },});
```

### Шаг 5: Запустите демонстрацию для проверки эффектов

> **Примечание:** Примерный проект требует запуска локального веб-сервера и обеспечивает доступ к HTML-файлу через указанный номер порта (пример кода находится в папке **TRTC_Web(5.x)**, запустите quick-demo-js/index.html).

После входа в комнату вам нужно подождать некоторое время для инициализации эффекта красоты. После инициализации вы сможете увидеть фактические эффекты красоты в действии. При успешном выполнении вы можете открыть новую вкладку браузера и войти в созданную комнату, чтобы имитировать присоединение других участников к комнате.

## Пакет образцового кода

Вы можете загрузить наш пакет образцового кода [здесь](https://github.com/tencentcloud-webar/web-demo-en). Образец кода находится в папке **TRTC_Web(5.x)**. Основные изменения, связанные с эффектами красоты, можно найти в папке **TRTC_Web(5.x)**, в частности в файлах quick-demo-js/index.html и quick-demo-js/js/index.js. Убедитесь, что вы заранее получили ключ TRTC и информацию о лицензии Web эффектов красоты.


---
*Источник: [https://trtc.io/document/67329](https://trtc.io/document/67329)*

---
*Источник (EN): [publishing-using-trtc-version-5x.md](./publishing-using-trtc-version-5x.md)*
