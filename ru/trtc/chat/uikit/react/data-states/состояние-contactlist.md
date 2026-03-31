# Состояние ContactList

`ContactListState` — это хук управления цепочкой отношений на основе Zustand, предоставляющий полные возможности управления данными для компонента `ContactList`. Он поддерживает список друзей, список групп, чёрный список, управление приложениями и другие функции. Если встроенные возможности компонента недостаточны для вашего бизнеса, вы можете использовать `ContactListState` для реализации ваших потребностей.

### Данные

| Имя атрибута | Тип | Описание |
| --- | --- | --- |
| friendList | Friend[] | список друзей |
| groupList | Group[] | список групп |
| blackList | UserProfile[] | чёрный список |
| friendApplicationUnreadCount | number | Количество непрочитанных запросов дружбы |
| friendGroupList | FriendGroup[] | список групп друзей |
| friendApplicationList | FriendApplication[] | список запросов дружбы |
| groupApplicationList | GroupApplication[] | список запросов присоединения к группе |

### Методы операций

| Имя атрибута | Тип | Описание |
| --- | --- | --- |
| addFriend | (options: AddFriendParams) => Promise | Добавить в друзья |
| deleteFriend | (options: DeleteFriendParams) => Promise | Удалить друга |
| setFriendRemark | (options: FriendRemarkParams) => Promise | Установить примечание друга |
| markFriendApplicationAsRead | () => Promise | Отметить запрос дружбы как прочитанный |
| acceptFriendApplication | (options: FriendApplicationParams) => Promise | Принять запрос дружбы |
| refuseFriendApplication | (userID: string) => Promise | Отклонить запрос дружбы |
| addToBlacklist | (userIDList: string[]) => Promise | Добавить в чёрный список |
| removeFromBlacklist | (userIDList: string[]) => Promise | Удалить из чёрного списка |
| createFriendGroup | (options: FriendGroupParams) => Promise | Создать группу друзей |
| deleteFriendGroup | (name: string) => Promise | Удалить группу друзей |
| addToFriendGroup | (options: FriendGroupParams) => Promise | Добавить друга в группу |
| removeFromFriendGroup | (options: FriendGroupParams) => Promise | Удалить друга из группы |
| renameFriendGroup | (options: RenameFriendGroupParams) => Promise | Переименовать группу друзей |
| joinGroup | (options: JoinGroupParams) => Promise | Запросить присоединение к группе |
| acceptGroupApplication | (options: GroupApplicationParams) => Promise | Принять запрос присоединения к группе |
| refuseGroupApplication | (options: GroupApplicationParams) => Promise | Отклонить запрос присоединения к группе |

## Примеры использования

```
friendList
```


---
*Источник: [https://trtc.io/document/72204](https://trtc.io/document/72204)*

---
*Источник (EN): [contactlist-state.md](состояние-contactlist.md)*
