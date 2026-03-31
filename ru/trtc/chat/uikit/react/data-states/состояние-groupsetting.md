# Состояние GroupSetting

## Введение

`GroupSettingState` — это мощный центр управления статусом группового чата, специализированный на управлении параметрами группового чата, информацией участников и контролем прав доступа. Он предоставляет комплексную поддержку функций для управления информацией группового чата, операций с участниками, проверки доступа и настроек группового чата, что делает его основным инструментом для создания интерфейса управления групповым чатом.

Этот Hook имеет следующие особенности:

- **Полное управление информацией группового чата** — основная информация группы, список участников, установка прав доступа
- **Интеллектуальный контроль прав доступа** — проверка доступа на основе ролей и ограничение операций
- **Различные операции с участниками** — добавление, удаление, установка ролей, отключение звука и другие функции управления
- **Синхронизация состояния в реальном времени** — автоматическое отслеживание изменений состояния группового чата и обновление локальных данных

## Свойства

### Состояние, связанное с групповым чатом

| Поле | Тип | Описание |
| --- | --- | --- |
| groupID | string \| undefined | ID группы |
| groupType | GroupType \| undefined | Тип группы |
| groupName | string \| undefined | Название группы |
| avatar | string \| undefined | URL аватара группы |
| notification | string \| undefined | Уведомление группы |
| isMuted | boolean \| undefined | Режим "не беспокоить" |
| isPinned | boolean \| undefined | Закреплено сверху |
| groupOwner | GroupMember \| undefined | Информация о владельце группы |
| adminMembers | GroupMember[] | Список администраторов |
| allMembers | GroupMember[] \| undefined | Список участников |
| memberCount | number \| undefined | Количество участников |
| maxMemberCount | number \| undefined | Максимальное количество участников |
| currentUserID | string \| undefined | ID текущего пользователя |
| currentUserRole | GroupMemberRole \| undefined | Роль пользователя |
| isMuteAllMembers | boolean \| undefined | Отключен ли звук для всех участников |
| isInGroup | boolean \| undefined | Находится ли текущий пользователь в группе |
| inviteOption | GroupInviteType \| undefined | Способ приглашения для присоединения к группе |

### Метод инструмента разрешений

| Методология | Тип | Описание |
| --- | --- | --- |
| hasPermission | (permission: GroupPermission, role?: GroupMemberRole, groupType?: GroupType) => boolean | Проверить наличие определенного разрешения |

### Метод деловой операции

| Методология | Тип | Описание |
| --- | --- | --- |
| getGroupMemberList | (params?: GetGroupMemberListParams) => Promise<IGroupMember[]> | Получить список участников группы |
| updateGroupProfile | (params: UpdateGroupProfileParams) => Promise<void> | Обновить профиль группы |
| addGroupMember | (params: AddGroupMemberParams) => Promise<IAddGroupMemberResult> | Добавить участника группы |
| deleteGroupMember | (params: DeleteGroupMemberParams) => Promise<void> | Удалить участника группы |
| changeGroupOwner | (params: ChangeGroupOwnerParams) => Promise<void> | Передать право собственности на группу |
| setGroupMemberRole | (params: SetGroupMemberRoleParams) => Promise<void> | Установить роль участника |
| setChatPinned | (value: boolean) => Promise<void> | Закрепить групповой чат сверху [Бета] |
| setChatMuted | (value: boolean) => Promise<void> | Отключить уведомления группового чата [Бета] |
| setGroupMemberMuteTime | (params: SetGroupMemberMuteTimeParams) => Promise<void> | Установить продолжительность отключения звука участника |
| dismissGroup | (groupID?: string) => Promise<void> | Распустить групповой чат |
| quitGroup | (groupID?: string) => Promise<void> | Выйти из группового чата |

## Детали свойств

### groupID

- **Тип**: `string | undefined`
- **Описание**: Уникальный идентификатор текущего группового чата. Используется для всех вызовов API и идентификации операций, связанных с групповым чатом. Если undefined, это означает, что в настоящее время нет активной группы.

### groupType

- **Тип**: `GroupType | undefined`
- **Описание**: Перечисление типов группового чата, влияющее на функции группового чата и модель разрешений. Если undefined, это указывает на отсутствие активного группового чата в настоящий момент.
- **Определение перечисления**:

