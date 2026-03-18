# ContactList

## Обзор

ContactList — это высоконастраиваемый компонент списка контактов. Он поддерживает список друзей, список групп, черный список и управление приложениями, предлагая основные функции, такие как свертывание групп, поиск с фильтром и пользовательский рендеринг. Он подходит для интерфейсов управления контактами в приложениях для обмена сообщениями и социальных сетей.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/41360ab1679511f0837f525400454e06.png)

## ContactList Props

| Поле | Тип | Значение по умолчанию | Описание |
| --- | --- | --- | --- |
| activeContactItem | ContactGroupItem \| undefined | `undefined` | Активный элемент контакта |
| enableSearch | boolean | `true` | Включена ли функция поиска |
| groupConfig | Partial<Record<ContactItemType, CustomGroupConfig>> | `{}` | Пользовательская конфигурация группы |
| className | string | `undefined` | Пользовательское имя CSS класса |
| style | React.CSSProperties | `undefined` | Пользовательский встроенный стиль |
| searchPlaceholder | string | `'Search contacts'` | Текст-заполнитель поля поиска |
| emptyText | string | `'No contacts'` | Текст подсказки при пустом статусе |
| ContactItem | React.ComponentType<ContactListItemProps> \| undefined | `ContactListItem` | Пользовательский компонент контакта |
| ContactSearchComponent | React.ComponentType<ContactSearchProps> \| undefined | `ContactSearch` | Пользовательский компонент поиска |
| GroupHeader | React.ComponentType<{ data: ContactGroup }> \| undefined | Заголовок группы по умолчанию | Пользовательский компонент заголовка группы |
| PlaceholderEmptyList | React.ReactNode \| undefined | Пустой статус по умолчанию | Пользовательский компонент пустого статуса |
| onContactItemClick | (item: ContactGroupItem) => void | `undefined` | Событие клика элемента контакта |
| onFriendApplicationAction | (action: 'accept' \| 'refuse', application: FriendApplication) => void | `undefined` | Событие операции заявки в друзья |
| onGroupApplicationAction | (action: 'accept' \| 'refuse', application: GroupApplication) => void | `undefined` | Событие операции заявки в группу |

## ContactInfo props

| Поле | Тип | Значение по умолчанию | Описание |
| --- | --- | --- | --- |
| contactItem | ContactGroupItem \| undefined | `undefined` | Текущий отображаемый элемент контакта |
| showActions | boolean | `true` | Показывать ли кнопку действия |
| PlaceholderEmpty | React.ReactNode \| undefined | `undefined` | Компонент заполнителя пустого статуса |
| FriendInfoComponent | React.ComponentType<FriendInfoProps> | `FriendInfo` | Компонент информации о друге |
| GroupInfoComponent | React.ComponentType<GroupInfoProps> | `GroupInfo` | Компонент информации о группе |
| BlacklistInfoComponent | React.ComponentType<BlacklistInfoProps> | `BlacklistInfo` | Компонент информации о черном списке |
| FriendApplicationInfoComponent | React.ComponentType<FriendApplicationInfoProps> | `FriendApplicationInfo` | Компонент информации о заявке в друзья |
| GroupApplicationInfoComponent | React.ComponentType<GroupApplicationInfoProps> | `GroupApplicationInfo` | Компонент информации о заявке в группу |
| SearchGroupInfoComponent | React.ComponentType<SearchGroupInfoProps> | `SearchGroupInfo` | Компонент поиска информации о группе |
| SearchUserInfoComponent | React.ComponentType<SearchUserInfoProps> | `SearchUserInfo` | Компонент поиска информации пользователя |
| onClose | () => void | `undefined` | Обратный вызов закрытия панели сообщений |
| onSendMessage | (friend: Friend) => void | `undefined` | Обратный вызов отправки сообщения |
| onDeleteFriend | (friend: Friend) => void | `undefined` | Обратный вызов удаления друга |
| onUpdateFriendRemark | (friend: Friend, remark: string) => void | `undefined` | Обратный вызов обновления примечания друга |
| onAddToBlacklist | (friend: Friend) => void | `undefined` | Обратный вызов добавления в черный список |
| onRemoveFromBlacklist | (profile: UserProfile) => void | `undefined` | Обратный вызов удаления из черного списка |
| onEnterGroup | (group: GroupModel) => void | `undefined` | Обратный вызов входа в группу |
| onLeaveGroup | (group: GroupModel) => void | `undefined` | Обратный вызов выхода из группы |
| onDismissGroup | (group: GroupModel) => void | `undefined` | Обратный вызов роспуска группы |
| onFriendApplicationAction | (action: 'accept' \| 'refuse', application: FriendApplication) => void | `undefined` | Обратный вызов операции заявки в друзья |
| onGroupApplicationAction | (action: 'accept' \| 'refuse', application: GroupApplication) => void | `undefined` | Обратный вызов операции заявки в группу |
| onAddFriend | (user: UserProfile, wording: string) => void | `undefined` | Обратный вызов заявки в друзья |
| onJoinGroup | (group: GroupModel, note: string) => void | `undefined` | Обратный вызов присоединения к группе |

