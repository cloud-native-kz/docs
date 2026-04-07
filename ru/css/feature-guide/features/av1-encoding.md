# Кодирование AV1

AOMedia Video 1 (AV1) — это бесплатный формат видеокодирования с открытым исходным кодом. Он кодирует видео со скоростью потока на 30% и более ниже, чем H.265 (HEVC), при этом обеспечивая то же качество видео. Это означает, что при одинаковой пропускной способности видео, закодированное в AV1, имеет более высокое качество, чем видео, закодированное в H.265. В этом документе показано, как кодировать видео с использованием AV1 и как воспроизводить видео, закодированное в AV1.

## Как использовать AV1

### Предварительные требования

- Вы [зарегистрировали учетную запись Tencent Cloud](https://intl.cloud.tencent.com/document/product/378/17985).
- Вы активировали CSS и добавили [домен воспроизведения и домен трансляции](https://intl.cloud.tencent.com/document/product/267/35970).

### Шаг 1. Создание шаблона транскодирования

1. Войдите в консоль CSS и в левой боковой панели выберите **Feature Configuration** > [Live Transcoding](https://console.tencentcloud.com/live/config/transcode).
2. Нажмите **Create template**.

![](https://staticintl.cloudcachetci.com/cms/backend-cms/b15d51582c7c11efb0275254006c0558.png)

3. Выберите тип транскодирования как **Standard Transcoding** или **Top Speed Codec Transcoding**, разверните дополнительную конфигурацию. В разделе Codec выберите **AV1**.

Standard Transcoding

Top Speed Codec Transcoding

![](https://staticintl.cloudcachetci.com/cms/backend-cms/b1633f4c2c7c11ef97da5254007d9c55.png)

![](https://staticintl.cloudcachetci.com/cms/backend-cms/b15c9b1d2c7c11efa4f552540077de32.png)

4. Нажмите **Save**.

### Шаг 2. Привязка домена

1. Выберите шаблон транскодирования и нажмите **Bind Domain Name**.

![](https://staticintl.cloudcachetci.com/cms/backend-cms/97f3a1662c7d11efb0275254006c0558.png)

2. Выберите **Transcoding Template** и **Playback Domain**, которые вы хотите привязать, а затем нажмите **Confirm**.

![](https://staticintl.cloudcachetci.com/cms/backend-cms/97f2346d2c7d11ef918f52540005b090.png)

> **Примечание:** привязка доменного имени вступит в силу примерно через 10 минут после привязки.

### Шаг 3. Генерация URL воспроизведения

1. Войдите в консоль CSS > перейдите в **CSS Toolkit** > [Address Generator](https://console.intl.cloud.tencent.com/live/addrgenerator/addrgenerator).
2. Выберите тип URL: адрес воспроизведения.
3. Выберите домен воспроизведения, привязанный на [шаге 2](https://www.tencentcloud.com/document/product/267/50796#step-2.-bind-a-domain), и шаблон транскодирования с [шага 1](https://www.tencentcloud.com/document/product/267/50796#step-1.-create-a-transcoding-template) для генерации адреса воспроизведения.

![](https://staticintl.cloudcachetci.com/cms/backend-cms/41149cd52c7e11ef918f52540005b090.png)

### Шаг 4. Воспроизведение видео, закодированного в AV1

Воспроизведите видео, закодированное в AV1, с помощью проигрывателя, поддерживающего AV1, используя адрес воспроизведения, созданный на [шаге 3](https://www.tencentcloud.com/document/product/267/50796#step-3.-generate-a-playback-url). Вы можете использовать проигрыватель третьей стороны, поддерживающий AV1, или создать свой собственный проигрыватель.

- **Проигрыватели третьей стороны, поддерживающие AV1**
  - **App**
    - [ExoPlayer](https://github.com/google/ExoPlayer) (использует `libgav1`)
    - [ijkplayer](https://github.com/bilibili/ijkplayer) FFmpeg (обновить FFmpeg и интегрировать [dav1d](https://code.videolan.org/videolan/dav1d))
  - **Web**
    - [dash.js](http://cdn.dashjs.org/v2.4.0/jsdoc/index.html). Проигрыватель поддерживает AV1, но возможность декодирования видео AV1 зависит от браузера. Chrome поддерживает декодирование AV1.
    - [shaka-player](https://github.com/shaka-project/shaka-player). Проигрыватель поддерживает AV1, но возможность декодирования видео AV1 зависит от браузера. Chrome поддерживает декодирование AV1.
  - **PC**
  VLC для [Windows](https://share.weiyun.com/haPT1L0W) и [macOS](https://share.weiyun.com/W2btBASt) поддерживает AV1 в FLV и HEVC в FLV.
- **Создание собственного проигрывателя**
Если ваш проигрыватель не может воспроизводить видео AV1, вы можете обратиться к [воспроизведению видео AV1](https://www.tencentcloud.com/document/product/267/51157) для создания своего проигрывателя соответственно.


---
*Источник: [https://www.tencentcloud.com/document/product/267/50796](https://www.tencentcloud.com/document/product/267/50796)*

---
*Источник (EN): [av1-encoding.md](./av1-encoding.md)*
