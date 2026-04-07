# 1.Примеры API

В этом документе показано, как быстро запустить TRTC-API-Example (Electron).

## Предварительные требования

Вы [зарегистрировали учетную запись Tencent Cloud](https://trtc.io/register?s_url=https://console.trtc.io).

## Инструкции

### Шаг 1. Создание приложения

1. Войдите на [страницу обзора консоли TRTC](https://console.trtc.io/), нажмите **Create Application**.
2. На появившейся странице выберите RTC Engine, введите имя приложения и нажмите **Create**.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/687c36ae0ddd11efaed35254002977b6.png)

### Шаг 2. Получение SDKAppId и SecretKey

После создания приложения вы можете получить `SDKAppID` и `SDKSecretKey` на странице Basic informaction. `SDKAppID` и `SDKSecretKey` необходимы для запуска демонстрационного приложения.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/4ff51cf2b5d411ee9fd6525400bb593a.png)

### Шаг 3. Загрузка примера кода

1. Перейдите на [GitHub](https://github.com/LiteAVSDK/TRTC_Electron) и загрузите пример кода для вашей платформы.

```
git clone https://github.com/LiteAVSDK/TRTC_Electron.git
```

2. Инструкции по импорту SDK можно найти в разделе [Electron SDK import](https://trtc.io/document/35097).

### Шаг 4. Конфигурация проекта

Найдите и откройте `Electron/TRTC-API-Example/assets/debug/gen-test-user-sig.js` и установите следующие параметры:

- `SDKAPPID`: по умолчанию имеет значение-заполнитель. Установите на фактический SDKAppID.
- `SDKSECRETKEY`: по умолчанию имеет значение-заполнитель. Установите на фактический ключ.

> **Примечание** Метод генерирования `UserSig`, описанный в этом документе, включает конфигурирование `SDKSECRETKEY` в коде клиента. При этом методе `SDKSECRETKEY` может быть легко декомпилирован и разобран, и если ваш ключ будет раскрыт, злоумышленники смогут украсть трафик вашей учетной записи Tencent Cloud. Поэтому **этот метод подходит только для локального выполнения и отладки TRTC-API-Example**. Лучшей практикой является интегрирование кода расчета `UserSig` на ваш сервер и предоставление API-интерфейса, ориентированного на приложение. Когда требуется `UserSig`, ваше приложение может отправить запрос на ваш сервер для получения динамического `UserSig`. Дополнительные сведения см. в разделе [How do I calculate UserSig during production?](https://www.tencentcloud.com/zh/document/product/1047/34385).

## Часто задаваемые вопросы

### 1. Какие ограничения брандмауэра действуют на SDK?

SDK использует протокол UDP для передачи аудио и видео, поэтому не может использоваться в корпоративных сетях, которые блокируют UDP. Если вы столкнулись с такой проблемой, см. раздел [Firewall Restrictions](https://trtc.io/document/35164) для устранения проблемы.


---
*Источник: [https://trtc.io/document/35089](https://trtc.io/document/35089)*

---
*Источник (EN): [1api-examples.md](./1api-examples.md)*
