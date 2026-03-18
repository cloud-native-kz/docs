# C2CSettingState

## Введение

`C2CSettingState` — это центр управления статусом, связанный с персональными настройками, специализирующийся на управлении статусом и операциями настроек чата 1v1 (C2C). Он обеспечивает управление информацией о пользователе, контроль параметров чата, запросы отношений дружбы и другие функции, служа основным инструментом для создания интерфейса настроек чата один-на-один.

`C2CSettingState` может автоматически отслеживать изменения в текущей сессии. При входе в сессию C2C он автоматически получает информацию о пользователе и параметры чата другой стороны, предоставляя удобные операции для изменения настроек закрепления, режима «Не беспокоить», заметок и других параметров.

## Список атрибутов

| Поле | Тип | Описание |
| --- | --- | --- |
| userID | string \| undefined | ID пользователя другой стороны |
| nick | string \| undefined | Никнейм другой стороны |
| avatar | string \| undefined | URL фотографии профиля другой стороны |
| signature | string \| undefined | Личная подпись другой стороны |
| remark | string \| undefined | Имя заметки о другой стороне |
| isMuted | boolean \| undefined | Установлен ли режим «Не беспокоить» |
| isPinned | boolean \| undefined | Закрепить чат наверху |
| isContact | boolean \| undefined | Есть ли отношение дружбы |
| setChatPinned | (value: boolean) => void | Метод установки статуса закрепления чата |
| setChatMuted | (value: boolean) => void | Метод установки статуса «Не беспокоить» |
| setUserRemark | (remark: string) => void | Метод установки заметки пользователя |

## Подробности атрибутов

### userID

- **Тип**: `string | undefined`
- **Описание**: Уникальный идентификатор другой стороны в текущей сессии C2C. Когда сессия C2C отсутствует или загружается, значение `undefined`.

### nick

- **Тип**: `string | undefined`
- **Описание**: Никнейм другой стороны. Если пользователь не установил никнейм или информация не загружена, значение `undefined`.

### avatar

- **Тип**: `string | undefined`
- **Описание**: URL изображения аватара другой стороны. Используется для отображения фотографии профиля пользователя. Если пользователь не установил аватар или информация не загружена, значение `undefined`.

### signature

- **Тип**: `string | undefined`
- **Описание**: Личная подпись другой стороны. Отображает статус или настроение пользователя. Если пользователь не установил подпись или информация не загружена, значение `undefined`.

### remark

- **Тип**: `string | undefined`
- **Описание**: Имя заметки, установленное текущим пользователем для другой стороны. Имя заметки обычно имеет приоритет над отображением никнейма для персонализированной идентификации контактов. Если заметка не установлена, значение `undefined`.

### isMuted

- **Тип**: `boolean | undefined`
- **Описание**: Установлен ли режим «Не беспокоить» для текущей сессии. Когда значение `true`, уведомления о сообщениях для этой сессии не будут получены; когда значение `false`, уведомления получаются нормально; когда значение `undefined`, статус еще не подтвержден.

### isPinned

- **Тип**: `boolean | undefined`
- **Описание**: Закреплена ли текущая сессия наверху. Когда значение `true`, сессия будет отображаться в верхней части списка сессий; когда значение `false`, она будет упорядочена в обычном порядке; когда значение `undefined`, статус еще не подтвержден.

### isContact

- **Тип**: `boolean | undefined`
- **Описание**: Является ли другая сторона контактом текущего пользователя. Когда значение `true`, это означает, что обе стороны являются взаимными контактами; когда значение `false`, это означает, что нет; когда значение `undefined`, запрос отношения дружбы еще не завершен.

### setChatPinned

- **Тип**: `(value: boolean) => void`
- **Описание**: Метод для установки статуса закрепления чата. Введите `true` для закрепления беседы наверху, введите `false` для открепления. Этот метод автоматически вызовет базовый API и обновит статус.

### setChatMuted

- **Тип**: `(value: boolean) => void`
- **Описание**: Метод для установки статуса «Не беспокоить». Введите `true` для включения режима «Не беспокоить», введите `false` для его отключения. Этот метод автоматически вызовет базовый API и обновит статус.

### setUserRemark

- **Тип**: `(remark: string) => void`
- **Описание**: Метод для установки заметки пользователя. Введите новое имя заметки для обновления заметки пользователя другой стороны. Этот метод автоматически вызовет API сервиса контактов и обновит статус.

## Примеры использования

Вот полный пример компонента C2CSettingPanel, который показывает, как использовать различные поля для создания панели настроек чата C2C:

```
import React, { useState } from 'react';import { useC2CSettingState } from './states/C2CSettingState/C2CSettingState';interface C2CSettingPanelProps {  className?: string;  onClose?: () => void;}const C2CSettingPanel: React.FC<C2CSettingPanelProps> = ({ className, onClose }) => {  const {    userID,    nick,    avatar,    signature,    remark,    isMuted,    isPinned,    isContact,    setChatPinned,    setChatMuted,    setUserRemark,  } = useC2CSettingState();  const [isEditingRemark, setIsEditingRemark] = useState(false);  const [remarkInput, setRemarkInput] = useState('');  // start edit remarks  const handleEditRemark = () => {    setRemarkInput(remark || nick || '');    setIsEditingRemark(true);  };  // save remark  const handleSaveRemark = () => {    if (remarkInput.trim() !== remark) {      setUserRemark(remarkInput.trim());    }    setIsEditingRemark(false);  };  // cancel edit remarks  const handleCancelEditRemark = () => {    setIsEditingRemark(false);    setRemarkInput('');  };  // Toggle pinned status  const handleTogglePinned = () => {    setChatPinned(!isPinned);  };  // Toggle Do Not Disturb status  const handleToggleMuted = () => {    setChatMuted(!isMuted);  };  if (!userID) {    return (      <div className={`c2c-setting-panel ${className || ''}`}>        <div className="no-conversation">          Select one C2C session        </div>      </div>    );  }  return (    <div className={`c2c-setting-panel ${className || ''}`}>      {/* header */}      <div className="panel-header">        <h3>Chat Settings</h3>        {onClose && (          <button className="close-btn" onClick={onClose}>            Ã          </button>        )}      </div>      {/* User information area */}      <div className="user-info-section">        <div className="user-avatar">          {avatar ? (            <img src={avatar} alt="user profile photo" />          ) : (            <div className="default-avatar">              {nick?.charAt(0) || userID?.charAt(0) || '?'}            </div>          )}        </div>        <div className="user-details">          <div className="user-name">            {remark || nick || userID}            {remark && nick && remark !== nick && (              <span className="original-nick">({nick})</span>            )}          </div>                    <div className="user-id">ID: {userID}</div>                    {signature && (            <div className="user-signature">{signature}</div>          )}                    <div className="friend-status">            {isContact === true && (              <span className="friend-badge">friend</span>            )}            {isContact === false && (              <span className="stranger-badge">stranger</span>            )}          </div>        </div>      </div>      {/* remark settings */}      <div className="setting-section">        <h4>remark settings</h4>        <div className="setting-item">          {isEditingRemark ? (            <div className="remark-edit">              <input                type="text"                value={remarkInput}                onChange={e => setRemarkInput(e.target.value)}                placeholder="Enter remark name"                className="remark-input"                autoFocus              />              <div className="edit-actions">                <button onClick={handleSaveRemark} className="save-btn">                  Save                </button>                <button onClick={handleCancelEditRemark} className="cancel-btn">                  Cancel                </button>              </div>            </div>          ) : (            <div className="remark-display">              <span className="remark-text">                {remark || 'No remark set'}              </span>              <button onClick={handleEditRemark} className="edit-btn">                Edit              </button>            </div>          )}        </div>      </div>      {/* Chat Settings */}      <div className="setting-section">        <h4>Chat Settings</h4>                <div className="setting-item">          <div className="setting-label">            <span>Pin chat</span>            <p className="setting-desc">When pinned to top, this chat will be displayed in list top</p>          </div>          <div className="setting-control">            <label className="toggle-switch">              <input                type="checkbox"                checked={isPinned || false}                onChange={handleTogglePinned}              />              <span className="slider"></span>            </label>          </div>        </div>        <div className="setting-item">          <div className="setting-label">            <span>Do not disturb</span>            <p className="setting-desc">No push notifications will be received for this chat when turned on</p>          </div>          <div className="setting-control">            <label className="toggle-switch">              <input                type="checkbox"                checked={isMuted || false}                onChange={handleToggleMuted}              />              <span className="slider"></span>            </label>          </div>        </div>      </div>      {/* other operations */}      <div className="setting-section">        <h4>Other operations</h4>        <div className="action-buttons">          {isContact && (            <button className="action-btn delete-friend danger">              Remove friend            </button>          )}        </div>      </div>    </div>  );};export default C2CSettingPanel;
```

Результат рендеринга показан ниже:

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/5bb75c48617a11f0b324525400e889b2.png)

### Справочник по стилям

