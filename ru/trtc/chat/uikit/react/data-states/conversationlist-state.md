# ConversationList State

## Обзор

`ConversationListState` — это основанный на Zustand хук для управления состоянием списка разговоров, обеспечивающий компонент ConversationList полными возможностями управления состоянием. Он управляет данными списка разговоров, активными сеансами, количеством непрочитанных сообщений, статусом сети и предоставляет методы для операций с сеансами.

## Базовое использование

```
import { useConversationListState } from '@tencentcloud/uikit-component-react';function ConversationComponent() {  const {    conversationList,    activeConversation,    totalUnRead,    netStatus,    setActiveConversation,    pinConversation,    deleteConversation,    muteConversation  } = useConversationListState();  return (    <div>      <div>Unread count: {totalUnRead}</div>      <div>Network status: {netStatus}</div>      {conversationList?.map(conversation => (        <div           key={conversation.conversationID}          onClick={() => setActiveConversation(conversation.conversationID)}        >          {conversation.getShowName()}        </div>      ))}    </div>  );}
```

## Порт состояния

### Данные

| Название атрибута | Тип | Обзор |
| --- | --- | --- |
| conversationList | ConversationModel[] \| undefined | Данные списка разговоров |
| activeConversation | ConversationModel \| undefined | Текущий активный сеанс |
| totalUnRead | number | Количество непрочитанных сообщений |
| netStatus | NET_STATE_CONNECTED \| NET_STATE_CONNECTING \| NET_STATE_DISCONNECTED | статус подключения к сети |

### Метод операции

| Название метода | Тип | Обзор |
| --- | --- | --- |
| setActiveConversation | (conversationID: string) => void | Установить текущий активный сеанс |
| createC2CConversation | (userID: string) => Promise | Создать сеанс приватного чата |
| createGroupConversation | (options: CreateGroupParams) => Promise | Создать сеанс группового чата |
| pinConversation | (conversationID: string, isPin: boolean) => Promise | Закрепить/Открепить разговор |
| deleteConversation | (conversationID: string) => Promise | Удалить разговор |
| muteConversation | (conversationID: string, isMute: boolean) => Promise | Включить/Отключить режим "Не беспокоить" |
| setConversationDraft | (options: SetConversationDraftParams) => Promise | Установить черновик сеанса |
| markConversationUnread | (conversationID: string, isUnread: boolean) => void | Отметить разговор как прочитанный/непрочитанный |

## Статус сети

Поддерживаются следующие типы статусов сети:

- `NET_STATE_CONNECTED` — подключено
- `NET_STATE_CONNECTING` — подключение
- `NET_STATE_DISCONNECTED` — отключено

## Примеры использования

### Базовый список сеансов

```
function ConversationList() {  const {    conversationList,    activeConversation,    totalUnRead,    setActiveConversation  } = useConversationListState();  return (    <div className="conversation-list">      <div className="header">        <h3>Conversation list</h3>        {totalUnRead > 0 && (          <span className="unread-badge">{totalUnRead}</span>        )}      </div>      <div className="list">        {conversationList?.map(conversation => (          <div            key={conversation.conversationID}            className={`conversation-item ${              activeConversation?.conversationID === conversation.conversationID                 ? 'active'                 : ''            }`}            onClick={() => setActiveConversation(conversation.conversationID)}          >            <div className="avatar">              <img src={conversation.getAvatar()} alt="avatar" />            </div>            <div className="content">              <div className="name">{conversation.getShowName()}</div>              <div className="last-message">{conversation.lastMessage?.messageForShow}</div>            </div>            {conversation.unreadCount > 0 && (              <div className="unread-count">{conversation.unreadCount}</div>            )}          </div>        ))}      </div>    </div>  );}
```

### 2. Функция действий с разговором

