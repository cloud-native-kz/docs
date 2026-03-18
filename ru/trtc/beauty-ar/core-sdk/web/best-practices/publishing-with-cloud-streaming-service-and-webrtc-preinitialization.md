# Публикация с использованием Cloud Streaming Service и WebRTC (предварительная инициализация)

## Подготовка

- Прочитайте [Обзор](https://www.tencentcloud.com/document/product/1143/50099), чтобы узнать, как использовать Beauty AR Web SDK.
- Дополнительную информацию о публикации WebRTC см. в [Публикация по WebRTC](https://www.tencentcloud.com/document/product/1143/53886). В этом документе описаны различия в коде и процессе при использовании схемы предварительной инициализации.
- Дополнительную информацию о схеме предварительной инициализации см. в [Оптимизация загрузки](https://www.tencentcloud.com/document/product/1143/50103).

## Начало работы

Схема предварительной инициализации отличается от общей схемы загрузки главным образом тем, что при инициализации SDK не требуется указывать атрибуты `input` или `camera`. То есть вместо указания входных данных для SDK при инициализации, вы позже вызываете API `initCore` для указания данных в подходящем месте на основе ваших потребностей. Таким образом, ресурсы, необходимые для SDK, загружаются заранее, и событие `ready` SDK будет срабатывать быстрее после последующего вызова `initCore`, что облегчает получение и отображение выходного потока. Ниже приведен ключевой образец кода:

### Инициализация SDK

```
...let resourceReady = false// Основные параметры конфигурации Beauty AR SDKconst config = {    // input: stream, // Не указывайте `input`.    auth: {        licenseKey: LICENSE_KEY,        appId: APPID,        authFunc: getSignature    },    // Начальные эффекты красоты (необязательные параметры)    beautify: {        whiten: 0.1, // Эффект осветления. Диапазон значений: 0–1.        dermabrasion: 0.5, // Эффект гладкой кожи. Диапазон значений: 0–1.        lift: 0.3, // Эффект стройного лица. Диапазон значений: 0–1.        shave: 0, // Эффект V-образной формы. Диапазон значений: 0–1.        eye: 0, // Эффект больших глаз. Диапазон значений: 0–1.        chin: 0, // Эффект формирования подбородка. Диапазон значений: 0–1.        ……    },    language: 'en'}// Передайте `ar sdk` для `config`.const ar = new ArSdk(config);// Если событие обратного вызова `resourceReady` срабатывает, ресурсы полностью загружены, и вам нужно дождаться `initCore` для предоставления входных данных.ar.on('resourceReady', () => {    resourceReady = true})// Событие `ready` будет срабатывать после вызова `initCore`.ar.on('ready', () => {    // Получите выходной поток данных Beauty AR SDK    const arStream = await ar.getOutput();    // Обработайте выходной поток    ...})...
```

### Срабатывание события `initCore` при действии пользователя

```
// Ниже описано, как установить входной поток для схемы предварительной инициализации на примере, где пользователь включает камеру.function onClickStartCamera(){    let w = 1280;    let h = 720;    // Получите входной поток устройства    const arInputStream = await navigator.mediaDevices.getUserMedia({        audio: true,        video: {            width: w,            height: h        }    });    if(!resourceReady){ // В этом режиме вызов `initCore` не будет иметь эффект, если `resourceReady` не срабатывает, и вы можете выполнить некоторую настройку.        return    }    // Установите входной поток данных Beauty AR SDK    ar.initCore({        input: arInputStream    })}
```

## Образец кода

Вы можете загрузить [образец кода](https://github.com/tencentcloud-webar/web-demo-en), распаковать его и просмотреть файл `AR_and_LEB_Preload.html` в директории кода `AR_LEB_WEB`.


---
*Источник: [https://trtc.io/document/53940](https://trtc.io/document/53940)*

---
*Источник (EN): [publishing-with-cloud-streaming-service-and-webrtc-preinitialization.md](./publishing-with-cloud-streaming-service-and-webrtc-preinitialization.md)*