```
enum GroupType {  WORK,  PUBLIC,  MEETING,  AVCHATROOM,  COMMUNITY,}
```

### groupName

- **Тип**: `string | undefined`
- **Описание**: Отображаемое имя группового чата. Может быть изменено с помощью метода `updateGroupProfile` (требуются соответствующие разрешения). Если это undefined, это означает, что в настоящее время нет активной группы.

### avatar

- **Тип**: `string | undefined`
- **Описание**: URL-адрес фотографии профиля группы. Может быть изменен с помощью метода `updateGroupProfile` (требуются соответствующие разрешения). Если это undefined, это означает, что в настоящее время нет активной группы.

### notification

- **Тип**: `string | undefined`
- **Описание**: Объявление группового чата, обычно используется для размещения важных уведомлений или правил группы. Может быть изменено с помощью метода `updateGroupProfile` (требуются соответствующие разрешения). Если это undefined, это означает, что в настоящее время нет активной группы.

### isMuted

- **Тип**: `boolean | undefined`
- **Описание**: Установил ли текущий пользователь отключение уведомлений для этого группового чата. После установки push-уведомления от группового чата не будут приниматься. Если это undefined, это означает, что в настоящее время нет активной группы.

### isPinned

- **Тип**: `boolean | undefined`
- **Описание**: Закрепил ли текущий пользователь этот групповой чат сверху. Закрепленные чаты будут отображаться в верхней части списка сеансов. Если это undefined, это означает, что в настоящее время нет активной группы.

### groupOwner

- **Тип**: `GroupMember | undefined`
- **Описание**: Подробная информация о владельце группы. Если undefined, это указывает на отсутствие активного группового чата в настоящий момент.
- **Определение API GroupMember**:

```
interface GroupMember {    userID: string;          // userID    nick: string;            // Псевдоним пользователя    avatar: string;          // URL аватара пользователя    role: GroupMemberRole;   // Роль пользователя    joinTime: number;        // Время присоединения    muteUntil: string;       // Время истечения периода отключения звука    memberCustomField: string; // Пользовательское поле участника}enum GroupMemberRole {    OWNER = 'Owner',   // владелец группы    ADMIN = 'Admin',   // администратор группы    COMMON = 'Member', // участник группы}
```

### adminMembers

- **Тип**: `GroupMember[]`
- **Описание**: Список администраторов группы, содержащий информацию участников с ролью администратора.

### allMembers

- **Тип**: `GroupMember[] | undefined`
- **Описание**: Список всех участников группового чата с поддержкой загрузки по страницам. Получение и обновление осуществляется с помощью метода `getGroupMemberList`.

### memberCount

- **Тип**: `number | undefined`
- **Описание**: Текущее количество участников. Если undefined, это указывает на отсутствие активного группового чата в настоящий момент.

### maxMemberCount

- **Тип**: `number | undefined`
- **Описание**: Максимальный лимит участников для группового чата. Если undefined, это означает, что в настоящее время нет активной группы.

### currentUserID

- **Тип**: `string | undefined`
- **Описание**: userID текущего вошедшего пользователя (вы). Если undefined, это указывает на отсутствие активного группового чата в настоящий момент.

### currentUserRole

- **Тип**: `GroupMemberRole | undefined`
- **Описание**: Роль текущего вошедшего пользователя (вы) в групповом чате, которая влияет на права доступа пользователя. Если undefined, это указывает на отсутствие активного группового чата в настоящий момент.
- **Определение перечисления**:

```
enum GroupMemberRole {  OWNER = 'OWNER',  ADMIN = 'ADMIN',  COMMON = 'COMMON'}
```

### isMuteAllMembers

- **Тип**: `boolean | undefined`
- **Описание**: Включено ли отключение звука для всей комнаты. После включения только владелец группы и администраторы могут говорить. Если undefined, это указывает на отсутствие активного группового чата в настоящий момент.

### isInGroup

- **Тип**: `boolean | undefined`
- **Описание**: Находится ли текущий вошедший пользователь (вы) все еще в групповом чате. Используется для обработки необычных ситуаций, таких как исключение из группы. Если undefined, это указывает на отсутствие активного группового чата в настоящий момент.

### inviteOption

- **Тип**: `GroupInviteType | undefined`
- **Описание**: Настройки способа приглашения для присоединения к групповому чату. Если это undefined, это означает, что в настоящее время нет активной группы.
- **Определение перечисления**:

