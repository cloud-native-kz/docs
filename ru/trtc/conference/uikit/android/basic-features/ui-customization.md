# Настройка интерфейса

В этой статье рассказывается о том, как настроить пользовательский интерфейс TUIRoomKit. Мы предоставляем вам два решения на выбор: **Решение для тонкой настройки** и **Решение с самостоятельной реализацией интерфейса**.

## Решение 1: Решение для тонкой настройки

Путем прямого изменения исходного кода интерфейса, который мы предоставляем, вы можете настроить пользовательский интерфейс TUIRoomKit. Исходный код интерфейса TUIRoomKit находится в папке `Android/tuiroomkit` на Github:

### Замена иконок

Вы можете напрямую заменить иконки в папке `src/res/drawable-xxhdpi`, чтобы обеспечить согласованность цветовой схемы и стиля иконок во всем приложении. При замене сохраняйте неизменным имя файла иконки.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/7b8d69ac35ba11ee922b525400cea498.png)

### Замена копирайтинга

Вы можете изменить текстовое содержимое интерфейса видеоконференции, модифицируя файлы `strings.xml` в папках values-zh и values-en.

## Решение 2: Решение для частной настройки интерфейса

Код интерфейса TUIRoomKit находится в директории `src/main/java/com/tencent/cloud/tuikit/roomkit/view`, а представление экрана находится в компоненте TUIVideoSeat.

Ключевые файлы представления TUIRoomKit приведены ниже. Вы можете изменить соответствующее представление в соответствии с вашими потребностями и настроить ваш интерфейс.

```
viewâââ basicâ   âââ BaseBottomDialog.java                // Общий диалог в нижней части экранаâ   âââ BaseDialogFragment.java              // Общий фрагмент диалогаâ   âââ BaseSettingItem.java                 // Общий элемент параметровâ   âââ ConfirmDialog.java                   // Общий диалог подтвержденияâ   âââ NotificationView.java                // Общая панель уведомленийâ   âââ PrepareView.java                     // Интерфейс подготовкиâ   âââ RoomToast.java                       // Общее уведомление Toastâ   âââ RoundRelativeLayout.java             // Общий RelativeLayout с округлёнными угламиâ   âââ SwitchSettingItem.java               // Общий переключаемый параметрâ   âââ TipToast.java                        // Общее уведомление-подсказка Toastâââ create                                   // Интерфейс создания встречиâ   âââ CreateConferenceActivity.java        â   âââ CreateConferenceView.java            â   âââ RoomTypeSelectView.java              âââ join                                     // Интерфейс присоединения к встречеâ   âââ EnterConferenceActivity.java         â   âââ EnterConferenceView.java             âââ main                                     // Главный интерфейс встречиâ   âââ ConferenceMainFragment.java          // Главный фрагмент встречиâ   âââ ConferenceMainView.java              // Главное представление встречиâ   âââ RoomMainActivity.java                // Главная операция встречиâ   âââ RoomWindowManager.java               // Менеджер переключения между интерфейсом встречи и плавающим окномâ   âââ aisssistant                          // AI ассистентâ   â   âââ AIAssistantDialog.java           â   âââ bottomnavigationbar                  // Навигационная панель внизуâ   â   âââ BottomLayout.java              â   â   âââ BottomView.javaâ   â   âââ SeatRequestCountView.javaâ   âââ chat                                 // Всплывающее окно чатаâ   â   âââ ChatActivity.javaâ   âââ conferenceinvitation                 // Приглашение во время встречиâ   â   âââ InvitationReceivedActivity.javaâ   â   âââ InvitationReceivedView.javaâ   â   âââ SlideToAcceptView.javaâ   âââ exitroom                             // Выход из встречиâ   â   âââ ExitRoomDialog.javaâ   âââ floatwindow                          // Плавающее окноâ   â   âââ screensharingindicateâ   â   â   âââ ScreenSharingIndicateFloatView.javaâ   â   âââ videoplaying                     // Плавающее окно воспроизведения видеоâ   â       âââ RoomFloatViewService.javaâ   â       âââ RoomVideoFloatView.javaâ   âââ invite                               // Диалог приглашения в нижней части экранаâ   â   âââ InviteDialog.javaâ   âââ localaudioindicator                  // Индикатор статуса локального аудиоâ   â   âââ LocalAudioToggleView.javaâ   âââ mediasettings                        // Параметры медиа (аудио/видео)â   â   âââ MediaSettingPanel.javaâ   â   âââ QualityInfoPanel.javaâ   â   âââ VideoFrameRateChoicePanel.javaâ   â   âââ VideoResolutionChoicePanel.javaâ   âââ raisehandcontrolpanel                // Панель управления пользователями, поднявшими рукуâ   â   âââ RaiseHandApplicationListPanel.javaâ   â   âââ RaiseHandNotificationView.javaâ   âââ roominfo                             // Информация о встречеâ   â   âââ RoomInfoDialog.javaâ   âââ screensharecontrol                   // Управление совместным использованием экрана (функции списка членов)â   â   âââ MoreFunctionDialog.javaâ   âââ share                                // Общая встречаâ   â   âââ ShareRoomDialog.javaâ   âââ speechtotext                         // Преобразование речи в текстâ   â   âââ SpeechToTextActivity.javaâ   â   âââ SpeechToTextRecyclerView.javaâ   â   âââ SpeechToTextSubtitleView.javaâ   âââ topnavigationbar                     // Навигационная панель вверхуâ   â   âââ AudioRouteSwitchView.javaâ   â   âââ CameraSwitchView.javaâ   â   âââ ConferenceDurationView.javaâ   â   âââ ConferenceNameView.javaâ   â   âââ TopView.javaâ   âââ transferownercontrolpanel            // Панель выбора передачи прав владельцаâ   â   âââ TransferMasterPanel.javaâ   âââ usercontrolpanel                     // Панель управления пользователямиâ   â   âââ UserListPanel.javaâ   â   âââ UserListTypeSelectView.javaâ   â   âââ UserRecyclerView.javaâ   â   âââ userlistitem                     // Элементы списка панели управления пользователямиâ   â   â   âââ CallUserView.javaâ   â   â   âââ CameraIconView.javaâ   â   â   âââ InviteSeatButton.javaâ   â   â   âââ ListUserInfoView.javaâ   â   â   âââ MicIconView.javaâ   â   â   âââ ScreenIconView.javaâ   â   âââ usermanager                      // Всплывающее окно управления пользователямиâ   â       âââ ModifyNameKeyboard.javaâ   â       âââ UserManagementPanel.javaâ   âââ videoseat                            // Расположение видеокресел (видеомест)â   â   âââ TUIVideoSeatView.javaâ   âââ watermark                            // Водяной знакâ       âââ TextWaterMarkView.java
```

