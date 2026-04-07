# Интернационализация

TUIKit Flutter включает встроенные языковые пакеты для **Упрощенного китайского, Традиционного китайского, английского, японского, корейского и арабского языков**. Эти пакеты позволяют легко установить язык пользовательского интерфейса. С помощью простой конфигурации вы можете включить динамическое переключение языков в приложении.

| Упрощенный китайский | Традиционный китайский | Английский | Японский | Корейский | Арабский |
| --- | --- | --- | --- | --- | --- |
| ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/35711948023c11f18ab45254001d6acc.jpeg) | ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/357c3ca2023c11f18e6252540073fd3b.jpeg) | ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/35710ab1023c11f198e252540097cba1.jpeg) | ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/357bfc88023c11f18ab45254001d6acc.jpeg) | ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/357bf517023c11f191b4525400ecee81.jpeg) | ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/358f4bbd023c11f191b4525400ecee81.jpeg) |

## Использование встроенных языков

### Настройка языка

После интеграции компонента, как описано в [TUIKit Flutter](https://www.tencentcloud.com/document/product/1047/77489), вы можете включить интернационализацию с помощью `LocaleProvider` и `AtomicLocalizations`. Оберните точку входа приложения с помощью `MultiProvider` и настройте параметры языка в `MaterialApp`, как показано ниже. Полный пример см. в [демонстрации](https://github.com/Tencent-RTC/TUIKit_Flutter/blob/main/chat/demo/lib/main.dart):

```
  @override  Widget build(BuildContext context) {    return ComponentTheme(      child: MultiProvider(        providers: [          // Language provider for dynamic language switching; notifies components when the language changes          ChangeNotifierProvider.value(value: LocaleProvider()),        ],        child: Builder(builder: (context) {          final themeState = BaseThemeProvider.of(context);          final isDarkMode = themeState.isDarkMode;          // Access the language provider          final localeProvider = Provider.of<LocaleProvider>(context);          return MaterialApp(            // ...... other configurations omitted            localizationsDelegates: const [              AtomicLocalizations.delegate,            // ...... you can add other localization delegates for additional components            ],            supportedLocales: AtomicLocalizations.supportedLocales, // Supported app languages            locale: localeProvider.locale, // Current language setting          );        }),      ),    );
```

### Адаптация к системному языку

После завершения настройки языка плагин автоматически соответствует системному языку по умолчанию.

### Переключение языков в реальном времени

`LocaleProvider` предоставляет метод `changeLanguage` для переключения языков во время выполнения. Выбранный язык кэшируется локально, поэтому приложение запомнит выбор пользователя после перезагрузки, прочитав значение из поля `locale`.

Для получения сведений о реализации обратитесь к [демонстрации страницы параметров](https://github.com/Tencent-RTC/TUIKit_Flutter/blob/main/chat/demo/lib/pages/settings_page.dart). Чтобы переключить языки, получите экземпляр `LocaleProvider` и вызовите `changeLanguage`:

```
final localeProvider = Provider.of<LocaleProvider>(context, listen: false);// Switch to EnglishlocaleProvider.changeLanguage('en');
```

После переключения языков подкласс `State` виджета `StatefulWidget` запустит метод жизненного цикла `didChangeDependencies`. В этом методе инициализируйте объект `AtomicLocalizations` и используйте встроенные локализованные записи.

Пример:

```
class ContactList extends StatefulWidget {  const ContactList({    super.key,  });  @override  State<ContactList> createState() => _ContactListState();}class _ContactListState extends State<ContactList> {  late AtomicLocalizations atomicLocale;  // Other code omitted    @override  void didChangeDependencies() {    super.didChangeDependencies();    // Initialize localization dynamically    atomicLocale = AtomicLocalizations.of(context);  }    @override  Widget build(BuildContext context) {    // Display the addFriend label in the current language    return Text(atomicLocale.addFriend);  }}
```

## Пользовательская интернационализация

Чтобы добавить пользовательскую интернационализацию, интегрируйте компонент tuikit_atomic_x из исходного кода, как описано в [TUIKit Flutter](https://www.tencentcloud.com/document/product/1047/77489).

### Добавление файлов языковых ресурсов

Записи локализации хранятся в файлах `.arb` в каталоге [l10n](https://github.com/Tencent-RTC/TUIKit_Flutter/tree/main/atomic-x/lib/base_component/l10n). Чтобы добавить новый язык, создайте новый файл `.arb` с соответствующим кодом языка и переведите все записи.

- Создайте файл: скопируйте существующий языковой файл и переименуйте его в `l10n_xx.arb` (например, для испанского: `l10n_es.arb`).
- Переведите содержимое: обновите все записи в новом файле переводами для целевого языка.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/353a73c5023c11f18ab45254001d6acc.png)

Затем запустите команду `flutter gen-l10n` в корневом каталоге компонента. Это обновит каталог локализаций новым языковым файлом.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/352eedbf023c11f191b4525400ecee81.png)

Добавьте логику в `locale_provider.dart` для локального кэширования испанского языка, затем вызовите `changeLanguage('es')` для переключения на испанский.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/357159fe023c11f191b4525400ecee81.png)

### Настройка переводов

Все ключи языков в файлах ресурсов в каталоге l10n согласованы. Вы можете изменять или добавлять переводы по мере необходимости, затем запустить команду `flutter gen-l10n` в корневом каталоге компонента для обновления файлов локализации.


---
*Источник: [https://trtc.io/document/52154](https://trtc.io/document/52154)*

---
*Источник (EN): [internationalization.md](./internationalization.md)*
