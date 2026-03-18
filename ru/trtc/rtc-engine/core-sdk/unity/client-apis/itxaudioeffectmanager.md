# ITXAudioEffectManager

Copyright (c) 2021 Tencent. All rights reserved.

Модуль: класс управления фоновой музыкой, короткими звуковыми эффектами и голосовыми эффектами

Описание: устанавливает фоновую музыку, короткие звуковые эффекты и голосовые эффекты

**ITXAudioEffectManager**

## ITXMusicPreloadObserver

| FuncList | DESC |
| --- | --- |
| [onLoadProgress](https://www.tencentcloud.com/document/product/647/72273#e0b94a4cf18adc2a2e0fcdddc1ad465c) | Прогресс предварительной загрузки фоновой музыки. |
| [onLoadError](https://www.tencentcloud.com/document/product/647/72273#44aad944a2269062b3524486f51c17ab) | Ошибка предварительной загрузки фоновой музыки. |

## ITXMusicPlayObserver

| FuncList | DESC |
| --- | --- |
| [onStart](https://www.tencentcloud.com/document/product/647/72273#e4f3ff72134a022db8cc565d0e77f7d9) | Фоновая музыка началась. |
| [onPlayProgress](https://www.tencentcloud.com/document/product/647/72273#2d171f6f722275fc437c808599a766b6) | Прогресс воспроизведения фоновой музыки. |
| [onComplete](https://www.tencentcloud.com/document/product/647/72273#073b462da62e99eaee062502f02aa291) | Фоновая музыка завершена. |

## ITXAudioEffectManager

| FuncList | DESC |
| --- | --- |
| [enableVoiceEarMonitor](https://www.tencentcloud.com/document/product/647/72273#4208acb73b2d4e039abf04e94586729b) | Включение мониторинга звука в ушах. |
| [setVoiceEarMonitorVolume](https://www.tencentcloud.com/document/product/647/72273#0e03a32ca874725c3f342d0f38994512) | Установка громкости мониторинга звука в ушах. |
| [setVoiceReverbType](https://www.tencentcloud.com/document/product/647/72273#594b1f8ea546e6feddd5bc099c068cc5) | Установка эффектов голосового реверберанса. |
| [setVoiceChangerType](https://www.tencentcloud.com/document/product/647/72273#2474a4d4d98f91a693782ab6ea4bd7da) | Установка эффектов изменения голоса. |
| [setVoiceCaptureVolume](https://www.tencentcloud.com/document/product/647/72273#dc7aeeff9a590980c9854baa113b943f) | Установка громкости речи. |
| [setVoicePitch](https://www.tencentcloud.com/document/product/647/72273#9a511a407bb75cf865e4f919751a900f) | Установка тона речи. |
| [setMusicObserver](https://www.tencentcloud.com/document/product/647/72273#6b23ff69ceef3aa371c5e309bd198b85) | Установка обратного вызова фоновой музыки. |
| [startPlayMusic](https://www.tencentcloud.com/document/product/647/72273#073eca5a2e42f70cc408965b99cf19ff) | Запуск фоновой музыки. |
| [stopPlayMusic](https://www.tencentcloud.com/document/product/647/72273#bfccd5a9ca588a180b7d2337f5abe33b) | Остановка фоновой музыки. |
| [pausePlayMusic](https://www.tencentcloud.com/document/product/647/72273#672ab09a8a0a7a0da267a5814b612852) | Пауза фоновой музыки. |
| [resumePlayMusic](https://www.tencentcloud.com/document/product/647/72273#5c7bc9b66cab58e977437101c68a079a) | Возобновление фоновой музыки. |
| [setAllMusicVolume](https://www.tencentcloud.com/document/product/647/72273#0927a2e81fd4905199a68c0fcf66afee) | Установка громкости локального и удаленного воспроизведения фоновой музыки. |
| [setMusicPublishVolume](https://www.tencentcloud.com/document/product/647/72273#7d3423ab272548add0b3f12370f812a7) | Установка громкости удаленного воспроизведения конкретного трека музыки. |
| [setMusicPlayoutVolume](https://www.tencentcloud.com/document/product/647/72273#22f37ab144dcaa375ce2c341048613db) | Установка громкости локального воспроизведения конкретного трека музыки. |
| [setMusicPitch](https://www.tencentcloud.com/document/product/647/72273#5603e2817da23a9e9a9d2b465c74bdf0) | Регулировка тона фоновой музыки. |
| [setMusicSpeedRate](https://www.tencentcloud.com/document/product/647/72273#24c9dbeb79e49234018e5a4184755c2b) | Изменение скорости фоновой музыки. |
| [getMusicCurrentPosInMS](https://www.tencentcloud.com/document/product/647/72273#c49b787c173f29158549da21d4aa912a) | Получение прогресса воспроизведения (мс) фоновой музыки. |
| [getMusicDurationInMS](https://www.tencentcloud.com/document/product/647/72273#9c48d562afecc985b647089d17e6a340) | Получение общей длительности (мс) фоновой музыки. |
| [seekMusicToPosInTime](https://www.tencentcloud.com/document/product/647/72273#d55525f4a9a7b6429c8e7900065632aa) | Установка прогресса воспроизведения (мс) фоновой музыки. |
| [setMusicScratchSpeedRate](https://www.tencentcloud.com/document/product/647/72273#b601fddbe341e40579d36822c2c7c6a3) | Регулировка эффекта изменения скорости скретч-диска. |
| [setPreloadObserver](https://www.tencentcloud.com/document/product/647/72273#f48f2e4545243e61691b59b889062561) | Установка обратного вызова предварительной загрузки музыки. |
| [preloadMusic](https://www.tencentcloud.com/document/product/647/72273#e5819722476a52454e1d603d8577b6cf) | Предварительная загрузка фоновой музыки. |
| [getMusicTrackCount](https://www.tencentcloud.com/document/product/647/72273#a79a27ddc6e945086c3241e74cd145d3) | Получение количества треков фоновой музыки. |
| [setMusicTrack](https://www.tencentcloud.com/document/product/647/72273#dba8f5ec8c03a44d9f3accbde4831e2c) | Указание трека воспроизведения фоновой музыки. |

## StructType

| FuncList | DESC |
| --- | --- |
| [AudioMusicParam](https://www.tencentcloud.com/document/product/647/72273#79f73cf8c10624089eddf7856fdb22c7) | Информация о воспроизведении фоновой музыки. |

## EnumType

| EnumType | DESC |
| --- | --- |
| [TXVoiceReverbType](https://www.tencentcloud.com/document/product/647/72273#b9abfb68de51b5a85074406dbe956cbf) | Эффекты реверберанса. |
| [TXVoiceChangeType](https://www.tencentcloud.com/document/product/647/72273#3b0f43f7ef1b3cd2b1fb7924f8d20319) | Эффекты изменения голоса. |

## onLoadProgress

**onLoadProgress**

| void onLoadProgress | (int musicId |
| --- | --- |
|  | int progress) |

#### Прогресс предварительной загрузки фоновой музыки.

## onLoadError

**onLoadError**

| void onLoadError | (int musicId |
| --- | --- |
|  | int errCode) |

#### Ошибка предварительной загрузки фоновой музыки.

| Param | DESC |
| --- | --- |
| errorCode | -4001: ошибка открытия файла, например обнаружены недействительные данные при обработке входных данных, протокол ffmpeg не найден и т. д.; -4002: ошибка декодирования, например повреждение аудиофайла, недоступность сервера сетевого аудиофайла и т. д.; -4003: количество предварительных загрузок превышено максимально допустимое, пожалуйста, сначала вызовите stopPlayMusic для освобождения ненужных предварительных загрузок; -4005: недействительный путь, пожалуйста, проверьте, указывает ли переданный путь на допустимый музыкальный файл; -4006: недействительный URL, пожалуйста, используйте браузер для проверки, может ли переданный URL-адрес загрузить требуемый музыкальный файл; -4007: отсутствует аудиопоток, пожалуйста, подтвердите, является ли переданный вами файл допустимым аудиофайлом и не поврежден ли файл; -4008: неподдерживаемый формат, пожалуйста, подтвердите, является ли формат файла, который вы передали, поддерживаемым форматом. Мобильная версия поддерживает [mp3, aac, m4a, wav, ogg, mp4, mkv], а версия для настольных компьютеров поддерживает [mp3, aac, m4a, wav, mp4, mkv]. |

## onStart

**onStart**

| void onStart | (int musicId |
| --- | --- |
|  | int errCode) |

#### Фоновая музыка началась.

Вызывается после запуска фоновой музыки.

| Param | DESC |
| --- | --- |
| errCode | 0: успешно начало воспроизведение; -4001: ошибка открытия файла, например обнаружены недействительные данные при обработке входных данных, протокол ffmpeg не найден и т. д.; -4005: недействительный путь, пожалуйста, проверьте, указывает ли переданный путь на допустимый музыкальный файл; -4006: недействительный URL, пожалуйста, используйте браузер для проверки, может ли переданный URL-адрес загрузить требуемый музыкальный файл. Если операционная система — iOS или MacOS, пожалуйста, убедитесь в использовании HTTPS-ссылок; -4007: отсутствует аудиопоток, пожалуйста, подтвердите, является ли переданный вами файл допустимым аудиофайлом и не поврежден ли файл; -4008: неподдерживаемый формат, пожалуйста, подтвердите, является ли формат файла, который вы передали, поддерживаемым форматом. Мобильная версия поддерживает [mp3, aac, m4a, wav, ogg, mp4, mkv], а версия для настольных компьютеров поддерживает [mp3, aac, m4a, wav, mp4, mkv]; -4009: количество одновременно воспроизводимой фоновой музыки превышено максимально допустимое. Эта ошибка возникает, когда одновременно воспроизводится более 10 фоновых музыкальных файлов. Пожалуйста, проверьте количество одновременно воспроизводимой фоновой музыки. |
| id | ID музыки. |

## onPlayProgress

**onPlayProgress**

| void onPlayProgress | (int musicId |
| --- | --- |
|  | long curPtsMS |
|  | long durationMS) |

#### Прогресс воспроизведения фоновой музыки.

## onComplete

**onComplete**

| void onComplete | (int musicId |
| --- | --- |
|  | int errCode) |

#### Фоновая музыка завершена.

Вызывается при завершении воспроизведения фоновой музыки или при возникновении ошибки.

| Param | DESC |
| --- | --- |
| errCode | 0: воспроизведение завершено; -4002: ошибка декодирования, например повреждение аудиофайла, недоступность сервера сетевого аудиофайла и т. д. |
| id | ID музыки. |

## enableVoiceEarMonitor

**enableVoiceEarMonitor**

| void enableVoiceEarMonitor | (bool enable) |
| --- | --- |

#### Включение мониторинга звука в ушах.

После включения мониторинга звука в ушах ведущие могут слышать в наушниках свой собственный голос, захватываемый микрофоном. Это предназначено для сценариев пения.

Мониторинг звука в ушах не может быть включен для наушников Bluetooth. Это связано с высокой задержкой наушников Bluetooth. Пожалуйста, попросите ведущих использовать проводные наушники через напоминание в пользовательском интерфейсе.

Поскольку не все телефоны обеспечивают отличные эффекты мониторинга звука в ушах, мы отключили эту функцию на некоторых телефонах.

| Param | DESC |
| --- | --- |
| enable | ` true: ` включить; ` false `: отключить |

> **Примечание**Мониторинг звука в ушах можно включить только при использовании наушников. Пожалуйста, напомните ведущим использовать проводные наушники.

## setVoiceEarMonitorVolume

**setVoiceEarMonitorVolume**

| void setVoiceEarMonitorVolume | (int volume) |
| --- | --- |

#### Установка громкости мониторинга звука в ушах.

Этот API используется для установки громкости мониторинга звука в ушах.

| Param | DESC |
| --- | --- |
| volume | Громкость. Диапазон значений: [0, 150]; по умолчанию: 100 |

> **Примечание**Если 100 все еще недостаточно громко для вас, вы можете установить громкость до 150, но это может иметь побочные эффекты.

## setVoiceReverbType

**setVoiceReverbType**

| void setVoiceReverbType | ([TXVoiceReverbType](https://www.tencentcloud.com/document/product/647/72273#b9abfb68de51b5a85074406dbe956cbf) reverbType) |
| --- | --- |

#### Установка эффектов голосового реверберанса.

Этот API используется для установки эффектов реверберанса для человеческого голоса. Подробнее о поддерживаемых эффектах см. в разделе [TXVoiceReverbType](https://www.tencentcloud.com/document/product/647/72273#b9abfb68de51b5a85074406dbe956cbf).

> **Примечание**Эффекты становятся недействительными после выхода из комнаты. Если вы хотите использовать тот же эффект после повторного входа в комнату, вам необходимо установить эффект снова, используя этот API.

## setVoiceChangerType

**setVoiceChangerType**

| void setVoiceChangerType | ([TXVoiceChangeType](https://www.tencentcloud.com/document/product/647/72273#3b0f43f7ef1b3cd2b1fb7924f8d20319) changerType) |
| --- | --- |

#### Установка эффектов изменения голоса.

Этот API используется для установки эффектов изменения голоса. Подробнее о поддерживаемых эффектах см. в разделе [TXVoiceChangeType](https://www.tencentcloud.com/document/product/647/72273#3b0f43f7ef1b3cd2b1fb7924f8d20319).

> **Примечание**Эффекты становятся недействительными после выхода из комнаты. Если вы хотите использовать тот же эффект после повторного входа в комнату, вам необходимо установить эффект снова, используя этот API.

## setVoiceCaptureVolume

**setVoiceCaptureVolume**

| void setVoiceCaptureVolume | (int volume) |
| --- | --- |

#### Установка громкости речи.

Этот API используется для установки громкости речи. Часто используется совместно с API установки громкости музыки [setAllMusicVolume](https://www.tencentcloud.com/document/product/647/72273#0927a2e81fd4905199a68c0fcf66afee) для балансировки громкости музыки и речи.

| Param | DESC |
| --- | --- |
| volume | Громкость. Диапазон значений: [0, 150]; по умолчанию: 100 |

> **Примечание**Если 100 все еще недостаточно громко для вас, вы можете установить громкость до 150, но это может иметь побочные эффекты.

## setVoicePitch

**setVoicePitch**

| void setVoicePitch | (double pitch) |
| --- | --- |

#### Установка тона речи.

Этот API используется для установки тона речи.

| Param | DESC |
| --- | --- |
| pitch | Тон. Диапазон значений: [-1.0f, 1.0f]; по умолчанию: 0.0f. |

## setMusicObserver

**setMusicObserver**

| void setMusicObserver | (int musicId |
| --- | --- |
|  | [ITXMusicPlayObserver](https://www.tencentcloud.com/document/product/647/72273#8bc42ffc210c9d2b244908a2c914e2d8) observer) |

#### Установка обратного вызова фоновой музыки.

Перед воспроизведением фоновой музыки используйте этот API для установки обратного вызова музыки, который может информировать вас о прогрессе воспроизведения.

| Param | DESC |
| --- | --- |
| musicId | ID музыки |
| observer | Дополнительную информацию см. в API, определенных в ` ITXMusicPlayObserver `. |

> **Примечание**1. Если ID не нужен, можно установить observer в NULL для полного его освобождения.

## startPlayMusic

**startPlayMusic**

| void startPlayMusic | ([AudioMusicParam](https://www.tencentcloud.com/document/product/647/72273#79f73cf8c10624089eddf7856fdb22c7) musicParam) |
| --- | --- |

#### Запуск фоновой музыки.

Вы должны назначить ID каждому музыкальному треку, чтобы вы могли запускать, останавливать или устанавливать громкость музыкальных треков по ID.

| Param | DESC |
| --- | --- |
| musicParam | Параметр музыки |

> **Примечание**1. Если вы воспроизводите один и тот же музыкальный трек несколько раз, пожалуйста, используйте один и тот же ID вместо отдельного ID для каждого воспроизведения. 2. Если вы хотите воспроизводить разные музыкальные треки одновременно, используйте для них разные ID. 3. Если вы используете один и тот же ID для воспроизведения музыкального трека, отличающегося от текущего, SDK остановит текущий трек перед воспроизведением нового.

## stopPlayMusic

**stopPlayMusic**

| void stopPlayMusic | (int musicId) |
| --- | --- |

#### Остановка фоновой музыки.

| Param | DESC |
| --- | --- |
| id | ID музыки |

## pausePlayMusic

**pausePlayMusic**

| void pausePlayMusic | (int musicId) |
| --- | --- |

#### Пауза фоновой музыки.

| Param | DESC |
| --- | --- |
| id | ID музыки |

## resumePlayMusic

**resumePlayMusic**

| void resumePlayMusic | (int musicId) |
| --- | --- |

#### Возобновление фоновой музыки.

| Param | DESC |
| --- | --- |
| id | ID музыки |

## setAllMusicVolume

**setAllMusicVolume**

| void setAllMusicVolume | (int volume) |
| --- | --- |

#### Установка громкости локального и удаленного воспроизведения фоновой музыки.

Этот API используется для установки громкости локального и удаленного воспроизведения фоновой музыки.

- Локальная громкость: громкость музыки, которую слышат ведущие
- Удаленная громкость: громкость музыки, которую слышит аудитория

| Param | DESC |
| --- | --- |
| volume | Громкость. Диапазон значений: [0, 150]; по умолчанию: 60 |

> **Примечание**Если 100 все еще недостаточно громко для вас, вы можете установить громкость до 150, но это может иметь побочные эффекты.

## setMusicPublishVolume

**setMusicPublishVolume**

| void setMusicPublishVolume | (int musicId |
| --- | --- |
|  | int volume) |

#### Установка громкости удаленного воспроизведения конкретного трека музыки.

Этот API используется для управления громкостью удаленного воспроизведения (громкостью, которую слышит аудитория) конкретного музыкального трека.

| Param | DESC |
| --- | --- |
| id | ID музыки |
| volume | Громкость. Диапазон значений: [0, 150]; по умолчанию: 60 |

> **Примечание**Если 100 все еще недостаточно громко для вас, вы можете установить громкость до 150, но это может иметь побочные эффекты.

## setMusicPlayoutVolume

**setMusicPlayoutVolume**

| void setMusicPlayoutVolume | (int musicId |
| --- | --- |
|  | int volume) |

#### Установка громкости локального воспроизведения конкретного трека музыки.

Этот API используется для управления громкостью локального воспроизведения (громкостью, которую слышат ведущие) конкретного музыкального трека.

| Param | DESC |
| --- | --- |
| id | ID музыки |
| volume | Громкость. Диапазон значений: [0, 150]. По умолчанию: 60 |

> **Примечание**Если 100 все еще недостаточно громко для вас, вы можете установить громкость до 150, но это может иметь побочные эффекты.

## setMusicPitch

**setMusicPitch**

| void setMusicPitch | (int musicId |
| --- | --- |
|  | double pitch) |

#### Регулировка тона фоновой музыки.

| Param | DESC |
| --- | --- |
| id | ID музыки |
| pitch | Тон. Диапазон значений: числа с плавающей запятой в диапазоне [-1, 1]; по умолчанию: 0.0f |

## setMusicSpeedRate

**setMusicSpeedRate**

| void setMusicSpeedRate | (int musicId |
| --- | --- |
|  | double speedRate) |

#### Изменение скорости фоновой музыки.

| Param | DESC |
| --- | --- |
| id | ID музыки |
| speedRate | Скорость музыки. Диапазон значений: числа с плавающей запятой в диапазоне [0.5, 2]; по умолчанию: 1.0f |

## getMusicCurrentPosInMS

**getMusicCurrentPosInMS**

| int getMusicCurrentPosInMS | (int musicId) |
| --- | --- |

#### Получение прогресса воспроизведения (мс) фоновой музыки.

| Param | DESC |
| --- | --- |
| id | ID музыки |

#### Return Desc:

Миллисекунды, прошедшие с начала воспроизведения. -1 указывает на ошибку при получении прогресса воспроизведения.

## getMusicDurationInMS

**getMusicDurationInMS**

| int getMusicDurationInMS | (string path) |
| --- | --- |

#### Получение общей длительности (мс) фоновой музыки.

| Param | DESC |
| --- | --- |
| path | Путь к музыкальному файлу. |

#### Return Desc:

Возвращает длительность указанного музыкального файла. -1 указывает на ошибку при получении длительности.

## seekMusicToPosInTime

**seekMusicToPosInTime**

| void seekMusicToPosInTime | (int musicId |
| --- | --- |
|  | int pts) |

#### Установка прогресса воспроизведения (мс) фоновой музыки.

| Param | DESC |
| --- | --- |
| id | ID музыки |
| pts | Единица: миллисекунда |

> **Примечание**Не вызывайте этот API часто, так как музыкальный файл может быть прочитан и записан каждый раз при вызове API, что может занять много времени. Дождитесь завершения перетаскивания пользователем ползунка прогресса перед вызовом этого API. Контроллер полосы прогресса в пользовательском интерфейсе имеет тенденцию обновлять прогресс с высокой частотой при перетаскивании пользователем полосы прогресса. Это приведет к плохому пользовательскому опыту, если вы не ограничиваете частоту.

## setMusicScratchSpeedRate

**setMusicScratchSpeedRate**

| void setMusicScratchSpeedRate | (int musicId |
| --- | --- |
|  | float scratchSpeedRate) |

#### Регулировка эффекта изменения скорости скретч-диска.

| Param | DESC |
| --- | --- |
| id | ID музыки |
| scratchSpeedRate | Скорость скретч-диска, значение по умолчанию 1.0f, диапазон: число с плавающей запятой в диапазоне [-12.0 ~ 12.0], положительное/отрицательное значение скорости указывает направление положительное/отрицательное, а абсолютное значение указывает скорость. |

> **Примечание**Условие: успешное выполнение preloadMusic.

## setPreloadObserver

**setPreloadObserver**

| void setPreloadObserver | ([ITXMusicPreloadObserver](https://www.tencentcloud.com/document/product/647/72273#98bf86ba1dcb3a8c0b7974bb09d50430) observer) |
| --- | --- |

#### Установка обратного вызова предварительной загрузки музыки.

Перед предварительной загрузкой музыки используйте этот API для установки обратного вызова предварительной загрузки, который может информировать вас о статусе предварительной загрузки.

| Param | DESC |
| --- | --- |
| observer | Дополнительную информацию см. в API, определенных в TXMusicPreloadObserver. |

## preloadMusic

**preloadMusic**

| void preloadMusic | ([AudioMusicParam](https://www.tencentcloud.com/document/product/647/72273#79f73cf8c10624089eddf7856fdb22c7) preloadParam)

---
*Источник (EN): [itxaudioeffectmanager.md](./itxaudioeffectmanager.md)*
