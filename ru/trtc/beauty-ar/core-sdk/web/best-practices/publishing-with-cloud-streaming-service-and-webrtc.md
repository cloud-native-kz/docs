# Публикация с использованием Cloud Streaming Service и WebRTC

## Перед началом

- Ознакомьтесь с [руководством интеграции](https://www.tencentcloud.com/document/product/1143/50099) для Beauty AR Web.
- Ознакомьтесь с [Начало работы](https://www.tencentcloud.com/document/product/267/41030) и [WebRTC Push](https://www.tencentcloud.com/document/product/267/41620), чтобы завершить основные настройки и научиться публиковать потоки через WebRTC.

## Инструкции

### Шаг 1. Импортируйте SDK Beauty AR Web

```
<script charset="utf-8" src="https://webar-static.tencent-cloud.com/ar-sdk/resources/latest/webar-sdk.umd.js"></script>
```

> **Примечание:** В приведенном выше примере используется тег script для импорта SDK. Вы также можете [импортировать его с помощью пакета npm](https://www.tencentcloud.com/document/product/1143/50099).

### Шаг 2. Импортируйте ресурсы публикации WebRTC

```
<script src="https://video.sdk.qcloudecdn.com/web/TXLivePusher-2.0.0.min.js" charset="utf-8"></script>
```

> **Примечание:** Убедитесь, что вы добавляете скрипт в тело HTML. Добавление его в head может вызвать ошибку.

### Шаг 3. Инициализируйте SDK Beauty AR Web

```
const { ArSdk } = window.AR;/** ----- Конфигурация аутентификации ----- *//** APPID учетной записи Tencent Cloud *  * Вы можете просмотреть свой APPID в [Центре учетной записи](https://console.tencentcloud.com/developer). */const APPID = ''; // Установите свой APPID учетной записи Tencent Cloud./** * Web LicenseKey *  * Войдите в консоль RT-Cube и нажмите [Web Licenses](https://console.tencentcloud.com/vcube/web) на левой боковой панели. Ключ лицензии будет автоматически сгенерирован после создания лицензии. */const LICENSE_KEY = ''; // Установите свой ключ лицензии./** * Токен, используемый для расчета подписи. *  * Примечание: Этот метод подходит только для отладки. В производственной среде вы должны хранить токен и вычислять подпись на сервере. Интерфейс может получить подпись, вызвав API. Подробности см. * [Подпись](https://cloud.tencent.com/document/product/616/71370#.E7.AD.BE.E5.90.8D.E6.96.B9.E6.B3.95) */const token = ''; // Установите свой токен./** ----------------------- *//** * Получить подпись * * Примечание: Этот метод подходит только для отладки. В производственной среде вы должны вычислять подпись на сервере. Интерфейс может получить подпись, вызвав API. * Пример: * async function () { *  return fetch('http://xxx.com/get-ar-sign').then(res => res.json()); * }; */const getSignature = function () {    const timestamp = Math.round(new Date().getTime() / 1000);    const signature = sha256(timestamp + token + APPID + timestamp).toUpperCase();    return { signature, timestamp };};let w = 720;let h = 480;// Получите входной поток const stream = await navigator.mediaDevices.getUserMedia({    audio: true,    video: { width: w, height: h }})// Основные параметры для SDK Tencent Effectconst config = {    input: stream,    auth: {        licenseKey: LICENSE_KEY,        appId: APPID,        authFunc: getSignature    },    // Настройка начальных эффектов (опционально)    beautify: {        whiten: 0.1, // Эффект отбеливания. Диапазон значений: 0-1.        dermabrasion: 0.5, // Эффект разглаживания кожи. Диапазон значений: 0-1.        lift: 0.3, // Эффект стройного лица. Диапазон значений: 0-1.        shave: 0, // Эффект V-образного лица. Диапазон значений: 0-1.        eye: 0, // Эффект больших глаз. Диапазон значений: 0-1.        chin: 0, // Эффект подбородка. Диапазон значений: 0-1.        …    },    language: 'en',    …}// Передайте `config` в SDK Tencent Effectconst ar = new ArSdk(config);// Вы можете отобразить список эффектов и фильтров в обратном вызове `created`.ar.on('created', () => {    // Получите встроенные эффекты макияжа и стикеры    ar.getEffectList({        Type: 'Preset'    }).then((res) => {        const list = res.map(item => ({            "name": *item.Name,            id: item.EffectId,            cover: item.CoverUrl,            url: item.Url,            label: item.Label,            type: item.PresetType,        }));        const makeupList = list.filter(item=>item.label.indexOf('Makeup')>=0)        const stickerList = list.filter(item=>item.label.indexOf('Sticker')>=0)        // Отобразите списки макияжа и стикеров        renderMakeupList(makeupList);        renderStickerList(stickerList);    }).catch((e) => {        console.log(e);    });    // Получите встроенные фильтры    ar.getCommonFilter().then((res) => {        const list = res.map(item => ({            "name": *item.Name,            id: item.EffectId,            cover: item.CoverUrl,            url: item.Url,            label: item.Label,            type: item.PresetType,        }));        // Отобразите список фильтров        renderFilterList(list);    }).catch((e) => {        console.log(e);    });});ar.on('ready', async (e) => {    // После получения обратного вызова `ready` вы можете вызвать `setBeautify`, `setEffect` или `setFilter` для настройки эффектов.    // Например, вы можете использовать `range input` для установки эффекта разглаживания кожи:    $('#dermabrasion_range_input').change((e) => {        ar.setBeautify({            dermabrasion: e.target.value, // Эффект разглаживания кожи. Диапазон значений: 0-1.        });    });    // В обратном вызове `created` применяйте эффекты на основе взаимодействия пользователя со списками макияжа и стикеров. API `setEffect` поддерживает три типа параметров запроса. Подробности см. в руководстве интеграции SDK.    $('#makeup_list li').click(() => {        ar.setEffect([{id: effect.id, intensity: 1}]);    });    $('#sticker_list li').click(() => {        ar.setEffect([{id: effect.id, intensity: 1}]);    });    // В обратном вызове `created` применяйте фильтр на основе взаимодействия пользователя со списком фильтров. Значение `1` для второго параметра `setFilter` указывает силу фильтра. Подробности см. в руководстве интеграции SDK.    ar.setFilter(filterList[0].id, 1);    $('#filter_list li').click(() => {        ar.setFilter(filter.id, 1);    });    // Получите выходной поток SDK Tencent Effect    const arStream = await ar.getOutput();});ar.on('error', (e) => {    console.log(e);});
```

Чтобы узнать больше об управлении пользовательским интерфейсом, вы можете скачать наш пакет кода в конце этого документа.

### Шаг 4. Опубликуйте поток

```
let livePusher = new TXLivePusher()// Установите основные параметры публикации потока (начало)let DOMAIN = 'Your push domain'let AppName = 'Your app name' let StreamName = 'Your stream name'let txSecret = 'Your txSecret'let txTime = 'Your txTime'// Установите основные параметры публикации потока (конец)let pushUrl = `webrtc://${DOMAIN}/${AppName}/${StreamName}?txSecret=${txSecret}&txTime=${txTime}`// Установите предпросмотр (опционально)livePusher.setRenderView('id_local_video')// Захватите поток livePusher.startCustomCapture(arStream).then(()=>{    // Опубликуйте поток немедленно (вы также можете использовать другой API для управления временем начала публикации потока)    livePusher.startPush(pushUrl)})
```

В приведенном выше коде оба параметра `txSecret` и `txTime` требуют расчета. Вы можете использовать [**генератор адресов**](https://console.tencentcloud.com/live/addrgenerator/addrgenerator) консоли **CSS** для быстрого создания параметров и получения URL публикации. Подробные инструкции см. в разделе [Генератор адресов](https://www.tencentcloud.com/document/product/267/31084).
После успешной публикации потока (`startPush`) вы должны увидеть видео с применяемыми эффектами.

### Шаг 5. Воспроизведите поток

> **Примечание:** Для примера проекта вам необходимо запустить веб-сервис вашего устройства и убедиться, что доступ к файлу HTML можно получить через указанный порт.

- Если у вас есть доступный домен воспроизведения, следуйте инструкциям в разделе [Прямая трансляция](https://www.tencentcloud.com/document/product/267/31559) для воспроизведения потока.
- Если у вас нет домена воспроизведения, вы можете просмотреть поток в [Управлении потоками](https://console.tencentcloud.com/live/streammanage) консоли **CSS**.

## Пакет примера кода

Вы можете скачать наш пакет примера кода [здесь](https://github.com/tencentcloud-webar/web-demo-en). Код для публикации через WebRTC находится в `AR_LEB_WEB`.


---
*Источник: [https://trtc.io/document/53886](https://trtc.io/document/53886)*

---
*Источник (EN): [publishing-with-cloud-streaming-service-and-webrtc.md](./publishing-with-cloud-streaming-service-and-webrtc.md)*
