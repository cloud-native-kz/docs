# Плавающее окно

## Введение в функцию

TUIRoomKit поддерживает функцию плавающего окна, которая позволяет пользователям создавать свободно перемещаемое плавающее окно для отображения и управления интерфейсом видеоконференции TUIRoomKit. Это облегчает пользователям выполнение других задач во время участия в видеоконференции.

## ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/56e36f3d128b11efa09b525400762795.png)

## Инструкции по использованию

1. Во время встречи нажмите кнопку **Ещё** > **Плавающее окно** в нижней панели инструментов для включения плавающего окна.
2. При первом включении функции "Плавающее окно" устройства Android будут перенаправлены на соответствующую страницу системных параметров. Необходимо включить соответствующие разрешения для приложения, такие как **Плавающее окно**, **Всплывающий интерфейс в фоне**, **Разрешить отображение поверх других приложений** и т. д. Названия соответствующих системных параметров могут незначительно отличаться в зависимости от модели устройства.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/bc250e5e128b11efa09b525400762795.png)

3. После включения соответствующих системных разрешений устройства Android поддерживают как встроенные, так и внеприложные плавающие окна, тогда как устройства iOS поддерживают только встроенные плавающие окна.
4. В режиме плавающего окна нажмите на плавающее окно, чтобы вернуться на конференцию.

## Ключевой код

Вы можете включить/отключить функцию плавающего окна, используя следующие методы для разных платформ:

Android

Вы можете удалить код `addFloatItemIfNeeded(itemDataList)` в функции createItemList файла [Android/tuiroomkit/src/main/java/com/tencent/cloud/tuikit/roomkit/view/main/bottomnavigationbar/BottomViewModel.java](https://github.com/Tencent-RTC/TUIRoomKit/blob/main/Android/tuiroomkit/src/main/java/com/tencent/cloud/tuikit/roomkit/view/main/bottomnavigationbar/BottomViewModel.java), чтобы отключить плавающее окно.

```
private List<BottomItemData> createItemList() {
    List<BottomItemData> itemDataList = new ArrayList<>();
    addUserListItemIfNeeded(itemDataList);
    addMicItemIfNeeded(itemDataList);
    addCameraItemIfNeeded(itemDataList);
    addRaiseHandItemIfNeeded(itemDataList);
    addApplyListItemIfNeeded(itemDataList);
    addScreenItemIfNeeded(itemDataList);
    addChatItemIfNeeded(itemDataList);
    addInviteItemIfNeeded(itemDataList);    // Delete this line of code to disable the Floating Window feature 
    // addFloatItemIfNeeded(itemDataList);
    addSettingsItemIfNeeded(itemDataList);
    return itemDataList;
}
```

> **Примечание:** Если у вас есть какие-либо требования или отзывы, вы можете связаться: info_rtc@tencent.com.


---
*Источник: [https://trtc.io/document/60484](https://trtc.io/document/60484)*

---
*Источник (EN): [floating-window.md](./floating-window.md)*
