# TXAudioEffectManager

Copyright (c) 2021 Tencent. All rights reserved.

Модуль: класс управления фоновой музыкой, короткими звуковыми эффектами и голосовыми эффектами

Описание: установка фоновой музыки, коротких звуковых эффектов и голосовых эффектов

**TXAudioEffectManager**

## TXAudioEffectManager

| FuncList | DESC |
| --- | --- |
| [enableVoiceEarMonitor:](https://www.tencentcloud.com/document/product/647/50757#300c68bccbf3480ab8c99cf2f31d014a) | Включение мониторинга в наушниках. |
| [setVoiceEarMonitorVolume:](https://www.tencentcloud.com/document/product/647/50757#3857607a3e9b5fc2e57a77f2c1dd6359) | Установка громкости мониторинга в наушниках. |
| [setVoiceReverbType:](https://www.tencentcloud.com/document/product/647/50757#7135a441f275bed8330db039f1bfba2d) | Установка эффектов реверберации голоса. |
| [setVoiceChangerType:](https://www.tencentcloud.com/document/product/647/50757#fee0da19f6060c0544e73a79da113bd0) | Установка эффектов изменения голоса. |
| [setVoiceVolume:](https://www.tencentcloud.com/document/product/647/50757#9fe5b02fc52fa9bfae721e1f0d4d9427) | Установка громкости речи. |
| [setVoicePitch:](https://www.tencentcloud.com/document/product/647/50757#517e19882847820a81b870d49d1ae2f4) | Установка высоты тона речи. |
| [startPlayMusic:onStart:onProgress:onComplete:](https://www.tencentcloud.com/document/product/647/50757#3e6d92e47d6770c50e0e4ca4df429c31) | Запуск фоновой музыки. |
| [stopPlayMusic:](https://www.tencentcloud.com/document/product/647/50757#2214eecbdca5062136821aff0d95bfbe) | Остановка фоновой музыки. |
| [pausePlayMusic:](https://www.tencentcloud.com/document/product/647/50757#8e5076dea4c4b43df4c07cf1fe4003f1) | Пауза фоновой музыки. |
| [resumePlayMusic:](https://www.tencentcloud.com/document/product/647/50757#15f5b80077c596dc1d39402d421a6ec2) | Возобновление фоновой музыки. |
| [setAllMusicVolume:](https://www.tencentcloud.com/document/product/647/50757#8fafba6b1d27799ea32812f08f564ee5) | Установка локальной и удаленной громкости воспроизведения фоновой музыки. |
| [setMusicPublishVolume:volume:](https://www.tencentcloud.com/document/product/647/50757#50a9fe2dc5ee4a6f92160ef4f1367c13) | Установка удаленной громкости воспроизведения конкретной музыкальной дорожки. |
| [setMusicPlayoutVolume:volume:](https://www.tencentcloud.com/document/product/647/50757#5ba979d09b84dfe360785c659ab7c8b7) | Установка локальной громкости воспроизведения конкретной музыкальной дорожки. |
| [setMusicPitch:pitch:](https://www.tencentcloud.com/document/product/647/50757#6f7407593caa553bccee1da218e79d2e) | Регулировка высоты тона фоновой музыки. |
| [setMusicSpeedRate:speedRate:](https://www.tencentcloud.com/document/product/647/50757#5a66bf1956d164a98f5f274f46b9c3a7) | Изменение скорости фоновой музыки. |
| [getMusicCurrentPosInMS:](https://www.tencentcloud.com/document/product/647/50757#4d6f9629f7623102e3e04f5e05bdea1e) | Получение прогресса воспроизведения (мс) фоновой музыки. |
| [getMusicDurationInMS:](https://www.tencentcloud.com/document/product/647/50757#6ca86334e6bf179bc3cfd98ca5e01975) | Получение общей длительности (мс) фоновой музыки. |
| [seekMusicToPosInMS:pts:](https://www.tencentcloud.com/document/product/647/50757#c00ed7c5735f4c126f0fbd099cae8998) | Установка прогресса воспроизведения (мс) фоновой музыки. |
| [setMusicScratchSpeedRate:speedRate:](https://www.tencentcloud.com/document/product/647/50757#76ccca8d0e4ad4ef6ba3abc02170b18b) | Регулировка эффекта изменения скорости скретча. |
| [preloadMusic:onProgress:onError:](https://www.tencentcloud.com/document/product/647/50757#c5a7017fe11985ad47ba9e935d726020) | Предзагрузка фоновой музыки. |
| [getMusicTrackCount:](https://www.tencentcloud.com/document/product/647/50757#19fc33f9be59df8b0f4524219fbd4350) | Получение количества дорожек фоновой музыки. |
| [setMusicTrack:track:](https://www.tencentcloud.com/document/product/647/50757#bcac516dcc63f775829e34f75646fdf4) | Указание дорожки воспроизведения фоновой музыки. |

## StructType

| FuncList | DESC |
| --- | --- |
| [TXAudioMusicParam](https://www.tencentcloud.com/document/product/647/50757#1b83f556d7876fc9f0ec4b5f8bea469c) | Информация о воспроизведении фоновой музыки. |

## EnumType

| EnumType | DESC |
| --- | --- |
| [TXVoiceReverbType](https://www.tencentcloud.com/document/product/647/50757#b9abfb68de51b5a85074406dbe956cbf) | Эффекты реверберации. |
| [TXVoiceChangeType](https://www.tencentcloud.com/document/product/647/50757#e6f03d6a29abd12b6ecc056432e40cc8) | Эффекты изменения голоса. |

## enableVoiceEarMonitor:

**enableVoiceEarMonitor:**

| - (void)enableVoiceEarMonitor: | (BOOL)enable |
| --- | --- |

**Включение мониторинга в наушниках.**

После включения мониторинга в наушниках ведущие могут слышать через наушники собственный голос, захватываемый микрофоном. Эта функция предназначена для сценариев пения.

Мониторинг в наушниках нельзя включить для беспроводных наушников Bluetooth. Это связано с высокой задержкой Bluetooth. Пожалуйста, попросите ведущих использовать проводные наушники через напоминание в интерфейсе.

Учитывая, что не все телефоны обеспечивают отличные эффекты мониторинга в наушниках, мы отключили эту функцию на некоторых телефонах.

| Param | DESC |
| --- | --- |
| enable | ` YES: ` включить; ` NO `: отключить |

> **Note**Мониторинг в наушниках можно включить только при использовании наушников. Пожалуйста, напомните ведущим использовать проводные наушники.

## setVoiceEarMonitorVolume:

**setVoiceEarMonitorVolume:**

| - (void)setVoiceEarMonitorVolume: | (NSInteger)volume |
| --- | --- |

**Установка громкости мониторинга в наушниках.**

Этот API используется для установки громкости мониторинга в наушниках.

| Param | DESC |
| --- | --- |
| volume | Громкость. Диапазон значений: [0, 150]; по умолчанию: 100 |

> **Note**Громкость мониторинга в наушниках является одним из наиболее важных факторов, влияющих на пользовательский опыт. Учитывая, что разные пользователи имеют разную чувствительность к громкости, настоятельно рекомендуется предоставить ползунок регулировки громкости мониторинга в наушниках в интерфейсе. Рекомендуемый диапазон регулировки составляет от 0 до 150. Эффект усиления 100-150 очень полезен для некоторых телефонов Android с низким уровнем записи.

## setVoiceReverbType:

**setVoiceReverbType:**

| - (void)setVoiceReverbType: | ([TXVoiceReverbType](https://www.tencentcloud.com/document/product/647/50757#b9abfb68de51b5a85074406dbe956cbf))reverbType |
| --- | --- |

**Установка эффектов реверберации голоса.**

Этот API используется для установки эффектов реверберации для человеческого голоса. О поддерживаемых эффектах см. [TXVoiceReverbType](https://www.tencentcloud.com/document/product/647/50757#b9abfb68de51b5a85074406dbe956cbf).

> **Note**Эффекты становятся недействительными после выхода из комнаты. Если вы хотите использовать один и тот же эффект после повторного входа в комнату, вам необходимо установить эффект снова с помощью этого API.

## setVoiceChangerType:

**setVoiceChangerType:**

| - (void)setVoiceChangerType: | ([TXVoiceChangeType](https://www.tencentcloud.com/document/product/647/50757#e6f03d6a29abd12b6ecc056432e40cc8))changerType |
| --- | --- |

**Установка эффектов изменения голоса.**

Этот API используется для установки эффектов изменения голоса. О поддерживаемых эффектах см. [TXVoiceChangeType](https://www.tencentcloud.com/document/product/647/50757#e6f03d6a29abd12b6ecc056432e40cc8).

> **Note**Эффекты становятся недействительными после выхода из комнаты. Если вы хотите использовать один и тот же эффект после повторного входа в комнату, вам необходимо установить эффект снова с помощью этого API.

## setVoiceVolume:

**setVoiceVolume:**

| - (void)setVoiceVolume: | (NSInteger)volume |
| --- | --- |

**Установка громкости речи.**

Этот API используется для установки громкости речи. Он часто используется вместе с API установки громкости музыки [setAllMusicVolume](https://www.tencentcloud.com/document/product/647/50757#8fafba6b1d27799ea32812f08f564ee5) для балансировки между громкостью музыки и речи.

| Param | DESC |
| --- | --- |
| volume | Громкость. Диапазон значений: [0, 150]; по умолчанию: 100 |

> **Note**Если 100 по-прежнему недостаточно громко, вы можете установить громкость до 150, но это может вызвать побочные эффекты.

## setVoicePitch:

**setVoicePitch:**

| -(void)setVoicePitch: | (double)pitch |
| --- | --- |

**Установка высоты тона речи.**

Этот API используется для установки высоты тона речи.

| Param | DESC |
| --- | --- |
| pitch | Высота тона. Диапазон значений: [-1.0f, 1.0f]; по умолчанию: 0.0f |

## startPlayMusic:onStart:onProgress:onComplete:

**startPlayMusic:onStart:onProgress:onComplete:**

| - (void)startPlayMusic: | ([TXAudioMusicParam](https://www.tencentcloud.com/document/product/647/50757#1b83f556d7876fc9f0ec4b5f8bea469c) *)musicParam |
| --- | --- |
| onStart: | (TXAudioMusicStartBlock _Nullable)startBlock |
| onProgress: | (TXAudioMusicProgressBlock _Nullable)progressBlock |
| onComplete: | (TXAudioMusicCompleteBlock _Nullable)completeBlock |

**Запуск фоновой музыки.**

Вы должны назначить идентификатор каждой музыкальной дорожке, чтобы вы могли запускать, останавливать или устанавливать громкость музыкальных дорожек по идентификатору.

| Param | DESC |
| --- | --- |
| completeBlock | Обратный вызов окончания музыки |
| musicParam | Параметр музыки |
| progressBlock | Обратный вызов прогресса воспроизведения |
| startBlock | Обратный вызов запуска музыки |

> **Note**1. Если вы воспроизводите одну и ту же музыкальную дорожку несколько раз, используйте один и тот же идентификатор вместо отдельного идентификатора для каждого воспроизведения. 2. Если вы хотите воспроизводить разные музыкальные дорожки одновременно, используйте для них разные идентификаторы. 3. Если вы используете один и тот же идентификатор для воспроизведения музыкальной дорожки, отличной от текущей, SDK остановит текущую дорожку и запустит новую.

## stopPlayMusic:

**stopPlayMusic:**

| - (void)stopPlayMusic: | (int32_t)id |
| --- | --- |

**Остановка фоновой музыки.**

| Param | DESC |
| --- | --- |
| id | Идентификатор музыки |

## pausePlayMusic:

**pausePlayMusic:**

| - (void)pausePlayMusic: | (int32_t)id |
| --- | --- |

**Пауза фоновой музыки.**

| Param | DESC |
| --- | --- |
| id | Идентификатор музыки |

## resumePlayMusic:

**resumePlayMusic:**

| - (void)resumePlayMusic: | (int32_t)id |
| --- | --- |

**Возобновление фоновой музыки.**

| Param | DESC |
| --- | --- |
| id | Идентификатор музыки |

## setAllMusicVolume:

**setAllMusicVolume:**

| - (void)setAllMusicVolume: | (NSInteger)volume |
| --- | --- |

**Установка локальной и удаленной громкости воспроизведения фоновой музыки.**

Этот API используется для установки локальной и удаленной громкости воспроизведения фоновой музыки.

- Локальная громкость: громкость музыки, слышимая ведущими
- Удаленная громкость: громкость музыки, слышимая аудиторией

| Param | DESC |
| --- | --- |
| volume | Громкость. Диапазон значений: [0, 150]; по умолчанию: 60 |

> **Note**Если 100 по-прежнему недостаточно громко, вы можете установить громкость до 150, но это может вызвать побочные эффекты.

## setMusicPublishVolume:volume:

**setMusicPublishVolume:volume:**

| - (void)setMusicPublishVolume: | (int32_t)id |
| --- | --- |
| volume: | (NSInteger)volume |

**Установка удаленной громкости воспроизведения конкретной музыкальной дорожки.**

Этот API используется для управления удаленной громкостью воспроизведения (громкость, слышимая аудиторией) конкретной музыкальной дорожки.

| Param | DESC |
| --- | --- |
| id | Идентификатор музыки |
| volume | Громкость. Диапазон значений: [0, 150]; по умолчанию: 60 |

> **Note**Если 100 по-прежнему недостаточно громко, вы можете установить громкость до 150, но это может вызвать побочные эффекты.

## setMusicPlayoutVolume:volume:

**setMusicPlayoutVolume:volume:**

| - (void)setMusicPlayoutVolume: | (int32_t)id |
| --- | --- |
| volume: | (NSInteger)volume |

**Установка локальной громкости воспроизведения конкретной музыкальной дорожки.**

Этот API используется для управления локальной громкостью воспроизведения (громкость, слышимая ведущими) конкретной музыкальной дорожки.

| Param | DESC |
| --- | --- |
| id | Идентификатор музыки |
| volume | Громкость. Диапазон значений: [0, 150]; по умолчанию: 60 |

> **Note**Если 100 по-прежнему недостаточно громко, вы можете установить громкость до 150, но это может вызвать побочные эффекты.

## setMusicPitch:pitch:

**setMusicPitch:pitch:**

| - (void)setMusicPitch: | (int32_t)id |
| --- | --- |
| pitch: | (double)pitch |

**Регулировка высоты тона фоновой музыки.**

| Param | DESC |
| --- | --- |
| id | Идентификатор музыки |
| pitch | Высота тона. Диапазон значений: числа с плавающей запятой в диапазоне [-1, 1]; по умолчанию: 0.0f |

## setMusicSpeedRate:speedRate:

**setMusicSpeedRate:speedRate:**

| - (void)setMusicSpeedRate: | (int32_t)id |
| --- | --- |
| speedRate: | (double)speedRate |

**Изменение скорости фоновой музыки.**

| Param | DESC |
| --- | --- |
| id | Идентификатор музыки |
| speedRate | Скорость музыки. Диапазон значений: числа с плавающей запятой в диапазоне [0.5, 2]; по умолчанию: 1.0f |

## getMusicCurrentPosInMS:

**getMusicCurrentPosInMS:**

| - (NSInteger)getMusicCurrentPosInMS: | (int32_t)id |
| --- | --- |

**Получение прогресса воспроизведения (мс) фоновой музыки.**

| Param | DESC |
| --- | --- |
| id | Идентификатор музыки |

**Return Desc:**

Миллисекунды, прошедшие с момента начала воспроизведения. -1 указывает на сбой при получении прогресса воспроизведения.

## getMusicDurationInMS:

**getMusicDurationInMS:**

| - (NSInteger)getMusicDurationInMS: | (NSString *)path |
| --- | --- |

**Получение общей длительности (мс) фоновой музыки.**

| Param | DESC |
| --- | --- |
| path | Путь к музыкальному файлу. |

**Return Desc:**

Возвращается длительность указанного музыкального файла. -1 указывает на сбой при получении длительности.

## seekMusicToPosInMS:pts:

**seekMusicToPosInMS:pts:**

| - (void)seekMusicToPosInMS: | (int32_t)id |
| --- | --- |
| pts: | (NSInteger)pts |

**Установка прогресса воспроизведения (мс) фоновой музыки.**

| Param | DESC |
| --- | --- |
| id | Идентификатор музыки |
| pts | Единица: миллисекунда |

> **Note**Не вызывайте этот API часто, так как музыкальный файл может быть прочитан и записан при каждом вызове API, что может занять много времени. Дождитесь, пока пользователи закончат перетаскивание полосы прогресса, прежде чем вызывать этот API. Контроллер полосы прогресса в интерфейсе имеет тенденцию обновлять прогресс с высокой частотой, когда пользователи перетаскивают полосу прогресса. Это приведет к плохому пользовательскому опыту, если вы не ограничиваете частоту.

## setMusicScratchSpeedRate:speedRate:

**setMusicScratchSpeedRate:speedRate:**

| - (void)setMusicScratchSpeedRate: | (int32_t)id |
| --- | --- |
| speedRate: | (double)scratchSpeedRate |

**Регулировка эффекта изменения скорости скретча.**

| Param | DESC |
| --- | --- |
| id | Идентификатор музыки |
| scratchSpeedRate | Скорость скретча, значение по умолчанию 1.0f, диапазон: число с плавающей запятой от [-12.0 ~ 12.0], положительное/отрицательное значение скорости указывает направление положительное/отрицательное, а абсолютное значение указывает скорость. |

> **Note**Предусловие: успешная предзагрузка с помощью preloadMusic.

## preloadMusic:onProgress:onError:

**preloadMusic:onProgress:onError:**

| - (void)preloadMusic: | ([TXAudioMusicParam](https://www.tencentcloud.com/document/product/647/50757#1b83f556d7876fc9f0ec4b5f8bea469c) *)preloadParam |
| --- | --- |
| onProgress: | (TXMusicPreloadProgressBlock _Nullable)progressBlock |
| onError: | (TXMusicPreloadErrorBlock _Nullable)errorBlock |

**Предзагрузка фоновой музыки.**

Вы должны назначить идентификатор каждой музыкальной дорожке, чтобы вы могли запускать, останавливать или устанавливать громкость музыкальных дорожек по идентификатору.

| Param | DESC |
| --- | --- |
| musicParam | Параметр музыки |

> **Note**1. Предзагрузка поддерживает одновременно до 2 предзагрузок с разными идентификаторами, а время предзагрузки не превышает 10 минут. Вам необходимо вызвать API [stopPlayMusic](https://www.tencentcloud.com/document/product/647/50757#2214eecbdca5062136821aff0d95bfbe) после использования, иначе память не будет освобождена. 2. Если музыка, соответствующая идентификатору, воспроизводится, предзагрузка не удается, и необходимо сначала вызвать [stopPlayMusic](https://www.tencentcloud.com/document/product/647/50757#2214eecbdca5062136821aff0d95bfbe). 3. Когда ` musicParam ` переданный в [startPlayMusic](https://www.tencentcloud.com/document/product/647/50757#3e6d92e47d6770c50e0e4ca4df429c31) точно совпадает, предзагрузка работает.

## getMusicTrackCount:

**getMusicTrackCount:**

| - (NSInteger)getMusicTrackCount: | (int32_t)id |
| --- | --- |

**Получение количества дорожек фоновой музыки.**

| Param | DESC |
| --- | --- |
| id | Идентификатор музыки |

## setMusicTrack:track:

**setMusicTrack:track:**

| - (void)setMusicTrack: | (int32_t)id |
| --- | --- |
| track: | (NSInteger)track |

**Указание дорожки воспроизведения фоновой музыки.**

| Param | DESC |
| --- | --- |
| id | Идентификатор музыки |
| index | Указание, какую дорожку воспроизводить (по умолчанию воспроизводится первая дорожка). Диапазон значений [0, общее количество дорожек). |

> **Note**Общее количество дорожек можно получить через интерфейс [getMusicTrackCount](https://www.tencentcloud.com/document/product/647/50757#19fc33f9be59df8b0f4524219fbd4350).

## TXVoiceReverbType

**TXVoiceReverbType**

**Эффекты реверберации.**

Эффекты реверберации можно применять к человеческому голосу. На основе акустических алгоритмов они могут имитировать голос в различных окружающих средах. В настоящее время поддерживаются следующие эффекты:

0: оригинальный; 1: караоке; 2: помещение; 3: зал; 4: низкий и глубокий; 5: резонансный; 6: металл; 7: сиплый; 8: эфирный; 9: студия; 10: мелодичный; 11: студия2;

| Enum | Value | DESC |
| --- | --- | --- |
| TXVoiceReverbType_0 | 0 | отключить |
| TXVoiceReverbType_1 | 1 | KTV |
| TXVoiceReverbType_2 | 2 | маленькое помещение |
| TXVoiceReverbType_3 | 3 | большой зал |
| TXVoiceReverbType_4 | 4 | глубокий голос |
| TXVoiceReverbType_5 | 5 | громкий голос |
| TXVoiceReverbType_6 | 6 | металлический звук |
| TXVoiceReverbType_7 | 7 | магнитный звук |
| TXVoiceReverbType_8 | 8 | эфирный |
| TXVoiceReverbType_9 | 9 | студия |
| TXVoiceReverbType_10 | 10 | мелодичный |
| TXVoiceReverbType_11 | 11 | студия2 |

## TXVoiceChangeType

**TXVoiceChangeType**

**Эффекты изменения голоса.**

Эффекты изменения голоса можно применять к человеческому голосу. На основе акустических алгоритмов они изменяют тембр голоса. В настоящее время поддерживаются следующие эффекты:

0: оригинальный; 1: ребенок; 2: маленькая девочка; 3: мужчина среднего возраста; 4: металл; 5: носовой; 6: иностранный акцент; 7: загнанный зверь; 8: отаку; 9: электрический; 10: робот; 11: эфирный; 12: король свиней; 13: халк

| Enum | Value | DESC |
| --- | --- | --- |
| TXVoiceChangeType_0 | 0 | отключить |
| TXVoiceChangeType_1 | 1 | озорной ребенок |
| TXVoiceChangeType_2 | 2 | Лолита |
| TXVoiceChangeType_3 | 3 | дядя |
| TXVoiceChangeType_4 | 4 | хэви-метал |
| TXVoiceChangeType_5 | 5 | простуда |
| TXVoiceChangeType_6 | 6 | иностранный акцент |
| TXVoiceChangeType_7 | 7 | загнанный зверь в клетке |
| TXVoiceChangeType_8 | 8 | домосед |
| TXVoiceChangeType_9 | 9 | сильный ток |
| TXVoiceChangeType_10 | 10 | тя

---
*Источник (EN): [txaudioeffectmanager.md](./txaudioeffectmanager.md)*
