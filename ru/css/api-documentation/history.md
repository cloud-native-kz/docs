# История

## Release 39

Время выпуска: 2025-07-10 16:12:06

Обновления выпуска:

Улучшение существующей документации.

Новые API:

CreateLivePadRule

## Release 38

Время выпуска: 2025-07-10 16:10:52

Обновления выпуска:

Улучшение существующей документации.

Новые API:

CreateLivePadTemplate

## Release 37

Время выпуска: 2025-07-07 11:26:29

Обновления выпуска:

Улучшение существующей документации.

Новые API:

StopLivePadStream

## Release 36

Время выпуска: 2025-07-01 20:14:06

Обновления выпуска:

Улучшение существующей документации.

Новые API:

StartLivePadStream

## Release 35

Время выпуска: 2023-09-20 11:38:24

Обновления выпуска:

Улучшение существующей документации.

Новые API:

RestartLivePullStreamTask

## Release 34

Время выпуска: 2023-09-20 10:28:23

Обновления выпуска:

Улучшение существующей документации.

Измененные структуры данных:

PullStreamTaskInfo
Новые члены: RecordTemplateId, BackupToUrl

## Release 33

Время выпуска: 2023-07-25 15:54:49

Обновления выпуска:

Улучшение существующей документации.

Новые API:

DescribeRecordTask

Новые структуры данных:

RecordTask

## Release 32

Время выпуска: 2023-05-15 11:50:28

Обновления выпуска:

Улучшение существующей документации.

Новые API:

DescribeBillBandwidthAndFluxList

Новые структуры данных:

BillDataInfo

## Release 31

Время выпуска: 2023-04-28 10:49:30

Обновления выпуска:

Улучшение существующей документации.

Новые API:

CreateScreenshotTask

Измененные структуры данных:

CallBackTemplateInfo
Новые члены: AudioAuditNotifyUrl

## Release 30

Время выпуска: 2023-02-21 16:13:45

Обновления выпуска:

Улучшение существующей документации.

Новые API:

CreateLiveTimeShiftRule
CreateLiveTimeShiftTemplate
DeleteLiveTimeShiftRule
DeleteLiveTimeShiftTemplate
DescribeLiveTimeShiftRules
DescribeLiveTimeShiftTemplates
DescribeTimeShiftRecordDetail
DescribeTimeShiftStreamList
ModifyLiveTimeShiftTemplate

Новые структуры данных:

TimeShiftRecord
TimeShiftStreamInfo
TimeShiftTemplate

## Release 29

Время выпуска: 2023-01-17 17:37:46

Обновления выпуска:

Улучшение существующей документации.

Измененные структуры данных:

CallBackRuleInfo
Измененные члены:
CreateTime, UpdateTime, TemplateId, DomainName, AppName
CertInfo
Измененные члены:
CertId, CertName, Description, CreateTime, HttpsCrt, CertType, CertExpireTime, DomainList
DomainCertInfo
Измененные члены:
CertId, CertName, Description, CreateTime, HttpsCrt, CertType, CertExpireTime, DomainName, Status, CertDomains, CloudCertId
DomainInfo
Измененные члены:
Name, Type, Status, CreateTime, BCName, TargetDomain, PlayType, IsDelayLive, CurrentCName, RentTag, RentExpireTime, IsMiniProgramLive
ForbidStreamInfo
Измененные члены:
StreamName, CreateTime, ExpireTime, AppName, DomainName
LiveDomainCertBindings
Измененные члены:
DomainName, CertificateAlias, CertType, Status, CertExpireTime, CertId, CloudCertId, UpdateTime
RuleInfo
Измененные члены:
CreateTime, UpdateTime, TemplateId, DomainName, AppName, StreamName
WatermarkInfo
Измененные члены:
WatermarkId, PictureUrl, XPosition, YPosition, WatermarkName, Status, CreateTime, Width, Height

## Release 28

Время выпуска: 2023-01-03 15:23:15

Обновления выпуска:

Улучшение существующей документации.

Новые API:

DescribeAllStreamPlayInfoList
DescribeStreamPushInfoList

Измененные API:

CreateLiveCallbackTemplate
Новые входные параметры: PushExceptionNotifyUrl
ModifyLiveCallbackTemplate
Новые входные параметры: PushExceptionNotifyUrl

Новые структуры данных:

MonitorStreamPlayInfo
PushQualityData

Измененные структуры данных:

CallBackTemplateInfo
Новые члены: PushExceptionNotifyUrl

## Release 27

Время выпуска: 2022-11-16 17:08:10

Обновления выпуска:

Улучшение существующей документации.

Измененные API:

CreateLivePullStreamTask
Новые входные параметры: VodLocalMode
ModifyLivePullStreamTask
Новые входные параметры: VodLocalMode

Измененные структуры данных:

PullStreamTaskInfo
Новые члены: VodLocalMode

## Release 26

Время выпуска: 2022-11-08 11:19:20

Обновления выпуска:

Улучшение существующей документации.

Новые API:

DropLiveStream

Измененные структуры данных:

TranscodeDetailInfo
Новые члены: MainlandOrOversea

## Release 25

Время выпуска: 2022-10-08 11:02:57

Обновления выпуска:

Улучшение существующей документации.

Новые API:

AuthenticateDomainOwner
DescribeTranscodeTaskNum

Измененные API:

AddLiveDomain
Новые входные параметры: VerifyOwnerType
ModifyLiveSnapshotTemplate
Измененные входные параметры:
CosAppId, CosBucket, CosRegion

Новые структуры данных:

TranscodeTaskNum

## Release 24

Время выпуска: 2022-08-31 10:17:40

Обновления выпуска:

Улучшение существующей документации.

Измененные API:

ModifyLivePullStreamTask
Новые входные параметры: WatermarkList

Измененные структуры данных:

PullPushWatermarkInfo
Новые члены: Location
Удаленные члены:
WatermarkId, WatermarkName, Status, CreateTime
PullStreamTaskInfo
Новые члены: BackupSourceType, BackupSourceUrl, WatermarkList

## Release 23

Время выпуска: 2022-08-23 14:24:31

Обновления выпуска:

Улучшение существующей документации.

Новые API:

DescribeLiveDomainCertBindings
ModifyLiveDomainCertBindings

**Удаленные API:**

BindLiveDomainCert
CreateLiveCert
DeleteLiveCert
ModifyLiveCert
ModifyLiveDomainCert

Измененные API:

CreateLivePullStreamTask
Новые входные параметры: WatermarkList
DescribeLiveDomains
Новые выходные параметры: PlayTypeCount

Новые структуры данных:

BatchDomainOperateErrors
LiveCertDomainInfo
LiveDomainCertBindings
PullPushWatermarkInfo

Измененные структуры данных:

ForbidStreamInfo
Новые члены: AppName, DomainName

## Release 22

Время выпуска: 2022-07-06 14:59:45

Обновления выпуска:

Улучшение существующей документации.

Новые API:

CreateLivePullStreamTask
DeleteLivePullStreamTask
DescribeLivePullStreamTasks
ModifyLivePullStreamTask

Новые структуры данных:

PullStreamTaskInfo
RecentPullInfo

## Release 21

Время выпуска: 2022-06-30 15:37:50

Обновления выпуска:

Улучшение существующей документации.

Измененные API:

CreateLiveTranscodeTemplate
Новые входные параметры: DRMType, DRMTracks
ModifyLiveTranscodeTemplate
Новые входные параметры: DRMType, DRMTracks

Измененные структуры данных:

TemplateInfo
Новые члены: DRMType, DRMTracks

## Release 20

Время выпуска: 2022-06-24 15:41:09

Обновления выпуска:

Улучшение существующей документации.

Новые API:

DescribeLiveTimeShiftBillInfoList

Новые структуры данных:

TimeShiftBillData

## Release 19

Время выпуска: 2022-06-15 16:16:30

Обновления выпуска:

Улучшение существующей документации.

**Удаленные API:**

DescribeAllStreamPlayInfoList
DescribeAreaBillBandwidthAndFluxList
DescribeLiveDomainPlayInfoList
DescribeProIspPlaySumInfoList
DropLiveStream

Измененные API:

CreateLiveRecordTemplate
Новые входные параметры: FlvSpecialParam
ModifyLiveRecordTemplate
Новые входные параметры: FlvSpecialParam

Новые структуры данных:

FlvSpecialParam

**Удаленные структуры данных:**

BillAreaInfo
BillCountryInfo
BillDataInfo
DomainDetailInfo
DomainInfoList
MonitorStreamPlayInfo
ProIspPlaySumInfo

Измененные структуры данных:

RecordTemplateInfo
Новые члены: FlvSpecialParam

## Release 18

Время выпуска: 2022-03-31 15:46:30

Обновления выпуска:

Улучшение существующей документации.

**Удаленные API:**

DescribeBillBandwidthAndFluxList
DescribeStreamPushInfoList

Измененные API:

CreateLiveRecordTemplate
Новые входные параметры: RemoveWatermark
ModifyLiveRecordTemplate
Новые входные параметры: RemoveWatermark

**Удаленные структуры данных:**

PushQualityData

Измененные структуры данных:

RecordTemplateInfo
Новые члены: RemoveWatermark

## Release 17

Время выпуска: 2022-01-24 14:29:35

Обновления выпуска:

Улучшение существующей документации.

Новые API:

DescribeLiveTranscodeTotalInfo

Новые структуры данных:

TranscodeTotalInfo

## Release 16

Время выпуска: 2022-01-19 14:55:06

Обновления выпуска:

Улучшение существующей документации.

Измененные API:

DescribeBillBandwidthAndFluxList
Новые входные параметры: RegionNames

## Release 15

Время выпуска: 2021-11-10 17:38:35

Обновления выпуска:

Улучшение существующей документации.

Измененные API:

DescribeLiveDomains
Новые входные параметры: PlayType

## Release 14

Время выпуска: 2021-09-14 10:19:36

Обновления выпуска:

Улучшение существующей документации.

Измененные API:

DescribeLiveDomains
Новые выходные параметры: CreateLimitCount

## Release 13

Время выпуска: 2021-08-06 15:40:33

Обновления выпуска:

Улучшение существующей документации.

Измененные API:

UnBindLiveDomainCert
Новые входные параметры: Type

## Release 12

Время выпуска: 2021-07-19 16:40:55

Обновления выпуска:

Улучшение существующей документации.

Измененные структуры данных:

RecordParam
Новые члены: Procedure, StorageMode, ClassId

## Release 11

Время выпуска: 2021-06-04 11:41:54

Обновления выпуска:

Улучшение существующей документации.

Новые API:

DescribeLiveDomainReferer
ModifyLiveDomainReferer

Новые структуры данных:

RefererAuthConfig

## Release 10

Время выпуска: 2021-05-12 19:12:07

Обновления выпуска:

Улучшение существующей документации.

Измененные API:

DescribeAllStreamPlayInfoList
Новые входные параметры: PlayDomains
DescribeStreamDayPlayInfoList
Новые входные параметры: MainlandOrOversea, ServiceName

## Release 9

Время выпуска: 2021-05-10 14:50:39

Обновления выпуска:

Улучшение существующей документации.

Измененные API:

DescribeLiveForbidStreamList
Новые входные параметры: StreamName

Измененные структуры данных:

CommonMixControlParams
Новые члены: PassInputSei

## Release 8

Время выпуска: 2021-04-15 16:24:25

Обновления выпуска:

Улучшение существующей документации.

Измененные структуры данных:

PushQualityData
Новые члены: StreamParam

## Release 7

Время выпуска: 2021-02-03 17:31:24

Обновления выпуска:

Улучшение существующей документации.

Измененные API:

DescribeStreamPlayInfoList
Новые входные параметры: ServiceName

## Release 6

Время выпуска: 2021-01-27 15:16:31

Обновления выпуска:

Улучшение существующей документации.

Новые API:

DescribeUploadStreamNums

Измененные API:

DescribeProvinceIspPlayInfoList
Новые входные параметры: IpType

## Release 5

Время выпуска: 2021-01-07 19:36:46

Обновления выпуска:

Улучшение существующей документации.

Измененные структуры данных:

DomainCertInfo
Новые члены: CertDomains, CloudCertId

## Release 4

Время выпуска: 2020-10-16 18:30:51

Обновления выпуска:

Улучшение существующей документации.

Новые API:

DescribeAreaBillBandwidthAndFluxList

Новые структуры данных:

BillAreaInfo
BillCountryInfo

Измененные структуры данных:

TemplateInfo
Новые члены: ShortEdgeAsHeight

## Release 3

Время выпуска: 2020-09-25 11:40:32

Обновления выпуска:

Улучшение существующей документации.

Измененные API:

CreateLiveTranscodeTemplate
Новые входные параметры: ShortEdgeAsHeight
DescribeLiveTranscodeRules
Новые входные параметры: TemplateIds, DomainNames
ModifyLiveTranscodeTemplate
Новые входные параметры: ShortEdgeAsHeight

## Release 2

Время выпуска: 2020-08-06 19:42:55

Обновления выпуска:

Улучшение существующей документации.

Новые API:

DescribeDeliverBandwidthList

Новые структуры данных:

BandwidthInfo

Измененные структуры данных:

CommonMixControlParams
Новые члены: AllowCopy

## Существующий выпуск

Время выпуска: 2020-07-30 20:02:43

Существующие API и структуры данных следующие:

Улучшение существующей документации.

Существующие API:

AddDelayLiveStream
AddLiveDomain
AddLiveWatermark
BindLiveDomainCert
CancelCommonMixStream
CreateCommonMixStream
CreateLiveCallbackRule
CreateLiveCallbackTemplate
CreateLiveCert
CreateLiveRecord
CreateLiveRecordRule
CreateLiveRecordTemplate
CreateLiveSnapshotRule
CreateLiveSnapshotTemplate
CreateLiveTranscodeRule
CreateLiveTranscodeTemplate
CreateLiveWatermarkRule
CreateRecordTask
DeleteLiveCallbackRule
DeleteLiveCallbackTemplate
DeleteLiveCert
DeleteLiveDomain
DeleteLiveRecord
DeleteLiveRecordRule
DeleteLiveRecordTemplate
DeleteLiveSnapshotRule
DeleteLiveSnapshotTemplate
DeleteLiveTranscodeRule
DeleteLiveTranscodeTemplate
DeleteLiveWatermark
DeleteLiveWatermarkRule
DeleteRecordTask
DescribeAllStreamPlayInfoList
DescribeBillBandwidthAndFluxList
DescribeConcurrentRecordStreamNum
DescribeGroupProIspPlayInfoList
DescribeHttpStatusInfoList
DescribeLiveCallbackRules
DescribeLiveCallbackTemplate
DescribeLiveCallbackTemplates
DescribeLiveCert
DescribeLiveCerts
DescribeLiveDelayInfoList
DescribeLiveDomain
DescribeLiveDomainCert
DescribeLiveDomainPlayInfoList
DescribeLiveDomains
DescribeLiveForbidStreamList
DescribeLivePlayAuthKey
DescribeLivePushAuthKey
DescribeLiveRecordRules
DescribeLiveRecordTemplate
DescribeLiveRecordTemplates
DescribeLiveSnapshotRules
DescribeLiveSnapshotTemplate
DescribeLiveSnapshotTemplates
DescribeLiveStreamEventList
DescribeLiveStreamOnlineList
DescribeLiveStreamPublishedList
DescribeLiveStreamPushInfoList
DescribeLiveStreamState
DescribeLiveTranscodeDetailInfo
DescribeLiveTranscodeRules
DescribeLiveTranscodeTemplate
DescribeLiveTranscodeTemplates
DescribeLiveWatermark
DescribeLiveWatermarkRules
DescribeLiveWatermarks
DescribePlayErrorCodeDetailInfoList
DescribePlayErrorCodeSumInfoList
DescribeProIspPlaySumInfoList
DescribeProvinceIspPlayInfoList
DescribeScreenShotSheetNumList
DescribeStreamDayPlayInfoList
DescribeStreamPlayInfoList
DescribeStreamPushInfoList
DescribeTopClientIpSumInfoList
DescribeVisitTopSumInfoList
DropLiveStream
EnableLiveDomain
ForbidLiveDomain
ForbidLiveStream
ModifyLiveCallbackTemplate
ModifyLiveCert
ModifyLiveDomainCert
ModifyLivePlayAuthKey
ModifyLivePlayDomain
ModifyLivePushAuthKey
ModifyLiveRecordTemplate
ModifyLiveSnapshotTemplate
ModifyLiveTranscodeTemplate
ResumeDelayLiveStream
ResumeLiveStream
StopLiveRecord
StopRecordTask
UnBindLiveDomainCert
UpdateLiveWatermark

Существующие структуры данных:

BillDataInfo
CallBackRuleInfo
CallBackTemplateInfo
CdnPlayStatData
CertInfo
ClientIpPlaySumInfo
CommonMixControlParams
CommonMixCropParams
CommonMixInputParam
CommonMixLayoutParams
CommonMixOutputParams
ConcurrentRecordStreamNum
DayStreamPlayInfo
DelayInfo
DomainCertInfo
DomainDetailInfo
DomainInfo
DomainInfoList
ForbidStreamInfo
GroupProIspDataInfo
HlsSpecialParam
HttpCodeInfo
HttpCodeValue
HttpStatusData
HttpStatusInfo
MonitorStreamPlayInfo
PlayAuthKeyInfo
PlayCodeTotalInfo
PlayDataInfoByStream
PlayStatInfo
PlaySumStatInfo
ProIspPlayCodeDataInfo
ProIspPlaySumInfo
PublishTime
PushAuthKeyInfo
PushDataInfo
PushQualityData
RecordParam
RecordTemplateInfo
RuleInfo
SnapshotTemplateInfo
StreamEventInfo
StreamName
StreamOnlineInfo
TemplateInfo
TimeValue
TranscodeDetailInfo
WatermarkInfo


---
*Источник: [https://www.tencentcloud.com/document/product/267/30766](https://www.tencentcloud.com/document/product/267/30766)*

---
*Источник (EN): [history.md](./history.md)*
