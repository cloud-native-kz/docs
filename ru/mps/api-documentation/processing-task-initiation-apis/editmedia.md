# EditMedia

## 1. Описание API

Доменное имя для запроса API: mps.intl.tencentcloudapi.com.

Этот API используется для редактирования видео с целью создания нового видеофайла. Функции редактирования включают:

**Задача редактирования**: простое редактирование видео, такое как обрезка и объединение.
1) Редактирование файла для создания нового видео.
2) Объединение нескольких файлов для создания нового видео.
3) Редактирование нескольких файлов и последующее их объединение для создания нового видео.

**Задача композитинга**: создание нового видео путем описания информации через API.
1) Многодорожечность (видео, аудио и субтитры) и различные типы элементов (видео, изображение, аудио, текст и пусто).
2) Уровень изображения: наложение, масштабирование, произвольное вращение, отражение и другое.
3) Уровень аудио: управление громкостью, плавное появление/затухание, микширование и другое.
4) Уровень видео: переход, регулировка скорости воспроизведения, объединение, обрезка, субтитры, картинка в картинке, разделение аудио-видео, анимация входа и выхода и другое.

Максимум 20 запросов можно инициировать в секунду для этого API.

Мы рекомендуем использовать API Explorer

Попробуйте

API Explorer предоставляет набор возможностей, включая онлайн-вызов, аутентификацию подписей, генерацию кода SDK и быстрый поиск API. Он позволяет просмотреть запрос, ответ и автоматически сгенерированные примеры.

## 2. Входные параметры

