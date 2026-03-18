# Документация API

В этом документе описаны основные параметры и методы Beauty AR Web SDK.

> **Примечание:** Beauty AR Web SDK использует аппаратное ускорение для достижения плавного воспроизведения. SDK позволяет проверить, поддерживает ли браузер аппаратное ускорение. Вы можете заблокировать браузер, если он не поддерживает аппаратное ускорение.

```
import {ArSdk, isWebGLSupported} from 'tencentcloud-webar'if(isWebGLSupported()) {    const sdk = new ArSdk({    ...})} else {    // The browser blocking logic}
```

## Параметры инициализации

```
import { ArSdk } from 'tencentcloud-webar'// Initialize the SDKconst sdk = new ArSdk({... // Refer to the following Config definition})
```

Параметр `Config` SDK поддерживает следующие параметры инициализации:

| Параметры | Описание | Тип | Обязательный |
| --- | --- | --- | --- |
| module | Конфигурация модуля | type SegmentationLevel = 0 \| 1 \| 2 // since version 1.0.19 type ModuleConfig = {  beautify: boolean // По умолчанию — `true`.  segmentation: boolean // По умолчанию — `false`  segmentationLevel: SegmentationLevel // По умолчанию — 0.  handGesture: boolean // Включить ли распознавание жестов, по умолчанию false. Поддерживается в версиях после 1.0.23.  handLandmark: boolean // Включить ли отслеживание рук, по умолчанию false. Поддерживается в версиях после 1.0.23. Не рекомендуется включать одновременно с beautify.} | Нет. По умолчанию установлено значение `{beautify: true, segmentation: false, segmentationLevel: 0,handLandmark: false}`. |
| auth | Параметр аутентификации | type AuthConfig = {  licenseKey: string // Можно получить на странице **Web licenses** в консоли.  appId: string // Можно посмотреть в разделе **Account Info** > **Basic Info** в консоли.  authFunc:() => Promise<{    signature:string,    timestamp:string  }> // См. конфигурацию лицензии.} | Да |
| input | Источник | MediaStream \| HTMLImageElement \| String \| HTMLVideoElement | Нет |
| camera | Встроенная камера | type CameraConfig = {    width: number, // Ширина видео.    height: number, // Высота видео.    mirror: boolean, // Отразить ли видео по горизонтали.    frameRate: number // Частота захвата кадров.} | Нет |
| mirror | Отражено или нет, поддерживается зеркалирование входных потоков.(поддерживается с 1.0.19) | Boolean | Нет |
| beautify | Параметр фильтра красоты | type BeautifyOptions = {      whiten?: number, // Эффект отбеливания. Диапазон значений: 0-1.       dermabrasion?: number // Эффект гладкой кожи. Диапазон значений: 0-1.       lift?: number // Эффект стройного лица. Диапазон значений: 0-1.       shave?: number // Ширина лица. Диапазон значений: 0-1.       eye?: number // Эффект больших глаз. Диапазон значений: 0-1.       chin?: number // Эффект подбородка. Диапазон значений: 0-1.    // Следующие параметры доступны только с версии 1.0.11       darkCircle?: number; // Эффект темных кругов. Диапазон значений: 0-1.       nasolabialFolds?: number; // Эффект носогубных складок. Диапазон значений: 0-1.       cheekbone?: number; // Эффект скул. Диапазон значений: 0-1.       head?: number; // Эффект головы. Диапазон значений: 0-1.       eyeBrightness?: number; // Эффект яркости глаз. Диапазон значений: 0-1.       lip?: number; // Эффект губ. Диапазон значений: 0-1.       forehead?: number; // Эффект лба. Диапазон значений: 0-1.       nose?: number; // Эффект носа. Диапазон значений: 0-1.       usm?: number; // Эффект четкости. Диапазон значений: 0-1.} | Нет |
| background | Параметр фона | type BackgroundOptions = {    type: 'image' \| 'blur' \| 'transparent' \| 'video',  // с версии 1.0.23 поддерживается динамический фон видеотипа.    src?: string, // адрес файла image \| video} | Нет |
| loading | Конфигурация встроенного значка загрузки | type loadingConfig = {    enable: boolean,    size?: number    lineWidth?: number    strokeColor?: number} | Нет |
| language | i18n, поддерживается 'jp' с версии 1.0.26 | String: zh \| en \| jp | Нет, по умолчанию 'zh' |
| logLevel | Уровень печати журнала консоли | 'OFF' \| 'ERROR' \| 'WARN' \| 'DEBUG' \| 'TRACE' \| 'INFO' | Нет, по умолчанию INFO, выводит все логи SDK |
| initReport | Инициализировать ли модуль отчетности журнала | Boolean | Нет, по умолчанию true |
| worker | Отключить ли worker браузера для оптимизации производительности в конкретных сценариях. | String: auto \| disable | Нет, по умолчанию auto, SDK определяет, использовать ли workers в зависимости от текущей среды браузера. |
| proxyServer | Использование режима прокси интрасети | type proxyServeConfig = {  webarProxy: string; // Адрес интрасети прокси интерфейса  staticProxy: string; // Адрес интрасети прокси ресурса} | Нет |

## Обратные вызовы

```
let effectList = [];let filterList = [];// Using the callbacks of the SDKsdk.on('created', () => {    // Pull and display the filter and effect list in the `created` callback    sdk.getEffectList({        Type: 'Preset',        Label: 'Makeup',    }).then(res => {        effectList = res    });    sdk.getCommonFilter().then(res => {        filterList = res    })})sdk.on('cameraReady', async () => {    // By getting the output stream in the `cameraReady` callback, you can display a video image sooner, but the initialization parameters have not taken effect at this point.    // You can choose this method if you want to display a video image as soon as possible but do not need to apply effects to the video the moment it is displayed.    // You donât need to update the stream after the effects start to work.    const arStream = await ar.getOutput();    // Play the stream locally    // localVideo.srcObject = arStream})sdk.on('ready', () => {    // Get the output stream in the `ready` callback. The initialization parameters have taken effect at this point.    // You can get the output stream in `ready` if you want your video to show effects the moment it is displayed but do not expect it to be displayed as soon as possible.    // Between the two methods, choose the one that fits your needs.    const arStream = await ar.getOutput();    // Play the stream locally    // localVideo.srcObject = arStream    // Call `setBeautify`, `setEffect`, or `setFilter` in the `ready` callback    sdk.setBeautify({        whiten: 0.3    });    sdk.setEffect({        id: effectList[0].EffectId,        intensity: 0.7    });    sdk.setEffect({        id: effectList[0].EffectId,        intensity: 0.7,        filterIntensity: 0.5 // In v0.1.18 and later, you can use this parameter to set the filter strength of a special effect. If you do not pass this parameter, the strength specified for the effect will be used.    });    sdk.setFilter(filterList[0].EffectId, 0.5)})// Triggered when a change in gesture is detected after enabling gesture recognitionsdk.on('handGesture',(hands)=>{    // none, thumb_up, thumb_down, victory, pointing_up, open_palm, iloveyou})// Error callback that affects the occurrence of errors during SDK usagesdk.on('error', (data)=>{    console.log('error', data.code, data.message)})// Warning callback, commonly triggered by the SDK when it detects an increase in time consumption.sdk.on('warning', (data)=>{    console.log('warning', data.code, data.message)})
```

| События | Описание | Параметр обратного вызова |
| --- | --- | --- |
| created | Аутентификация SDK завершена, экземпляр успешно создан. | - |
| cameraReady | SDK создал выходной поток видео (видео еще не обработано). | - |
| ready | Обнаружение инициализировано. Эффекты теперь применяются к выходному видео. Вы можете изменить параметры эффектов. | - |
| error | Этот обратный вызов срабатывает при возникновении ошибки в SDK. | Объект `error` |
| warning | Этот обратный вызов срабатывает при возникновении предупреждения в SDK. | Объект `warning` |
| handGesture | Срабатывает при обнаружении изменения жеста после включения распознавания жестов | Распознанный жест |
| detectStatusChange | Срабатывает при изменении статуса обнаружения лица. | Boolean, обнаружено ли лицо |

## API

| API | Параметры | Возврат | Описание |
| --- | --- | --- | --- |
| setBeautify(options) | type BeautifyOptions = {  whiten?: number, // Эффект отбеливания. Диапазон значений: 0-1.  dermabrasion?: number // Эффект гладкой кожи. Диапазон значений: 0-1.  lift?: number // Эффект стройного лица. Диапазон значений: 0-1.  shave?: number // Ширина лица. Диапазон значений: 0-1.  eye?: number // Эффект больших глаз. Диапазон значений: 0-1.  chin?: number // Эффект коррекции подбородка. Диапазон значений: 0-1.  darkCircle?: number; // Эффект темных кругов. Диапазон значений: 0-1.  nasolabialFolds?: number; // Эффект носогубных складок. Диапазон значений: 0-1.  cheekbone?: number; // Эффект скул. Диапазон значений: 0-1.  head?: number; // Эффект головы. Диапазон значений: 0-1.  eyeBrightness?: number; // Эффект яркости глаз. Диапазон значений: 0-1.  lip?: number; // Эффект губ. Диапазон значений: 0-1.  forehead?: number; // Эффект лба. Диапазон значений: 0-1.  nose?: number; // Эффект носа. Диапазон значений: 0-1.  usm?: number; // Эффект четкости. Диапазон значений: 0-1.} | - | Этот API используется для установки параметра фильтра красоты. Необходимо включить модуль фильтра красоты. |
| setEffect(effects, callback) | effects: ID эффекта \| Объект эффекта \| Массив (ID эффекта \| Объекта эффекта)type Effect = {    id: string,    intensity: number, // Интенсивность эффекта. Диапазон значений: 0-1. По умолчанию: 1.    filterIntensity: number // Интенсивность фильтра эффекта (поддерживается в v0.1.18 и позже). Диапазон значений: 0-1. По умолчанию этот параметр совпадает с `intensity`.}callback: Обратный вызов успешной конфигурации | - | Этот API используется для установки эффекта. Необходимо включить модуль фильтра красоты.**3D эффекты поддерживаются только лицензиями Advanced.** |
| setAvatar(params) | {    mode: 'AR' \| 'VR',    effectId?: string, // Передайте `effectId` для использования встроенной модели    url?: string, // Передайте `url` для использования пользовательской модели    backgroundUrl?: string, // URL фонового изображения, применяется только в режиме VR.} | - | Этот API используется для установки анимодзи или виртуального аватара. Необходимо включить модуль фильтра красоты.**Поддерживается только лицензиями Advanced** |
| setBackground(options) | {    type: 'image\|video\|blur\|transparent', // с версии 1.0.23 поддерживается динамический фон видеотипа.    src: string, // Этот параметр требуется только если `type` — `image` или `video`.} | - | Для конфигурации фона необходимо активировать модуль сегментации портрета. |
| setForeground(options)**（С версии 1.0.23）** | {    type: 'image\|video',    src: string // Путь ресурса: Base64 или онлайн-URL} | - | Установить фиксированный эффект переднего плана на весь экран. |
| setSegmentationLevel(level) | level: 0 \| 1 \| 2 | - | Переключить модель сегментации фона |
| setFilter(id, intensity, callback) | id: ID фильтраintensity: Интенсивность фильтра. Диапазон значений: 0 - 1.callback: Обратный вызов успешной конфигурации. | - | Этот API используется для установки фильтра. |
| getEffectList(params) | {    PageNumber: number, // номер страницы, по умолчанию 0    PageSize: number,// размер страницы, по умолчанию 1000    Name: '', // имя эффекта    Label: string \| Array, // метка эффекта    Type: 'Custom' \| 'Preset' // Пользовательский эффект или предустановленный эффект} |  | Этот API используется для получения списка эффектов. |
| getAvatarList(type) | type = 'AR' \| 'VR' | Список виртуальных аватаров | Получить список Анимодзи/виртуальных аватаров. |
| getEffect(effectId) | effectId: ID эффекта | Информация об одном эффекте | Этот API используется для получения информации об указанном эффекте. |
| getCommonFilter() | - | Список встроенных фильтров | Этот API используется для получения списка встроенных фильтров. |
| async initCore() |  {  input?:MediaStream\|HTMLImageElement\|String; // Входной источник   camera?:CameraConfig; // Только для режима камеры  mirror?:boolean;  // Отразить или нет} | - | Только для сценариев предварительной инициализации, предоставляет SDK информацию о входе. Подробнее см. [Loading Optimization](https://www.tencentcloud.com/document/product/1143/50103) |
| async updateInputStream(src, stopOldTracks) | src: Новый входной поток (`MediaStream`)stopOldTracks: остановить старый MediaTrack или нет, по умолчанию true | - | Этот API используется для обновления входного потока. |
| updateInputImage(options)**（с версии 1.0.24）** | {width: number;// ширина рендеринга изображенияheight: number; // высота рендеринга изображенияinput: string;// источник изображения} | - | Обновить входное изображение |
| async getOutput(fps:number,type:OUTPUT_TYPES) | enum OUTPUT_TYPES {  IMAGE = 3,  MEDIA_STREAM = 4,}fps (необязательный): Частота кадров вывода, по умолчанию совпадает с частотой входного медиа.type(необязательный):  3 \| 4 // 3 для изображения, 4 для потока мультимедиа. Вывод по умолчанию 3, если входное изображение, и по умолчанию 4, если входное не изображение. | MediaStream\|String | - |
| disable() | - | - | Этот API используется для отключения обнаружения лиц, что может снизить использование CPU. После отключения будет возвращен исходный поток. |
| enable() | - | - | Этот API используется для включения обнаружения лиц. После включения возвращаемый поток будет обработан. |
| stop() | - | - | Приостановить экран, экран замерзает. |
| resume() | - | - | Возобновить экран, экран воспроизводится. |
| async takePhoto() | - | {    data: Uint8Array,     width: number,     height: number} | Этот API используется для съемки фотографии и возвращает объект, содержащий данные буфера. |
| async initLocalPlayer(id) | id: string // HTML DOM id для локального просмотра. | - | Позволить выходному потоку мультимедиа SDK воспроизводиться в указанном контейнере DOM как видео. |
| async resetCore(input) | input: MediaStream\|HTMLImageElement\|String | - | Вызовите этот API для восстановления при возникновении ошибки потери контекста. |
| destroy() | - | - | Этот API используется для завершения текущего экземпляра SDK и соответствующих ресурсов текстуры. |

## Обработка ошибок

Объект ошибки, возвращаемый обратным вызовом ошибки, включает код ошибки и сообщение об ошибке, которые облегчают устранение неполадок.

```
sdk.on('error', (error) => {    // Handle an error in the error callback    const {code, message} = error    ...})
```

| Код ошибки | Описание | Замечания |
| --- | --- | --- |
| 10000001 | Текущая среда браузера несовместима. | Рекомендуется использовать Chrome, Firefox, Safari или браузер Weixin. |
| 10000002 | Контекст рендеринга отсутствует. | - |
| 10000003 | Рендеринг происходит медленно. | Рассмотрите возможность снижения разрешения видео или отключения функции. |
| 10000005 | Ошибка при анализе входного источника. | - |
| 10000006 | Могут возникнуть задержки из-за недостаточной поддержки браузером. | Рекомендуется использовать Chrome, Firefox, Safari или браузер Weixin. |
| 10001101 | Ошибка при конфигурации эффекта. | - |
| 10001102 | Ошибка при конфигурации фильтра. | - |
| 10001103 | Параметр интенсивности эффекта неправильный. | - |
| 10001104 | sdk отключен, невозможно установить эффекты | - |
| 10001105 | Неверный ID эффекта | - |
| 10001201 | Ошибка при включении камеры. | - |
| 10001202 | Камера остановлена. | - |
| 10001203 | Ошибка при получении разрешения камеры. | Пользователю необходимо включить разрешение камеры в разделе **Settings** > **Privacy** > **Camera**. |
| 10001204 | Не удается получить доступ к устройствам мультимедиа (несмотря на авторизацию). | Не удалось найти тип медиа, соответствующий параметрам запроса, или системная ошибка препятствует доступу к устройству. |
| 10001205 | Разрешение микрофона не допустимо | Пользователю необходимо включить разрешение микрофона в разделе **Settings** > **Privacy** > **Microphone**. |
| 10001206 | В некоторых браузерах могут быть расхождения между шириной и высотой, возвращаемыми интерфейсом getUserMedia, и параметрами пользователя. | - |
| 10004001 | Проблемы с разрешением камеры и микрофона требуют обновления страницы для продолжения использования. | - |
| 20002001 | Параметр аутентификации отсутствует. | - |
| 20001001 | Ошибка аутентификации | Убедитесь, что вы создали лицензию и подпись правильна. |
| 20001002 | Ошибка запроса API. | Обратный вызов ошибки вернет данные, возвращаемые API. Подробнее см. [API Error Codes](https://www.tencentcloud.com/document/product/1143/50107). |
| 20001003 | Ошибка аутентификации интерфейса параметров эффектов | Доступ к этому эффекту запрещен; стандартная лицензия не может использовать функции Advanced License. |
| 20001004 | Истечение срока действия подписи | Истечение срока действия подписи, и ошибка все еще возникает после повторного попытки. |
| 20001005 | Истечение срока авторизации | Истечение срока авторизации, и ошибка все еще возникает после повторного попытки. |
| 40000000 | Произошло необработанное исключение. | - |
| 40000001 | Так как текущая версия SDK слишком низка, некоторые эффекты не могут отображаться правильно. Обновите версию SDK. | - |
| 50000002 | Эффект потерян из-за изменения разрешения. | Эффект необходимо переконфигурировать. |

### Обработка предупреждений

Объект, возвращаемый в обратном вызове предупреждения, содержит код предупреждения и сообщение о предупреждении.

```
sdk.on('warning', (warning) => {    // Handle a warning in the warning callback    const {code, message} = warning    ...})
```

| Код ошибки | Описание | Замечания |
| --- | --- | --- |
| 50005 | Обнаружение заняло слишком много времени. | Динамический мониторинг: предупреждение выдается, когда время обработки одного кадра превышает 150 мс, что указывает на то, что частота кадров рендеринга падает ниже 10 fps, что приводит к заиканию. |

### Обработка ошибки отсутствия контекста рендеринга

На некоторых компьютерах, если SDK находится в фоне длительное время, может возникнуть ошибка `contextlost`. В таких случаях вы можете вызвать `ArSdk.prototype.resetCore(input: MediaStream)` для возобновления рендеринга.

```
sdk.on('error', async (error) => {    if (error.code === 10000002) {        const newInput = await navigator.mediaDevices.getUserMedia({...})        await sdk.resetCore(newInput)    }})
```


---
*Источник: [https://trtc.io/document/50106](https://trtc.io/document/50106)*

---
*Источник (EN): [api-document.md](./api-document.md)*
