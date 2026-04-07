# AI Субтитры в Реальном Времени

## Введение в функцию

После входа в TUIRoomKit вы можете включить функцию AI субтитров в реальном времени, нажав на «AI Помощник» в нижней панели:

- **AI субтитры в реальном времени:** Отображение обсуждения во время встречи в виде субтитров.
- **AI запись встречи в реальном времени:** Письменная запись обсуждаемого материала во время встречи.

> **Примечание:** [Требуется подписка TUIRoomKit на месяц](https://www.tencentcloud.com/document/product/647/59973) для использования этой функции. Помимо обычных расходов на вызовы ([инструкции по почасовому счету за аудио и видео](https://www.tencentcloud.com/document/product/647/42734)); эта функция будет взимать дополнительные сборы за распознавание ИИ за преобразование речи в текст, подробнее см. [инструкции по выставлению счетов за распознавание ИИ](https://www.tencentcloud.com/document/product/647/67832).

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/cc736bbef12e11f09d62525400ecee81.png)

## Доступ к функции

### Шаг 1: Запустите локальный внутренний сервис

> **Примечание:** Открытие транскрипции ИИ требует использования облачного ID и ключа пользователя, что является конфиденциальным, поэтому не интегрируйте этот интерфейс в клиент, вам нужно добавить код, связанный с StartAITranscription в вашу собственную деловую фоновую часть. Здесь приводится пример с использованием сервиса Nodejs.

Откройте внутренний сервис Nodejs, клиент прослушивает вход пользователя в комнату и открывает задачу транскрипции ИИ через HTTP-запрос, пример кода: [нажмите для загрузки](https://web.sdk.qcloud.com/trtc/AITask/server.zip).

```
require('dotenv').config();const express = require('express');const tencentcloud = require('tencentcloud-sdk-nodejs-trtc');const cors = require('cors')const TrtcClient = tencentcloud.trtc.v20190722.Client;// Get the Tencent Cloud account SecretId and SecretKey from the environment variable// You need to pass the Tencent Cloud account SecretId and SecretKey into the entry parameter, and you also need to pay attention to the confidentiality of the key pair here.// Code leaks can lead to SecretId and SecretKey leaks and threaten the security of all resources under the account.// The following code example is for reference only, a more secure way of using the key is recommended, see: https://cloud.tencent.com/document/product/1278/85305// The key can be obtained by going to the official console at https://console.cloud.tencent.com/cam/capi.const secretId = process.env.TENCENT_SECRET_ID || '';const secretKey = process.env.TENCENT_SECRET_KEY || '';const region = process.env.TENCENT_REGION || '';const clientConfig = {  credential: {    secretId: secretId,    secretKey: secretKey,  },  region: region,  profile: {    httpProfile: {      endpoint: 'trtc.tencentcloudapi.com',    },  },};const client = new TrtcClient(clientConfig);const app = express();app.use(express.json());app.use(cors());app.post('/start', async (req, res) => {  const { SdkAppId, RoomId, RoomIdType = 1, UserId, UserSig } = req.body;  const params = {    SdkAppId: SdkAppId,    RoomId: RoomId,    RoomIdType: RoomIdType,    TranscriptionParams: {      UserId: UserId,      UserSig: UserSig,    },  };  try {    const data = await client.StartAITranscription(params);    console.log('success',data)    res.status(200).json(data);  } catch (err) {    console.error('error', err);    res.status(500).json({ error: err.message });  }});app.post('/stop', async (req, res) => {  const { TaskId } = req.body;  try {    const data = await client.StopAITranscription({ TaskId: TaskId });    res.status(200).json(data);  } catch (err) {    console.error('error', err);    res.status(500).json({ error: err.message });  }});const port = process.env.PORT || 3000;app.listen(port, () => {  console.log(`Server is running on port ${port}`);});
```

### Шаг 2: RoomKit включает AI Помощника

> **Примечание:** RoomKit только обрабатывает данные для подписей ИИ/записи встреч, фактическое распознавание речи включается, когда пользователь клиента входит в комнату, здесь вы можете отрегулировать время в зависимости от потребностей вашего бизнеса.

```
<template>  <conference-main-view display-mode="permanent"></conference-main-view></template><script setup lang="ts">import { roomService } from '@tencentcloud/roomkit-web-vue3';// Called before the conference-main-view component is onmounted.roomService.setComponentConfig({ AIControl: { visible: true } });</script>
```

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/f709ab3c0aeb11f0b3015254001c06ec.png)

### Шаг 3: RoomKit прослушивает вход пользователя в комнату и вызывает сервис node для включения транскрипции ИИ.

```
<template>  <conference-main-view display-mode="permanent"></conference-main-view></template><script setup lang="ts">import { conference } from '@tencentcloud/roomkit-web-vue3';import { startAITranscription } from '../http';const handleAITask = (data: {roomId: string}) => {  const { roomId } = data;  startAITranscription({    RoomId: roomId,    UserId: 'robot', // A robot user is required here, in the case of robot, this should not be the same as the userId of the user in the room, it is recommended to use robot.    UserSig: 'xxx', // The userSig of the robot    SdkAppId: sdkAppId,    RoomIdType: 1, // Room type is string room  });};conference.on(RoomEvent.ROOM_JOIN, handleAITask);conference.on(RoomEvent.ROOM_START, handleAITask);onUnmounted(() => {  conference.off(RoomEvent.ROOM_JOIN, handleAITask);  conference.off(RoomEvent.ROOM_START, handleAITask);});</script>
```

```
// http.tsimport axios from 'axios';const http = axios.create({  baseURL: 'http://localhost:3000', // Your Node.js service address.  timeout: 10000, // Request timeout});interface TranscriptionParams {    SdkAppId: number;    RoomId: string;    RoomIdType?: number;    UserId: string;    UserSig: string;  }  interface StopParams {    TaskId: string;  }// Start the AI transcription taskexport function startAITranscription(params: TranscriptionParams) {  return http.post('/start', params);}// Stop the AI transcription taskexport function stopAITranscription(params: StopParams) {  return http.post('/stop', params);}
```

> **Примечание:** Если у вас есть какие-либо вопросы или отзывы о процессе доступа и использования, вы можете связаться с info_rtc@tencent.com.


---
*Источник: [https://trtc.io/document/68951](https://trtc.io/document/68951)*

---
*Источник (EN): [ai-real-time-subtitles.md](./ai-real-time-subtitles.md)*
