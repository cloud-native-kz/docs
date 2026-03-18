# Включение эффекта изменения голоса

## Описание функции

Данный документ описывает использование плагина Voice Changer.

## Предварительные требования

- Информация о ценах см. в разделе [RTC-Engine Packages](https://trtc.io/document/56025#f10b65d1-6e8d-41e3-8686-84909b00a1a2).
- Версия TRTC Web SDK ≥ 5.10.
- Поддерживаемые браузеры: Chrome 66+, Edge 79+, Safari 15+, Firefox 76+, Chrome для Android 126+.

## Процесс реализации

### 1. Импорт и регистрация плагина

```
import { VoiceChanger } from 'trtc-sdk-v5/plugins/voice-changer';let trtc = TRTC.create({ plugins: [VoiceChanger] });
```

### 2. Включение микрофона

```
await trtc.startLocalAudio();
```

### 3. Использование плагина Voice Changer

```
await trtc.startPlugin('VoiceChanger', {  voiceType: 1,  sdkAppId: 123456,  userId: 'user_123',  userSig: 'XXXXXXXX'});// Обновление параметров после активацииawait trtc.updatePlugin('VoiceChanger', {  voiceType: 2,});// Отключите плагин перед остановкой микрофонаawait trtc.stopPlugin('VoiceChanger');await trtc.stopLocalAudio();
```

## Справочник API

### trtc.startPlugin('BasicBeauty', options)

Включение эффектов изменения голоса

#### options

| Название | Тип | Атрибуты |
| --- | --- | --- |
| sdkAppId | `number` | sdkAppId текущего приложения |
| userId | `string` | userId текущего пользователя |
| userSig | `string` | userSig текущего пользователя |
| voiceType | `number` | 1: Mischievous Kid 2: Loli 3: Uncle 4: Heavy Metal 5: Cold 6: Foreign Accent 7: Caged Beast 8: Otaku 9: Strong Current 10: Heavy Machinery 11: Ethereal |

**Пример:**

```
await trtc.startLocalAudio();await trtc.startPlugin('VoiceChanger', {  voiceType: 1,  sdkAppId: 123456,  userId: 'user_123',  userSig: 'XXXXXXXX'});
```

### trtc.updatePlugin('VoiceChanger', options)

Изменение эффектов изменения голоса

#### options

| Название | Тип | Атрибуты |
| --- | --- | --- |
| voiceType | `number` | 1: Mischievous Kid 2: Loli 3: Uncle 4: Heavy Metal 5: Cold 6: Foreign Accent 7: Caged Beast 8: Otaku 9: Strong Current 10: Heavy Machinery 11: Ethereal |

**Пример:**

```
await trtc.updatePlugin('VoiceChanger', {  voiceType: 2,});
```

### trtc.stopPlugin('VoiceChanger')

Отключение эффектов изменения голоса

```
// Отключите плагин перед остановкой микрофонаawait trtc.stopPlugin('VoiceChanger');await trtc.stopLocalAudio();
```


---
*Источник: [https://trtc.io/document/69472](https://trtc.io/document/69472)*

---
*Источник (EN): [enable-voice-changer-effect.md](./enable-voice-changer-effect.md)*
