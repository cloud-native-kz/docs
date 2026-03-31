# Включение аудио микшера

В этой статье описано, как добавить фоновую музыку во время звонка.

## Демонстрация

## Предварительные требования

- TRTC версии 5.1+
- Следующие платформы поддерживают добавление фоновой музыки во время звонка:

| Операционная система | Тип браузера | Минимальная версия браузера |
| --- | --- | --- |
| Mac OS | Desktop Chrome | 56+ |
|  | Desktop Safari | 11+ |
|  | Desktop Firefox | 56+ |
|  | Desktop Edge | 80+ |
| Windows | Desktop Chrome | 56+ |
|  | Desktop QQ Browser | 10.4+ |
|  | Desktop Firefox | 56+ |
|  | Desktop Edge | 80+ |
| iOS | Mobile Safari | 14+ |
|  | WeChat Embedded Web | ✓ |
| Android | Mobile Chrome | 81+ |
|  | WeChat Embedded Web | ✓ |
|  | Mobile QQ Browser | ✓ |

## Процесс внедрения

### Запуск фоновой музыки

> - При воспроизведении файлов звуковых эффектов из интернета файлы звуковых эффектов должны поддерживать `CORS` и протокол доступа должен быть `https`.
> - Поддерживаемые форматы включают MP3, AAC (и другие аудиоформаты, поддерживаемые браузерами).
> - До любого взаимодействия пользователя браузеры запрещают веб-страницам воспроизводить медиа со звуком. Рекомендуется направить пользователей на выполнение действия клика перед вызовом этого интерфейса.
> - Справка: [Autoplay_guide](https://developer.mozilla.org/en-US/docs/Web/Media/Autoplay_guide).

```
await trtc.startPlugin('AudioMixer', {  id: 'count',  url: '../assets/count.mp3',  loop: true,  volume: 0.2})
```

### Обновление фоновой музыки

Выполните операции с фоновой музыкой.

```
// отключить повторное воспроизведение
await trtc.updatePlugin('AudioMixer', {  id: 'count',  loop: false})
// установка громкости
await trtc.updatePlugin('AudioMixer', {  id: 'count',  volume: 1})
// пауза музыки `count`
await trtc.updatePlugin('AudioMixer', {  id: 'count',  loop: true,  volume: 0.2,  operation: 'pause'})
// возобновление музыки `count`
await trtc.updatePlugin('AudioMixer', {  id: 'count',  operation: 'resume'})
// воспроизведение `count` с 5 секунды
await trtc.updatePlugin('AudioMixer', {  id: 'count',  seekFrom: 5})
```

### Остановка фоновой музыки

Остановите фоновую музыку, которая больше не требуется.

```
await trtc.stopPlugin('AudioMixer', {  id: 'count'})
```

## API

### trtc.startPlugin('AudioMixer', options)

Запустить фоновую музыку.

#### options

| Название | Тип | Обязательно | Описание |
| --- | --- | --- | --- |
| id | `string` | Да | Установите уникальный ID для каждого входящего URL музыки |
| url | `string` | Да | URL музыкального файла. **Необходимо передать один из url и track**. Если переданы оба, будет выбран url. |
| track | `MediaStreamAudioTrack` | Да | Трек MediaStream музыки. **Необходимо передать один из url и track**. Вы можете передать трек, извлеченный из тега `<audio/>`. Если переданы оба, будет выбран url. |
| loop | `boolean` | Нет | Повторное воспроизведение, по умолчанию false |
| volume | `number` | Нет | Установите начальную громкость, по умолчанию 1 (0-1) |

```
await trtc.startPlugin('AudioMixer', {  id: 'count',  url: '../assets/count.mp3',  loop: true,  volume: 0.2})
```

### trtc.updatePlugin('AudioMixer', options)

Обновить фоновую музыку.

#### options

| Название | Тип | Обязательно | Описание |
| --- | --- | --- | --- |
| id | `string` | Да | Уникальный ID для каждого входящего URL музыки, установленный при вызове startPlugin |
| loop | `boolean` | Нет | Повторное воспроизведение, по умолчанию false |
| volume | `number` | Нет | Установите начальную громкость, по умолчанию 1 (0-1) |
| seekFrom | `number` | Нет | Начать воспроизведение с какой-то секунды, этот параметр требует, чтобы файл музыкального ресурса поддерживал [HTTP range requests](https://developer.mozilla.org/en-US/docs/Web/HTTP/Range_requests). |
| operation | `number` | Нет | Операция над фоновой музыкой: 'pause' | 'resume' | 'stop' |

**Пример:**

```
await trtc.updatePlugin('AudioMixer', {  id: 'count',  loop: true,  volume: 0.2,  operation: 'pause'})
```

### trtc.stopPlugin('AudioMixer', options)

Остановить фоновую музыку, которая больше не требуется.

#### options

| Название | Тип | Обязательно | Описание |
| --- | --- | --- | --- |
| id | `string` | Да | Уникальный ID для каждого входящего URL музыки, установленный при вызове startPlugin |

**Пример:**

```
await trtc.stopPlugin('AudioMixer', {  id: 'count'})
```

## Часто задаваемые вопросы

1. **Ошибка Cross-Origin?**

Например: Access to audio at XXX from origin XXX has been blocked by CORS policy: No 'Access-Control-Allow-Origin' header is
present on the requested resource.

Решение: Необходимо настроить протокол CORS для ваших файлов музыки из интернета.

2. **Неправильный аудиоформат, невозможно воспроизвести в браузере?**

Например: NotSupportedError: The operation is not supported.

Решение: Необходимо использовать аудиоформат, поддерживаемый браузером.


---
*Источник: [https://trtc.io/document/59660](https://trtc.io/document/59660)*

---
*Источник (EN): [enable-audio-mixer.md](./enable-audio-mixer.md)*
