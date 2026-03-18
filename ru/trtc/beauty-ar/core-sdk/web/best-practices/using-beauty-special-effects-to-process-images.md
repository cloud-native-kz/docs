# Использование специальных эффектов красоты для обработки изображений

Это руководство показывает, как использовать SDK для улучшения изображений, применения эффектов, загрузки обработанных изображений и выполнения других операций в браузере.

## Перед началом

- Пожалуйста, прочитайте [Активировать сервис](https://trtc.io/document/60218?platform=web&product=beautyar), чтобы ознакомиться с процессом получения лицензии и ее использованием, а также подготовьте лицензию.
- Пожалуйста, прочитайте руководство [Начало интеграции](https://trtc.io/document/68777?platform=web&product=beautyar), чтобы понять основное использование SDK.

## Инструкции

### Шаг 1. Импортируйте Beauty AR Web SDK

Создайте файл ar-demo.html и включите следующие файлы JavaScript зависимостей.

```
<script charset="utf-8" src="https://webar-static.tencent-cloud.com/ar-sdk/resources/latest/webar-sdk.umd.js"></script><script src="https://webar-static.tencent-cloud.com/docs/examples/js-sha256/0.9.0/sha256.min.js"></script>
```

> **Примечание:** В демонстрации используется метод включения с помощью тега script. Вы также можете использовать методы из руководства интеграции [Начало интеграции](https://trtc.io/document/68777?platform=web&product=beautyar). webar-sdk.umd.js — это основной пакет и является обязательным. sha256.min.js — это пакет, используемый для получения подписи Signature, и он включен здесь только в целях демонстрации в проекте демонстрации.

### Шаг 2. Инициализируйте Beauty AR Web SDK

Заполните APPID, LICENSE_KEY и token, полученные из [подготовительной работы](https://www.tencentcloud.com/document/product/1143/68964#.E5.87.86.E5.A4.87.E5.B7.A5.E4.BD.9C) в примере кода ниже:

```
<img id="inputImageElement" src="https://webar-static.tencent-cloud.com/docs/test/m4-1080.jpg"><canvas id="arOutputElement" style="width: 400px;display: inline-block;margin-left: 20px;"></canvas>
```

```
/** ----- Authentication configuration ----- *//** * Tencent Cloud account's APPID *  * You can view your APPID in the [Account Center](https://console.tencentcloud.com/developer). */const APPID = ''; // Set it to your Tencent Cloud account APPID./** * Web LicenseKey *  * obtained from Before You Start */const LICENSE_KEY = ''; // Set it to your license key./** * The token used to calculate the signature. *  * Note: This method is only suitable for debugging. In a production environment, you should store the token and calculate the signature on your server. The front end can get the signature by calling an API. For details, see * https://trtc.io/zh/document/68777?platform=web&product=beautyar#cf3401f9-e22e-4f54-9e2d-942c08be0f93 */const token = ''; // Set it to your token./** ----------------------- *//** * Get the signature * * Note: This method is only suitable for debugging. In a production environment, you should store the token and calculate the signature on your server. The front end can get the signature by calling an API. For details, see * https://trtc.io/zh/document/68777?platform=web&product=beautyar#e4ce3483-41f7-4391-83ae-f4b61e221ea0 */const getSignature = function () {    const timestamp = Math.round(new Date().getTime() / 1000);    const signature = sha256(timestamp + token + APPID + timestamp).toUpperCase();    return { signature, timestamp };};const inputImageElement = document.getElementById('inputImageElement');const arOutputElement = document.getElementById('arOutputElement');// ar sdk configconst config = {    module: {        beautify: true,    },    auth: {        licenseKey: LICENSE_KEY,        appId: APPID,        authFunc: getSignature    },    input: inputImageElement, // input image element    output: arOutputElement, // output canvas element    beautify: { // default Beautify config        "eye": 0.5,        "whiten": 0.4,        "dermabrasion": 0.6,        "lift": 0.1,        "shave": 0.2,    },}// init ArSdkconst { ArSdk } = window.AR;const arSdk = new ArSdk(config);arSdk.on('error', (e) => {    console.log(e);});
```

## Шаг 3. Обновите входное изображение

Вы можете выбрать файл изображения, используя тег input, и вызвать интерфейс `updateInputImage`, чтобы обновить изображение.

```
<input type="file" id="imageInput" accept="image/*" style="display: none;">
```

```
const imageInput = document.getElementById('imageInput');imageInput.addEventListener('change', function () {    const file = this.files[0];    if (file) {        const reader = new FileReader();        reader.onload = function (event) {            inputImageElement.src = event.target.result;            inputImageElement.onload = function () {                arSdk.updateInputImage({                    width: inputImageElement.width,                    height: inputImageElement.height,                    input: inputImageElement,                })            };        };        reader.readAsDataURL(file);    }});
```

## Шаг 4. Установите эффект красоты, макияж и фильтры

Используйте интерфейс `setBeautify` для применения эффектов красоты и интерфейс `setEffect` для применения макияжа, наклеек на лицо и других эффектов.

```
// set effectfunction setMakeUp() {    if (!arSdk) return    arSdk.setEffect([{        id: 'CE82819618A6CDA3', // makeupãeffect id        intensity: 0.8    }])}// clear effectfunction clearMakeUp() {    if (!arSdk) return    arSdk.setEffect(null)}// set beautifyfunction setBeautify() {    if (!arSdk) return    arSdk.setBeautify({        "eye": Math.random() * 1,        "whiten": Math.random() * 1,        "dermabrasion": Math.random() * 1,        "lift": Math.random() * 1,        "shave": Math.random() * 1,    })}// clear beautifyfunction clearBeautify() {    if (!arSdk) return    arSdk.setBeautify({        "eye": 0,        "whiten": 0,        "dermabrasion": 0,        "lift": 0,        "shave": 0,    })}
```

## Шаг 5. Загрузите изображение

Используйте интерфейс `takePhoto` для получения обработанного изображения ImageData, отрисуйте его на canvas и загрузите его.

```
<canvas id="photoCanvas" style="display: none;"></canvas><button id="downloadImage">Download Image</button>
```

```
const downloadImage = document.getElementById('downloadImage');downloadImage.addEventListener('click', async () => {    if (!arSdk) {        alert('Please initAR firstï½')        return    }    const imageData = await arSdk.takePhoto();    photoCanvas.width = imageData.width;    photoCanvas.height = imageData.height;    const context = photoCanvas.getContext("2d");    context.putImageData(imageData, 0, 0);    const base64Image = photoCanvas.toDataURL("image/png");    const a = document.createElement("a");    a.href = base64Image;    a.download = "downloadedImage.png";    document.body.appendChild(a);    a.click();    document.body.removeChild(a);})
```

### Шаг 6. Запустите демонстрацию

Запустите локальный сервис и получите доступ к определенному порту.

Здесь мы используем в качестве примера [модуль serve](https://www.npmjs.com/package/serve). Запустите `serve .` в каталоге, где находится демонстрация.

Следующий вывод указывает, что локальный сервис запущен успешно.

```
    Serving!                                       â   â                                                  â   â   - Local:            http://localhost:57965     â   â   - On Your Network:  http://10.91.28.94:57965   â   â                                                  â   â   This port was picked because 5000 is in use.   â   â                                                  â   â   Copied local address to clipboard!
```

Получите доступ к указанному порту в Chrome для предварительного просмотра результата.

> **Примечание:** Демонстрация требует доступа к разрешениям браузера на **камеру** и **микрофон**. Пожалуйста, убедитесь, что страница, к которой вы получаете доступ, имеет эти разрешения.

Полный фрагмент кода приведен ниже. Перед запуском заполните информацию APPID, LICENSE_KEY и token в коде.

```
<!DOCTYPE html><html lang="en"><head>    <meta charset="UTF-8">    <meta name="viewport" content="width=device-width, initial-scale=1.0">    <title>Image Upload and Display</title></head><body>    <div>        step1: <button id="initAR">Init AR SDK</button>        </br>        step2: <button id="selectAndProcess">Update Input Image</button>    </div>    <div>        step3: <button onclick="setMakeUp()">Set Makeup</button>        <button onclick="clearMakeUp()">Clear Makeup</button>        <button onclick="setBeautify()">Set Beautify</button>        <button onclick="clearBeautify()">Clear Beautify</button>    </div>    <div>        step4: <button id="downloadImage">Download Image</button>    </div>    <input type="file" id="imageInput" accept="image/*" style="display: none;">    <br>    <img id="inputImageElement" src="https://webar-static.tencent-cloud.com/docs/test/m4-1080.jpg">    <canvas id="arOutputElement" style="display: inline-block;"></canvas>    <canvas id="photoCanvas" style="display: none;"></canvas>    <script charset="utf-8" src="https://webar-static.tencent-cloud.com/ar-sdk/resources/latest/webar-sdk.umd.js">    </script>    <script src="https://webar-static.tencent-cloud.com/docs/examples/js-sha256/0.9.0/sha256.min.js"></script>    <script>        let arSdk;        // todoï¼Enter the license information        const APPID = "";        const LICENSE_KEY = "";        const token = "";        const getSignature = function () {            const timestamp = Math.round(new Date().getTime() / 1000);            const signature = sha256(timestamp + token + APPID + timestamp).toUpperCase();            return {                signature,                timestamp            };        };        const selectAndProcess = document.getElementById('selectAndProcess');        const imageInput = document.getElementById('imageInput');        const downloadImage = document.getElementById('downloadImage');        const inputImageElement = document.getElementById('inputImageElement');        const initArBtn = document.getElementById('initAR');        const arOutputElement = document.getElementById('arOutputElement');        const photoCanvas = document.getElementById('photoCanvas');        initArBtn.addEventListener('click', async () => {            arSdk = await getInstance();            alert('Init AR SDK Success!!!')        })        selectAndProcess.addEventListener('click', () => {            if (!arSdk) {                alert('Please click initAR to init AR SDK')                return            }            imageInput.click();        })        downloadImage.addEventListener('click', async () => {            if (!arSdk) {                alert('Please click initAR to init AR SDK')                return            }            const imageData = await arSdk.takePhoto();            photoCanvas.width = imageData.width;            photoCanvas.height = imageData.height;            const context = photoCanvas.getContext("2d");            context.putImageData(imageData, 0, 0);            const base64Image = photoCanvas.toDataURL("image/png");            const a = document.createElement("a");            a.href = base64Image;            a.download = "downloadedImage.png";            document.body.appendChild(a);            a.click();            document.body.removeChild(a);        })        imageInput.addEventListener('change', function () {            const file = this.files[0];            if (file) {                const reader = new FileReader();                reader.onload = function (event) {                    inputImageElement.src = event.target.result;                    inputImageElement.onload = function () {                        arSdk.updateInputImage({                            width: inputImageElement.width,                            height: inputImageElement.height,                            input: inputImageElement,                        })                    };                };                reader.readAsDataURL(file);            }        });        function setMakeUp() {            if (!arSdk) return            arSdk.setEffect([{                id: 'CE82819618A6CDA3', // makeupãeffect id                intensity: 0.8            }])        }        function clearMakeUp() {            if (!arSdk) return            arSdk.setEffect(null)        }        function clearBeautify() {            if (!arSdk) return            arSdk.setBeautify({                "eye": 0,                "whiten": 0,                "dermabrasion": 0,                "lift": 0,                "shave": 0,            })        }        function setBeautify() {            if (!arSdk) return            arSdk.setBeautify({                "eye": Math.random() * 1,                "whiten": Math.random() * 1,                "dermabrasion": Math.random() * 1,                "lift": Math.random() * 1,                "shave": Math.random() * 1,            })        }        async function getInstance() {            if (arSdk) {                return Promise.resolve(arSdk)            }            const config = {                module: {                    beautify: true,                    segmentation: false                },                auth: {                    licenseKey: LICENSE_KEY,                    appId: APPID,                    authFunc: getSignature                },                input: inputImageElement,                output: arOutputElement,                beautify: {                    "eye": Math.random() * 1,                    "whiten": Math.random() * 1,                    "dermabrasion": Math.random() * 1,                    "lift": Math.random() * 1,                    "shave": Math.random() * 1,                },            }            return new Promise((resolve) => {                const sdk = new window.AR.ArSdk(config)                sdk.on('resourceReady', async () => {                    // get makeuplist                     sdk.getEffectList({                        Type: 'Preset',                        Label: 'Makeup',                    }).then((res) => {                        const list = res.map(item => ({                            name: item.Name,                            id: item.EffectId,                            cover: item.CoverUrl,                            url: item.Url,                            label: item.Label,                            type: item.PresetType,                        }));                        console.log('makeuplist', list)                    })                    resolve(sdk)                })                sdk.on('ready', () => {                })                sdk.on('error', (e) => {                    console.log(e);                });            })        }    </script></body></html>
```


---
*Источник: [https://trtc.io/document/69310](https://trtc.io/document/69310)*

---
*Источник (EN): [using-beauty-special-effects-to-process-images.md](./using-beauty-special-effects-to-process-images.md)*
