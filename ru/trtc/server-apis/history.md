# История

## Release 40

Время выпуска: 2026-01-22 14:43:57

Обновления выпуска:

Улучшение существующей документации.

Измененные структуры данных:

MixLayoutParams
Новые члены: PureAudioDisableLayout
RecordParams
Новые члены: FillType, SubscribeAbility

## Release 39

Время выпуска: 2026-01-21 14:24:54

Обновления выпуска:

Улучшение существующей документации.

Измененные API:

ControlAIConversation
Новые входные параметры: InvokeLLM

Новые структуры данных:

InvokeLLM

Измененные структуры данных:

ServerPushText
Новые члены: Audio, DropMode, Priority, AddHistory, MetaInfo

## Release 38

Время выпуска: 2025-09-25 22:51:58

Обновления выпуска:

Улучшение существующей документации.

Измененные API:

StartAITranscription
Новые входные параметры: TranslationConfig

Новые структуры данных:

TTSConfig
Terminology
TranslationConfig

## Release 37

Время выпуска: 2025-08-14 16:14:37

Обновления выпуска:

Улучшение существующей документации.

Новые API:

CreateCloudModeration
DeleteCloudModeration
DescribeCloudModeration
ModifyCloudModeration

Новые структуры данных:

CloudModerationStorage
ModerationParams
ModerationStorageParams
ModerationSupplierParam
SubscribeModerationUserIds

## Release 36

Время выпуска: 2025-08-06 16:19:00

Обновления выпуска:

Улучшение существующей документации.

Новые API:

CreateCloudSliceTask
DeleteCloudSliceTask
DescribeCloudSliceTask
ModifyCloudSliceTask

Новые структуры данных:

CloudSliceStorage
SliceParams
SliceStorageParams

## Release 35

Время выпуска: 2025-07-22 15:44:41

Обновления выпуска:

Улучшение существующей документации.

Новые API:

DescribeWebRecord
StartWebRecord
StopWebRecord

Новые структуры данных:

EmulateMobileParams
WebRecordVideoParams

## Release 34

Время выпуска: 2025-07-14 10:52:39

Обновления выпуска:

Улучшение существующей документации.

Измененные API:

StartPublishCdnStream
Новые входные параметры: RecordParams

Новые структуры данных:

McuCloudVod
McuRecordParams
McuStorageParams
McuTencentVod

## Release 33

Время выпуска: 2024-12-30 11:47:01

Обновления выпуска:

Улучшение существующей документации.

Измененные API:

UpdateStreamIngest
Новые входные параметры: IsPause

## Release 32

Время выпуска: 2024-11-20 17:56:59

Обновления выпуска:

Улучшение существующей документации.

Измененные API:

StartStreamIngest
Новые входные параметры: Volume
UpdateStreamIngest
Новые входные параметры: Volume
Измененные входные параметры:
StreamUrl

Измененные структуры данных:

AudioEncodeParams
Измененные члены:
SampleRate, Channel, BitRate
VideoEncodeParams
Измененные члены:
Width, Height, Fps, BitRate, Gop

## Release 31

Время выпуска: 2024-10-24 21:28:08

Обновления выпуска:

Улучшение существующей документации.

Новые API:

StopAIConversation

## Release 30

Время выпуска: 2024-10-22 15:06:52

Обновления выпуска:

Улучшение существующей документации.

Новые API:

DescribeAITranscription
StartAITranscription
StopAITranscription

Новые структуры данных:

RecognizeConfig
TranscriptionParams

## Release 29

Время выпуска: 2024-10-22 15:06:19

Обновления выпуска:

Улучшение существующей документации.

Новые API:

ControlAIConversation
DescribeAIConversation
StartAIConversation
UpdateAIConversation

Новые структуры данных:

AgentConfig
STTConfig
ServerPushText

## Release 28

Время выпуска: 2024-08-13 11:43:31

Обновления выпуска:

Улучшение существующей документации.

Новые API:

UpdateStreamIngest

Измененные API:

StartStreamIngest
Новые входные параметры: SeekSecond, AutoPush, RepeatNum, MaxDuration
Устаревшие входные параметры:
VideoEncodeParams, AudioEncodeParams, SourceUrl

## Release 27

Время выпуска: 2024-07-22 15:13:00

Обновления выпуска:

Улучшение существующей документации.

Измененные API:

StartStreamIngest
Новые входные параметры: StreamUrl
Измененные входные параметры:
SourceUrl

## Release 26

Время выпуска: 2024-01-25 19:47:42

Обновления выпуска:

Улучшение существующей документации.

Новые API:

DescribeTRTCMarketQualityData
DescribeTRTCMarketScaleData
DescribeTRTCRealTimeQualityData
DescribeTRTCRealTimeScaleData

Новые структуры данных:

RowValues
SeriesInfos
TRTCDataResult

## Release 25

Время выпуска: 2023-11-24 16:25:45

Обновления выпуска:

Улучшение существующей документации.

Новые API:

DescribeStreamIngest
StartStreamIngest
StopStreamIngest

Новые структуры данных:

AudioEncodeParams
VideoEncodeParams

## Release 24

Время выпуска: 2023-07-28 15:26:39

Обновления выпуска:

Улучшение существующей документации.

Измененные структуры данных:

McuLayout
Новые члены: BackgroundRenderMode
McuVideoParams
Новые члены: BackgroundRenderMode

## Release 23

Время выпуска: 2023-05-12 11:26:05

Обновления выпуска:

Улучшение существующей документации.

Новые API:

DescribeCallDetailInfo
DescribeRoomInfo
DescribeScaleInfo
DescribeUnusualEvent
DescribeUserEvent
DescribeUserInfo

Измененные API:

DescribeTrtcRoomUsage
Новые выходные параметры: Data

Новые структуры данных:

AbnormalEvent
AbnormalExperience
EventList
EventMessage
QualityData
RoomState
ScaleInfomation
TimeValue
UserInformation
WaterMarkChar
WaterMarkTimestamp

Измененные структуры данных:

McuLayoutParams
Новые члены: RenderMode
WaterMark
Новые члены: WaterMarkChar, WaterMarkTimestamp

## Release 22

Время выпуска: 2023-03-31 11:13:18

Обновления выпуска:

Улучшение существующей документации.

Новые API:

DescribeTrtcRoomUsage

## Release 21

Время выпуска: 2023-03-17 11:38:29

Обновления выпуска:

Улучшение существующей документации.

Новые API:

DescribeMixTranscodingUsage
DescribeRecordingUsage
DescribeRelayUsage
DescribeTrtcUsage

Новые структуры данных:

McuWaterMarkText
TrtcUsage

Измененные структуры данных:

McuWaterMarkParams
Новые члены: WaterMarkText

## Release 20

Время выпуска: 2023-03-14 16:04:41

Обновления выпуска:

Улучшение существующей документации.

Измененные структуры данных:

McuLayoutVolume
Новые члены: Interval, FollowIdr
McuPassThrough
Новые члены: Interval, FollowIdr

## Release 19

Время выпуска: 2023-03-02 17:29:46

Обновления выпуска:

Улучшение существующей документации.

Измененные структуры данных:

RecordParams
Новые члены: MediaId

## Release 18

Время выпуска: 2022-12-16 15:45:24

Обновления выпуска:

Улучшение существующей документации.

Измененные структуры данных:

MixLayoutParams
Новые члены: RenderMode, MaxResolutionUserAlign
RecordParams
Новые члены: MaxMediaFileDuration
TencentVod
Новые члены: UserDefineRecordId

## Release 17

Время выпуска: 2022-11-10 16:45:18

Обновления выпуска:

Улучшение существующей документации.

Новые API:

SetUserBlocked
SetUserBlockedByStrRoomId