```
function ConversationWithActions() {  const {    conversationList,    pinConversation,    deleteConversation,    muteConversation,    markConversationUnread  } = useConversationListState();  const handlePin = async (conversationID: string, isPin: boolean) => {    try {      await pinConversation(conversationID, isPin);      console.log(`Session ${isPin ? 'pinned to top' : 'unpinned'} successfully`);    } catch (error) {      console.error('Pin to top operation failed:', error);    }  };  const handleDelete = async (conversationID: string) => {    if (confirm('Delete this session?')) {      try {        await deleteConversation(conversationID);        console.log('Session deleted successfully');      } catch (error) {        console.error('Failed to delete conversation:', error);      }    }  };  const handleMute = async (conversationID: string, isMute: boolean) => {    try {      await muteConversation(conversationID, isMute);      console.log(`Session ${isMute ? 'set' : 'cancel'} do not disturb successfully`);    } catch (error) {      console.error('Do Not Disturb setting failed:', error);    }  };  const handleMarkUnread = (conversationID: string, isUnread: boolean) => {    markConversationUnread(conversationID, isUnread);    console.log(`Session tagged as ${isUnread ? 'unread' : 'read'}`);  };  return (    <div>      {conversationList?.map(conversation => (        <div key={conversation.conversationID} className="conversation-item">          <div className="conversation-info">            {conversation.getShowName()}          </div>          <div className="conversation-actions">            <button              onClick={() => handlePin(                conversation.conversationID,                 !conversation.isPinned              )}            >              {conversation.isPinned ? 'unpin' : 'pin to top'}            </button>            <button              onClick={() => handleMute(                conversation.conversationID,                 !conversation.isMuted              )}            >              {conversation.isMuted ? 'Cancel do not disturb' : 'Do not disturb'}            </button>            <button              onClick={() => handleMarkUnread(                conversation.conversationID,                 conversation.unreadCount === 0              )}            >              {conversation.unreadCount > 0 ? 'mark as read' : 'mark as unread'}            </button>            <button              onClick={() => handleDelete(conversation.conversationID)}              className="danger"            >              Delete            </button>          </div>        </div>      ))}    </div>  );}
```

### 3. Функция создания сеанса

```
function ConversationCreator() {  const {    createC2CConversation,    createGroupConversation,    setActiveConversation  } = useConversationListState();  const [userID, setUserID] = useState('');  const [groupName, setGroupName] = useState('');  const [selectedUsers, setSelectedUsers] = useState<string[]>([]);  const handleCreateC2C = async () => {    if (!userID.trim()) {      alert('enter user ID');      return;    }    try {      const conversation = await createC2CConversation(userID);      setActiveConversation(conversation.conversationID);      console.log('Private chat created successfully:', conversation.conversationID);      setUserID('');    } catch (error) {      console.error('Create private chat failed:', error);    }  };  const handleCreateGroup = async () => {    if (!groupName.trim()) {      alert('enter group name');      return;    }    if (selectedUsers.length === 0) {      alert('select group member');      return;    }    try {      const groupParams: CreateGroupParams = {        name: groupName,        memberList: selectedUsers.map(userID => ({ userID })),        type: 'Work', // Work group      };      const conversation = await createGroupConversation(groupParams);      setActiveConversation(conversation.conversationID);      console.log('Group chat created successfully:', conversation.conversationID);      setGroupName('');      setSelectedUsers([]);    } catch (error) {      console.error('Create group chat failed:', error);    }  };  return (    <div className="conversation-creator">      <div className="create-c2c">        <h4>Create private chat</h4>        <input          type="text"          value={userID}          onChange={(e) => setUserID(e.target.value)}          placeholder="enter user ID"        />        <button onClick={handleCreateC2C}>Create private chat</button>      </div>      <div className="create-group">        <h4>Create group chat</h4>        <input          type="text"          value={groupName}          onChange={(e) => setGroupName(e.target.value)}          placeholder="enter group name"        />        <div className="member-selector">          <select components>        </div>        <button onClick={handleCreateGroup}>Create group chat</button>      </div>    </div>  );}
```

### 4. Функция черновика разговора

```
function ConversationDraft() {  const { setConversationDraft, activeConversation } = useConversationListState();  const [draftContent, setDraftContent] = useState('');  const saveDraft = async () => {    if (!activeConversation) {      alert('Please select first a session');      return;    }    try {      await setConversationDraft({        conversationID: activeConversation.conversationID,        draftText: draftContent      });      console.log('Draft saved successfully');    } catch (error) {      console.error('Draft saving failed:', error);    }  };  return (    <div className="conversation-draft">      <textarea        value={draftContent}        onChange={(e) => setDraftContent(e.target.value)}        placeholder="enter draft content..."      />      <button onClick={saveDraft}>Save draft</button>    </div>  );}
```


---
*Источник: [https://trtc.io/document/64704](https://trtc.io/document/64704)*

---
*Источник (EN): [conversationlist-state.md](./conversationlist-state.md)*
