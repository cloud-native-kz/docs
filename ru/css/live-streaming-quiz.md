# Викторина прямой трансляции

## Загрузка SDK

- **LiteAVSDK (6.5.7272)**
используется для RTMP-трансляции и воспроизведения FLV. Версия Smart имеет обе упомянутые функции, в то время как версия LivePlay поддерживает только функцию воспроизведения FLV.

| Операционная система | Ссылка для загрузки | RTMP-трансляция | RTMP-воспроизведение | FLV-воспроизведение | Примечания |
| --- | --- | --- | --- | --- | --- |
| iOS | [DOWNLOAD](http://liteavsdk-1252463788.cosgz.myqcloud.com/6.5/TXLiteAVSDK_Smart_iOS_6.5.7273.zip) | ДА | ДА | ДА | ZIP-файл SDK |
| Android | [DOWNLOAD](https://github.com/tencentyun/MLVBSDK/blob/master/Android/SDK/) | ДА | ДА | ДА | ZIP-файл и AAR-файл SDK |

## Наши преимущества

- **Точная синхронизация "звука-изображения-вопроса"**
SDK Tencent Cloud и облако поддерживают вставку **вопросов** или **сигналов синхронизации времени** в потоки CSS для достижения идеальной синхронизации звука, изображения и всплывающих окон с вопросами.
- **Сверхнизкое отклонение задержки на стороне зрителя**
Технология коррекции задержки, поддерживаемая режимом быстрого воспроизведения в SDK Tencent Cloud, позволяет сохранять отклонение задержки между зрителями в пределах 1 сек, обеспечивая синхронный ответ зрителей на вопросы.
- **Интеграция с мини-программами WeChat**
SDK Tencent Cloud интегрирован в WeChat по умолчанию и доступен публично как тег live-player. Установите режим на live и также установите min-cache и max-cache на 1 для включения воспроизведения с супернизкой задержкой.

## Детали метода

### NTP Синхронизация времени

![](https://staticintl.cloudcachetci.com/cms/backend-cms/406dee96d45711eea2b0525400bb593a.png)

#### Принцип работы

1. Tencent Cloud в режиме реального времени вставляет международный стандартный временной отметка (временная отметка UTC), откалиброванную NTP, в потоки CSS каждые две секунды.
2. Режиссер программы в студии назначает вопросы в подходящее время в зависимости от темпа, с которым ведущий задает вопросы. Система назначения вставляет текущее международное стандартное время в каждый назначенный вопрос.
3. При воспроизведении видеопотоков с вставленными такими временными отметками SDK уведомляет ваше приложение о времени, когда было записано текущее воспроизводимое изображение. Обратите внимание на задержку от студии к облаку и убедитесь, что вы заранее исправили отклонение.
4. Ваше приложение может отображать указанные вопросы по мере необходимости в соответствии с уведомлениями о времени записи текущего изображения из SDK.

## Руководство интеграции

### Шаг 1: Активируйте сервис Tencent Cloud CSS

Свяжитесь с нами для активации сервиса [CSS](https://intl.cloud.tencent.com/document/product/267) и лицензии MLVB компании Tencent Cloud. Вы можете позвонить нам по номеру +1-888-652-2736, чтобы ускорить процесс одобрения, если это требуется срочно.

### Шаг 2: Получите URL трансляции

Пожалуйста, обратитесь к документации [Как быстро получить URL](https://intl.cloud.tencent.com/document/product/267/7977).

- Для простого получения URL трансляции
- Для понимания связи между URL трансляции и ID комнаты прямой трансляции
- Для защиты URL трансляции от кражи

Для добавления временной отметки NTP добавьте параметр &txAddTimestamp=2 к URL трансляции. (txAddTimestamp=1 вызывает сбой экрана в мини-программе). Сервер будет отправлять международную стандартную временную отметку SEI в поток CSS каждые две секунды (с отклонением менее 100 мс). Если вы используете наш плеер для воспроизведения этого видео, вы будете получать уведомление о текущем временном коде NTP экрана каждые две секунды.

### Шаг 3: Получите URL воспроизведения

Существует взаимно однозначное соответствие между URL воспроизведения и URL трансляции. Пожалуйста, обратитесь к следующему рисунку для правила преобразования.

![](https://staticintl.cloudcachetci.com/cms/backend-cms/40535b26d45711eeb0d9525400461a83.png)

Обязательно используйте URL воспроизведения в формате **FLV**, потому что RTMP имеет тенденцию к заиканию в сценариях с высокой конкурентностью.

### Шаг 4: Настройка стороны трансляции

Если вы используете свое приложение для трансляции потоков, пожалуйста, обратитесь к документации (iOS|Android).

### Шаг 5: Интегрируйте плеер

1. Загрузите версию [SDK](#SDK), указанную во втором разделе документа.
2. Обратитесь к документации интеграции (iOS | Android) для интеграции плеера. Это займет около 1/2 дня для завершения работы на обеих платформах.
3. **Измените параметры по умолчанию**
По умолчанию в SDK установлены параметры для обычных сценариев CSS, поэтому необходимо изменить параметры следующим образом:

```
//iOS Source CodeTXLivePlayConfig *config = [[TXLivePlayConfig alloc] init];TXLivePlayer *player = [[TXLivePlayer alloc] init];////Enable message receiving. Failure to receive messages means this function has not been enabled (default: disabled).config.enableMessage = YES;////Set the break-event point for latency to 2 seconds. (Given the latency due to the transmission from the cloud and the push end, the actual latency is more than 3 seconds: 3 seconds for SDK push latency and 4-5 seconds for obs push latency.)config.bAutoAdjustCacheTime = YES;config.maxAutoAdjustCacheTime = 2;config.minAutoAdjustCacheTime = 2;config.cacheTime = 2;config.connectRetryCount = 3;config.connectRetryInterval = 3;config.enableAEC = NO;//First setConfig and then startPlay[player setConfig:config];
```

```
//Android Source CodemTXLivePlayConfig = new TXLivePlayConfig();mTXLivePlayer = new TXLivePlayer(context);////Enable message receiving. Failure to receive messages means this function has not been enabled (default: disabled).mTXLivePlayConfig.setEnableMessage(true);////Set the break-event point for latency to 2 seconds. (Given the latency due to the transmission from the cloud and the push end, the actual latency is more than 3 seconds: 3 seconds for SDK push latency and 4-5 seconds for OBS push latency.)mTXLivePlayConfig.setAutoAdjustCacheTime(true);mTXLivePlayConfig.setCacheTime(2.0f);mTXLivePlayConfig.setMaxAutoAdjustCacheTime(2.0f);mTXLivePlayConfig.setMinAutoAdjustCacheTime(2.0f);////First setConfig and then startPlaymTXLivePlayer.setConfig(mTXLivePlayConfig);
```

4. Обязательно используйте URL воспроизведения в формате **FLV**, потому что RTMP имеет тенденцию к заиканию в сценариях с высокой конкурентностью.

### Шаг 6: Распределение вопросов

Если вы используете свое приложение для назначения вопросов, вы можете использовать метод вызова sendMessage в TXLivePusher. Пожалуйста, обратитесь к документации (iOS | Android) для получения подробной информации.

**Оценка надежности**
Некоторые клиенты могут беспокоиться о том, что нестабильные каналы аудио/видео вызовут заикание или потерю видеоданных, и зрители не смогут увидеть вопросы.

- Потеря кадров с данными аудио/видео CSS происходит на основе GOP. Если GOP равен 1, то каждый раз будут потеряны данные аудио/видео за 1 секунду.
- Согласно развертыванию узлов Tencent Cloud, 90% заиканий видео вызваны медленным сетевым подключением на стороне зрителя. В этом случае использование других сетевых соединений даст те же результаты.

Решение этой проблемы состоит в отправке сообщения вопроса каждую секунду (если GOP установлен на 1 секунду) и исключении повторяющихся номеров вопросов на стороне зрителя. Это предотвращает влияние заикания аудио/видео на надежность доставки вопросов.

### Шаг 7: Получение сообщений с вопросами

После получения этого буфера вы можете распарсить 8-байтовую (64-битную) временную отметку и использовать соответствующий вопрос (если в этот момент есть вопрос) для завершения отображения интерфейса.

- Переключите опцию **enableMessage** в TXLivePlayConfig на **YES**.
- TXLivePlayer прослушивает сообщения с помощью **TXLivePlayListener**, номер сообщения: **PLAY_EVT_GET_MESSAGE (2012)**.

```
 //iOS code -(void) onPlayEvent:(int)EvtID withParam:(NSDictionary *)param {    [self asyncRun:^{        if (EvtID == PLAY_EVT_GET_MESSAGE) {            dispatch_async(dispatch_get_main_queue(), ^{ //Throw to the main thread to avoid thread security issues                if ([_delegate respondsToSelector:@selector(onPlayerMessage:)]) {                    [_delegate onPlayerMessage:param[@"EVT_GET_MSG"]];                }            });        }    }];}
```

```
//Android sample codemTXLivePlayer.setPlayListener(new ITXLivePlayListener() {        @Override        public void onPlayEvent(int event, Bundle param) {            if (event == TXLiveConstants.PLAY_ERR_NET_DISCONNECT) {                roomListenerCallback.onDebugLog("[AnswerRoom] Pull failed: network disconnected");                roomListenerCallback.onError(-1, "Network disconnected, pull failed");            }            else if (event == TXLiveConstants.PLAY_EVT_GET_MESSAGE) {                String msg = null;                try {                    msg = new String(param.getByteArray(TXLiveConstants.EVT_GET_MSG), "UTF-8");                    roomListenerCallback.onRecvAnswerMsg(msg);                } catch (UnsupportedEncodingException e) {                    e.printStackTrace();                }            }        }});
```

### Шаг 8: Разработка системы викторины

Система викторины, тесно связанная с вашим бизнесом, не входит в пакет услуг, которые мы предлагаем как поставщик услуг PaaS. Система должна быть разработана вами.

Общее решение — собирать ответы клиентов как HTTP(S)-запросы на сервер викторины. Будьте готовы к всплескам высоко конкурентных запросов.

Некоторые клиенты могут спросить, можно ли использовать систему IM для проведения викторин. Ответ на данный момент — нет, потому что система IM предназначена для распределения сообщений, в то время как викторины предназначены для сбора информации.

### Шаг 9: Отображение результатов викторины

Викторина будет закрыта после того, как вопросы отображаются в течение определенного периода времени. Затем система викторины соберет результаты и доставит их зрителям.


---
*Источник: [https://www.tencentcloud.com/document/product/267/30965](https://www.tencentcloud.com/document/product/267/30965)*

---
*Источник (EN): [live-streaming-quiz.md](./live-streaming-quiz.md)*