```
enum GroupInviteType {  FREE_ACCESS = 'FREE_ACCESS',  NEED_PERMISSION = 'NEED_PERMISSION',  DISABLE_APPLY = 'DISABLE_APPLY'}
```

### hasPermission

- **Тип**: `(permission: GroupPermission, role?: GroupMemberRole, groupType?: GroupType) => boolean`
- **Описание**: Проверить наличие определенного разрешения у назначенной роли в определенном типе группы. Если роль и groupType не предоставлены, система автоматически будет использовать роль текущего вошедшего пользователя (вас) и тип активной группы.
- **Определение перечисления GroupPermission**:

```
enum GroupPermission {  EDIT_GROUP_PROFILE_NAME = 'EDIT_GROUP_PROFILE_NAME',    // Редактировать название группы  EDIT_GROUP_PROFILE_AVATAR = 'EDIT_GROUP_PROFILE_AVATAR', // Редактировать аватар группы  EDIT_GROUP_PROFILE_NOTIFICATION = 'EDIT_GROUP_PROFILE_NOTIFICATION', // Редактировать объявление группы  REMOVE_MEMBER = 'REMOVE_MEMBER',                        // Удалить участника  SET_MEMBER_ROLE = 'SET_MEMBER_ROLE',                    // Установить роль участника  MUTE_MEMBER = 'MUTE_MEMBER',                            // Отключить звук участника  MUTE_ALL_MEMBERS = 'MUTE_ALL_MEMBERS',                  // Отключить звук всем  TRANSFER_OWNERSHIP = 'TRANSFER_OWNERSHIP',              // Передать право собственности на группу  DISMISS_GROUP = 'DISMISS_GROUP',                        // Распустить групповой чат  QUIT_GROUP = 'QUIT_GROUP'                               // Выйти из группового чата}
```

### getGroupMemberList

- **Тип**: `(params?: GetGroupMemberListParams) => Promise<GroupMember[]>`
- **Описание**: Получить список участников группы с поддержкой загрузки по страницам. После завершения загрузки результаты автоматически заполнят groupOwner, allMembers и adminMembers. Никаких действий с возвращаемым значением не требуется.
- **Определение API GetGroupMemberListParams**:

```
interface GetGroupMemberListParams {  count?: number;    // Количество для получения, максимум 100, по умолчанию 100  groupID?: string;  // ID группы, опционально  role?: string;     // Фильтр по роли, опционально  offset?: number;   // Смещение, по умолчанию 0}
```

### updateGroupProfile

- **Тип**: `(params: UpdateGroupProfileParams) => Promise<void>`
- **Описание**: Обновить профиль группы. groupID опционален и автоматически использует ID активной группы. Убедитесь, что предоставлено по крайней мере одно из остальных полей.
- **Определение API UpdateGroupProfileParams**:

```
interface UpdateGroupProfileParams {  groupID?: string;      // ID группы, опционально  name?: string;         // Название группы, опционально  avatar?: string;       // URL аватара группы, опционально  introduction?: string; // Описание группы, опционально  notification?: string; // Объявление группы, опционально}
```

### addGroupMember

- **Тип**: `(params: AddGroupMemberParams) => Promise<AddGroupMemberResult>`
- **Описание**: Добавить участников группы. groupID опционален и автоматически использует ID активной группы.
- **Определение API AddGroupMemberParams**:

```
interface AddGroupMemberParams {  groupID?: string;       // ID группы, опционально  userIDList: string[];   // Список ID пользователей для добавления}
```

### deleteGroupMember

- **Тип**: `(params: DeleteGroupMemberParams) => Promise<void>`
- **Описание**: Удалить участников группы. groupID опционален и автоматически использует ID активной группы.
- **Определение API DeleteGroupMemberParams**:

```
interface DeleteGroupMemberParams {  groupID?: string;       // ID группы, опционально  userIDList: string[];   // Список ID пользователей для удаления}
```

### changeGroupOwner

- **Тип**: `(params: ChangeGroupOwnerParams) => Promise<void>`
- **Описание**: Передать право собственности на группу. groupID опционален и автоматически использует ID активной группы.
- **Определение API ChangeGroupOwnerParams**:

```
interface ChangeGroupOwnerParams {  groupID?: string;    // ID группы, опционально  newOwnerID: string;  // ID нового владельца группы}
```

