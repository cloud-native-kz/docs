# Настраиваемый значок

Android

iOS

uni-app

### Поддерживаемые поставщики

Huawei и Google FCM поддерживают настраиваемый значок; другие производители не поддерживают настраиваемый значок и по умолчанию используют значок приложения.

### Способ конфигурации

Действует при конфигурации в файле Manifest основного проекта:

Huawei

Google FCM

```
<meta-data    android:name="com.huawei.messaging.default_notification_icon"    android:resource="@drawable/Icon Resource Name" />
```

```
<!-- [START fcm_default_icon] --><!-- Set custom default icon. This is used when no icon is set for incoming notification messages.     See README(https://goo.gl/l4GJaQ) for more. --><meta-data    android:name="com.google.firebase.messaging.default_notification_icon"    android:resource="@drawable/Icon Resource Name" /><!-- Set color used with incoming notification messages. This is used when no color is set for the incoming     notification message. See README(https://goo.gl/6BKBk7) for more. --><meta-data    android:name="com.google.firebase.messaging.default_notification_color"    android:resource="@android:color/white" /><!-- [END fcm_default_icon] -->
```

> **Примечание:** Требования к значку FCM: Маленький значок должен быть изображением PNG с каналом альфа-прозрачности. Фон должен быть прозрачным. Избегайте оставления чрезмерного пространства вокруг значка. Рекомендуется использовать размер 46 x 46px. Меньшие изображения будут нечеткими, а большие будут автоматически уменьшены системой.

Настраиваемые определения не поддерживаются; по умолчанию используется значок приложения.

> **Примечание:** Только **Huawei** поддерживает настройки, другие производители не поддерживают, и по умолчанию используется значок приложения.

Поместите маленькие значки в папку `nativeResources/android/res/drawable` и переименуйте файл ресурса на `huawei_private_icon.png`. Как показано на рисунке:

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/9fb71bfac1d211efbcd1525400bf7822.png)


---
*Источник: [https://trtc.io/document/60574](https://trtc.io/document/60574)*

---
*Источник (EN): [customized-icon.md](./customized-icon.md)*
