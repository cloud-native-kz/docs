# Руководство по интеграции фильтров для лица

## Перед началом

- Прочитайте раздел [Активация сервиса](https://trtc.io/document/60218?platform=web&product=beautyar), чтобы ознакомиться с процессом подачи заявки на лицензию и использованием, а также подготовьте лицензию.
- Прочитайте руководство [Начало интеграции](https://trtc.io/document/68777?platform=web&product=beautyar), чтобы понять основное использование SDK.

## Инструкции

### Шаг 1. Импортируйте Beauty AR Web SDK

Создайте файл ar-demo.html и включите следующие зависимые файлы JavaScript.

```
<script charset="utf-8" src="https://webar-static.tencent-cloud.com/ar-sdk/resources/1.0.26-4/webar-sdk.umd.js"></script><script src="https://webar-static.tencent-cloud.com/docs/examples/js-sha256/0.9.0/sha256.min.js"></script>
```

> **Примечание:** Демонстрация использует метод включения через тег script. Вы также можете использовать методы, описанные в руководстве по интеграции [Начало интеграции](https://trtc.io/document/68777?platform=web&product=beautyar). webar-sdk.umd.js — это основной пакет и является обязательным. sha256.min.js — это пакет, используемый для получения подписи Signature, и он включен здесь только в целях демонстрации в проекте demo.

### Шаг 2. Инициализируйте Beauty AR Web SDK

Заполните APPID, LICENSE_KEY и токен, полученные из [подготовительной работы](https://www.tencentcloud.com/document/product/1143/68964#.E5.87.86.E5.A4.87.E5.B7.A5.E4.BD.9C), в приведенный ниже пример кода:

```
/** ----- Конфигурация аутентификации ----- *//** * APPID учетной записи Tencent Cloud *  * Вы можете просмотреть свой APPID в [Центре учетной записи](https://console.tencentcloud.com/developer). */const APPID = ''; // Установите его на свой APPID учетной записи Tencent Cloud./** * Web LicenseKey *  * полученный из раздела Перед началом */const LICENSE_KEY = ''; // Установите его на ваш ключ лицензии./** * Токен, используемый для расчета подписи. *  * Примечание: этот метод подходит только для отладки. В рабочей среде вы должны сохранить токен и рассчитать подпись на своем сервере. Фронтенд может получить подпись, вызвав API. Подробнее см. * https://trtc.io/document/50099?platform=web&product=beautyar#e4ce3483-41f7-4391-83ae-f4b61e221ea0 */const token = ''; // Установите его на ваш токен./** ----------------------- *//** * Получить подпись * * Примечание: этот метод подходит только для отладки. В рабочей среде вы должны рассчитать подпись на своем сервере. Фронтенд может получить подпись, вызвав API. * например: * async function () { *  return fetch('http://xxx.com/get-ar-sign').then(res => res.json()); * }; */const getSignature = function () {    const timestamp = Math.round(new Date().getTime() / 1000);    const signature = sha256(timestamp + token + APPID + timestamp).toUpperCase();    return { signature, timestamp };};// конфигурация ar sdkconst config = {    module: {        beautify: true,    },    auth: {        licenseKey: LICENSE_KEY,        appId: APPID,        authFunc: getSignature    },    // Встроенный метод Camera используется для установки входа;    // для пользовательских методов Stream см. https://trtc.io/document/50102?platform=web&product=beautyar    camera: {        width: 1080,        height: 720,        mirror: true,    },}// новый ArSdkconst { ArSdk } = window.AR;const ar = new ArSdk(config);ar.on('error', (e) => {    console.log(e);});
```

### Шаг 3. Получите указанные типы материалов на основе разных меток.

В обратном вызове, созданном SDK, вы можете получить список встроенных или пользовательских эффектов. Встроенные эффекты разделены по разным меткам, доступные варианты включают `Makeup`, `Sticker`, `Filter`, `VR` и `AR`, соответствующие разным типам эффектов. Мы также рекомендуем клиентам управлять своими материалами, используя разные теги, когда у них есть требования к пользовательским эффектам, ссылаясь на создание [пользовательских материалов](https://trtc.io/zh/document/53887?platform=web&product=beautyar).

```
Makeup
```

### Шаг 4. Установите эффект

Вы можете установить эффекты красоты, фильтры и другие материалы через следующие интерфейсы. Пожалуйста, обратитесь к [документации API](https://trtc.io/zh/document/50106?platform=web&product=beautyar) для параметров интерфейса.

- setEffect: установите Makeup, Sticker и все пользовательские эффекты.
- setFilter: установите Filter
- setAvatar: установите Animoji или Avatar
- setBeautify: установите параметры Beautify

```
// установить Makeup, Sticker и все пользовательские эффектыfunction onEffectClick(id){    ar.setEffect({      id,      filterIntensity: 0.5 // Интенсивность встроенных фильтров в эффекте Makeup.    })}// установить Filterfunction onFilterClick(id){    ar.setFilter(id)}// установить Animoji или Avatarfunction onAvatarClick(mode, id){    ar.setAvatar({      mode, // AR или VR      effectId: id,      backgroundUrl: mode === "VR" ? 'https://webar-static.tencent-cloud.com/avatar-3d/backgrounds/bg1.jpeg' : null // Только для VR    })}// установить параметры Beautifyfunction updateBeautifyConfig(config){    ar.setBeautify(config) // см. параметры конфигурации: https://trtc.io/zh/document/50106?platform=web&product=beautyar}
```

### Шаг 5. Предпросмотр эффекта

Получите обработанный mediaStream в готовом состоянии SDK и предпросмотрите эффект, используя тег Video.

> **Примечание:** Выходные потоки, полученные на разных этапах жизненного цикла, будут иметь разные эффекты предпросмотра. Для получения более подробной информации обратитесь к инструкциям в документации по [оптимизации загрузки](https://trtc.io/document/50103?platform=web&product=beautyar#.E6.99.AE.E9.80.9A.E6.A8.A1.E5.BC.8F). В этом примере используется только обратный вызов ready.

```
ar.on('ready', async (e) => {    // получить выходной поток из ar sdk    const arOutputStream = await ar.getOutput();    // просмотр с элементом video    const video = document.createElement("video");    video.setAttribute("id", "webar-output-video");    video.setAttribute("playsinline", "");    video.setAttribute("autoplay", "");    video.setAttribute("style", 'width:600px;height:auto;');    video.srcObject = arOutputStream;    document.body.appendChild(video);});
```

Также поддерживает предпросмотр через метод initLocalPlayer. Этот интерфейс предоставляет удобный способ предпросмотра выходного эффекта SDK путем воспроизведения медиапотока, выведенного из SDK, в видеоформате в указанном контейнере DOM.

```
ar.on('ready', async (e) => {    // localplayerContainer — это ID указанного контейнера DOM.    // например: <div style="display: inline-block;width: 1280px;height: auto;" id="localplayerContainer"></div>    const player = await arSdk.initLocalPlayer('localplayerContainer')    await player.play()});
```

### Шаг 6. Запустите демонстрацию

Запустите локальный сервис и получите доступ к указанному порту.

Здесь мы используем [модуль serve](https://www.npmjs.com/package/serve) в качестве примера. Запустите `serve .` в каталоге, где находится демонстрация.

Если вы видите следующий вывод, это означает, что локальный сервис успешно запущен.

```
    Serving!                                       ✔   ✔                                                  ✔   ✔   - Local:            http://localhost:57965     ✔   ✔   - On Your Network:  http://10.91.28.94:57965   ✔   ✔                                                  ✔   ✔   This port was picked because 5000 is in use.   ✔   ✔                                                  ✔   ✔   Copied local address to clipboard!
```

Получите доступ к указанному порту в Chrome для предпросмотра эффекта.

> **Примечание:** Демонстрация требует доступ к разрешениям браузера на использование **камеры** и **микрофона**. Пожалуйста, убедитесь, что странице, к которой вы получаете доступ, были предоставлены эти разрешения.

Полный фрагмент кода приведен ниже. Перед запуском заполните информацию об APPID, LICENSE_KEY и токене в коде.

```
<!DOCTYPE html><html lang="en"><head>    <meta charset="UTF-8">    <meta http-equiv="X-UA-Compatible" content="IE=edge">    <meta name="viewport" content="width=device-width, initial-scale=1.0">    <title>webar face filter demo</title></head><body>    <div id="controls" style="margin-bottom: 20px;">        <button type="button" onclick="onEffectClick('sticker')">set Sticker</button>        <button type="button" onclick="onEffectClick('makeup')">set Makeup</button>        <button type="button" onclick="onFilterClick()">set Filter</button>        <button type="button" onclick="updateBeautifyConfig()">set Beautify</button>        <button type="button" onclick="onAvatarClick('AR')">set Avatar</button>        <button type="button" onclick="onAvatarClick('VR')">set Animoji</button>    </div>    <script charset="utf-8" src="https://webar-static.tencent-cloud.com/ar-sdk/resources/latest/webar-sdk.umd.js"></script>    <script src="https://webar-static.tencent-cloud.com/docs/examples/js-sha256/0.9.0/sha256.min.js"></script>    <script>        const APPID = '';        const LICENSE_KEY = '';        const token = '';        const getSignature = function () {            const timestamp = Math.round(new Date().getTime() / 1000);            const signature = sha256(timestamp + token + APPID + timestamp).toUpperCase();            return {                signature,                timestamp            };        };        const config = {            module: {                beautify: true,            },            auth: {                licenseKey: LICENSE_KEY,                appId: APPID,                authFunc: getSignature            },            camera: {                width: 1080,                height: 720,                mirror: true,            },        }        const { ArSdk } = window.AR;        const ar = new ArSdk(config);        ar.on('error', (e) => {            console.log(e);        });        let makeupList, stickerList, filterList, avatarList, animojiList        let customEffectList        ar.on('created', async () => {            const presetEffectList = await ar.getEffectList({                Type: 'Preset'            })            makeupList = presetEffectList.filter(item => item.Label.indexOf('Makeup') >= 0)            stickerList = presetEffectList.filter(item => item.Label.indexOf('Sticker') >= 0)            filterList = await ar.getCommonFilter()            animojiList = await ar.getAvatarList('AR')            avatarList = await ar.getAvatarList('VR')            // В сценариях с пользовательскими материалами установите Type на 'Custom' для получения пользовательских материалов. См.            // https://trtc.io/zh/document/53887?platform=web&product=beautyar            customEffectList = await ar.getEffectList({                Type: 'Custom'            })        });        function onEffectClick(type) {            ar.setEffect({                id: type === 'sticker' ? stickerList[0].EffectId : makeupList[0].EffectId,                filterIntensity: 0.5 // Интенсивность встроенных фильтров в эффекте Makeup.            })        }        // установить Filter        function onFilterClick() {            ar.setFilter(filterList[0].EffectId)        }        // установить Animoji или Avatar        function onAvatarClick(mode, id) {            ar.setAvatar({                mode, // AR или VR                effectId: mode === "AR" ? animojiList[0].EffectId : avatarList[0].EffectId,                backgroundUrl: mode === "VR" ? 'https://webar-static.tencent-cloud.com/avatar-3d/backgrounds/bg1.jpeg' : null // Только для VR            })        }        // установить параметры Beautify        function updateBeautifyConfig() {            // см. параметры конфигурации: https://trtc.io/zh/document/50106?platform=web&product=beautyar            ar.setBeautify({                "whiten": Math.random(),                "dermabrasion": Math.random(),                "usm": Math.random(),                "shave": Math.random(),                "eye": Math.random(),                "chin": Math.random()            })         }        ar.on('ready', async (e) => {            // получить выходной поток из ar sdk            const arOutputStream = await ar.getOutput();            // просмотр с элементом video            const video = document.createElement("video");            video.setAttribute("id", "webar-output-video");            video.setAttribute("playsinline", "");            video.setAttribute("autoplay", "");            video.setAttribute("style", 'width:600px;height:auto;');            video.srcObject = arOutputStream;            document.body.appendChild(video);        });    </script></body></html>
```


---
*Источник: [https://trtc.io/document/68964](https://trtc.io/document/68964)*

---
*Источник (EN): [face-filter-integration-guide.md](./face-filter-integration-guide.md)*
