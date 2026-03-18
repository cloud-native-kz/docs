# Глобальные настройки

Следующее содержание показывает вам, как установить глобальные настраиваемые параметры.

## Переключение языка TUIKit

Функциональность API: переключение языка TUIKit.

Прототип метода:

Swift

Objective-C

```
// TUIConfig_Minimalist.swift/** * Переключить язык TUIKit. * В настоящее время поддерживаемые языки: "en", "zh-Hans" и "ar". */static func switchLanguage(to targetLanguage: String) {    TUIGlobalization.setPreferredLanguage(targetLanguage)}
```

```
// TUIConfig_Minimalist.h/** * Переключить язык TUIKit.  * В настоящее время поддерживаемые языки: "en", "zh-Hans" и "ar". */+ (void)switchLanguageToTarget:(NSString *)targetLanguage;
```

Пример кода:

Swift

Objective-C

```
// Когда вызывать: перед инициализацией интерфейса TUIKit.TUIConfig_Minimalist.switchLanguage(to: "en")
```

```
// Когда вызывать: перед инициализацией интерфейса TUIKit.[TUIConfig_Minimalist switchLanguageToTarget:@"en"];
```

Результат:

| Установлен английский | Установлен арабский |
| --- | --- |
| ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/ec9ffd335af711ef998b525400f69702.png) | ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/eca129ba5af711efb927525400fdb830.png) |

## Включение встроенных подсказок TUIKit

Функциональность API: включение встроенных всплывающих подсказок TUIKit. При включении компоненты TUIKit будут отображать встроенные подсказки.

Прототип метода:

Swift

Objective-C

```
// TUIConfig_Minimalist.swift/*** Показать встроенную всплывающую подсказку TUIKit.* Значение по умолчанию: YES.*/static func enableToast(_ enable: Bool) {    TUIConfig.default().enableToast = enable}
```

```
// TUIConfig_Minimalist.h/** *  Показать встроенную всплывающую подсказку TUIKit. *  Значение по умолчанию: YES. */+ (void)enableToast:(BOOL)enable;
```

Пример кода:

Swift

Objective-C

```
// Когда вызывать: перед инициализацией интерфейса TUIKit.TUIConfig_Minimalist.enableToast(false)
```

```
// Когда вызывать: перед инициализацией интерфейса TUIKit.[TUIConfig_Minimalist enableToast:NO];
```

Результат:

| Включить всплывающие подсказки | Отключить всплывающие подсказки |
| --- | --- |
| ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/a4a1ff455af511efb66652540055f650.png) | ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/807d43b25af511efb36952540075b605.png) |


---
*Источник: [https://trtc.io/document/65369](https://trtc.io/document/65369)*

---
*Источник (EN): [global.md](./global.md)*