Следующий список параметров запроса содержит только параметры запроса API и некоторые общие параметры. Для полного списка общих параметров см. [Общие параметры запроса](https://www.tencentcloud.com/document/api/1041/33628).

| Имя параметра | Обязательный | Тип | Описание |
| --- | --- | --- | --- |
| Action | Да | String | [Общие параметры](https://www.tencentcloud.com/document/api/1041/33628). Значение, используемое для этого API: EditMedia. |
| Version | Да | String | [Общие параметры](https://www.tencentcloud.com/document/api/1041/33628). Значение, используемое для этого API: 2019-06-12. |
| Region | Нет | String | [Общие параметры](https://www.tencentcloud.com/document/api/1041/33628). Этот параметр не требуется для этого API. |
| FileInfos.N | Да | Array of [EditMediaFileInfo](https://www.tencentcloud.com/document/api/1041/33690#EditMediaFileInfo) | Информация входного видеофайла. |
| OutputStorage | Да | [TaskOutputStorage](https://www.tencentcloud.com/document/api/1041/33690#TaskOutputStorage) | Место хранения выходного файла обработки медиа. |
| OutputObjectPath | Да | String | Путь для сохранения выходного файла обработки медиа. |
| OutputConfig | Нет | [EditMediaOutputConfig](https://www.tencentcloud.com/document/api/1041/33690#EditMediaOutputConfig) | Параметры вывода для задачи обрезки видео. |
| ComposeConfig | Нет | [ComposeMediaConfig](https://www.tencentcloud.com/document/api/1041/33690#ComposeMediaConfig) | Параметры задачи композитинга видео. |
| TaskNotifyConfig | Нет | [TaskNotifyConfig](https://www.tencentcloud.com/document/api/1041/33690#TaskNotifyConfig) | Информация об уведомлении о событии задачи. Если этот параметр не указан, уведомления о событиях получены не будут. |
| TasksPriority | Нет | Integer | Приоритет задачи. Чем выше значение, тем выше приоритет. Диапазон значений: -10 - 10. Если этот параметр не указан, будет использовано значение 0. |
| SessionId | Нет | String | ID, используемый для дедупликации. Если запрос с тем же ID был сделан в течение последних трех дней, текущий запрос вернет ошибку. ID может содержать до 50 символов. Если этот параметр не указан или указана пустая строка, дедупликация не будет выполняться. |
| SessionContext | Нет | String | Контекст источника, используемый для передачи информации запроса пользователя. Обратный вызов изменения статуса рабочего процесса задачи вернет значение этого поля. Может содержать до 1000 символов. |

## 3. Выходные параметры

| Имя параметра | Тип | Описание |
| --- | --- | --- |
| TaskId | String | ID задачи редактирования видео, который можно использовать для запроса статуса задачи редактирования. |
| RequestId | String | Уникальный ID запроса, генерируемый сервером, будет возвращен для каждого запроса (если запрос не достигает сервера по другим причинам, запрос не получит RequestId). RequestId требуется для определения проблемы. |

## 4. Примеры

### Пример 1 [Задача редактирования] Редактирование файла для создания нового видео

#### Пример входных данных

```
https://mps.intl.tencentcloudapi.com/?Action=EditMedia
&FileInfos.0.InputInfo.Type=COS
&FileInfos.0.InputInfo.CosInputInfo.Bucket=TopRankVideo-125xxx88
&FileInfos.0.InputInfo.CosInputInfo.Region=ap-chongqing
&FileInfos.0.InputInfo.CosInputInfo.Object=/movie/201907/WildAnimal.mov
&FileInfos.0.StartTimeOffset=60.0
&FileInfos.0.EndTimeOffset=120.0
&OutputStorage.Type=COS
&OutputStorage.CosOutputStorage.Bucket=TopRankVideo-125xxx88
&OutputStorage.CosOutputStorage.Region=ap-chongqing
&OutputObjectPath=/clip_result/clip_WildAnimal.{format}
&<Common request parameters>
```

#### Пример выходных данных

```json
{
    "Response": {
        "RequestId": "6ca31e3a-6b8e-4b4e-9256-fdc700064ef3",
        "TaskId": "125xxx88-EditMedia-bffb15f07530b57bc1aabb01fac74bca"
    }
}
```

### Пример 2 [Задача композитинга] Композитинг изображений и аудио в видео

Этот пример показывает, как объединить набор изображений и фоновую музыку в видео и добавить эффект перехода между изображениями. Форма дорожек выглядит следующим образом:![](https://ie-mps-1258344699.cos.ap-nanjing.tencentcos.cn/common/cloud/mps-demo/01_img_audio_to_video/track-en.png) [Пример эффекта](https://ie-mps-1258344699.cos.ap-nanjing.tencentcos.cn/common/cloud/mps-demo/01_img_audio_to_video/01_img_audio_to_video.mp4) Примечание: переход потребляет продолжительность дорожки элементов до и после него. Если переходы находятся до и после элемента, необходимо убедиться, что продолжительность дорожки элемента больше суммы продолжительности переходов до и после него.

#### Пример входных данных

```
POST / HTTP/1.1
Host: mps.intl.tencentcloudapi.com
Content-Type: application/json
X-TC-Action: EditMedia
<Common request parameters>

{
    "FileInfos": [
        {
            "Id": "img01",
            "InputInfo": {
                "Type": "URL",
                "UrlInputInfo": {
                    "Url": "https://.../1.jpg"
                }
            }
        },
        {
            "Id": "img02",
            "InputInfo": {
                "Type": "URL",
                "UrlInputInfo": {
                    "Url": "https://.../2.jpg"
                }
            }
        },
        {
            "Id": "img03",
            "InputInfo": {
                "Type": "URL",
                "UrlInputInfo": {
                    "Url": "https://.../3.jpg"
                }
            }
        },
        {
            "Id": "img04",
            "InputInfo": {
                "Type": "URL",
                "UrlInputInfo": {
                    "Url": "https://.../4.jpg"
                }
            }
        },
        {
            "Id": "img05",
            "InputInfo": {
                "Type": "URL",
                "UrlInputInfo": {
                    "Url": "https://.../5.jpg"
                }
            }
        },
        {
            "Id": "img06",
            "InputInfo": {
                "Type": "URL",
                "UrlInputInfo": {
                    "Url": "https://.../6.jpg"
                }
            }
        },
        {
            "Id": "img07",
            "InputInfo": {
                "Type": "URL",
                "UrlInputInfo": {
                    "Url": "https://.../7.jpg"
                }
            }
        },
        {
            "Id": "img08",
            "InputInfo": {
                "Type": "URL",
                "UrlInputInfo": {
                    "Url": "https://.../8.jpg"
                }
            }
        },
        {
            "Id": "img09",
            "InputInfo": {
                "Type": "URL",
                "UrlInputInfo": {
                    "Url": "https://.../9.jpg"
                }
            }
        },
        {
            "Id": "img10",
            "InputInfo": {
                "Type": "URL",
                "UrlInputInfo": {
                    "Url": "https://.../10.jpg"
                }
            }
        },
        {
            "Id": "adu",
            "InputInfo": {
                "Type": "URL",
                "UrlInputInfo": {
                    "Url": "https://.../back_music.mp3"
                }
            }
        }
    ],
    "OutputStorage": {
        "Type": "COS",
        "CosOutputStorage": {
            "Bucket": "your_bucket",
            "Region": "your_bucket_region"
        }
    },
    "OutputObjectPath": "/your/output/dir/",
    "ComposeConfig": {
        "TargetInfo": {
            "Container": "mp4",
            "VideoStream": {
                "Fps": 30
            }
        },
        "Tracks": [
            {
                "Type": "Video",
                "Items": [
                    {
                        "Type": "Image",
                        "Image": {
                            "SourceMedia": {
                                "FileId": "img01"
                            },
                            "TrackTime": {
                                "Duration": "3s"
                            }
                        }
                    },
                    {
                        "Type": "Transition",
                        "Transition": {
                            "Transitions": [
                                {
                                    "Type": "Dreamy"
                                }
                            ]
                        }
                    },
                    {
                        "Type": "Image",
                        "Image": {
                            "SourceMedia": {
                                "FileId": "img02"
                            },
                            "TrackTime": {
                                "Duration": "3s"
                            }
                        }
                    },
                    {
                        "Type": "Transition",
                        "Transition": {
                            "Transitions": [
                                {
                                    "Type": "Circleopen"
                                }
                            ]
                        }
                    },
                    {
                        "Type": "Image",
                        "Image": {
                            "SourceMedia": {
                                "FileId": "img03"
                            },
                            "TrackTime": {
                                "Duration": "3s"
                            }
                        }
                    },
                    {
                        "Type": "Transition",
                        "Transition": {
                            "Transitions": [
                                {
                                    "Type": "Heart"
                                }
                            ]
                        }
                    },
                    {
                        "Type": "Image",
                        "Image": {
                            "SourceMedia": {
                                "FileId": "img04"
                            },
                            "TrackTime": {
                                "Duration": "3s"
                            }
                        }
                    },
                    {
                        "Type": "Transition",
                        "Transition": {
                            "Transitions": [
                                {
                                    "Type": "PolarFunction"
                                }
                            ]
                        }
                    },
                    {
                        "Type": "Image",
                        "Image": {
                            "SourceMedia": {
                                "FileId": "img05"
                            },
                            "TrackTime": {
                                "Duration": "3s"
                            }
                        }
                    },
                    {
                        "Type": "Transition",
                        "Transition": {
                            "Transitions": [
                                {
                                    "Type": "Swirl"
                                }
                            ]
                        }
                    },
                    {
                        "Type": "Image",
                        "Image": {
                            "SourceMedia": {
                                "FileId": "img06"
                            },
                            "TrackTime": {
                                "Duration": "3s"
                            }
                        }
                    },
                    {
                        "Type": "Transition",
                        "Transition": {
                            "Transitions": [
                                {
                                    "Type": "WipeRight"
                                }
                            ]
                        }
                    },
                    {
                        "Type": "Image",
                        "Image": {
                            "SourceMedia": {
                                "FileId": "img07"
                            },
                            "TrackTime": {
                                "Duration": "3s"
                            }
                        }
                    },
                    {
                        "Type": "Transition",
                        "Transition": {
                            "Transitions": [
                                {
                                    "Type": "ZoomInCircles"
                                }
                            ]
                        }
                    },
                    {
                        "Type": "Image",
                        "Image": {
                            "SourceMedia": {
                                "FileId": "img08"
                            },
                            "TrackTime": {
                                "Duration": "3s"
                            }
                        }
                    },
                    {
                        "Type": "Transition",
                        "Transition": {
                            "Transitions": [
                                {
                                    "Type": "ImageFadeInFadeOut"
                                }
                            ]
                        }
                    },
                    {
                        "Type": "Image",
                        "Image": {
                            "SourceMedia": {
                                "FileId": "img09"
                            },
                            "TrackTime": {
                                "Duration": "3s"
                            }
                        }
                    },
                    {
                        "Type": "Transition",
                        "Transition": {
                            "Transitions": [
                                {
                                    "Type": "ButterflyWaveScrawler"
                                }
                            ]
                        }
                    },
                    {
                        "Type": "Image",
                        "Image": {
                            "SourceMedia": {
                                "FileId": "img10"
                            },
                            "TrackTime": {
                                "Duration": "3s"
                            }
                        }
                    }
                ]
            },
            {
                "Type": "Audio",
                "Items": [
                    {
                        "Type": "Audio",
                        "Audio": {
                            "SourceMedia": {
                                "FileId": "adu"
                            },
                            "TrackTime": {
                                "Duration": "21s"
                            }
                        }
                    }
                ]
            }
        ]
    }
}
```

#### Пример выходных данных

```json
{
    "Response": {
        "RequestId": "6ca31e3a-6b8e-4b4e-9256-fdc700064ef3",
        "TaskId": "125xxx88-EditMedia-bffb15f07530b57bc1aabb01fac74bca"
    }
}
```

### Пример 3 [Задача композитинга] Редактирование и открывающая сцена и закрывающая сцена и изображения водяных знаков и текст и замена аудио

Этот пример показывает, как редактировать видео и добавлять открывающую и закрывающую сцены, изображения водяных знаков, подписи и замену аудио для создания нового видео. Форма дорожек выглядит следующим образом:![](https://ie-mps-1258344699.cos.ap-nanjing.tencentcos.cn/common/cloud/mps-demo/02_video_start_end_logo_txt/track-en.png) [Пример эффекта](https://ie-mps-1258344699.cos.ap-nanjing.tencentcos.cn/common/cloud/mps-demo/02_video_start_end_logo_txt/02_video_start_end_logo_txt.mp4) Примечание: открывающая и закрывающая сцены могут быть видео или изображениями. Примечание: параметр Canvas используется для указания размера выходного видео. Если не указан, используется размер первого видео по умолчанию. Поэтому рекомендуется размещать подлинное видео на первом месте в списке материалов.

#### Пример входных данных

```
POST / HTTP/1.1
Host: mps.intl.tencentcloudapi.com
Content-Type: application/json
X-TC-Action: EditMedia
<Common request parameters>

{
    "FileInfos": [
        {
            "Id": "start",
            "InputInfo": {
                "Type": "URL",
                "UrlInputInfo": {
                    "Url": "https://.../start.mp4"
                }
            }
        },
        {
            "Id": "video",
            "InputInfo": {
                "Type": "URL",
                "UrlInputInfo": {
                    "Url": "https://.../video.mp4"
                }
            }
        },
        {
            "Id": "end",
            "InputInfo": {
                "Type": "URL",
                "UrlInputInfo": {
                    "Url": "https://.../end.png"
                }
            }
        },
        {
            "Id": "img",
            "InputInfo": {
                "Type": "URL",
                "UrlInputInfo": {
                    "Url": "https://.../logo.png"
                }
            }
        },
        {
            "Id": "aud",
            "InputInfo": {
                "Type": "URL",
                "UrlInputInfo": {
                    "Url": ".../back_music.mp3"
                }
            }
        }
    ],
    "OutputStorage": {
        "Type": "COS",
        "CosOutputStorage": {
            "Bucket": "your_bucket",
            "Region": "your_bucket_region"
        }
    },
    "OutputObjectPath": "/your/output/dir/",
    "ComposeConfig": {
        "TargetInfo": {
            "Container": "mp4",
            "VideoStream": {
                "Fps": 30
            }
        },
        "Styles": [
            {
                "Id": "ss",
                "Type": "Subtitle",
                "Subtitle": {
                    "MarginBottom": "50%",
                    "FontType": "SimHei",
                    "FontSize": "8%",
                    "FontBold": 1,
                    "FontColor": "#FF0000FF",
                    "BorderWidth": "2px",
                    "BorderColor": "#00FF00FF",
                    "BottomColor": "#0000FFFF"
                }
            }
        ],
        "Tracks": [
            {
                "Type": "Title",
                "Items": [
                    {
                        "Type": "Subtitle",
                        "Subtitle": {
                            "StyleId": "ss",
                            "TrackTime": {
                                "Start": "0s",
                                "Duration": "2s"
                            },
                            "Text": "Opening Scene - Example"
                        }
                    },
                    {
                        "Type": "Subtitle",
                        "Subtitle": {
                            "StyleId": "ss",
                            "TrackTime": {
                                "Start": "2s",
                                "Duration": "8s"
                            },
                            "Text": "Main Content - Example"
                        }
                    },
                    {
                        "Type": "Subtitle",
                        "Subtitle": {
                            "StyleId": "ss",
                            "TrackTime": {
                                "Start": "12s",
                                "Duration": "2s"
                            },
                            "Text": "Closing Scene - Example"
                        }
                    }
                ]
            },
            {
                "Type": "Video",
                "Items": [
                    {
                        "Type": "Image",
                        "Image": {
                            "SourceMedia": {
                                "FileId": "img"
                            },
                            "TrackTime": {
                                "Duration": "14s"
                            },
                            "XPos": "85%",
                            "YPos": "10%",
                            "Width": "15%"
                        }
                    }
                ]
            },
            {
                "Type": "Video",
                "Items": [
                    {
                        "Type": "Video",
                        "Video": {
                            "SourceMedia": {
                                "FileId": "start"
                            },
                            "AudioOperations": [
                                {
                                    "Type": "Volume",
                                    "Volume": 0.0
                                }
                            ]
                        }
                    },
                    {
                        "Type": "Video",
                        "Video": {
                            "SourceMedia": {
                                "FileId": "video",
                                "StartTime": "10s",
                                "EndTime": "20s"
                            },
                            "AudioOperations": [
                                {
                                    "Type": "Volume",
                                    "Volume": 0.0
                                }
                            ]
                        }
                    },
                    {
                        "Type": "Transition",
                        "Transition": {
                            "Transitions": [
                                {
                                    "Type": "Heart"
                                }
                            ]
                        }
                    },
                    {
                        "Type": "Image",
                        "Image": {
                            "SourceMedia": {
                                "FileId": "end"
                            },
                            "TrackTime": {
                                "Duration": "3s"
                            }
                        }
                    }
                ]
            },
            {
                "Type": "Audio",
                "Items": [
                    {
                        "Type": "Audio",
                        "Audio": {
                            "SourceMedia": {
                                "FileId": "aud"
                            },
                            "TrackTime": {
                                "Duration": "14s"
                            }
                        }
                    }
                ]
            }
        ]
    }
}
```

#### Пример выходных данных

```json
{
    "Response": {
        "RequestId": "6ca31e3a-6b8e-4b4e-9256-fdc700064ef3",
        "TaskId": "125xxx88-EditMedia-bffb15f07530b57bc1aabb01fac74bca"
    }
}
```

### Пример 4 [Задача композитинга] Картинка в картинке

Этот пример показывает, как масштабировать одно видео и наложить его на другое видео, чтобы создать новое видео. Форма дорожек выглядит следующим образом:![](https://ie-mps-1258344699.cos.ap-nanjing.tencentcos.cn/common/cloud/mps-demo/03_video_in_video/track-en.png) [Пример эффекта](https://ie-mps-1258344699.cos.ap-nanjing.tencentcos.cn/common/cloud/mps-demo/03_video_in_video/03_video_in_video.mp4)

#### Пример входных данных

```
POST / HTTP/1.1
Host: mps.intl.tencentcloudapi.com
Content-Type: application/json
X-TC-Action: EditMedia
<Common request parameters>

{
    "FileInfos": [
        {
            "Id": "back",
            "InputInfo": {
                "Type": "URL",
                "UrlInputInfo": {
                    "Url": "https://.../video.mp4"
                }
            }
        },
        {
            "Id": "over",
            "InputInfo": {
                "Type": "URL",
                "UrlInputInfo": {
                    "Url": "https://.../over.mp4"
                }
            }
        }
    ],
    "OutputStorage": {
        "Type": "COS",
        "CosOutputStorage": {
            "Bucket": "your_bucket",
            "Region": "your_bucket_region"
        }
    },
    "OutputObjectPath": "/your/output/dir/",
    "ComposeConfig": {
        "Tracks": [
            {
                "Type": "Video",
                "Items": [
                    {
                        "Type": "Video",
                        "Video": {
                            "SourceMedia": {
                                "FileId": "over",
                                "StartTime": "30s",
                                "EndTime": "40s"
                            },
                            "AudioOperations": [
                                {
                                    "Type": "Volume",
                                    "Volume": 0.0
                                }
                            ],
                            "XPos": "60%",
                            "YPos": "30%",
                            "Width": "300px"
                        }
                    }
                ]
            },
            {
                "Type": "Video",
                "Items": [
                    {
                        "Type": "Video",
                        "Video": {
                            "SourceMedia": {
                                "FileId": "back",
                                "StartTime": "10s",
                                "EndTime": "20s"
                            }
                        }
                    }
                ]
            }
        ]
    }
}
```

#### Пример выходных данных

```json
{
    "Response": {
        "RequestId": "6ca31e3a-6b8e-4b4e-9256-fdc700064ef3",
        "TaskId": "125xxx88-EditMedia-bffb15f07530b57bc1aabb01fac74bca"
    }
}
```

### Пример 5 [Задача композитинга] Регулировка скорости воспроизведения видео

Этот пример показывает, как редактировать видео для создания нового видео, чтобы оно воспроизводилось с скоростью 2x в течение первых 10 секунд и с скоростью 0,8x в течение последних 10 секунд. Форма дорожек выглядит следующим образом:![](https://ie-mps-1258344699.cos.ap-nanjing.tencentcos.cn/common/cloud/mps-demo/04_video_speed/track-en.png)[Пример эффекта](https://ie-mps-1258344699.cos.ap-nanjing.tencentcos.cn/common/cloud/mps-demo/04_video_speed/04_video_speed.mp4) Примечание: когда продолжительность материала в SourceMedia отличается от TrackTime, может быть достигнут эффект регулировки скорости воспроизведения. Примечание: эффект регулировки скорости воспроизведения не может использоваться одновременно с эффектом перехода.

#### Пример входных данных

```
POST / HTTP/1.1
Host: mps.intl.tencentcloudapi.com
Content-Type: application/json
X-TC-Action: EditMedia
<Common request parameters>

{
    "FileInfos": [
        {
            "Id": "vod",
            "InputInfo": {
                "Type": "URL",
                "UrlInputInfo": {
                    "Url": "https://.../video.mp4"
                }
            }
        }
    ],
    "OutputStorage": {
        "Type": "COS",
        "CosOutputStorage": {
            "Bucket": "your_bucket",
            "Region": "your_bucket_region"
        }
    },
    "OutputObjectPath": "/your/output/dir/",
    "ComposeConfig": {
        "Tracks": [
            {
                "Type": "Video",
                "Items": [
                    {
                        "Type": "Video",
                        "Video": {
                            "SourceMedia": {
                                "FileId": "vod",
                                "StartTime": "10s",
                                "EndTime": "20s"
                            },
                            "TrackTime": {
                                "Duration": "5s"
                            }
                        }
                    }
                ]
            },
            {
                "Type": "Video",
                "Items": [
                    {
                        "Type": "

---
*Источник (EN): [editmedia.md](./editmedia.md)*
