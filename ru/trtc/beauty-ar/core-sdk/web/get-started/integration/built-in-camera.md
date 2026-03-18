# Встроенная камера

Вы можете выбрать этот режим интеграции, если хотите использовать SDK со встроенной камерой устройства или если ваш сценарий бизнеса предполагает взаимодействие со встроенной камерой.

## Шаг 1. Импорт SDK

- используйте npm-пакет:

```
npm install tencentcloud-webar
```

```
import { ArSdk } from 'tencentcloud-webar';
```

- вы также можете импортировать SDK следующим способом:

```
<script charset="utf-8" src="https://webar-static.tencent-cloud.com/ar-sdk/resources/latest/webar-sdk.umd.js"></script><script>    // Получите класс ArSdk из window.AR    const { ArSdk } = window.AR;    ......</script>
```

## Шаг 2. Инициализация экземпляра

```
// Получите информацию аутентификацииconst authData = {    licenseKey: 'xxxxxxxxx',    appId: 'xxx',    authFunc: authFunc // Дополнительно см. «Настройка и использование лицензии - Подпись»};const config = {    module: {        beautify: true, // Включить ли модуль эффектов, который предоставляет эффекты красоты и макияжа, а также стикеры        segmentation: true, // Включить ли модуль keying, который позволяет изменять фон        segmentationLevel: 0 // Допустимые значения: 0 | 1 | 2. Чем выше значение, тем лучше качество segmentation, но это также увеличивает потребление ресурсов и требования к оборудованию устройства.    },    auth: authData, // Информация аутентификации    camera: { // Передайте параметры камеры        width: 1280,        height: 720    },    beautify: { // Параметры эффектов для инициализации (опционально)        whiten: 0.1,        dermabrasion: 0.3,        eye: 0.2,        chin: 0,        lift: 0.1,        shave: 0.2,        // Дополнительные параметры красоты см. в документе «API Documentation»    },    // Дополнительные параметры config см. в документе «API Documentation»}const sdk = new ArSdk(    // Передайте объект config для инициализации SDK    config)let effectList = [];let filterList = [];sdk.on('created', () => {    // Вы можете отобразить список эффектов и фильтров в callback `created`. Дополнительно см. «SDK Integration - Parameters and APIs».    sdk.getEffectList({        Type: 'Preset',        Label: 'Makeup',    }).then(res => {        effectList = res    });    sdk.getCommonFilter().then(res => {        filterList = res    })})// Вызовите `setBeautify`, `setEffect` или `setFilter` в callback `ready`// Дополнительно см. «SDK Integration - Configuring Effects»sdk.on('ready', () => {    // Настройте эффекты красоты    sdk.setBeautify({        whiten: 0.2    });    // Настройте специальные эффекты    sdk.setEffect({        id: effectList[0].EffectId,        intensity: 0.7    });    // Настройте фильтры    sdk.setFilter(filterList[0].EffectId, 0.5)})
```