## Базовое использование

```
import { ContactList, ContactInfo } from '@tencentcloud/chat-uikit-react';function App() {  return (    <div>      <ContactList />      <ContactInfo />    </div>  );}
```

## Пользовательские возможности

### Пользовательский переключатель функции поиска списка контактов

Установив параметр `enableSearch`, вы можете гибко управлять отображением функции поиска группы друзей в ContactList.

```
<ContactList enableSearch={false} />
```

Результат показан ниже.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/3d1879db679511f09b85525400bf7822.png)

### Пользовательская конфигурация группы контактов списка контактов

`groupConfig` используется для пользовательской конфигурации группы, включая название, порядок отображения, скрытое состояние и т. д. Значение по умолчанию — `{}`.

Пользовательское название заголовка группы

Скрыть конкретную группу

```
import React from 'react';import { ContactList } from '@tencentcloud/chat-uikit-react';import { ContactItemType } from '@tencentcloud/chat-uikit-react';function CustomGroupTitlesContactList() {  const groupConfig = {    [ContactItemType.FRIEND]: {      title: 'My friend',      order: 1    },    [ContactItemType.GROUP]: {      title: 'My Groups',      order: 2    },    [ContactItemType.FRIEND_REQUEST]: {      title: 'Friend request',      order: 0    }  };  return (    <ContactList      groupConfig={groupConfig}      onContactItemClick={(item) => {        console.log('contact person click:', item);      }}    />  );}
```

Результат показан ниже.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/3d333139679511f09a9d52540044a08e.png)

```
import React from 'react';import { ContactList } from '@tencentcloud/chat-uikit-react';import { ContactItemType } from '@tencentcloud/chat-uikit-react';function HiddenGroupsContactList() {  const groupConfig = {    [ContactItemType.BLACK]: {      title: 'blocklist',      hidden: true // hide blocklist grouping    },    [ContactItemType.GROUP_REQUEST]: {      title: 'Group Application',      hidden: true // hide group application grouping    }  };  return (    <ContactList      groupConfig={groupConfig}      onContactItemClick={(item) => {        console.log('contact person click:', item);      }}    />  );}
```

Результат показан ниже.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/3d119649679511f09b85525400bf7822.png)

### Пользовательский подэлемент списка контактов

ContactItem используется для пользовательского компонента рендеринга контакта, значение по умолчанию — встроенный компонент `ContactListItem`.

```
import React from 'react';import { ContactList, Avatar } from '@tencentcloud/chat-uikit-react';import type { ContactListItemProps } from '@tencentcloud/chat-uikit-react';const SimpleContactItem: React.FC<ContactListItemProps> = ({   contactItem,   onClick,   activeContactItem }) => {  const isActive = activeContactItem?.data.userID === contactItem.data.userID;  return (    <div      className={`simple-contact-item ${isActive ? 'active' : ''}`}      onClick={() => onClick?.(contactItem.type, contactItem.data)}      style={{        padding: '8px 12px',        borderBottom: '1px solid #f0f0f0',        cursor: 'pointer',        backgroundColor: isActive ? '#e6f7ff' : 'transparent'      }}    >      <div style={{ display: 'flex', alignItems: 'center', gap: '10px' }}>        <Avatar src={contactItem.data.avatar}  alt="avatar" />        <span>{contactItem.data.nick || contactItem.data.name}</span>      </div>    </div>  );};function ContactListWithSimpleItems() {  return (    <ContactList      ContactItem={SimpleContactItem}      onContactItemClick={(item) => {        console.log('contact person click:', item);      }}    />  );}
```