### setGroupMemberRole

- **Тип**: `(params: SetGroupMemberRoleParams) => Promise<void>`
- **Описание**: Установить роль участника. groupID опционален и автоматически использует ID активной группы.
- **Определение API SetGroupMemberRoleParams**:

```
interface SetGroupMemberRoleParams {  groupID?: string;         // ID группы, опционально  userID: string;           // userId  role: GroupMemberRole;    // новая роль [GroupMemberRole.ADMIN, GroupMemberRole.COMMON]}
```

### setChatPinned

- **Тип**: `(value: boolean) => Promise<void>`
- **Описание**: Установить статус закрепления группового чата. Автоматически использует ID активной группы. [Бета]

### setChatMuted

- **Тип**: `(value: boolean) => Promise<void>`
- **Описание**: Установить статус режима "не беспокоить" для группового чата. Автоматически использует ID активной группы. [Бета]

### setGroupMemberMuteTime

- **Тип**: `(params: SetGroupMemberMuteTimeParams) => Promise<void>`
- **Описание**: Установить продолжительность отключения звука участника. groupID опционален и автоматически использует ID активной группы. Чтобы включить звук, просто установите время на 0.
- **Определение API SetGroupMemberMuteTimeParams**:

```
interface SetGroupMemberMuteTimeParams {  groupID?: string;  // ID группы, опционально  userID: string;    // uid  time: number;      // продолжительность отключения звука (секунды)}
```

### dismissGroup

- **Тип**: `(groupID?: string) => Promise<void>`
- **Описание**: Распустить групповой чат. groupID опционален и автоматически использует ID активной группы.

### quitGroup

- **Тип**: `(groupID?: string) => Promise<void>`
- **Описание**: Выйти из группы. groupID может быть оставлен пустым и автоматически использует ID активной группы.

## Примеры использования

### Компонент базовых настроек группового чата

```
import React, { useState } from 'react';import { useGroupSettingState, GroupPermission } from '@tencentcloud/chat-uikit-react';const GroupSettingPanel = () => {  const {    groupID,    groupName,    avatar,    memberCount,    maxMemberCount,    isMuted,    isPinned,    hasPermission,    setChatPinned,    setChatMuted,    updateGroupProfile,    quitGroup,  } = useGroupSettingState();  const [isEditing, setIsEditing] = useState(false);  const [newName, setNewName] = useState(groupName || '');  const handleUpdateName = async () => {    try {      await updateGroupProfile({ name: newName });      setIsEditing(false);    } catch (error) {      console.error('update failed:', error);    }  };  if (!groupID) return <div>Select group</div>;  return (    <div className="group-setting">      {/* Информация о групповом чате */}      <div className="group-info">        <img src={avatar} alt="group avatar" className="group-avatar" />        {isEditing ? (          <div className="edit-form">            <input               value={newName}               onChange={e => setNewName(e.target.value)}              className="name-input"            />            <button onClick={handleUpdateName}>save</button>            <button onClick={() => setIsEditing(false)}>cancel</button>          </div>        ) : (          <div className="group-details">            <h3>{groupName}</h3>            <span>member: {memberCount}/{maxMemberCount}</span>            {hasPermission(GroupPermission.UPDATE_GROUP_INFO) && (              <button onClick={() => setIsEditing(true)}>Edit</button>            )}          </div>        )}      </div>      {/* Параметры чата */}      <div className="chat-settings">        <div className="setting-item">          <span>pin conversation</span>          <input             type="checkbox"             checked={isPinned || false}            onChange={e => setChatPinned(e.target.checked)}          />        </div>        <div className="setting-item">          <span>mute</span>          <input             type="checkbox"             checked={isMuted || false}            onChange={e => setChatMuted(e.target.checked)}          />        </div>      </div>      {/* Кнопка действия */}      <div className="actions">        <button onClick={quitGroup} className="danger-btn">          Quit Group        </button>      </div>    </div>  );};
```

Отображение показано ниже:

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/dabe6773617a11f0bac1525400454e06.png)

### Компонент управления участниками