## Release 16

Время выпуска: 2022-11-03 14:29:50

Обновления выпуска:

Улучшение существующей документации.

Измененные API:

StartPublishCdnStream
Новые входные параметры: FeedBackRoomParams
UpdatePublishCdnStream
Новые входные параметры: FeedBackRoomParams

Новые структуры данных:

McuFeedBackRoomParams

Измененные структуры данных:

McuAudioParams
Новые члены: UnSubscribeAudioList

## Release 15

Время выпуска: 2022-09-20 10:16:48

Обновления выпуска:

Улучшение существующей документации.

Новые структуры данных:

McuCustomCrop

Измененные структуры данных:

McuLayout
Новые члены: CustomCrop
RecordParams
Новые члены: AvMerge
TencentVod
Новые члены: MediaType

## Release 14

Время выпуска: 2022-08-19 10:23:41

Обновления выпуска:

Улучшение существующей документации.

Измененные API:

StartPublishCdnStream
Новые входные параметры: SeiParams
UpdatePublishCdnStream
Новые входные параметры: SeiParams

Новые структуры данных:

McuLayoutVolume
McuPassThrough
McuSeiParams

Измененные структуры данных:

McuWaterMarkParams
Новые члены: WaterMarkType

## Release 13

Время выпуска: 2022-07-04 11:00:48

Обновления выпуска:

Улучшение существующей документации.

Новые API:

StartPublishCdnStream
StopPublishCdnStream
UpdatePublishCdnStream

Новые структуры данных:

AgentParams
AudioEncode
MaxVideoUser
McuAudioParams
McuLayout
McuLayoutParams
McuPublishCdnParam
McuUserInfoParams
McuVideoParams
McuWaterMarkImage
McuWaterMarkParams
MixUserInfo
SingleSubscribeParams
UserMediaStream
VideoEncode

## Release 12

Время выпуска: 2022-05-11 15:16:52

Обновления выпуска:

Улучшение существующей документации.

Новые API:

CreateCloudRecording
DeleteCloudRecording
DescribeCloudRecording
ModifyCloudRecording

**Удаленные API:**

CreatePicture
CreateTroubleInfo
DeletePicture
DescribeAbnormalEvent
DescribeCallDetail
DescribeDetailEvent
DescribeHistoryScale
DescribePicture
DescribeRecordStatistic
DescribeRoomInformation
DescribeTrtcInteractiveTime
DescribeTrtcMcuTranscodeTime
DescribeUserInformation
ModifyPicture
StartMCUMixTranscode
StartMCUMixTranscodeByStrRoomId
StopMCUMixTranscode
StopMCUMixTranscodeByStrRoomId

Новые структуры данных:

AudioParams
CloudStorage
CloudVod
MixLayout
MixLayoutParams
MixTranscodeParams
RecordParams
StorageFile
StorageParams
SubscribeStreamUserIds
TencentVod
VideoParams
WaterMark
WaterMarkImage

**Удаленные структуры данных:**

AbnormalEvent
AbnormalExperience
EncodeParams
EventList
EventMessage
LayoutParams
OneSdkAppIdTranscodeTimeUsagesInfo
OneSdkAppIdUsagesInfo
OutputParams
PictureInfo
PresetLayoutConfig
PublishCdnParams
QualityData
RecordUsage
RoomState
ScaleInfomation
SdkAppIdRecordUsage
SdkAppIdTrtcMcuTranscodeTimeUsage
SdkAppIdTrtcUsage
SmallVideoLayoutParams
TimeValue
UserInformation
WaterMarkParams

## Release 11

Время выпуска: 2021-11-09 10:13:12

Обновления выпуска:

Улучшение существующей документации.

Новые API:

DescribeRecordStatistic
DescribeTrtcInteractiveTime
DescribeTrtcMcuTranscodeTime

**Удаленные API:**

