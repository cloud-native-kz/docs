# Пользовательский поток

Вы можете использовать этот режим интеграции, если хотите применить эффекты к собственным потокам или вам нужна большая гибкость и контроль.

### Шаг 1. Импортируйте SDK

- использование npm пакета:

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

### Шаг 2. Инициализируйте экземпляр

```
// Получите информацию аутентификацииconst authData = { licenseKey: 'xxxxxxxxx', appId: 'xxx', authFunc: authFunc // Подробнее см. в разделе «Конфигурирование и использование лицензии - Подпись»};// Входной потокconst stream = await navigator.mediaDevices.getUserMedia({ audio: true, video: { width: w, height: h }})const config = { module: {     beautify: true, // Следует ли включить модуль эффектов, который предлагает эффекты красоты и макияжа, а также стикеры     segmentation: true, // Следует ли включить модуль кеинга, который позволяет вам менять фон     segmentationLevel: 0 // Возможные значения: 0 | 1 | 2. Чем выше значение, тем лучше эффект сегментации, но это также увеличивает потребление ресурсов и требования к оборудованию устройства. }, auth: authData, // Информация аутентификации input: stream, // Входной поток beautify: { // Параметры эффектов для инициализации (опционально)     whiten: 0.1,     dermabrasion: 0.3,     eye: 0.2,     chin: 0,     lift: 0.1,     shave: 0.2,     // Дополнительные параметры красоты см. в разделе «Документация API» } // Дополнительные параметры конфигурации см. в разделе «Документация API»}const sdk = new ArSdk( // Передайте объект конфигурации для инициализации SDK config)
```

> **Примечание:** Загрузка модулей эффектов и сегментации требует времени и потребляет ресурсы. Вы можете включить только необходимый вам модуль во время инициализации. Модуль, который не включен, не будет загружен и инициализирован.

2. Для `input` вы также можете передать `string|HTMLImageElement` для обработки изображения и `HTMLVideoElement` для обработки видео.

```
const config = { auth: authData, // Информация аутентификации input: 'https://xxx.png', // Входной поток, также поддерживает элементы изображения и видео}const sdk = new ArSdk( // Передайте объект конфигурации для инициализации SDK config)// Вы можете отобразить список эффектов и фильтров в обратном вызове `created`. Подробнее см. в разделе «Интеграция SDK - Параметры и API».sdk.on('created', () => { // Получите встроенные эффекты макияжа sdk.getEffectList({     Type: 'Preset',     Label: 'Makeup', }).then(res => {     effectList = res }); // Получите встроенные фильтры sdk.getCommonFilter().then(res => {     filterList = res })})// Вызовите `setBeautify`, `setEffect` или `setFilter` в обратном вызове `ready`// Подробнее см. в разделе «Интеграция SDK - Конфигурирование эффектов»sdk.on('ready', () => { // Конфигурируйте эффекты красоты sdk.setBeautify({     whiten: 0.2 }); // Конфигурируйте специальные эффекты sdk.setEffect({     id: effectList[0].EffectId,     intensity: 0.7 }); // Конфигурируйте фильтры sdk.setFilter(filterList[0].EffectId, 0.5)})
```

### Шаг 3. Воспроизведите поток

- Если вы хотите отобразить видеоизображение как можно быстрее, получите и воспроизведите поток в обратном вызове `cameraReady`. Поскольку SDK еще не загрузил ресурсы и не завершил инициализацию на этом этапе, будет воспроизводиться исходное видео. Эффект будет применен автоматически после завершения инициализации SDK.

```
sdk.on('cameraReady', async () => {  // Получив выходной поток в обратном вызове `cameraReady`, вы можете отобразить видеоизображение быстрее. Однако, поскольку параметры инициализации еще не вступили в силу на этом этапе, полученный выходной поток будет таким же, как исходный поток.  // Вы можете выбрать этот метод, если хотите отобразить видеоизображение как можно скорее, но вам не нужно применять эффекты к видео в момент его отображения.  // Вам не нужно обновлять поток после начала работы эффектов.  const output = await ar.getOutput();  // Используйте `video` для предпросмотра выходного потока  const video = document.createElement('video')  video.setAttribute('playsinline', '');  video.setAttribute('autoplay', '');  video.srcObject = output  document.body.appendChild(video)  video.play()})
```

- Если вы хотите воспроизвести видео после инициализации SDK и применения эффектов, получите и воспроизведите выходной поток в обратном вызове `ready`.

