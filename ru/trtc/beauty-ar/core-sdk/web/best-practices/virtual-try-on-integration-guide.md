# Руководство по интеграции Virtual Try-On

## Перед началом

- Прочитайте [Активировать сервис](https://trtc.io/document/60218?platform=web&product=beautyar), чтобы ознакомиться с процессом подачи заявки на лицензию и использованием, а также подготовьте лицензию.
- Прочитайте руководство [Начать интеграцию](https://trtc.io/document/68777?platform=web&product=beautyar), чтобы понять базовое использование SDK.

## Инструкции

### Шаг 1. Импортируйте Beauty AR Web SDK

Создайте файл ar-demo.html и включите следующие файлы JavaScript зависимостей.

```
<script charset="utf-8" src="https://webar-static.tencent-cloud.com/ar-sdk/resources/1.0.26-4/webar-sdk.umd.js"></script><script src="https://webar-static.tencent-cloud.com/docs/examples/js-sha256/0.9.0/sha256.min.js"></script>
```

> **Примечание:** Demo использует метод включения через тег script. Вы также можете обратиться к методам в руководстве по интеграции [Начать интеграцию](https://trtc.io/document/68777?platform=web&product=beautyar). webar-sdk.umd.js — это основной пакет и является обязательным. sha256.min.js — это пакет, используемый для получения сигнатуры Signature, и здесь он включен только в демонстрационных целях в проекте demo.

### Шаг 2. Инициализируйте Beauty AR Web SDK

Заполните APPID, LICENSE_KEY и токен, полученные из [подготовительной работы](https://www.tencentcloud.com/document/product/1143/68965#.E5.87.86.E5.A4.87.E5.B7.A5.E4.BD.9C), в примере кода ниже:

```
/** ----- Authentication configuration ----- *//** * Tencent Cloud account's APPID *  * You can view your APPID in the [Account Center](https://console.tencentcloud.com/developer). */const APPID = ''; // Set it to your Tencent Cloud account APPID./** * Web LicenseKey *  * obtained from Before You Start */const LICENSE_KEY = ''; // Set it to your license key./** * The token used to calculate the signature. *  * Note: This method is only suitable for debugging. In a production environment, you should store the token and calculate the signature on your server. The front end can get the signature by calling an API. For details, see * https://trtc.io/document/50099?platform=web&product=beautyar#e4ce3483-41f7-4391-83ae-f4b61e221ea0 */const token = ''; // Set it to your token./** ----------------------- *//** * Get the signature * * Note: This method is only suitable for debugging. In a production environment, you should calculate the signature on your server. The front end can get the signature by calling an API. * eg: * async function () { *  return fetch('http://xxx.com/get-ar-sign').then(res => res.json()); * }; */const getSignature = function () {    const timestamp = Math.round(new Date().getTime() / 1000);    const signature = sha256(timestamp + token + APPID + timestamp).toUpperCase();    return { signature, timestamp };};// ar sdk configconst config = {    module: {        beautify: true,        handLandmark: true // rings try on require handLandmark module    },    auth: {        licenseKey: LICENSE_KEY,        appId: APPID,        authFunc: getSignature    },    // Built-in Camera method is used to set the input;    // for Custom Stream methods, please refer to. https://trtc.io/document/50102?platform=web&product=beautyar    camera: {        width: 1080,        height: 720,        mirror: true,    },}// new ArSdkconst { ArSdk } = window.AR;const ar = new ArSdk(config);ar.on('error', (e) => {    console.log(e);});
```

### Шаг 3. Получите указанные типы материалов на основе различных меток.

В обратном вызове, созданном SDK, вы можете получить список встроенных или пользовательских эффектов. Встроенные эффекты различаются по разным меткам, а распространенные типы меток включают:

- Makeup: Эффект макияжа лица
- Blush: Эффект румян
- Eyes: Эффект глаз
- Eyebrows: Эффект бровей
- Lips: Эффект губ
- Iris: Эффект контактных линз
- glasses: Примерка очков
- rings: Примерка колец
- Headwear: Примерка головных уборов

Мы также рекомендуем клиентам управлять материалами, используя различные метки, когда есть потребность в пользовательских эффектах, следуя примеру создания [пользовательских материалов](https://trtc.io/zh/document/53887?platform=web&product=beautyar).

```
let makeupList, glassesList, contactLensesList,  headwearList, ringListlet customEffectListar.on('created', async () => {    makeupList = await ar.getEffectList({        Type: 'Preset',        Label: ['Makeup', 'Woman']    })    glassesList = await ar.getEffectList({        Type: 'Preset',        Label: ['glasses']    })    contactLensesList = await ar.getEffectList({        Type: 'Preset',        Label: ['Iris']    })    headwearList = await ar.getEffectList({        Type: 'Preset',        Label: ['Headwear']    })    ringList = await ar.getEffectList({        Type: 'Preset',        Label: ['rings']    })    // In scenarios with custom materials, set the Type to 'Custom' to retrieve the custom materials. See    // https://trtc.io/zh/document/53887?platform=web&product=beautyar    customEffectList = await ar.getEffectList({        Type: 'Custom'    })});
```

### Шаг 4. Установите эффект

Используйте `setEffect` для применения различных материалов красоты, очков, колец и головных уборов, а также всех пользовательских эффектов. Пожалуйста, обратитесь к [документации API](https://trtc.io/zh/document/50106?platform=web&product=beautyar) для параметров интерфейса.

```
function setMakeup() {    ar.setEffect({        id: makeupList[0].EffectId,    })}function setGlasses() {    ar.setEffect({        id: glassesList[0].EffectId,    })}function setContactLenses() {    ar.setEffect({        id: contactLensesList[0].EffectId,        intensity: 0.6    })}function setHeadwear() {    ar.setEffect({        id: headwearList[0].EffectId,    })}function setRings() {    ar.setEffect({        id: ringList[0].EffectId,    })}
```

> **Примечание:** При использовании примерки колец необходимо включить модуль **handLandmark** в конфигурации **module** и убедиться, что ладонь полностью видна в поле зрения камеры во время предпросмотра.

### Шаг 5. Предпросмотр эффекта

Получите обработанный mediaStream в состоянии готовности SDK и предпросмотрите эффект, используя тег Video.

> **Примечание:** Выходные потоки, полученные на разных этапах жизненного цикла, будут иметь различные эффекты предпросмотра. Для получения более подробной информации обратитесь к инструкциям в документации [оптимизация загрузки](https://trtc.io/document/50103?platform=web&product=beautyar#.E6.99.AE.E9.80.9A.E6.A8.A1.E5.BC.8F). В этом примере используется только обратный вызов ready.

```
ar.on('ready', async (e) => {    // get output stream from ar sdk    const arOutputStream = await ar.getOutput();    // view with video element    const video = document.createElement("video");    video.setAttribute("id", "webar-output-video");    video.setAttribute("playsinline", "");    video.setAttribute("autoplay", "");    video.setAttribute("style", 'width:600px;height:auto;');    video.srcObject = arOutputStream;    document.body.appendChild(video);});
```

Также поддерживает предпросмотр через метод initLocalPlayer. Этот интерфейс предоставляет удобный способ предпросмотра выходного эффекта SDK путем воспроизведения потока мультимедиа, выводимого из SDK, в видеоформате внутри указанного контейнера DOM.

```
ar.on('ready', async (e) => {    // localplayerContainer is the ID of the specified DOM container.    // eg. <div style="display: inline-block;width: 1280px;height: auto;" id="localplayerContainer"></div>    const player = await arSdk.initLocalPlayer('localplayerContainer')    await player.play()});
```

### Шаг 6. Запустите Demo

Запустите локальный серверный сервис и получите доступ к указанному порту.

Здесь мы используем [модуль serve](https://www.npmjs.com/package/serve) в качестве примера. Запустите `serve .` в директории, где находится demo.

Следующий вывод указывает на успешный запуск локального серверного сервиса.

```
    Serving!                                       â   â                                                  â   â   - Local:            http://localhost:57965     â   â   - On Your Network:  http://10.91.28.94:57965   â   â                                                  â   â   This port was picked because 5000 is in use.   â   â                                                  â   â   Copied local address to clipboard!
```

Получите доступ к указанному порту в Chrome для предпросмотра эффекта.

> **Примечание:** Demo требует доступа к разрешениям **камеры** и **микрофона** браузера. Пожалуйста, убедитесь, что странице были предоставлены эти разрешения.

Полный фрагмент кода приведен ниже. Перед запуском пожалуйста заполните информацию, связанную с APPID, LICENSE_KEY и token в коде.

```
<!DOCTYPE html><html lang="en"><head>    <meta charset="UTF-8">    <meta http-equiv="X-UA-Compatible" content="IE=edge">    <meta name="viewport" content="width=device-width, initial-scale=1.0">    <title>webar virtual try on demo</title></head><body>    <div id="controls" style="margin-bottom: 20px;">        <button type="button" onclick="setMakeup()">set Makeup</button>        <button type="button" onclick="setGlasses()">set Glasses</button>        <button type="button" onclick="setContactLenses()">set Contact Lenses</button>        <button type="button" onclick="setHeadwear()">set Headwear</button>        <button type="button" onclick="setRings()">set Rings</button>    </div>    <script charset="utf-8" src="https://webar-static.tencent-cloud.com/ar-sdk/resources/1.0.26-4/webar-sdk.umd.js"></script>    <script src="https://webar-static.tencent-cloud.com/docs/examples/js-sha256/0.9.0/sha256.min.js"></script>    <script>        const APPID = '';        const LICENSE_KEY = '';        const token = '';        const getSignature = function () {            const timestamp = Math.round(new Date().getTime() / 1000);            const signature = sha256(timestamp + token + APPID + timestamp).toUpperCase();            return {                signature,                timestamp            };        };        const config = {            module: {                beautify: true,                handLandmark: true // rings try on require handLandmark module            },            auth: {                licenseKey: LICENSE_KEY,                appId: APPID,                authFunc: getSignature            },            camera: {                width: 1080,                height: 720,                mirror: true,            },        }        // new ArSdk        const { ArSdk } = window.AR;        const ar = new ArSdk(config);        ar.on('error', (e) => {            console.log(e);            alert(e.message);        });        let makeupList, glassesList, contactLensesList,  headwearList, ringList        let customEffectList        // get effect list        ar.on('created', async () => {            makeupList = await ar.getEffectList({                Type: 'Preset',                Label: ['Makeup', 'Woman']            })            glassesList = await ar.getEffectList({                Type: 'Preset',                Label: ['glasses']            })            contactLensesList = await ar.getEffectList({                Type: 'Preset',                Label: ['Iris']            })            headwearList = await ar.getEffectList({                Type: 'Preset',                Label: ['Headwear']            })            ringList = await ar.getEffectList({                Type: 'Preset',                Label: ['rings']            })            // In scenarios with custom materials, set the Type to 'Custom' to retrieve the custom materials. See            // https://trtc.io/zh/document/53887?platform=web&product=beautyar            customEffectList = await ar.getEffectList({                Type: 'Custom'            })        });        function setMakeup() {            ar.setEffect({                id: makeupList[0].EffectId,            })        }        function setGlasses() {            ar.setEffect({                id: glassesList[0].EffectId,            })        }        function setContactLenses() {            ar.setEffect({                id: contactLensesList[0].EffectId,                intensity: 0.6            })        }        function setHeadwear() {            ar.setEffect({                id: headwearList[0].EffectId,            })        }        function setRings() {            ar.setEffect({                id: ringList[0].EffectId,            })        }                ar.on('ready', async (e) => {            // get output stream from ar sdk            const arOutputStream = await ar.getOutput();            // view with video element            const video = document.createElement("video");            video.setAttribute("id", "webar-output-video");            video.setAttribute("playsinline", "");            video.setAttribute("autoplay", "");            video.setAttribute("style", 'width:600px;height:auto;');            video.srcObject = arOutputStream;            document.body.appendChild(video);        });    </script></body></html>
```


---
*Источник: [https://trtc.io/document/68965](https://trtc.io/document/68965)*

---
*Источник (EN): [virtual-try-on-integration-guide.md](./virtual-try-on-integration-guide.md)*