DescribeRealtimeNetwork
DescribeRealtimeQuality
DescribeRealtimeScale

Новые структуры данных:

OneSdkAppIdTranscodeTimeUsagesInfo
OneSdkAppIdUsagesInfo
RecordUsage
SdkAppIdRecordUsage
SdkAppIdTrtcMcuTranscodeTimeUsage
SdkAppIdTrtcUsage

**Удаленные структуры данных:**

RealtimeData

## Release 10

Время выпуска: 2021-10-27 16:00:34

Обновления выпуска:

Улучшение существующей документации.

Измененные структуры данных:

EncodeParams
Новые члены: BackgroundImageUrl
WaterMarkParams
Новые члены: WaterMarkUrl

## Release 9

Время выпуска: 2021-06-15 16:57:07

Обновления выпуска:

Улучшение существующей документации.

Новые структуры данных:

WaterMarkParams

Измененные структуры данных:

LayoutParams
Новые члены: WaterMarkParams

## Release 8

Время выпуска: 2021-04-28 11:08:14

Обновления выпуска:

Улучшение существующей документации.

Новые API:

CreatePicture
DeletePicture
DescribePicture
ModifyPicture

Новые структуры данных:

PictureInfo

## Release 7

Время выпуска: 2021-04-07 19:54:14

Обновления выпуска:

Улучшение существующей документации.

Измененные структуры данных:

EncodeParams
Новые члены: AudioCodec

## Release 6

Время выпуска: 2021-02-20 17:51:34

Обновления выпуска:

Улучшение существующей документации.

Новые API:

StartMCUMixTranscodeByStrRoomId
StopMCUMixTranscodeByStrRoomId

Измененные структуры данных:

LayoutParams
Новые члены: PureAudioHoldPlaceMode

## Release 5

Время выпуска: 2021-02-19 16:22:07

Обновления выпуска:

Улучшение существующей документации.

Новые API:

DismissRoomByStrRoomId
RemoveUserByStrRoomId

## Release 4

Время выпуска: 2021-01-21 17:40:36

Обновления выпуска:

Улучшение существующей документации.

Измененные API:

StartMCUMixTranscode
Новые входные параметры: PublishCdnParams

Новые структуры данных:

PublishCdnParams

Измененные структуры данных:

LayoutParams
Новые члены: PlaceHolderMode
PresetLayoutConfig
Новые члены: MixInputType, PlaceImageId

## Release 3

Время выпуска: 2020-12-21 17:07:47

Обновления выпуска:

Улучшение существующей документации.

Новые API:

DescribeUserInformation

Новые структуры данных:

PresetLayoutConfig

Измененные структуры данных:

LayoutParams
Новые члены: PresetLayoutConfig

## Release 2

Время выпуска: 2020-09-25 11:41:53

Обновления выпуска:

Улучшение существующей документации.

Измененные API:

DescribeCallDetail
Новые входные параметры: PageNumber, PageSize

Измененные структуры данных:

LayoutParams
Новые члены: MixVideoUids

## Существующий выпуск

Время выпуска: 2020-07-30 20:35:23

Существующие API и структуры данных:

Улучшение существующей документации.

Существующие API:

CreateTroubleInfo
DescribeAbnormalEvent
DescribeCallDetail
DescribeDetailEvent
DescribeHistoryScale
DescribeRealtimeNetwork
DescribeRealtimeQuality
DescribeRealtimeScale
DescribeRoomInformation
DismissRoom
RemoveUser
StartMCUMixTranscode
StopMCUMixTranscode

Существующие структуры данных:

AbnormalEvent
AbnormalExperience
EncodeParams
EventList
EventMessage
LayoutParams
OutputParams
QualityData
RealtimeData
RoomState
ScaleInfomation
SmallVideoLayoutParams
TimeValue
UserInformation


---
*Источник: [https://trtc.io/document/38192](https://trtc.io/document/38192)*

---
*Источник (EN): [history.md](./history.md)*