```
import React, { useEffect } from 'react';import { useGroupSettingState, GroupMemberRole, GroupPermission } from '@tencentcloud/chat-uikit-react';const GroupMemberList: React.FC = () => {  const {    allMembers,    hasPermission,    getGroupMemberList,    setGroupMemberRole,    deleteGroupMember,  } = useGroupSettingState();  useEffect(() => {    getGroupMemberList({ count: 50 });  }, []);  const handlePromote = (userID: string) => {    setGroupMemberRole({ userID, role: GroupMemberRole.ADMIN });  };  const handleRemove = (userID: string) => {    deleteGroupMember({ userIDList: [userID] });  };  return (    <div className="member-list">      {allMembers?.map(member => (        <div key={member.userID} className="member-item">          <img src={member.avatar} alt="" className="member-avatar" />          <span className="member-name">{member.nick}</span>          <span className="member-role">{member.role}</span>                    {hasPermission(GroupPermission.SET_MEMBER_ROLE) && (            <div className="member-actions">              {member.role === GroupMemberRole.COMMON && (                <button onClick={() => handlePromote(member.userID)}>                  Promote to Admin                </button>              )}              <button onClick={() => handleRemove(member.userID)}>                Remove              </button>            </div>          )}        </div>      ))}    </div>  );};
```

Отображение показано ниже:

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/dabfc7c7617a11f0b324525400e889b2.png)

### Файл стилей

```
// Стиль компонента базовых настроек группового чата.group-setting {  padding: 20px;  background: white;  border-radius: 8px;  .group-info {    display: flex;    align-items: center;    gap: 15px;    margin-bottom: 20px;    .group-avatar {      width: 60px;      height: 60px;      border-radius: 50%;      object-fit: cover;    }    .group-details {      flex: 1;      h3 {        margin: 0 0 5px 0;        font-size: 18px;      }      span {        color: #666;        font-size: 14px;      }      button {        margin-top: 8px;        padding: 4px 8px;        background: #f0f0f0;        border: none;        border-radius: 4px;        cursor: pointer;      }    }    .edit-form {      display: flex;      flex-direction: column;      gap: 10px;      .name-input {        padding: 8px;        border: 1px solid #ddd;        border-radius: 4px;      }      button {        padding: 6px 12px;        border: none;        border-radius: 4px;        cursor: pointer;        &:first-child {          background: #1890ff;          color: white;        }        &:last-child {          background: #f0f0f0;        }      }    }  }  .chat-settings {    margin-bottom: 20px;    .setting-item {      display: flex;      justify-content: space-between;      align-items: center;      padding: 12px 0;      border-bottom: 1px solid #f0f0f0;      span {        font-size: 14px;      }      input[type="checkbox"] {        width: 20px;        height: 20px;      }    }  }  .actions {    .danger-btn {      padding: 10px 20px;      background: #ff4d4f;      color: white;      border: none;      border-radius: 4px;      cursor: pointer;      &:hover {        background: #ff7875;      }    }  }}// Стиль компонента управления участниками.member-list {  .member-item {    display: flex;    align-items: center;    gap: 12px;    padding: 12px;    border-bottom: 1px solid #f0f0f0;    .member-avatar {      width: 40px;      height: 40px;      border-radius: 50%;      object-fit: cover;    }    .member-name {      flex: 1;      font-size: 14px;    }    .member-role {      color: #666;      font-size: 12px;      margin-right: 10px;    }    .member-actions {      display: flex;      gap: 8px;      button {        padding: 4px 8px;        font-size: 12px;        border: 1px solid #ddd;        border-radius: 4px;        background: white;        cursor: pointer;        &:hover {          border-color: #1890ff;          color: #1890ff;        }      }    }  }}
```

## Практические советы

### Проверка доступа

- Проверьте наличие необходимого разрешения перед выполнением действий группового чата
- Используйте метод `hasPermission` для управления отображением интерфейса

### Оптимизация производительности

- Разумное использование загрузки списка участников по страницам
- Избегайте частых вызовов API, рассмотрите использование debounce
- Использование памяти в сценариях больших групповых чатов

### Опыт пользователя

- Предоставьте индикацию статуса загрузки
- Проверьте подтверждение перед операцией
- Обновите локальное состояние для немедленной обратной связи

Благодаря этому документу вы можете полностью разобраться и использовать все функции GroupSettingState для создания полного интерфейса управления групповым чатом.


---
*Источник: [https://trtc.io/document/72096](https://trtc.io/document/72096)*

---
*Источник (EN): [groupsetting-state.md](состояние-groupsetting.md)*
