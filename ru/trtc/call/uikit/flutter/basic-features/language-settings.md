# Языковые параметры

## Поддерживаемые языки

В настоящее время поддерживаются **китайский упрощённый, английский и японский** языки, языком по умолчанию является **английский**.

## Переключение языка

`TUICallKit` не предоставляет отдельный интерфейс для переключения языка. `TUICallKit` автоматически переключает языки в соответствии с параметром языка `MaterialApp` (или компонентов стиля CupertinoApp и т. д.) текущего приложения `Application`. Просто измените язык, используемый `MaterialApp` (или компонентами стиля CupertinoApp и т. д.).

## Добавление нового языка

### Шаг 1: интеграция исходного кода

1. Загрузка исходного кода

Перейдите на [`https://pub.dev/packages/tencent_calls_uikit`](https://pub.dev/packages/tencent_calls_uikit) для загрузки последней версии исходного кода `TUICallKit`.

2. Зависимость от локального исходного кода

В файле `pubspec.yaml` проекта приложения `Application` измените `TUICallKit` на локальную зависимость:

```
dependencies:  tencent_calls_uikit:
    path: /TUICallKit local_path/
```

### Шаг 2: добавление нового языкового пакета

#### Используя **испанский** язык в качестве примера:

1. Добавьте новый файл испанского языка.

Перейдите в папку `lib/src/i18n` в директории исходного кода `TUICallKit` и добавьте файл `strings_es.i18n.json`.

2. Скопируйте содержимое из `lib/src/i18n/strings.i18n.json` в только что добавленный файл `lib/src/i18n/strings_es.i18n.json`.
3. Переведите английское содержимое в файле `lib/src/i18n/strings_es.i18n.json` на испанский язык.
4. Обновление пакета перевода

В директории исходного кода `TUICallKit` перейдите в TCCLI и запустите следующие команды для обновления пакета перевода:

```
  flutter pub add fast_i18nflutter pub run fast_i18n
```

5. Обновление метода адаптации языка для `TUICallKit`.

Перейдите к исходному файлу `lib/src/i18n/i18n_utils.dart` и измените метод `setLanguage` следующим образом:

```
  static setLanguage(Locale currentLocale) {
  switch (currentLocale.languageCode) {
    case 'zh':
      {
        CallKitI18nUtils(null, 'zh');
        break;
      }
    case 'en':
      {
        CallKitI18nUtils(null, 'en');
        break;
      }
    case 'ja':
      {
        CallKitI18nUtils(null, 'ja');
        break;
      }    // Add case 'es'
    case 'es':
      {
        CallKitI18nUtils(null, 'es');
        break;
      }
  }
}
```


---
*Источник: [https://trtc.io/document/63265](https://trtc.io/document/63265)*

---
*Источник (EN): [language-settings.md](./language-settings.md)*
