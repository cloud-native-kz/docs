# Статус онлайна пользователя

## Описание

@tencentcloud/chat-uikit-vue начиная с версии v2.0.0, начал поддерживать функцию "Статус онлайна пользователя"ã

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/40f030cd1cc111efb7495254005ac0ca.png)

> **Примечание:** Функция "Статус онлайна пользователя" **поддерживается только** издением Pro ãEdition Pro Plus ãEnterprise Edition, пожалуйста, проверьте перед использованием. Функция "Статус онлайна пользователя" должна быть активирована через [Chat Console](https://console.trtc.io/chat/login-message), пожалуйста, проверьте перед использованием.

## Включение/отключение статуса онлайна пользователя

**"Статус онлайна пользователя" отключен по умолчанию**, вам необходимо выполнить следующие шаги для его включения:

```
import { TUIUserService } from "@tencentcloud/chat-uikit-engine";// открыть статус онлайна пользователя// Этот интерфейс действителен только при вызове после успешного входа TUIUserService.switchUserStatus({ displayOnlineStatus: true });// закрыть статус онлайна пользователя// Этот интерфейс действителен только при вызове после успешного входа TUIUserService.switchUserStatus({ displayOnlineStatus: false });
```

> **Примечание:** Интерфейс выше `TUIUserService.switchUserStatus` **действует только после успешного входа**, пожалуйста, убедитесь, что вы вызываете этот интерфейс только после входа. Вот пример кода для включения статуса онлайна пользователя путем вызова этого интерфейса после входа:

```
import { TUILogin } from "@tencentcloud/tui-core";import { TUIUserService } from "@tencentcloud/chat-uikit-engine";TUILogin.login(loginInfo).then((res: any) => {  TUIUserService.switchUserStatus({ displayOnlineStatus: true });});
```

## Дополнительная информация: как TUIKit внутри реализует функцию "статус онлайна пользователя"?

> **Примечание:** Следующее содержание предназначено только для вспомогательного чтения. Функция статуса онлайна пользователя уже включена в TUIKit по умолчанию, что избавляет пользователя от необходимости ручной реализации.

Оба компонента `TUIConversion` и `TUIContact` поддерживают функцию "Статус онлайна пользователя". `TUIContact` приводится в качестве примера для обсуждения ниже:

##### 1. Мониторинг изменений списка статусов онлайна пользователей

В `TUIKit/components/TUIContact/contact-list/index.vue` мониторьте изменения списка статусов онлайна пользователей:

```
TUIStore.watch(StoreName.USER, {  ...  displayOnlineStatus: (status: boolean) => {    displayOnlineStatus.value = status;  },  userStatusList: (list: Map<string, IUserStatus>) => {    list?.size && (userOnlineStatusMap.value = Object.fromEntries(list?.entries()));  },});
```

##### 2. Отображение статуса онлайна пользователя

В `TUIKit/components/TUIContact/contact-list/contact-list-item/index.vue`:

**2.1 Интерпретация статуса онлайна пользователя:**

```
function getOnlineStatus(): boolean {  return (    props.displayOnlineStatus &&    props.userOnlineStatusMap &&    props.item?.userID &&    props.userOnlineStatusMap?.[props.item.userID]?.statusType === TUIChatEngine.TYPES.USER_STATUS_ONLINE   );};
```

**2.2 Отображение статуса онлайна пользователя:**

```
<div  v-if="props.displayOnlineStatus"  :class="{    'online-status': true,    'online-status-online': isOnline,    'online-status-offline': !isOnline  }"></div>
```

## Часто задаваемые вопросы

### При вызове API подписки/отмены подписки интерфейс выдает код ошибки "72001"

Код ошибки 72001 указывает на то, что соответствующая функция не включена в консоли. Пожалуйста, войдите в [Chat Console](https://console.trtc.io/chat/login-message), чтобы активировать соответствующий функциональный переключатель.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/ce29129a126d11ef9fa952540019e87e.png)

### Ошибка: пакет не поддерживает использование этого API, пожалуйста, обновитесь до Edition Pro ãEdition Pro Plus ãEnterprise Edition

Функция "Статус онлайна пользователя" поддерживается только Edition Pro ãEdition Pro Plus или Enterprise Edition. Это сообщение об ошибке указывает на то, что ваш текущий пакет не поддерживает эту функцию.

## Свяжитесь с нами

Присоединитесь к [технической группе обмена в Telegram](https://t.me/tencent_imsdk) или [группе обсуждения в WhatsApp](https://chat.whatsapp.com/IVa11ZkVmKTEwSWsAzSyik), воспользуйтесь поддержкой профессиональных инженеров и решите ваши самые сложные задачи.


---
*Источник: [https://trtc.io/document/58651](https://trtc.io/document/58651)*

---
*Источник (EN): [user-online-status.md](./user-online-status.md)*
