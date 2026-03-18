# Включение водяного знака

Данная статья описывает использование плагина водяного знака для добавления изображений-водяных знаков на потоки камеры.

## Демонстрация

## Предварительные требования

- TRTC Web SDK версии ≥ 5.3.0.

## Этапы реализации

### Установка плагина водяного знака

```
import { Watermark } from 'trtc-sdk-v5/plugins/video-effect/watermark';let trtc = TRTC.create({ plugins: [Watermark] });
```

### Открытие камеры

```
await trtc.startLocalVideo({  view: 'local-video'  option: {    mirror: false  }});
```

### Запуск плагина водяного знака

```
await trtc.startPlugin('Watermark', {  imageUrl: 'https://web.sdk.qcloud.com/trtc/webrtc/test/qer-test/watermark/trtc-watermark-test.png'});
```

После тестирования можно заменить URL тестового изображения на URL собственного водяного знака. Рекомендуется использовать формат PNG с прозрачностью.

### Остановка плагина водяного знака

```
await trtc.stopPlugin('Watermark');
```

## Описание API

### trtc.startPlugin('Watermark', options)

Запуск плагина водяного знака.

#### options

| Имя | Тип | Атрибуты | Описание |
| --- | --- | --- | --- |
| imageUrl | `string` | Обязательно | URL изображения водяного знака |
| x | `string` | Опционально | Левый отступ водяного знака |
| y | `string` | Опционально | Верхний отступ водяного знака |
| size | `string` \|`number` \|`object` | Опционально | **При передаче строки:**`"cover"` масштабирует изображение фона полностью на область фона, что может привести к невидимости части изображения. `"contain"` масштабирует изображение фона так, чтобы оно полностью поместилось в область фона, возможно оставляя некоторые области пустыми. **При передаче числа:**`x` масштабирует изображение фона в x раз, например 0.5, с допустимым диапазоном `(0,1]` **При передаче объекта:**Вы можете указать вручную, передав `{width: 200, height: 300}` **По умолчанию**`cover` |

**Пример:**

```
await trtc.startPlugin('Watermark', {  imageUrl: 'https://web.sdk.qcloud.com/trtc/webrtc/test/qer-test/watermark/tv2.png',  size: 'contain'});
```

```
await trtc.startPlugin('Watermark', {  imageUrl: 'https://web.sdk.qcloud.com/trtc/webrtc/test/qer-test/watermark/tv2.png',  size: 'cover'});
```

```
await trtc.startPlugin('Watermark', {  imageUrl: 'https://web.sdk.qcloud.com/trtc/webrtc/test/qer-test/watermark/tv2.png',  x: 0,  y: 0,  size: 0.5});
```

```
await trtc.startPlugin('Watermark', {  imageUrl: 'https://web.sdk.qcloud.com/trtc/webrtc/test/qer-test/watermark/tv2.png',  x: 0,  y: 0,  size: {    width: 100,    height: 200  }});
```

### trtc.stopPlugin('Watermark')

Остановка плагина водяного знака.

**Пример:**

```
await trtc.stopPlugin('Watermark');
```

## Часто задаваемые вопросы

1. **Зеркалится ли водяной знак?**

По умолчанию включено зеркалирование локального предпросмотра, поэтому водяной знак также будет зеркален. Вы можете отключить зеркалирование локального изображения предпросмотра.

```
await trtc.updateLocalVideo({  option: {    mirror: false  }});
```


---
*Источник: [https://trtc.io/document/59661](https://trtc.io/document/59661)*

---
*Источник (EN): [enable-watermark.md](./enable-watermark.md)*
