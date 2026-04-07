# Обработка ограничений брандмауэра

В этом руководстве рассматриваются лучшие практики работы с ограничениями брандмауэра. Например, в сетевой среде с брандмауэром, таком как корпоративная интрасеть, TRTC Web SDK не может работать нормально из-за ограничений брандмауэра. В этом случае существует два решения:

- **Решение 1**: Отслеживайте ошибки SDK и направляйте пользователей на изменение сети или настройку белого списка брандмауэра.
- **Решение 2**: Используйте решение прокси Nginx + coturn.

> **Примечание**TRTC Web SDK по умолчанию использует UDP для передачи медиаданных на сервер TRTC и имеет встроенный Turn Server, поддерживающий передачу медиаданных через UDP или TCP. В общедоступной сети пользователи не должны устанавливать прокси-серверы, так как SDK попытается установить медиасоединение в следующем порядке: прямое соединение, Turn Server UDP и Turn Server TCP. Если известно, что пользователь будет использовать SDK во внутренней сетевой интрасети, может быть невозможно установить медиасоединение, и потребуется настройка прокси-сервера.

## Решение 1

Это решение подходит в том случае, если вы не можете подтвердить, будет ли сеть пользователя ограничена брандмауэром. В этом случае вы можете отслеживать ошибки SDK и направлять пользователей на изменение сети или проверку брандмауэра.

При вызове таких API как startLocalVideo, startLocalAudio, startRemoteVideo и т. д. SDK внутренне устанавливает канал медиасоединения для передачи медиаданных. При возникновении ограничений брандмауэра SDK может не установить соединение, и SDK выдаст ошибку ограничения брандмауэра и будет продолжать повторные попытки.

Вы можете ссылаться на следующий пример кода для отслеживания этой ошибки и направления пользователей на изменение сети или проверку параметров брандмауэра сети и добавление доменов и портов, используемых TRTC Web SDK, в белый список.

```
trtc.on(TRTC.EVENT.ERROR, error => {  // User network firewall restrictions may cause audio and video calls to fail.  // At this time, guide users to change networks or check network firewall settings.  if (error.code === TRTC.ERROR_CODE.OPERATION_FAILED && error.extraCode === 5501) {      }});
```

### Какие порты и имена доменов я должен добавить в белый список брандмауэра для WebRTC?

Добавьте следующие порты в белый список

| WebRTC (H5) | Порты |
| --- | --- |
| TCP | 443 |
| UDP | 8000, 8080, 8800, 843, 443, 16285 |

Добавьте следующие имена доменов в белый список

```
apisgp.my-imcloud.com# version after v5.5.0*.rtc-web.com*.rtc-web.io# version before v5.5.0signailing.rtc.tencentcloud.comschedule.rtc.tencentcloud.com*.rtc.tencentcloud.com
```

## Решение 2

Это решение подходит в том случае, если вы подтверждаете, что сеть пользователя ограничена брандмауэром, и вам необходимо установить прокси-сервер для решения проблемы.

Это решение требует развертывания двух серверов: Nginx + Turn Server. Вы можете связаться с коллегами по эксплуатации вашей компании для оказания помощи в построении. Прокси-сервер Nginx используется для проксирования пакетов сигнализации Websocket TRTC Web SDK. Turn Server используется для передачи медиаданных.

| Решение | Применимые сценарии | Требования к сети |
| --- | --- | --- |
| A | Пользователи могут получать доступ к определенному внешнему прокси-серверу в сети | Прокси-сервер развернут во внешней сети, и во внутреннем сетевом брандмауэре необходимо открыть белый список для разрешения доступа пользователей внутренней сети к внешнему прокси-серверу. |
| B | Пользователи могут получать доступ только к прокси-серверу внутренней сети | Прокси-сервер развернут во внутренней сети, и во внутреннем сетевом брандмауэре необходимо открыть белый список для разрешения прокси-серверу внутренней сети доступа во внешнюю сеть. |

![Figure 2-A](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/086a8647e5bc11ee9ca3525400bb593a.png)

![Figure 2-B](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/0b8f19bfe5bc11eeb1eb525400b5f95f.png)

### Решение 2-A

#### Настройка сервера Nginx

1. Развертывание сервера Nginx

Обратитесь к руководству по развертыванию сервера Nginx, которое вы найдете в Интернете, для развертывания. Если на предприятии уже развернута служба Nginx, ее можно настроить непосредственно.

2. Настройка сервера Nginx.

```
vi /etc/nginx/nginx.conf
```

```
http {  server {     # The access domain name of the Nginx server    server_name proxy.example.com;     # The access port of the Nginx server    listen 443;     ssl on;     location /ws/ { # Corresponding to the websocketProxy parameter in setProxyServer      proxy_pass https://signaling.rtc.qq.com/; # TRTC server      proxy_http_version 1.1;       proxy_set_header Upgrade $http_upgrade;       proxy_set_header Connection "upgrade";     }    location /logger/ { # Corresponding to the loggerProxy parameter in setProxyServer      proxy_pass https://yun.tim.qq.com/;    }    # SSL certificate corresponding to the domain name, used for HTTPS, users need to apply for it themselves    ssl_certificate ./crt/1_proxy.trtcapi.com_bundle.crt;     ssl_certificate_key ./crt/2_proxy.trtcapi.com.key;   }}
```

