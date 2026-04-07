# Локальное смешивание потоков на базе WebRTC

SDK предоставляет различные функции обработки видеопотоков, включая смешивание нескольких видеопотоков (такие как "картинка в картинке"), обработку эффектов изображения (такие как зеркалирование и фильтры) и добавление других элементов (такие как водяные знаки и текст). Основной процесс выглядит следующим образом: SDK сначала собирает несколько потоков и смешивает их локально, объединяя изображения и микшируя звук. Затем он обрабатывает другие эффекты. Поскольку все функции зависят от поддержки браузером, SDK имеет определённые требования к производительности браузера. Для получения информации об API, см. [TXVideoEffectManager](https://webrtc-demo.myqcloud.com/push-sdk/v2/docs/TXVideoEffectManager.html). В этом документе описано базовое использование функции локального смешивания потоков.

## Базовое использование

Для использования функции локального смешивания потоков необходимо инициализировать SDK и получить экземпляр SDK `livePusher`. Код инициализации см. в разделе [WebRTC Push](https://intl.cloud.tencent.com/document/product/267/41620).

### Шаг 1. Получение экземпляра управления видеоэффектами

```
var videoEffectManager = livePusher.getVideoEffectManager();
```

### Шаг 2. Включение локального смешивания потоков

Сначала необходимо включить функцию локального смешивания потоков. По умолчанию SDK собирает только один видеопоток и один аудиопоток. После включения этой функции SDK может собирать несколько потоков, которые будут смешаны локально в браузере.

```
videoEffectManager.enableMixing(true);
```

### Шаг 3. Установка параметров смешивания потоков

Установите параметры смешивания потоков, особенно разрешение и частоту кадров выходного видео после смешивания потоков.

```
videoEffectManager.setMixingConfig({    videoWidth: 1280,    videoHeight: 720,    videoFramerate: 15});
```

### Шаг 4. Сбор нескольких потоков

После включения локального смешивания потоков SDK начинает собирать несколько потоков, таких как камера и общий экран. Обязательно сохраните ID потоков, так как они потребуются в последующих операциях.

```
var cameraStreamId = null;var screenStreamId = null;livePusher.startCamera().then((streamId) => {    cameraStreamId = streamId;}).catch((error) => {    console.log('Failed to turn on the camera:'+ error.toString());});livePusher.startScreenCapture().then((streamId) => {    screenStreamId = streamId;}).catch((error) => {    console.log('Failed to share the screen:'+ error.toString());});
```

### Шаг 5. Установка макета изображения

Установите макет изображений собранных двух потоков. Здесь общий экран отображается как основное изображение, а изображение с камеры находится в левом верхнем углу. Для получения информации об определённой конфигурации параметров см. [TXLayoutConfig](https://webrtc-demo.myqcloud.com/push-sdk/v2/docs/TXVideoEffectManager.html#~TXLayoutConfig).

```
videoEffectManager.setLayout([{    streamId: screenStreamId,    x: 640,    y: 360,    width: 1280,    height: 720,    zOrder: 1}, {    streamId: cameraStreamId,    x: 160,    y: 90,    width: 320,    height: 180,    zOrder: 2}]);
```

### Шаг 6. Установка эффекта зеркалирования

Зеркалируйте изображение с камеры, так как изображение, собранное камерой, фактически отражено.

```
videoEffectManager.setMirror({    streamId: cameraStreamId,    mirrorType: 1});
```

### Шаг 7. Добавление водяного знака

Подготовьте объект изображения и добавьте его к видеопотоку в качестве водяного знака. Здесь изображение водяного знака размещается в правом верхнем углу.

```
var image = new Image();image.src = './xxx.png'; // Note that the image address cannot be under another domain; otherwise, cross-domain issues will occur.videoEffectManager.setWatermark({    image: image,    x: 1230,    y: 50,    width: 100,    height: 100,    zOrder: 3});
```

### Шаг 8. Запуск трансляции потока

Отправьте видеопоток с макетом "картинка в картинке", зеркальным изображением и водяным знаком на сервер после выполнения вышеописанных шагов.

```
livePusher.startPush('webrtc://domain/AppName/StreamName?txSecret=xxx&txTime=xxx');
```

> **Примечание** Для получения дополнительной информации об API смешивания потоков на базе WebRTC см. [TXLivePusher](https://webrtc-demo.myqcloud.com/push-sdk/v2/docs/TXLivePusher.html).


---
*Источник: [https://www.tencentcloud.com/document/product/267/51160](https://www.tencentcloud.com/document/product/267/51160)*

---
*Источник (EN): [webrtc-based-local-stream-mix.md](./webrtc-based-local-stream-mix.md)*
