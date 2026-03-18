# Оптимизация загрузки

## Обычный режим

В отличие от этого, если вы вызываете `getOutput` в обратном вызове `ready`, полученный выходной поток будет обработан. Поскольку обратный вызов `ready` происходит позже `cameraReady`, вы можете вызвать `getOutput` в обратном вызове `ready`, если хотите применить эффекты к видео в момент его отображения, но не ожидайте, что видео будет воспроизведено как можно скорее.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/4012eb46bf3e11ee9976525400c26da5.jpeg)

Пример кода:

```
// Get the authentication informationconst authData = {    licenseKey: 'xxxxxxxxx',    appId: 'xxx',    authFunc: authFunc // For details, see âConfiguring and Using a License - Signatureâ};// When initializing the SDK in regular mode, pass in the input or camera parametersconst config = {    auth: authData, // The authentication information    beautify: { // The effect parameters        whiten: 0.1,        dermabrasion: 0.5,        lift: 0,        shave: 0,        eye: 0.2,        chin: 0,    },    input: inputStream // Prepare the stream data fed into the SDK as the input. For details, see âSDK Integration - Parameters and APIsâ.}const sdk = new ArSdk(    // Pass in a config object to initialize the SDK    config)// After authentication succeeds, the SDK will trigger the `created` callback immediatelysdk.on('created', () => {    // Pull and display the filter and effect list in the `created` callback    sdk.getEffectList({        Type: 'Preset',        Label: 'Makeup',    }).then(res => {        effectList = res    });    sdk.getCommonFilter().then(res => {        filterList = res    })})// The data you get by calling `getOutput` in different callbacks vary slightly. Choose the one that fits your needs.sdk.on('cameraReady', async () => {    const output = await sdk.getOutput() // The effect parameters have not taken effect    // Play the stream    ...})sdk.on('ready', async () => {    const output = await sdk.getOutput() // The effect parameters have taken effect    // Play the stream    ...    // Call `setBeautify`, `setEffect`, or `setFilter` in the `ready` callback})
```

## Предварительная инициализация

При первой загрузке SDK требуется загрузить статические ресурсы для инициализации модуля обнаружения. В результате загрузка SDK зависит от условий сети. Учитывая, что в некоторых сценариях вам может потребоваться отобразить видеоизображение как можно скорее, мы предлагаем план предварительной инициализации, который загружает статические ресурсы заранее.

**Случаи использования предварительной инициализации**

- Случай 1: SDK эффектов не требуется при инициализации веб-страницы. Видео отображается только после выполнения пользователем определённого действия.
- Случай 2: Эффекты требуются для страницы B, а на страницу B осуществляется переход со страницы A.

В таких случаях вы можете загрузить ресурсы заранее (как можно раньше), передать входной поток в SDK при необходимости, а затем получить обработанный выходной поток.

Например, в случае 1 вы можете загрузить ресурсы при инициализации веб-страницы; в случае 2 вы можете получить экземпляр SDK на странице A и передать его на страницу B.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/626650740ce511efafb0525400493f3c.jpg)

**Приведённый ниже код работает для случая 1**

```
<button id="start">Enable the camera</button>
```

```
// Get the authentication informationconst authData = {    licenseKey: 'xxxxxxxxx',    appId: 'xxx',    authFunc: authFunc // For details, see âConfiguring and Using a License - Signatureâ};// Do not pass in the input or camera parameters when initializing the SDK. After an instance is obtained, the SDK will start loading the necessary resources.const config = {    auth: authData, // The authentication information    beautify: { // The effect parameters        whiten: 0.1,        dermabrasion: 0.5,        lift: 0,        shave: 0,        eye: 0.2,        chin: 0,    },}const sdk = new ArSdk(    // Pass in a config object to initialize the SDK    config)// After authentication succeeds, the SDK will trigger the `created` callback immediatelysdk.on('created', () => {    // Pull and display the filter and effect list in the `created` callback    sdk.getEffectList({        Type: 'Preset',        Label: 'Makeup',    }).then(res => {        effectList = res    });    sdk.getCommonFilter().then(res => {        filterList = res    })})// `resourceReady` indicates that the necessary resources are ready. After receiving this callback, you can call `initCore` to feed an input stream to the SDK.sdk.on('resourceReady', () => {})// In this mode, the SDK will trigger the `ready` callback only after `initCore` is called.sdk.on('ready', async () => {    const output = await sdk.getOutput() // The effects have been applied.    // Play the stream    ...    // Call `setBeautify`, `setEffect`, or `setFilter` in the `ready` callback})// Feed stream data to the SDK when the user turns the camera ondocument.getElementById('start').onclick = async function(){    const devices = await navigator.mediaDevices.enumerateDevices()    const cameraDevice = devices.find(d=>d.kind === 'videoinput')    navigator.mediaDevices.getUserMedia({        audio: false,        video: {            deviceId: cameraDevice.deviceId            ... // Other configuration        }    }).then(mediaStream => {        // In this mode, make sure you call `initCore` after the `resourceReady` callback.        sdk.initCore({            input: mediaStream // Prepare the stream data fed into the SDK as the input. For details, see âSDK Integration - Parameters and APIsâ.        })    })    }
```


---
*Источник: [https://trtc.io/document/50103](https://trtc.io/document/50103)*

---
*Источник (EN): [loading-optimization.md](./loading-optimization.md)*
