# Глобальные настройки

В следующем содержании показано, как установить глобальные пользовательские параметры.

## Переключение языка TUIKit

Функциональность API: переключение языка TUIKit.

Прототип метода:

```
// TUIConfigMinimalist.java/** * Переключить язык TUIKit.  * Поддерживаемые в настоящее время языки: "en", "zh" и "ar". */public static void switchLanguageToTarget(Context context, String targetLanguage)
```

Пример кода:

```
// Когда вызывать: на этапе инициализации приложения.TUIConfigMinimalist.switchLanguageToTarget(context, "en");
```

Результат:

| На английском языке | На арабском языке |
| --- | --- |
| ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/92c1bd4b8f4a11ef9897525400d5f8ef.png) | ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/92b81d468f4a11efb3eb525400bdab9d.png) |

## Включение встроенных подсказок TUIKit

Функциональность API: включение встроенных всплывающих подсказок (toast) TUIKit. При включении компоненты TUIKit будут отображать встроенные подсказки.

Прототип метода:

```
// TUIConfigMinimalist.java/** *  Показать встроенную подсказку toast в TUIKit. *  Значение по умолчанию — true. */public static void enableToast(boolean enableToast)
```

Пример кода:

```
// Когда вызывать: перед инициализацией интерфейса TUIKit.TUIConfigMinimalist.enableToast(false);
```

Результат:

| Включены подсказки Toast | Отключены подсказки Toast |
| --- | --- |
| ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/92b6f39c8f4a11efac345254002693fd.png) | ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/92b440488f4a11efb3eb525400bdab9d.png) |


---
*Источник: [https://trtc.io/document/65364](https://trtc.io/document/65364)*

---
*Источник (EN): [global.md](./global.md)*