Результат показан ниже.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/410ebb3d679511f08e915254007c27c5.png)

### Пользовательский переключатель кнопки действия сведений о контакте

`showActions` указывает, показывать ли кнопки действия. Значение по умолчанию — `true`.

```
import React from 'react';import { ContactInfo } from '@tencentcloud/chat-uikit-react';function ReadOnlyContactInfo() {  const friendData = {    type: ContactItemType.FRIEND,    data: {      userID: 'user123',      nick: 'Zhang San',      avatar: 'https://example.com/avatar.jpg',      remark: 'colleague',      // ... other friend properties    },  };  return (    <ContactInfo       contactItem={friendData}      showActions={false} // Hide ALL action buttons and display information only    />  );}
```

Результат показан ниже.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/3d38fc0c679511f0924f5254005ef0f7.png)

### Пользовательский пустой статус деталей контакта

`PlaceholderEmpty` используется для пользовательского отображения содержимого пустого статуса, значение по умолчанию — `undefined`.

```
import React from 'react';import { ContactInfo } from '@tencentcloud/chat-uikit-react';function CustomEmptyState() {  const EmptyPlaceholder = () => (    <div style={{       width: '100%',      textAlign: 'center',       padding: '40px 20px',      color: '#999',      fontSize: '14px',      background: '#fff',    }}>      <div style={{ fontSize: '48px', marginBottom: '16px' }}>ð¤</div>      <div>Select one contact person to view detailed information</div>      <div style={{ marginTop: '8px', fontSize: '12px' }}>        click any item in the left-side contact list      </div>    </div>  );  return (    <ContactInfo       PlaceholderEmpty={<EmptyPlaceholder />}    />  );}
```

Результат показан ниже.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/410e35cf679511f0837f525400454e06.png)

### Пользовательский компонент деталей контакта

> **Примечание:** `FriendInfoComponent` для пользовательского компонента информации о друге, значение по умолчанию — встроенный компонент `FriendInfo`. `GroupInfoComponent` для пользовательского компонента информации о группе, значение по умолчанию — встроенный компонент `GroupInfo`. `BlacklistInfoComponent` для пользовательского компонента информации о черном списке, значение по умолчанию — встроенный компонент `BlacklistInfo`. `FriendApplicationInfoComponent` для пользовательского компонента информации о заявке в друзья, значение по умолчанию — встроенный компонент `FriendApplicationInfo`. `GroupApplicationInfoComponent` для пользовательского компонента информации о заявке в группу, значение по умолчанию — встроенный компонент `GroupApplicationInfo`.

Пользовательский компонент информации о друге

Пользовательский компонент информации о группе

Пользовательский компонент информации о черном списке

Пользовательский компонент информации о заявке в друзья

Пользовательский компонент информации о заявке в группу

```
import React from 'react';import { ContactInfo } from '@tencentcloud/chat-uikit-react';import type { FriendInfoProps, Friend } from '@tencentcloud/chat-uikit-react';import { Button } from '@tencentcloud/uikit-base-component-react';// Custom Friend Information Componentconst CustomFriendInfo: React.FC<FriendInfoProps> = ({   friend,   showActions,   onClose,   onSendMessage,  onDeleteFriend }) => {  return (    <div style={{ padding: '20px', border: '1px solid #e0e0e0', borderRadius: '8px' }}>      <div style={{ display: 'flex', alignItems: 'center', marginBottom: '16px' }}>        <img           src={friend.avatar}           alt="avatar"           style={{ width: '60px', height: '60px', borderRadius: '50%', marginRight: '16px' }}        />        <div>          <h3 style={{ margin: '0 0 4px 0' }}>{friend.nick}</h3>          <p style={{ margin: '0', color: '#666' }}>Remark: {friend.remark}</p>        </div>      </div>            <div style={{ display: 'flex', flexDirection: 'column', gap: '10px',  marginBottom: '16px' }}>        <p><strong>uid:</strong> {friend.userID}</p>        <p><strong>Personal signature:</strong> {friend.selfSignature}</p>        <p><strong>Location:</strong> {friend.location}</p>      </div>      {showActions && (        <div style={{ display: 'flex', gap: '8px' }}>          <Button onClick={() => onSendMessage?.(friend)}>Send Message</Button>          <Button onClick={() => onDeleteFriend?.(friend)}>Remove Friend</Button>          <Button onClick={onClose}>Close</Button>        </div>      )}    </div>  );};function CustomFriendInfoDemo() {  const friendData = {    type: ContactItemType.FRIEND,    data: {      userID: 'user123',      nick: 'Zhang San',      avatar: 'https://example.com/avatar.jpg',      remark: 'colleague',      selfSignature: 'Love technology, love life',      location: 'Beijing',      // ... other attributes    },  };  return (    <ContactInfo       contactItem={friendData}      FriendInfoComponent={CustomFriendInfo}      onSendMessage={(friend) => console.log('Send message to:', friend.nick)}      onDeleteFriend={(friend) => console.log('Remove friend:', friend.nick)}    />  );}
```

