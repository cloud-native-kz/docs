# Многопользовательский чат

Chat предоставляет мультиплатформенные API чата, компоненты пользовательского интерфейса и серверные API, позволяющие вам построить полнофункциональное приложение чата за десять минут. В приложении чата вы можете легко добавить функции аудио и видео вызовов всего в три строки кода.

## Демонстрация интеграции

После интеграции Chat и TUICallKit вы можете легко инициировать аудио и видео вызовы на странице сообщений чата и странице информации о пользователе.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/1eed16a2b2ec11ef8c01525400fdb830.png)

## Быстрая интеграция

### Подготовка

- Убедитесь, что ваше приложение [интегрировано с Chat](https://trtc.io/document/58585?platform=flutter&product=chat&menulabel=uikit).

### Активация сервиса

1. Войдите в [консоль чата](https://console.trtc.io/) для активации сервисов аудио и видео. Подробные инструкции см. в документации [Активация сервиса](https://trtc.io/document/60220).
2. В диалоговом окне активации сервиса TRTC нажмите "Подтвердить". Система создаст приложение TRTC с тем же SDKAppID, что и текущее приложение чата. [Консоль TRTC](https://trtc.io/login?s_url=https://console.trtc.io/) позволяет повторно использовать учетную запись и аутентификацию.

### Интеграция TUICallKit.

1. В консоли перейдите в каталог вашего проекта Flutter и выполните следующую команду для установки плагина [tencent_calls_uikit](https://pub.dev/packages/tencent_calls_uikit):

```
flutter pub add tencent_calls_uikit
```

2. В фреймворке приложения Flutter добавьте TUICallKit.navigatorObserver в navigatorObservers. Например, используя фреймворк MaterialApp, код выглядит следующим образом:

```
import 'package:tencent_calls_uikit/tencent_calls_uikit.dart'; ......class XXX extends StatelessWidget {  const XXX({super.key}); @override  Widget build(BuildContext context) {    return MaterialApp(      navigatorObservers: [TUICallKit.navigatorObserver],      ......    );  }}
```

После интеграции компонента TUICallKit интерфейс чата и интерфейс информации о контактах по умолчанию будут отображать кнопки "видео вызов" и "голосовой вызов". Когда пользователь нажимает кнопку, TUICallKit автоматически отображает UI приглашения на вызов и отправляет запрос приглашения на вызов другой стороне.


---
*Источник: [https://trtc.io/document/66905](https://trtc.io/document/66905)*

---
*Источник (EN): [conversational-chat.md](./conversational-chat.md)*
