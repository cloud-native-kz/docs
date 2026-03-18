# Обзор Webhooks

Для удобства управления функциональной формой вашего приложения CallKit предоставляет возможность использования callbacks.

## Описание функции

Пользователи могут настроить callback для указанного URL через метод REST API. Когда выполняемая CallbackCommand находится в списке конфигурации, callback будет активирован.

## Важная информация

- Только один callback можно настроить для sdkAppId.
- Убедитесь, что callback URL доступен нормально.

> **Предупреждение:** Если вы используете устаревшие интерфейсы `TUICallKit.call()` или `TUICallKit.groupCall()` для инициирования вызова, пожалуйста, проверьте папку **Deprecated Document**. Если у вас есть вопросы, вы можете связаться с: info_rtc@tencent.com.


---
*Источник: [https://trtc.io/document/68933](https://trtc.io/document/68933)*

---
*Источник (EN): [webhooks-overview.md](./webhooks-overview.md)*