Результат показан ниже.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/3d11e473679511f0924f5254005ef0f7.png)

```
import React from 'react';import { ContactInfo, GroupMemberRole } from '@tencentcloud/uikit-component-react';import type { GroupInfoProps, GroupModel } from '@tencentcloud/uikit-component-react';import { Button } from '@tencentcloud/uikit-base-component-react';// Custom Group Information Componentconst CustomGroupInfo: React.FC<GroupInfoProps> = ({   group,   showActions,   onClose,   onEnterGroup,  onLeaveGroup,  onDismissGroup }) => {  const isOwner = group.selfInfo?.role === GroupMemberRole.OWNER; // group owner  const isAdmin = group.selfInfo?.role === GroupMemberRole.ADMIN; // admin  return (    <div style={{ padding: '20px', border: '1px solid #e0e0e0', borderRadius: '8px' }}>      <div style={{ display: 'flex', alignItems: 'center', marginBottom: '16px' }}>        <img           src={group.avatar}           alt="group avatar"           style={{ width: '60px', height: '60px', borderRadius: '8px', marginRight: '16px' }}        />        <div>          <h3 style={{ margin: '0 0 4px 0' }}>{group.name}</h3>          <p style={{ margin: '0', color: '#666' }}>            Group ID: {group.groupID}          </p>        </div>      </div>            <div style={{ display: 'flex', flexDirection: 'column', gap: '10px',  marginBottom: '16px' }}>        <p><strong>Group introduction:</strong> {group.introduction}</p>        <p><strong>Group notice:</strong> {group.notification}</p>        <p><strong>Member count:</strong> {group.memberCount}/{group.maxMemberCount}</p>        <p><strong>My role:</strong> {          isOwner ? 'group owner' : isAdmin ? 'admin' : 'ordinary member'        }</p>      </div>      {showActions && (        <div style={{ display: 'flex', gap: '8px' }}>          <Button onClick={() => onEnterGroup?.(group)}>Enter group</Button>          <Button onClick={() => onLeaveGroup?.(group)}>Exit group</Button>          {isOwner && (            <Button onClick={() => onDismissGroup?.(group)}>Dissolve group</Button>          )}          <Button onClick={onClose}>Close</Button>        </div>      )}    </div>  );};function CustomGroupInfoDemo() {  const groupData = {    type: ContactItemType.GROUP,    data: {      groupID: 'group123',      name: 'technical exchange group',      avatar: 'https://example.com/group-avatar.jpg',      type: 'Public',      introduction: 'technical exchange and sharing',      notification: 'Welcome to join the technical exchange group',      ownerID: 'owner123',      memberCount: 100,      maxMemberCount: 200,      selfInfo: {        userID: 'currentUser',        role: GroupMemberRole.OWNER, // group owner        nameCard: 'group owner',        joinTime: Date.now(),      },    },  };  return (    <ContactInfo       contactItem={groupData}      GroupInfoComponent={CustomGroupInfo}      onEnterGroup={(group) => console.log('Enter group:', group.name)}      onLeaveGroup={(group) => console.log('Exit group:', group.name)}      onDismissGroup={(group) => console.log('Dissolve group:', group.name)}    />  );}
```