### Изменение кнопок в нижней части BottomView

Чтобы облегчить вам настройку кнопок нижних функций, наше BottomView автоматически строится путём чтения списка. На примере кнопки переключения видео код выглядит следующим образом.

```
private BottomItemData createCameraItem() {       BottomItemData cameraItemData = new BottomItemData();   //Установите тип кнопки для различения разных кнопок     cameraItemData.setType(BottomItemData.Type.VIDEO);       //Установите, является ли кнопка активной   if (isOwner()) {          cameraItemData.setEnable(true);      } else if (mRoomStore.roomInfo.enableSeatControl) {          cameraItemData.setEnable(false);     } else {           cameraItemData.setEnable(mRoomStore.roomInfo.enableVideo);      }    //Установите значок кнопки по умолчанию   cameraItemData.setIconId(R.drawable.tuiroomkit_ic_camera_off);     //Установите фоновое изображение кнопки    cameraItemData.setBackground(R.drawable.tuiroomkit_bg_bottom_item_black);    //Установите значок кнопки, когда она неактивна        cameraItemData.setDisableIconId(R.drawable.tuiroomkit_ic_camera_off);       //Установите значок кнопки по умолчанию   cameraItemData.setName(mContext.getString(R.string.tuiroomkit_item_open_camera));         //Эффект клика на кнопку, если ваша кнопка нуждается в переключении изображений/названий и т.д. при нажатии, вам нужно создать эти данные   BottomSelectItemData camaraSelectItemData = new BottomSelectItemData();       //Установите название кнопки при выборе           camaraSelectItemData.setSelectedName(mContext.getString(R.string.tuiroomkit_item_close_camera));     //Установите название кнопки при отсутствии выбора      camaraSelectItemData.setUnSelectedName(mContext.getString(R.string.tuiroomkit_item_open_camera));    //Установите, выбрана ли кнопка     camaraSelectItemData.setSelected(false);       //Установите значок кнопки при выборе    camaraSelectItemData.setSelectedIconId(R.drawable.tuiroomkit_ic_camera_on);      //Установите значок кнопки при отсутствии выбора     camaraSelectItemData.setUnSelectedIconId(R.drawable.tuiroomkit_ic_camera_off);     //Установите событие клика кнопки при выборе/отсутствии выбора   camaraSelectItemData.setOnItemSelectListener(new BottomSelectItemData.OnItemSelectListener() {                 @Override               public void onItemSelected(boolean isSelected) {                   enableCamera(isSelected);              }      });       cameraItemData.setSelectItemData(camaraSelectItemData);      return cameraItemData;   }
```

## Решение 3: Решение для полной настройки интерфейса

Общие функции TUIRoomKit основаны на TUIRoomEngine, SDK без интерфейса. Вы можете полностью реализовать свой собственный интерфейс на основе TUIRoomEngine. Подробнее см.

в адресе API интерфейса TUIRoomEngine.


---
*Источник: [https://trtc.io/document/54848](https://trtc.io/document/54848)*

---
*Источник (EN): [ui-customization.md](./ui-customization.md)*
