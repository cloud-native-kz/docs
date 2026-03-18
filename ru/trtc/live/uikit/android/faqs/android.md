# Android

### Может ли TUILiveKit использовать TRTC без подключения IM SDK?

**Нет**, все компоненты TUIKit используют IM SDK Tencent Cloud в качестве базового сервиса коммуникации, такого как основная логика создания сигнализации комнаты, сигнализации микрофона и т. д., все используют сервисы IM. Если вы приобрели другие продукты IM, вы также можете обратиться к логике TUILiveKit для адаптации.

### Исключение allowBackup, как его обработать?

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/c293ca53128511ef9af4525400720cb5.png)

- **Причины:** Свойство `allowBackup` настроено в `AndroidManifest.xml` нескольких модулей, что вызывает конфликты.
- **Решение:** Вы можете удалить атрибут `allowBackup` из файла `AndroidManifest.xml` вашего проекта или изменить его на false, чтобы отключить резервное копирование и восстановление, а также добавить `tools:replace="android:allowBackup"` в узел приложения файла `AndroidManifest.xml`; это указывает на переопределение параметров других модулей с использованием собственных параметров.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/37e7d004128611efbf645254007bbd8c.png)

### Activity требует использования темы Theme.AppCompat?

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/8ca2de08133311efbf645254007bbd8c.png)

- **Причины:** Поскольку `LoginActivity` наследуется от `AppCompatActivity`, необходимо предоставить тему `Theme.AppCompat` для `LoginActivity`.
- **Решение:** Вы можете добавить тему `Theme.AppCompat` в конфигурацию `LoginActivity` в файле `AndroidManifest.xml` вашего проекта. Вы также можете использовать собственную тему `Theme.AppCompat`. Пример исправления показан на изображении:

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/8c7a9ed1133311efbf645254007bbd8c.png)

### Не удается открыть веб-адрес в браузере?

**Решение:** Вы можете добавить следующие конфигурации в файл AndroidManifest.xml вашего проекта:

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/78d7a6fb2eae11efb0275254006c0558.png)


---
*Источник: [https://trtc.io/document/60043](https://trtc.io/document/60043)*

---
*Источник (EN): [android.md](./android.md)*