Результат показан ниже.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/3d17ba45679511f0b5365254001c06ec.png)

```
import React from 'react';import { ContactInfo } from '@tencentcloud/uikit-component-react';import type { BlacklistInfoProps, UserProfile } from '@tencentcloud/uikit-component-react';import { Button } from '@tencentcloud/uikit-base-component-react';// Custom Blocklist Information Componentconst CustomBlacklistInfo: React.FC<BlacklistInfoProps> = ({   profile,   showActions,   onClose,   onRemoveFromBlacklist }) => {  return (    <div style={{ padding: '20px', border: '1px solid #e0e0e0', borderRadius: '8px' }}>      <div style={{ display: 'flex', alignItems: 'center', marginBottom: '16px' }}>        <img           src={profile.src}           alt="avatar"           style={{ width: '60px', height: '60px', borderRadius: '50%', marginRight: '16px' }}        />        <div>          <h3 style={{ margin: '0 0 4px 0', color: '#ff4d4f' }}>{profile.nick}</h3>          <p style={{ margin: '0', color: '#666' }}>uid: {profile.userID}</p>        </div>      </div>            <div style={{ display: 'flex', flexDirection: 'column', gap: '10px',  marginBottom: '16px' }}>        <p><strong>Personal signature:</strong> {profile.selfSignature}</p>        <p><strong>Location:</strong> {profile.location}</p>        <p style={{ color: '#ff4d4f', fontWeight: 'bold' }}>          This user has been added to the blocklist        </p>      </div>      {showActions && (        <div style={{ display: 'flex', gap: '8px' }}>          <Button             onClick={() => onRemoveFromBlacklist?.(profile)}            style={{ backgroundColor: '#52c41a', color: 'white', border: 'none' }}          >            Move from blocklist          </Button>          <Button onClick={onClose}>Close</Button>        </div>      )}    </div>  );};function CustomBlacklistInfoDemo() {  const blacklistData = {    type: ContactItemType.BLACK,    data: {      userID: 'user456',      nick: 'Li Si',      src: 'https://example.com/avatar2.jpg',      gender: 1,      birthday: 19920101,      location: 'Shenzhen',      selfSignature: 'blocklisted user',      allowType: 1,      adminForbidType: 0,    },  };  return (    <ContactInfo       contactItem={blacklistData}      BlacklistInfoComponent={CustomBlacklistInfo}      onRemoveFromBlacklist={(profile) => console.log('Removing from blocklist:', profile.nick)}    />  );}
```

Результат показан ниже.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/410ce2c7679511f0837f525400454e06.png)

```
import React from 'react';import { ContactInfo } from '@tencentcloud/uikit-component-react';import type { FriendApplicationInfoProps, FriendApplication } from '@tencentcloud/uikit-component-react';import { Button } from '@tencentcloud/uikit-base-component-react';// Custom Friend Request Information Componentconst CustomFriendApplicationInfo: React.FC<FriendApplicationInfoProps> = ({   application,   showActions,   onClose,   onAccept,  onRefuse }) => {  const formatTime = (timestamp: number) => {    return new Date(timestamp).toLocaleString();  };  return (    <div style={{ padding: '20px', border: '1px solid #e0e0e0', borderRadius: '8px' }}>      <div style={{ display: 'flex', alignItems: 'center', marginBottom: '16px' }}>        <img           src={application.src}           alt="avatar"           style={{ width: '60px', height: '60px', borderRadius: '50%', marginRight: '16px' }}        />        <div>          <h3 style={{ margin: '0 0 4px 0' }}>{application.nick}</h3>          <p style={{ margin: '0', color: '#666' }}>Application time: {formatTime(application.time)}</p>        </div>      </div>            <div style={{ display: 'flex', flexDirection: 'column', gap: '10px',  marginBottom: '16px' }}>        <p><strong>Application source:</strong> {application.source}</p>        <p><strong>Remarks:</strong> {application.wording}</p>        <p style={{ color: '#1890ff', fontWeight: 'bold' }}>          Friend request        </p>      </div>      {showActions && (        <div style={{ display: 'flex', gap: '8px' }}>          <Button             onClick={() => onAccept?.(application)}            style={{ backgroundColor: '#52c41a', color: 'white', border: 'none' }}          >            accept application          </Button>          <Button             onClick={() => onRefuse?.(application)}            style={{ backgroundColor: '#ff4d4f', color: 'white', border: 'none' }}          >            reject application          </Button>          <Button onClick={onClose}>Close</Button>        </div>      )}    </div>  );};function CustomFriendApplicationInfoDemo() {  const applicationData = {    type: ContactItemType.FRIEND_REQUEST,    data: {      userID: 'user789',      nick: 'Wang Wu',      src: 'https://example.com/avatar3.jpg',      time: Date.now(),      source: 'search add',      wording: 'hello, i want to add you as a friend to discuss technology together',      type: 1,    },  };  return (    <ContactInfo       contactItem={applicationData}      FriendApplicationInfoComponent={CustomFriendApplicationInfo}      onFriendApplicationAction={(action, application) => {        if (action === 'accept') {          console.log('Accept friend request:', application.nick);        } else {          console.log('Refuse friend application:', application.nick);        }      }}    />  );}
```