> **Примечание:**загрузка модулей эффектов и keying требует времени и потребляет ресурсы. Вы можете включить только необходимый вам модуль при инициализации. Модуль, который не включен, не будет загружен или инициализирован.Если вы указываете параметр `camera` в `config`, видеоданные, которые SDK захватывает с камеры устройства, будут использоваться в качестве входа. Мы также предоставляем некоторые базовые API управления устройствами. Дополнительно см. [Шаг 6. Управление устройствами](#step6).

## Шаг 3. Воспроизведение потока

- Если вы хотите отобразить видеоизображение как можно скорее, получите плеер в callback `cameraReady`. Поскольку SDK еще не загрузил ресурсы или не завершил инициализацию на этом этапе, плеер может воспроизводить только исходное видео.

```
sdk.on('cameraReady', async () => {  // Инициализируйте плеер SDK. `my-dom-id` — это ID контейнера плеера.  const player = await sdk.initLocalPlayer('my-dom-id')  // Воспроизведите видео  await player.play()})
```

- Если вы хотите воспроизвести видео после инициализации SDK и применения эффектов, получите плеер в callback `ready`.

```
sdk.on('ready', async () => {  // Инициализируйте плеер SDK. `my-dom-id` — это ID контейнера плеера.  const player = await sdk.initLocalPlayer('my-dom-id')  // Воспроизведите видео  await player.play()})
```

> **Примечание:**плеер, полученный `initLocalPlayer`, по умолчанию отключен по звуку. Если вы включите звук, могут возникнуть эхо.Полученный плеер интегрирован с API `sdk.getOutput()`.

Объект плеера, полученный `initLocalPlayer`, интегрирован со следующими API:

| API | Описание | Параметр запроса | Возвращаемое значение |
| --- | --- | --- | --- |
| play | Воспроизводит видео. | - | Promise; |
| pause | Приостанавливает видео. Это не останавливает поток. Вы можете возобновить воспроизведение. | - | - |
| stop | Останавливает видео. Это останавливает поток. | - | - |
| mute | Отключает звук видео. | - | - |
| unmute | Включает звук видео. | - | - |
| setMirror | Устанавливает зеркальное отображение видео. | true\|false | - |
| getVideoElement | Получает встроенный объект видео. | - | HTMLVideoElement |
| destroy | Завершает плеер. | - | - |

> **Примечание:**поведение плеера зависит от [настроек камеры](#step6). Настройки камеры имеют приоритет над настройками `LocalPlayer`.Например, после вызова `camera.muteVideo` для отключения видео воспроизведение не начнется, даже если вы вызовете `play`.После вызова `camera.unmuteVideo` для включения видео плеер автоматически воспроизведет видео.
> Поэтому, если вы указываете `camera`, вам не нужно вручную настраивать `localPlayer`.

## Шаг 4. Получение вывода

```
const output = await sdk.getOutput()
```

> **Примечание:**если вы используете встроенную камеру, тип всех медиа, возвращаемых `getOutput`, — это `MediaStream`.видеодорожка выходного потока обрабатывается в реальном времени Tencent Effect SDK. Аудиодорожка (если присутствует) сохраняется.`getOutput` — это асинхронный API. Вывод будет возвращен только после инициализации SDK и создания потока.Вы можете передать параметр `FPS` в `getOutput` для указания частоты кадров вывода (например, 15). Если вы не передаете этот параметр, будет сохранена исходная частота кадров.Дополнительно о публикации обработанных потоков см. в документах [Publishing Using TRTC](https://www.tencentcloud.com/document/product/1143/53885) и [Publishing over WebRTC](https://www.tencentcloud.com/document/product/1143/53886).

## Шаг 5. Настройка эффектов

Подробные инструкции см. в документе [Configuring Effects](https://www.tencentcloud.com/document/product/1143/54291).

## Шаг 6. Управление устройствами

```
const output = await sdk.getOutput()// Ваша бизнес-логика// ...// `sdk.camera` будет инициализирован после `getOutput`. Вы можете получить экземпляр напрямую.const cameraApi = sdk.camera// Получите список устройств const devices = await cameraApi.getDevices()console.log(devices)// Отключите видеодорожку// cameraApi.muteVideo()// Включите видеодорожку// cameraApi.unmuteVideo()// Переключитесь на другую камеру, указав ID устройства (если есть несколько камер)// await cameraApi.switchDevice('video', 'your-device-id')
```

Если вы хотите получить экземпляр `sdk.camera` как можно скорее, вы можете получить его в callback `cameraReady`.

```
// Параметры инициализации// ...const sdk = new ArSdk(    config)let cameraApi;sdk.on('cameraReady', async () => {    cameraApi = sdk.camera    // Получите список устройств    const devices = await cameraApi.getDevices()    console.log(devices)    // Отключите видеодорожку    // cameraApi.muteVideo()    // Включите видеодорожку    // cameraApi.unmuteVideo()    // Переключитесь на другую камеру, указав ID устройства (если есть несколько камер)    // await cameraApi.switchDevice('video', 'your-device-id')})
```

Вы можете использовать следующие API `camera` для управления встроенной камерой.

| API | Описание | Параметр запроса | Возвращаемое значение |
| --- | --- | --- | --- |
| getDevices | Получает все устройства. | - | Promise<Array<MediaDeviceInfo>> |
| switchDevice | Переключает устройство. | type:string, deviceId:string | Promise |
| muteAudio | Отключает звук текущего потока. | - | - |
| unmuteAudio | Включает звук текущего потока. | - | - |
| muteVideo | Отключает видеодорожку потока камеры. Это не останавливает поток. | - | - |
| unmuteVideo | Включает видео потока камеры. | - | - |
| stopVideo | Отключает камеру. Это останавливает видеопоток, но аудиопоток не затрагивается. | - | - |
| restartVideo | Включает камеру. Этот API можно вызывать только после `stopVideo`. | - | Promise |
| stop | Отключает текущую камеру и устройство воспроизведения звука. | - | - |


---
*Источник: [https://trtc.io/document/50101](https://trtc.io/document/50101)*

---
*Источник (EN): [built-in-camera.md](./built-in-camera.md)*
