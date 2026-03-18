# Поддерживаемые платформы

## Поддерживаемые платформы

TRTC Web SDK поддерживает все основные браузеры, такие как **Chrome, Edge, Firefox, Safari и Opera**. В теории SDK поддерживает все браузеры на основе Chromium версии 56+.

Чтобы обеспечить наилучший опыт пользователя, рекомендуется предлагать пользователям использовать последнюю версию каждого браузера в последней версии операционной системы.

Загрузите последнюю версию [Chrome](https://www.google.com/intl/en/chrome/), [Edge](https://microsoft.com/edge), [Firefox](https://www.mozilla.org/firefox/new/), [Safari](https://support.apple.com/en-hk/HT201541).

| ОС | Тип браузера | Версия | Получение аудио/видео | Отправка аудио/видео | Совместное использование экрана |
| --- | --- | --- | --- | --- | --- |
| Windows | Chrome | 56+ | Да | Да | 72+ |
|  | Firefox | 56+ | Да | Да | 66+ |
|  | Edge | 80+ | Да | Да | 80+ |
|  | Opera | 46+ | Да | Да | 60+ |
|  | Другие (на основе Chromium) | 56+ | Да | Да | 72+ |
| Mac OS | Safari | 11+ | Да | Да | 13+ |
|  | Chrome | 56+ | Да | Да | 72+ |
|  | Firefox | 56+ | Да | Да | 66+[(Примечание [3])](https://web.sdk.qcloud.com/trtc/webrtc/v5/doc/en/tutorial-05-info-browser.html#attention3) |
|  | Edge | 80+ | Да | Да | 80+ |
|  | Opera | 46+ | Да | Да | 60+ |
| Chrome OS | Chrome | 56+ | Да | Да | 72+ |
| Android | Chrome | 79+ | Да | Да | Нет |
|  | Edge | 80+ | Да | Да | Нет |
|  | Firefox | 80+ | Да | Да | Нет |
|  | Chrome Webview | 79+ | Да | Да | Нет |
| iOS | Safari | iOS 11+ | Да | Да | Нет |
|  | Chrome | iOS 11+ | Да | iOS 14.3+ | Нет |
|  | Edge | iOS 11+ | Да | iOS 14.3+ | Нет |
|  | Другие (на основе WKWebview) | iOS 11+ | Да | iOS 14.3+ | Нет |

## Определение возможностей браузера

Если вашего браузера нет в списке, вы можете использовать API [TRTC.isSupported()](https://web.sdk.qcloud.com/trtc/webrtc/v5/doc/en/TRTC.html#.isSupported) или запустить [тест уровня поддержки TRTC Web SDK](https://web.sdk.qcloud.com/trtc/webrtc/demo/detect/index.html) в браузере, чтобы проверить, полностью ли он поддерживает WebRTC.

См. раздел [Определение возможностей](https://www.tencentcloud.com/document/product/647/59656).

## Поддержка протоколов URL

Из-за [безопасных контекстов](https://developer.mozilla.org/en-US/docs/Web/Security/Secure_Contexts) браузеров существуют требования к протоколу, используемому для доступа при использовании TRTC Web SDK.

| Сценарий | Протокол | Получение аудио/видео | Отправка аудио/видео | Совместное использование экрана | Примечания |
| --- | --- | --- | --- | --- | --- |
| Production | HTTPS | Да | Да | Да | **Рекомендуется** |
| Production | HTTP | Да | Нет | Нет | - |
| Локальная разработка | http://localhost | Да | Да | Да | **Рекомендуется** |
| Локальная разработка | http://127.0.0.1 | Да | Да | Да | - |
| Локальная разработка | http://[локальный IP-адрес] | Да | Нет | Нет | - |
| Локальная разработка | file:/// | Да | Да | Да | - |


---
*Источник: [https://trtc.io/document/59733](https://trtc.io/document/59733)*

---
*Источник (EN): [supported-platforms.md](./supported-platforms.md)*
