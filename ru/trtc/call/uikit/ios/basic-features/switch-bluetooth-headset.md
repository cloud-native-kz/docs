# Переключение Bluetooth-гарнитуры

## Обзор функции

Когда Bluetooth-наушники не подключены, поддерживается только выбор между динамиком и наушником. Если обнаружены Bluetooth-наушники, переключение между Bluetooth-наушниками, наушником и динамиком реализуется с помощью компонента **Apple AVRoutePickerView**.

> **Примечание:** В настоящее время функция переключения Bluetooth-наушников поддерживается только на платформе iOS.

## Использование

1. Bluetooth-наушники не подключены. Используйте пользовательский интерфейс в TUICallKit для переключения между динамиком и наушником. Настройка пользовательского интерфейса выглядит следующим образом.

| Наушник | Динамик |
| --- | --- |
| ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/aa9496c8662c11f09a9d52540044a08e.png) | ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/b59cb4a4662c11f0b5365254001c06ec.png) |

2. После подключения Bluetooth-наушников стиль кнопки выбора звукового маршрута в TUICallKit изменяется. Нажмите кнопку, чтобы активировать **AVRoutePickerView**, переключите звуковой маршрут из **AVRoutePickerView**, и название кнопки в TUICallKit будет обновлено соответственно.

| Кнопка переключения звукового маршрута при подключении Bluetooth-наушников | AVRoutePickerView |
| --- | --- |
| ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/c7c77768662c11f088c4525400454e06.png) | ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/ef5ae3be662c11f088c4525400454e06.png) |


---
*Источник: [https://trtc.io/document/72205](https://trtc.io/document/72205)*

---
*Источник (EN): [switch-bluetooth-headset.md](./switch-bluetooth-headset.md)*
