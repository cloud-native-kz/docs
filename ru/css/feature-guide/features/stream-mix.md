# Микширование потоков

CSS предоставляет функцию микширования потоков в реальном времени, которая может синхронно объединять несколько входных потоков в новый поток на основе настроенного макета микширования потока для интерактивной прямой трансляции. Кроме того, функция микширования потоков интегрирована с TencentCloud API 3.0. Для получения дополнительной информации см. [CreateCommonMixStream](https://intl.cloud.tencent.com/document/product/267/35997). В этом документе на примерах описано, как реализовать микширование потоков в различных сценариях.

## Примечания

- Использование микширования потоков приводит к взиманию платежей за трансcodирование. Для получения дополнительной информации см. [Live Transcoding (Watermarking, Stream Mixing)](https://intl.cloud.tencent.com/document/product/267/39604).
- Для использования функции кроппинга и обрезки значение параметра кроппинга не должно превышать значение параметра входного потока.

## Поддерживаемые функции

- Одновременное микширование до **16** потоков.
- Микширование до **5** типов входных источников (аудио и видео, только аудио, только видео, изображение и канва).
- Выход смешанных потоков в виде нового потока.
- Поддержка кроппинга и водяных знаков.
- Поддержка конфигурации шаблонов.
- Поддержка записи на основе микширования потока.
- Переключение типов и позиций микширования потока в реальном времени.
- Беспрерывное запуск/отмена микширования потока.

## Общие шаблоны макетов

Общие шаблоны включают 10, 30, 40, 310, 410, 510 и 610. При их использовании вам не требуется вводить параметры позиции и длину/ширину входного потока, и **исходное изображение будет автоматически масштабировано.** Вам нужно только передать ID шаблона.

**Изображения превью общих шаблонов макетов:**

| Изображение превью шаблона 10 | Изображение превью шаблона 30 |
| --- | --- |
| ![](https://staticintl.cloudcachetci.com/cms/backend-cms/9ac65e4e507911ee974d5254005f490f.jpeg) | ![](https://staticintl.cloudcachetci.com/cms/backend-cms/a231b195507911ee94c3525400d793d0.jpeg) |
| Изображение превью шаблона 40 | Изображение превью шаблона 310 |
| ![](https://staticintl.cloudcachetci.com/cms/backend-cms/34989b9c507911ee84f2525400494e51.jpeg) | ![](https://staticintl.cloudcachetci.com/cms/backend-cms/3a74ad7f507911ee84f2525400494e51.jpeg) |
| Изображение превью шаблона 410 | Изображение превью шаблона 510 |
| ![](https://staticintl.cloudcachetci.com/cms/backend-cms/b2f66b48507911ee974d5254005f490f.jpeg) | ![](https://staticintl.cloudcachetci.com/cms/backend-cms/b6b119b2507911ee974d5254005f490f.jpeg) |
| Изображение превью шаблона 610 |  |
| ![](https://staticintl.cloudcachetci.com/cms/backend-cms/ba64aaac507911ee84f2525400494e51.jpeg) |  |

## Создание сеанса микширования потока

### Параметры

Для получения дополнительной информации см. [CreateCommonMixStream](https://intl.cloud.tencent.com/document/product/267/35997).

### Сценарий 1. Применение микширования потока — использование шаблона 20

Этот пример показывает, как использовать предустановленный шаблон микширования потока для микширования потоков.

#### Образец входного кода

```
https://live.tencentcloudapi.com/?Action=CreateCommonMixStream&MixStreamSessionId=test_room&MixStreamTemplateId=20&OutputParams.OutputStreamName=test_stream1&InputStreamList.0.InputStreamName=test_stream1&InputStreamList.0.LayoutParams.ImageLayer=1&InputStreamList.1.InputStreamName=test_stream2&InputStreamList.1.LayoutParams.ImageLayer=2&<Common request parameters>
```

#### Образец выходного кода

```
{  "Response": {    "RequestId": "e8fa8015-0892-40d5-95c4-12a4bc06ed31"  }}
```

#### Эффект микширования потока для подключения микрофона

![img](https://staticintl.cloudcachetci.com/cms/backend-cms/f1de0933507911ee94c3525400d793d0.jpeg)

### Сценарий 2. Применение микширования потока — использование шаблона 390

Этот пример показывает, как использовать предустановленный шаблон микширования потока для микширования потоков.

#### Образец входного кода

```
https://live.tencentcloudapi.com/?Action=CreateCommonMixStream&MixStreamSessionId=test_room&MixStreamTemplateId=390&OutputParams.OutputStreamName=test_stream2&InputStreamList.0.InputStreamName=test_stream1&InputStreamList.0.LayoutParams.ImageLayer=1&InputStreamList.0.LayoutParams.InputType=3&InputStreamList.0.LayoutParams.ImageWidth=1920 (canvas width)&InputStreamList.0.LayoutParams.ImageHeight=1080 (canvas height)&InputStreamList.0.LayoutParams.Color=0x000000&InputStreamList.1.InputStreamName=test_stream2&InputStreamList.1.LayoutParams.ImageLayer=2&InputStreamList.2.InputStreamName=test_stream3&InputStreamList.2.LayoutParams.ImageLayer=3&<Common request parameters>
```

#### Образец выходного кода

```
{  "Response": {    "RequestId": "9d8d5837-2273-4936-8661-781aeab9bc9c"  }}
```

#### Эффект микширования потока для конкурса хостов

![img](https://staticintl.cloudcachetci.com/cms/backend-cms/f1df3c8f507911eeabd75254005810a4.jpeg)

### Сценарий 3. Пользовательское микширование потока

Используйте пользовательский макет, где параметры позиции `LocationX` и `LocationY` представляют абсолютное расстояние в пикселях между верхним левым углом небольшого изображения и верхним левым углом фонового изображения.

![](https://staticintl.cloudcachetci.com/cms/backend-cms/f1bceb81507911ee974d5254005f490f.png)

#### Образец входного кода

```
https://live.tencentcloudapi.com/?Action=CreateCommonMixStream&MixStreamSessionId=test_room&OutputParams.OutputStreamName=test_stream2&InputStreamList.0.InputStreamName=test_stream1&InputStreamList.0.LayoutParams.ImageLayer=1&InputStreamList.0.LayoutParams.InputType=3&InputStreamList.0.LayoutParams.ImageWidth = 1920&InputStreamList.0.LayoutParams.ImageHeight= 1080&InputStreamList.0.LayoutParams.Color=0x000000&InputStreamList.1.InputStreamName=test_stream2&InputStreamList.1.LayoutParams.ImageLayer=2&InputStreamList.1.LayoutParams.ImageWidth = 640&InputStreamList.1.LayoutParams.ImageHeight= 360&InputStreamList.1.LayoutParams.LocationX= 50&InputStreamList.1.LayoutParams.LocationY= 720&InputStreamList.2.InputStreamName=test_stream3&InputStreamList.2.LayoutParams.ImageLayer=3&InputStreamList.2.LayoutParams.ImageWidth = 640&InputStreamList.2.LayoutParams.ImageHeight= 360&InputStreamList.2.LayoutParams.LocationX= 740&InputStreamList.2.LayoutParams.LocationY= 720&<Common request parameters>
```

#### Образец выходного кода

```
{  "Response": {    "RequestId": "8c443359-ba07-4b81-add8-a6ff54f9bf54"  }}
```

#### Эффект пользовательского микширования потока

![](https://staticintl.cloudcachetci.com/cms/backend-cms/f1de8b50507911ee94c3525400d793d0.png)

## Отмена микширования потока

### Параметры

Для получения дополнительной информации см. [CancelCommonMixStream](https://intl.cloud.tencent.com/document/product/267/35998).

### Примеры

Этот пример показывает, как отменить микширование потока по ID сеанса.

#### Образец входного кода

```
https://live.tencentcloudapi.com/?Action=CancelCommonMixStream&MixStreamSessionId=test_room
```

#### Образец выходного кода

```
{  "Response": {    "RequestId": "3c140219-cfe9-470e-b241-907877d6fb03"  }}
```

> **Примечание:** После применения отмены микширования потока подождите как минимум 5 секунд перед его отменой. После отмены микширования потока подождите как минимум половину минуты перед повторным применением микширования потока с использованием того же ID сеанса.

## Коды ошибок

Для API микширования потока 3.0 большинство распространённых кодов ошибок преобразованы в стиль [кода ошибки API 3.0](https://www.tencentcloud.com/en/document/product/267/35997#6.-error-code). Однако некоторые коды ошибок остаются неизменными, которые будут предоставлены в формате `err_code [ $code ],msg [ $message ]` в `Message` и выведены как ошибка `InvalidParameter`. Причины конкретных кодов приведены ниже:

| Код ошибки | Причина | Устранение проблемы |
| --- | --- | --- |
| -1 | При разборе входных параметров произошла ошибка | Проверьте, правильный ли формат JSON в теле запроса. Проверьте, не пустой ли `InputStreamList`. |
| -2 | Неправильный входной параметр | Проверьте, не слишком ли велик параметр изображения. |
| -3 | Неправильное количество потоков | Проверьте, находится ли количество входных потоков в диапазоне [1,16]. |
| -4 | Неправильный параметр потока | Проверьте, находится ли длина/ширина входного/выходного потока в диапазоне (0,3000). Проверьте, находится ли количество входных потоков в диапазоне (0,16]. Проверьте, несёт ли входной поток `LayoutParams`. Проверьте, поддерживается ли `InputType` (допустимые значения: 0, 2, 3, 4, 5). Проверьте, находится ли длина ID потока в диапазоне (1,80). |
| -11 | Ошибка слоя | Проверьте, совпадает ли количество слоёв с количеством входных потоков. Проверьте, нет ли дублирования ID слоя. Проверьте, находится ли ID слоя в диапазоне (0,16]. |
| -20 | Входной параметр не соответствует API | Проверьте, соответствует ли количество входных потоков ID шаблона. Проверьте, правильный ли параметр цвета. |
| -21 | Неправильное количество входных потоков для микширования потока | Проверьте, есть ли как минимум два входных потока. |
| -28 | Ошибка при получении длины/ширины фона | Проверьте, установлены ли длина и ширина канвы при установке канвы. Проверьте, существует ли фоновый поток (микширование потока должно начаться через 5 секунд после начала передачи). |
| -29 | Неправильный параметр кроппинга | Проверьте, не выходит ли позиция кроппинга за пределы диапазона длины/ширины потока. |
| -33 | Неправильный ID изображения водяного знака | Проверьте, установлен ли ID входного изображения. |
| -34 | Ошибка при получении URL-адреса изображения водяного знака | Проверьте, было ли изображение успешно загружено и был ли сгенерирован URL-адрес. |
| -111 | Параметр `OutputStreamName` не соответствует `OutputStreamType` | Если `OutputStreamType` установлен на `0`, `OutputStreamName` должен быть в `InputStreamList`. Если `OutputStreamType` установлен на `1`, `OutputStreamName` не должен быть в `InputStreamList`. |
| -300 | ID выходного потока уже использован | Проверьте, принадлежит ли текущий выходной поток другой задаче микширования потока. |
| -505 | Ошибка поиска входного потока в `upload` | Проверьте, началось ли микширование потока через 5 секунд после начала передачи и может ли поток воспроизводиться. |
| -507 | Ошибка при запросе параметров длины/ширины потока | Проверьте, установлены ли длина и ширина канвы. Проверьте, была ли передача успешной. Рекомендуется начать микширование потока через 5 секунд после начала передачи. |
| -508 | Неправильный ID выходного потока | Проверьте, используются ли разные ID выходных потоков одним и тем же `MixStreamSessionId`. |
| -10031 | Ошибка при запуске микширования потока | Рекомендуется начать микширование потока через 5 секунд после начала передачи. |
| -30300-31001-31002 | `sessionid` не существует при отмене микширования потока | Проверьте, существует ли `MixStreamSessionId`. |
| -31003 | ID выходного потока не соответствует идентификатору в `session` | Проверьте ID выходного потока, введённый при отмене микширования потока. |
| -31004 | Неправильный битрейт выходного потока | Проверьте, находится ли битрейт выходного потока в диапазоне [1,50000]. |
| Прочие | Для других ошибок, пожалуйста, [свяжитесь с службой поддержки](https://www.tencentcloud.com/contact-us). | - |

## Часто задаваемые вопросы

- [Как обеспечить автоматическое масштабирование входных потоков без чёрных полос в видеоизображении при микшировании потока?](https://intl.cloud.tencent.com/document/product/267/38255)
- [Что делать, если код ошибки -505 возвращается при микшировании потока после передачи?](https://intl.cloud.tencent.com/document/product/267/38255)
- [Что произойдёт, если не отменить микширование потока после его применения?](https://intl.cloud.tencent.com/document/product/267/38255)
- [Почему видеоизображение помощника хоста в смешанном потоке находится не в ожидаемой позиции?](https://intl.cloud.tencent.com/document/product/267/38255)

> **Примечание:** Дополнительно о микшировании потока см. [On-cloud Stream Mix](https://intl.cloud.tencent.com/document/product/267/38255).


---
*Источник: [https://www.tencentcloud.com/document/product/267/37665](https://www.tencentcloud.com/document/product/267/37665)*

---
*Источник (EN): [stream-mix.md](./stream-mix.md)*