Результат показан ниже.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/3d12304b679511f0bd33525400e889b2.png)

```
import React from 'react';import { ContactInfo } from '@tencentcloud/uikit-component-react';import type { GroupApplicationInfoProps, GroupApplication } from '@tencentcloud/uikit-component-react';import { Button } from '@tencentcloud/uikit-base-component-react';// Custom Group Application Information Componentconst CustomGroupApplicationInfo: React.FC<GroupApplicationInfoProps> = ({   application,   showActions,   onClose,   onAccept,  onRefuse }) => {  const getApplicationTypeText = (type: number) => {    return type === 0 ? 'user application to join' : 'invite user joined';  };  return (    <div style={{ padding: '20px', border: '1px solid #e0e0e0', borderRadius: '8px' }}>      <div style={{ display: 'flex', alignItems: 'center', marginBottom: '16px' }}>        <div style={{ width: '60px', height: '60px', borderRadius: '8px', marginRight: '16px', backgroundColor: '#f0f0f0', display: 'flex', alignItems: 'center', justifyContent: 'center' }}>          ð¥        </div>        <div>          <h3 style={{ margin: '0 0 4px 0' }}>{application.groupName}</h3>          <p style={{ margin: '0', color: '#666' }}>            {getApplicationTypeText(application.applicationType)}          </p>        </div>      </div>             <div style={{ display: 'flex', flexDirection: 'column', gap: '10px',  marginBottom: '16px' }}>        <p><strong>Applicant:</strong> {application.applicantNick}</p>        <p><strong>Group ID:</strong> {application.groupID}</p>        <p><strong>Application remarks:</strong> {application.note}</p>        <p style={{ color: '#1890ff', fontWeight: 'bold' }}>          Group request pending        </p>      </div>      {showActions && (        <div style={{ display: 'flex', gap: '8px' }}>          <Button             onClick={() => onAccept?.(application)}            style={{ backgroundColor: '#52c41a', color: 'white', border: 'none' }}          >            Approving Applications          </Button>          <Button             onClick={() => onRefuse?.(application)}            style={{ backgroundColor: '#ff4d4f', color: 'white', border: 'none' }}          >            reject application          </Button>          <Button onClick={onClose}>Close</Button>        </div>      )}    </div>  );};function CustomGroupApplicationInfoDemo() {  const applicationData = {    type: ContactItemType.GROUP_REQUEST,    data: {      applicant: 'user999',      applicantNick: 'Zhao Liu',      groupID: 'group456',      groupName: 'product manager communication group',      applicationType: 0,      userID: 'user999',      note: 'I want to join the product manager communication group to learn product design experience',    },  };  return (    <ContactInfo       contactItem={applicationData}      GroupApplicationInfoComponent={CustomGroupApplicationInfo}      onGroupApplicationAction={(action, application) => {        if (action === 'accept') {          console.log('Approve group request:', application.groupName);        } else {          console.log('Reject group request:', application.groupName);        }      }}    />  );}
```

Результат показан ниже.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/3d42e3cb679511f08e915254007c27c5.png)

##


---
*Источник: [https://trtc.io/document/72203](https://trtc.io/document/72203)*

---
*Источник (EN): [contactlist.md](./contactlist.md)*