```
sdk.on('ready', async () => {  // Если вы получаете выходной поток в обратном вызове `ready`, поскольку параметры инициализации вступили в силу на этом этапе, полученный выходной поток будет показывать эффекты.  // Обратный вызов `ready` происходит позже, чем `cameraReady`. Вы можете получить выходной поток в `ready`, если хотите, чтобы ваше видео показывало эффекты в момент его отображения, но не ожидаете, что оно будет отображено как можно скорее.  const output = await ar.getOutput();  // Используйте `video` для предпросмотра выходного потока  const video = document.createElement('video')  video.setAttribute('playsinline', '');  video.setAttribute('autoplay', '');  video.srcObject = output  document.body.appendChild(video)  video.play()})
```

### Шаг 4. Получите выходной поток

```
const output = await sdk.getOutput()
```

Для получения дополнительной информации о том, как публиковать обработанные потоки, см. [Publishing Using TRTC](https://www.tencentcloud.com/document/product/1143/53885) и [Publishing over WebRTC](https://www.tencentcloud.com/document/product/1143/53886).

> **Примечание:** Если переданное значение `input` является изображением, по умолчанию будет возвращена строка типа data URL. Вы можете установить getOutput(OUTPUT_TYPES.MEDIA_STREAM), чтобы принудительно установить тип возврата в MediaStream; другие сценарии входных данных всегда будут возвращать тип MediaStream. Видеодорожка выходного потока обрабатывается в реальном времени Tencent Effect SDK. Аудиодорожка (если присутствует) сохраняется. `getOutput` является асинхронным API. Выходной поток будет возвращен только после инициализации SDK и создания потока. Вы можете передать параметр `FPS` в `getOutput`, чтобы указать скорость кадров выходного потока (например, 15). Если вы не передадите этот параметр, исходная скорость кадров будет сохранена. Вы можете вызвать `getOutput` несколько раз для создания потоков с разными скоростями кадров для разных сценариев (например, вы можете использовать высокую скорость кадров для предпросмотра и низкую скорость кадров для публикации потока).

### Шаг 5. Конфигурирование эффектов

Подробные инструкции см. в разделе [Configuring Effects](https://www.tencentcloud.com/document/product/1143/54291).

## Обновление входного потока

Если вы хотите подать новый входной поток в SDK после смены устройства или включения/отключения камеры, вам не нужно инициализировать SDK повторно. Просто вызовите `sdk.updateInputStream` для обновления входного потока.

Следующий код показывает, как использовать `updateInputStream` для обновления входного потока при переключении с камеры по умолчанию компьютера на внешнюю камеру.

```
async function getVideoDeviceList(){    const devices = await navigator.mediaDevices.enumerateDevices()    const videoDevices = []    devices.forEach((device)=>{        if(device.kind === 'videoinput'){            videoDevices.push({                label: device.label,                id: device.deviceId            })        }    })    return videoDevices}async function initDom(){    const videoDeviceList = await getVideoDeviceList()    let dom = ''    videoDeviceList.forEach(device=>{        dom = `${dom}        <button id=${device.id} onclick='toggleVideo("${device.id}")'>${device.label}<nbutton>        `    })    const div = document.createElement('div');    div.id = 'container';    div.innerHTML = dom;    document.body.appendChild(div);}async function toggleVideo(deviceId){    const stream = await navigator.mediaDevices.getUserMedia({        video: {            deviceId,            width: 1280,            height: 720,          }    })    // Вызовите API, предоставленный SDK, для изменения входного потока.     // После обновления входного потока вам не нужно вызывать `getOutput` повторно. SDK получит выходной поток.    sdk.updateInputStream(stream, true) // Второй параметр по умолчанию имеет значение true, указывая, что старый mediaTrack будет остановлен; если вам нужно оставить его, установите значение false. }initDom()
```

## Приостановка и возобновление обнаружения

Вы можете вызвать `disable` и `enable` для ручной паузы и возобновления обнаружения. Пауза обнаружения может снизить использование CPU.

```
<button id="disable">Отключить обнаружение</button><button id="enable">Включить обнаружение</button>
```

```
// Отключить обнаружение и вывести исходный потокdisableButton.onClick = () => {    sdk.disable()}// Включить обнаружение и вывести обработанный потокenableButton.onClick = () => {    sdk.enable()}
```

## Воспроизведение и пауза выходного экрана

Вы можете использовать методы `stop` и `resume` для паузы и воспроизведения выходного экрана. В состоянии паузы экран остается статичным и воспроизведение останавливается.

```
<button id="stop">stop</button><button id="resume">resume</button>
```

```
// Остановить выводstopButton.onClick = () => {    sdk.stop()}// Возобновить выводresumeButton.onClick = () => {    sdk.resume()}
```


---
*Источник: [https://trtc.io/document/50102](https://trtc.io/document/50102)*

---
*Источник (EN): [custom-stream.md](./custom-stream.md)*
