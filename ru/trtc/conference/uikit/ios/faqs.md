# Часто задаваемые вопросы

### **Мне нужно самостоятельно изменить UI. Каждый раз при обновлении пода исходный код будет обновлен, и изменения будут потеряны. Как это обработать?**

Рекомендуется форкировать [репозиторий TUIRoomKit](https://github.com/tencentyun/TUIRoomKit/tree/main) на свой личный аккаунт GitHub, а затем использовать [локальный pod](https://guides.cocoapods.org/using/the-podfile.html) или [git pod path](https://guides.cocoapods.org/using/the-podfile.html) для ссылки на соответствующий код в вашем проекте.

Подробности см. в [официальной документации Pod](https://guides.cocoapods.org/using/the-podfile.html):

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/3b68eed135c311eeaa5e5254005c1bd1.png)

### Есть ли конфликт между TUIRoomKit и интегрированной аудио-видео библиотекой?

Аудио-видео библиотеки Tencent Cloud не могут быть интегрированы одновременно, и могут возникнуть конфликты символов. Вы можете обработать это согласно следующим сценариям.

1. Если вы используете библиотеку `TXLiteAVSDK_TRTC`, конфликтов символов не будет. Вы можете напрямую добавить зависимости в файл Podfile.

```
pod 'TUIRoomKit'
```

2. Если вы используете библиотеку `TXLiteAVSDK_Professional`, будут конфликты символов. Вы можете добавить зависимости в файл `Podfile`.

```
pod 'TUIRoomKit/Professional'
```

3. Если вы используете библиотеку `TXLiteAVSDK_Enterprise`, будут конфликты символов. Рекомендуется обновиться до `TXLiteAVSDK_Professional`, а затем использовать TUIRoomKit/Professional.

### Как просмотреть логи TRTC?

Логи TRTC по умолчанию сжимаются и шифруются с расширением .xlog. Возможность шифрования логов можно контролировать с помощью setLogCompressEnabled. Имя файла, содержащее C (compressed), зашифровано и сжато, а имя файла, содержащее R (raw), — это открытый текст.

- iOS&Mac: `Documents/log` Sandbox
- Android:
  - Версии 6.7 и ранее: `/sdcard/log/tencent/liteav`
  - Версии после 6.8: `/sdcard/Android/data/имя пакета/files/log/tencent/liteav/`
  - Версии после 8.5: `/sdcard/Android/data/имя пакета/files/log/liteav/`
- Windows:
  - Версии до 8.8: `%appdata%/tencent/liteav/log`
  - Версии 8.8 и позже: `%appdata%/liteav/log`
- Web: Откройте консоль браузера или используйте vConsole для записи информации печати SDK.

> **Примечание:** Для просмотра файла .xlog необходимо загрузить [инструмент дешифровки](https://dldir1.qq.com/hudongzhibo/log_tool/decode_mars_log_file.py) и запустить его непосредственно в окружении Python 2.7 с файлом xlog в одной директории, используя команду `python decode_mars_log_file.py`. Для просмотра файла .clog (новый формат логов после версии 9.6) необходимо загрузить [инструмент дешифровки](http://dldir1.qq.com/hudongzhibo/log_tool/decompress_clog.py) и запустить его непосредственно в окружении Python 2.7 с файлом clog в одной директории, используя команду `python decompress_clog.py`.


---
*Источник: [https://trtc.io/document/54895](https://trtc.io/document/54895)*

---
*Источник (EN): [faqs.md](./faqs.md)*
