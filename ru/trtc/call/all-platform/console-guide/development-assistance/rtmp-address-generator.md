# Генератор RTMP-адресов

Консоль TRTC поддерживает генерацию адресов потоков для [функции входа в комнату потокового вещания RTMP](https://www.tencentcloud.com/document/product/647/62716#3b96cc52-90be-46ee-aec0-218dcf302119), которая подходит только для фазы тестирования. Для официального онлайн-бизнеса рекомендуется развернуть логику генерации адресов на серверных сервисах, чтобы избежать кражи трафика в результате утечки ключа шифрования.

## Генерирование адреса потока

1. Перейдите в [консоль Tencent RTC](https://console.trtc.io), выберите **Development Tools >** [**RTMP Address Generator**](https://console.trtc.io/rtmptool) на левой боковой панели и откройте модуль **Generating Stream Address**.
2. Нажмите на выпадающее меню для выбора созданного приложения (SDKAppID).
3. Заполните **Push Roomname (RoomID)** и **Push Username (UserID)**.
4. Нажмите **Generate**, чтобы сразу же сгенерировать соответствующий адрес потока RTMP.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/25046b34d23e11ef97675254007c27c5.png)


---
*Источник: [https://trtc.io/document/67774](https://trtc.io/document/67774)*

---
*Источник (EN): [rtmp-address-generator.md](./rtmp-address-generator.md)*