```
.c2c-setting-panel {  width: 300px;  height: 100%;  background: white;  border-left: 1px solid #e5e5e5;  display: flex;  flex-direction: column;    .no-conversation {    flex: 1;    display: flex;    align-items: center;    justify-content: center;    color: #999;    font-size: 14px;  }    .panel-header {    display: flex;    align-items: center;    justify-content: space-between;    padding: 15px 20px;    border-bottom: 1px solid #e5e5e5;        h3 {      margin: 0;      font-size: 16px;      font-weight: 500;    }        .close-btn {      background: none;      border: none;      font-size: 20px;      cursor: pointer;      color: #999;            &:hover {        color: #333;      }    }  }    .user-info-section {    padding: 20px;    border-bottom: 1px solid #f0f0f0;    display: flex;    gap: 15px;        .user-avatar {      flex-shrink: 0;            img, .default-avatar {        width: 60px;        height: 60px;        border-radius: 50%;      }            img {        object-fit: cover;      }            .default-avatar {        background: #e5e5e5;        display: flex;        align-items: center;        justify-content: center;        font-size: 24px;        font-weight: 500;        color: #999;      }    }        .user-details {      flex: 1;            .user-name {        font-size: 16px;        font-weight: 500;        margin-bottom: 5px;                .original-nick {          color: #999;          font-weight: normal;          margin-left: 5px;        }      }            .user-id {        font-size: 12px;        color: #999;        margin-bottom: 8px;      }            .user-signature {        font-size: 14px;        color: #666;        margin-bottom: 8px;        line-height: 1.4;      }            .friend-status {        .friend-badge, .stranger-badge {          display: inline-block;          padding: 2px 6px;          border-radius: 10px;          font-size: 12px;        }                .friend-badge {          background: #e8f5e8;          color: #52c41a;        }                .stranger-badge {          background: #fff2e8;          color: #fa8c16;        }      }    }  }    .setting-section {    padding: 20px;    border-bottom: 1px solid #f0f0f0;        h4 {      margin: 0 0 15px 0;      font-size: 14px;      font-weight: 500;      color: #333;    }        .setting-item {      display: flex;      align-items: center;      justify-content: space-between;      margin-bottom: 15px;            &:last-child {        margin-bottom: 0;      }            .setting-label {        flex: 1;                span {          font-size: 14px;          color: #333;        }                .setting-desc {          margin: 2px 0 0 0;          font-size: 12px;          color: #999;        }      }            .setting-control {        flex-shrink: 0;      }    }        .remark-edit {      width: 100%;            .remark-input {        width: 100%;        padding: 8px 12px;        border: 1px solid #d9d9d9;        border-radius: 4px;        font-size: 14px;        margin-bottom: 10px;                &:focus {          outline: none;          border-color: #1890ff;        }      }            .edit-actions {        display: flex;        gap: 10px;                button {          flex: 1;          padding: 6px 12px;          border-radius: 4px;          font-size: 12px;          cursor: pointer;        }                .save-btn {          background: #1890ff;          color: white;          border: none;                    &:hover {            background: #40a9ff;          }        }                .cancel-btn {          background: white;          color: #666;          border: 1px solid #d9d9d9;                    &:hover {            border-color: #40a9ff;            color: #40a9ff;          }        }      }    }        .remark-display {      display: flex;      align-items: center;      justify-content: space-between;      width: 100%;            .remark-text {        font-size: 14px;        color: #333;      }            .edit-btn {        background: none;        border: none;        color: #1890ff;        font-size: 12px;        cursor: pointer;                &:hover {          color: #40a9ff;        }      }    }        .action-buttons {      display: flex;      flex-direction: column;      gap: 10px;            .action-btn {        padding: 10px;        border: 1px solid #d9d9d9;        border-radius: 4px;        background: white;        cursor: pointer;        font-size: 14px;                &:hover {          border-color: #40a9ff;          color: #40a9ff;        }                &.danger {          border-color: #ff4d4f;          color: #ff4d4f;                    &:hover {            background: #ff4d4f;            color: white;          }        }      }    }  }    // Toggle switch styles  .toggle-switch {    position: relative;    display: inline-block;    width: 44px;    height: 24px;        input {      opacity: 0;      width: 0;      height: 0;    }        .slider {      position: absolute;      cursor: pointer;      top: 0;      left: 0;      right: 0;      bottom: 0;      background-color: #ccc;      transition: .4s;      border-radius: 24px;            &:before {        position: absolute;        content: "";        height: 18px;        width: 18px;        left: 3px;        bottom: 3px;        background-color: white;        transition: .4s;        border-radius: 50%;      }    }        input:checked + .slider {      background-color: #1890ff;    }        input:checked + .slider:before {      transform: translateX(20px);    }  }}
```

## Ключевые моменты использования

Этот пример показывает, как:

1. **Отображение информации о пользователе** - используйте поля такие как `userID`, `nick`, `avatar` и `signature` для отображения полной информации о пользователе.
2. **Флаг отношения дружбы** - отобразите статус дружбы через поле `isContact`.
3. **Управление заметками** - используйте поле `remark` для отображения текущей заметки и изменения через метод `setUserRemark`.
4. **Контроль настроек чата** - используйте поля `isPinned` и `isMuted` для управления статусом закрепления наверху и режима «Не беспокоить».
5. **Интерактивная операция** - реализуйте переключатель через методы `setChatPinned` и `setChatMuted`.
6. **Обработка статуса** - правильно обрабатывайте статус `undefined` полей для обеспечения хорошего пользовательского опыта.


---
*Источник: [https://trtc.io/document/72095](https://trtc.io/document/72095)*

---
*Источник (EN): [c2csetting-state.md](./c2csetting-state.md)*