3. Перезагрузка Nginx.

```
sudo nginx -s reload
```

4. Убедитесь, что брандмауэр компании разрешает доступ к IP-адресу и порту сервера Nginx.

#### Настройка Turn сервера

Вы можете поискать в Интернете учебные пособия по настройке Turn сервера для установки или использовать следующий скрипт для настройки Turn сервера в **CentOS**.

1. Создайте файл скрипта **turn.sh** на сервере Linux, содержимое скрипта выглядит следующим образом.

```
#!/usr/bin/env bash# current file name is turn.sh# ref:# https://gabrieltanner.org/blog/turn-server    STEP 3 testing turn server# https://medium.com/av-transcode/what-is-webrtc-and-how-to-setup-stun-turn-server-for-webrtc-communication-63314728b9d0# as super-user# usage:  current_program <external-ip>set -xset -eip apwdwhoamidisplay_usage() {        echo "This script must be run with super-user privileges."        echo -e "\\nUsage: $0 <external-ip> \\ne.g. $0 154.8.246.205"}# if less than two arguments supplied, display usageif [ $# -lt 1 ]then        display_usage        exit 1fiif [[ $1 =~ ^[0-9]+\\.[0-9]+\\.[0-9]+\\.[0-9]+$ ]]; then  echo "get external ip $1"else  echo "wrong external ip $1 , must not have whitespace, tab and other char"  exit 2fiyum install -y coturn# $1 is <external-ip>cat <<EOF > /etc/coturn/turnserver.confexternal-ip=$1listening-port=3478lt-cred-mechmax-port=65535min-port=20000no-dtlsno-tlsrealm=tencentuser=turn:turnverboseEOF
```

2. Добавьте разрешение на выполнение.

```
chmod +x turn.sh
```

3. Выполните скрипт от имени root, например:

```
sudo ./turn.sh <server public IP>
```

4. Запустите Turn сервер.

```
systemctl start coturn# Check if turn is started successfullyps aux | grep coturn# If you want to restart the service, executeservice coturn restartÂ
```

5. Настройте брандмауэр для Turn сервера, откройте входящий порт 3478 (TCP и UDP) и исходящие порты (UDP) между минимальным и максимальным портами в приведенной выше конфигурации.
6. Настройте брандмауэр внутренней сети компании, чтобы разрешить доступ к IP-адресу Turn сервера и откройте исходящий порт 3478 (TCP и UDP).
7. Тестирование Turn сервера

Используйте эту [тестовую страницу](https://webrtc.github.io/samples/src/content/peerconnection/trickle-ice/) для проверки доступности Turn сервера. Если результат показывает "done", как показано на скриншоте ниже, Turn сервер работает правильно.

![turn-test](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/70df0db4e5be11ee9f745254008eb8a8.png)

### Решение 2-B

Решение 2-B строится прокси Nginx так же, как Решение 2-A.

Есть два основных отличия:

1. При построении Turn сервера поле external-ip в файле конфигурации должно быть заполнено адресом сервера в вашей корпоративной интрасети.

```
# The start script in Solution 2-A is the server's external address, e.g. 14.3.3.3sudo . /turn.sh 14.3.3.3# In Solution 2-B, the start script fills in the server's intranet address, # e.g. 10.0.0.4 for the intranetsudo . /turn.sh 10.0.0.4
```

2. Конфигурация брандмауэра:
- Для сервера Nginx необходимо настроить белый список имен доменов во внутреннем сетевом брандмауэре компании, чтобы разрешить серверу Nginx доступ к связанным доменам TRTC. Обратитесь к [Белый список](#какие-порты-и-имена-доменов-я-должен-добавить-в-белый-список-брандмауэра-для-webrtc).
- Для Turn Server разрешите Turn Server получать доступ во внешнюю сеть.

### Настройка прокси-сервера для TRTC Web SDK

После установки серверов Nginx и Turn вы можете обратиться к следующему примеру для настройки прокси-сервера.

```
const trtc = TRTC.create(); await trtc.enterRoom({  ...,  proxy: {    // Set up a Websocket proxy to relay signaling data packets between the SDK and the TRTC backend.    websocketProxy: 'wss://proxy.example.com/ws/',    // Set up a turn server to relay media data packets between the SDK and the TRTC backend. 14.3.3.3:3478 is the IP address and port of the turn server.    turnServer: { url: '14.3.3.3:3478', username: 'turn', credential: 'turn', credentialType: 'password' },    // By default, the SDK will connect to trtc server directly, if connection failed, then SDK will try to connect the TURN server to relay the media data. You can set 'relay' to force the connection through the TURN server.    iceTransportPolicy: 'all',     // By default, the SDK reports logs to the yun.tim.qq.com domain name. If this domain name cannot be accessed in your internal network, you need to whitelist the domain name or configure the following log proxy.    // Set up a log reporting proxy. Logs are key data for troubleshooting, so be sure to set up this proxy.    loggerProxy: 'https://proxy.example.com/logger/',  }})
```


---
*Источник: [https://trtc.io/document/59667](https://trtc.io/document/59667)*

---
*Источник (EN): [handle-firewall-restriction.md](./handle-firewall-restriction.md)*
