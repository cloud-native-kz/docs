# Как отправить поток в комнату TRTC с помощью OBS WHIP

## Обзор

OBS включает поддержку WHIP, что позволяет вам делать много интересных вещей, объединяя возможности OBS и WHIP.

WHIP — это стандартный протокол, который позволяет использовать HTML5 и различные клиенты для публикации и воспроизведения прямых трансляций. Кроме того, вы можете использовать инструменты с открытым исходным кодом для создания собственной платформы прямого вещания.

Вы также можете использовать облачные сервисы TRTC (Tencent Real-Time Communication) с поддержкой OBS WHIP для платформы потокового вещания. Это отличный вариант, если вы не хотите создавать собственную платформу или вам нужна более надежная и стабильная платформа с выделенной поддержкой.

Кроме того, TRTC (Tencent Real-Time Communication) предоставляет бесплатный пробный период, который включает определенное количество времени потокового вещания, что позволяет легко попробовать сервис.

Если вам нужна помощь или у вас возникли проблемы, не стесняйтесь обратиться к нам на [Discord](https://discord.gg/vDHty6ddrZ).

## Предварительные требования

Перед тем как приступить, убедитесь, что у вас есть все необходимые элементы:

- OBS с поддержкой WHIP, загрузите с [OBS](https://obsproject.com/)
- Учетная запись TRTC (Tencent Real-Time Communication), зарегистрируйтесь [здесь](https://www.tencentcloud.com/account/login?s_url=https%253A%252F%252Fconsole.tencentcloud.com%252Ftrtc&utm_source=community&utm_medium=github&utm_campaign=OBS-WHIP-TRTC&_channel_track_key=6vGiu0P3)

Далее вам необходимо создать приложение TRTC и сгенерировать Bearer Token для WHIP.

## Шаг 1: Создание приложения TRTC

Следуйте приведенным ниже шагам для создания приложения TRTC:

1. Войдите в [консоль Tencent RTC](https://console.trtc.io/app) и нажмите **Create Application**.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/37f69b16508011ef9bf1525400a9236a.png)

2. В появившемся окне создания выберите продукт в зависимости от ваших потребностей, введите имя приложения, выберите **Region** для хранения данных и нажмите **Create**.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/fddbe3a7508011efb66652540055f650.png)

3. После завершения создания приложения вы автоматически перейдете на страницу сведений о приложении выбранного продукта. Вы можете просмотреть `SDKAppID` и `SDKSecretKey` в разделе **Application Overview**, которые будут использоваться на последующих этапах.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/f64f834c508011efbaba525400d5f8ef.png)

## Шаг 2: Создание Bearer Token для WHIP

После этого вы должны сгенерировать Bearer Token для WHIP, который будет использоваться в OBS.

Вы можете напрямую перейти на [https://tencent-rtc.github.io/obs-trtc/bearer.html](https://tencent-rtc.github.io/obs-trtc/bearer.html), чтобы создать WHIP Bearer Token. Убедитесь, что используете AppID со своим `SDKAppID` и secret со своим `SDKSecretKey`, затем нажмите кнопку `Generate Bearer Token`.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/677cd8520b2b11eea359525400088f3a.png)

> **Примечание:** Вы также можете получить доступ к URL `https://tencent-rtc.github.io/obs-trtc/bearer.html?appid=2000xxx&secret=yyyyyy` для настройки параметров.

Далее используйте сгенерированный WHIP Bearer Token для конфигурации OBS.

## Шаг 3: Конфигурация OBS

В разделе `OBS WHIP` вы найдете сгенерированные WHIP `Server` и `Bearer Token` для конфигурации OBS.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/7f8ca6760b2b11eead3b5254007e6a5b.png)

Следуйте приведенным ниже шагам для конфигурации OBS:

1. Откройте OBS и нажмите **Settings**.
2. На левой боковой панели нажмите **Stream**.
3. Выберите `WHIP` для **Service**.
4. Убедитесь, что вы правильно ввели `Server` и `Bearer Token`.
5. Нажмите **OK** для сохранения параметров.
6. Нажмите **Start Streaming** для начала трансляции.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/8c4822660b2b11eead3b5254007e6a5b.png)

На этом этапе поток транслируется в сервис TRTC.

## Шаг 4: Воспроизведение потока

Откройте предыдущую веб-страницу, перейдите в раздел `WHEP Player` и нажмите **Play Stream** для воспроизведения потока через WHEP.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/9f50b1f80b2b11ee95bc5254002af9e0.png)

Альтернативный вариант — перейти в раздел `TRTC Room` и нажать **Join Room** для входа в комнату TRTC и просмотра потока через TRTC, либо вы можете использовать мобильный SDK TRTC для входа в комнату и просмотра потока.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/aa304be50b2b11eea359525400088f3a.png)

Поскольку WHIP и WHEP — это стандартные протоколы, вы можете использовать любой клиент, который их поддерживает, для воспроизведения потока.

## Заключение

Мы рассмотрели использование облачных сервисов TRTC (Tencent Real-Time Communication) для создания более мощной платформы потокового вещания и шаги, необходимые для создания приложения TRTC с поддержкой OBS WHIP. Эти инструменты упрощают организацию и предоставление возможностей прямого вещания в реальном времени для различных ситуаций, используя мощь OBS.

Если вам требуется помощь или у вас возникли какие-либо трудности, пожалуйста, не стесняйтесь обратиться к нам через [Discord](https://discord.gg/vDHty6ddrZ).


---
*Источник: [https://trtc.io/document/55633](https://trtc.io/document/55633)*

---
*Источник (EN): [how-to-push-stream-to-trtc-room-with-obs-whip.md](./how-to-push-stream-to-trtc-room-with-obs-whip.md)*
