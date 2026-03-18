# История

## Релиз 60

Время релиза: 2026-02-25 15:13:48

Обновления релиза:

Улучшение существующей документации.

Новые API:

SyncDubbing

Измененные API:

CreateAigcVideoTask
Новые входные параметры: VideoInfos
CreateBlindWatermarkTemplate
Новые входные параметры: Strength
CreateProcessImageTemplate
Новые входные параметры: StdExtInfo
ModifyBlindWatermarkTemplate
Новые входные параметры: Strength
ParseLiveStreamProcessNotification
Новые выходные параметры: AiSmartSubtitleResultInfo
ProcessImage
Новые входные параметры: StdExtInfo
ProcessLiveStream
Новые входные параметры: SmartSubtitlesTask

Новые структуры данных:

AigcVideoReferenceVideoInfo
LiveSmartSubtitleResult
LiveSmartSubtitlesTaskInput
LiveStreamAiSmartSubtitleResultInfo
VideoComprehensionResultItem

Измененные структуры данных:

AiAnalysisTaskReelOutput
Новые члены: VideoPaths
AiAnalysisTaskVideoComprehensionOutput
Новые члены: VideoComprehensionExtInfo, VideoComprehensionResultList
BlindWatermarkTemplate
Новые члены: Strength
ScheduleQualityControlTaskResult
Новые члены: Progress
SubtitleTemplate
Новые члены: FontFileInput, BoardWidthUnit, BoardHeightUnit, OutlineWidthUnit, ShadowWidthUnit, LineSpacingUnit

## Релиз 59

Время релиза: 2026-02-02 11:45:53

Обновления релиза:

Улучшение существующей документации.

Новые API:

RecognizeAudio

Измененные API:

CreateAigcVideoTask
Новые входные параметры: SceneType
CreateSmartSubtitleTemplate
Новые входные параметры: SelectingSubtitleAreasConfig
ModifySmartSubtitleTemplate
Новые входные параметры: SelectingSubtitleAreasConfig

Новые структуры данных:

AiAnalysisTaskCutoutInput
AiAnalysisTaskCutoutOutput
AiAnalysisTaskCutoutResult
AiAnalysisTaskReelInput
AiAnalysisTaskReelOutput
AiAnalysisTaskReelResult
RecognizeAudioSentence

Измененные структуры данных:

AdvancedSuperResolutionConfig
Новые члены: LongSide, ShortSide
AiAnalysisResult
Новые члены: CutoutTask, ReelTask
AiAnalysisTaskDubbingOutput
Новые члены: VoiceId
AigcVideoExtraParam
Новые члены: LogoAdd, EnableAudio, OffPeak
ImageProcessTaskOutput
Новые члены: Content
SmartSubtitleTaskAsrFullTextSegmentItem
Новые члены: SpeakerId
SmartSubtitleTemplateItem
Новые члены: SelectingSubtitleAreasConfig

## Релиз 58

Время релиза: 2026-01-08 15:02:34

Обновления релиза:

Улучшение существующей документации.

Новые API:

CreateAigcImageTask
CreateAigcVideoTask
DescribeAigcImageTask
DescribeAigcVideoTask

Новые структуры данных:

AigcImageExtraParam
AigcImageInfo
AigcStoreCosParam
AigcVideoExtraParam
AigcVideoReferenceImageInfo

## Релиз 57

Время релиза: 2025-12-30 17:49:48

Обновления релиза:

Улучшение существующей документации.

Новые API:

TextTranslation

Новые структуры данных:

SelectingSubtitleAreasConfig
SmartSubtitleTaskFullTextResult
SmartSubtitleTaskTextResultOutput
SubtitleResult

Измененные структуры данных:

RawSmartSubtitleParameter
Новые члены: SelectingSubtitleAreasConfig
SmartSubtitlesResult
Новые члены: OcrFullTextTask

## Релиз 56

Время релиза: 2025-12-16 15:41:29

Обновления релиза:

Улучшение существующей документации.

Новые API:

DescribeUsageData

Новые структуры данных:

SpecificationDataItem
TaskStatData
TaskStatDataItem

Измененные структуры данных:

MediaAiAnalysisDescriptionItem
Новые члены: MindMapPath, SubtitlePath, OutputStorage

## Релиз 55

Время релиза: 2025-12-02 14:25:01

Обновления релиза:

Улучшение существующей документации.

Новые API:

CreateBlindWatermarkTemplate
CreateProcessImageTemplate
DeleteBlindWatermarkTemplate
DeleteProcessImageTemplate
DescribeBlindWatermarkTemplates
DescribeProcessImageTemplates
ExtractBlindWatermark
ModifyBlindWatermarkTemplate
ModifyProcessImageTemplate

Измененные API:

DescribeSmartEraseTemplates
Новые входные параметры: EraseType
ParseNotification
Новые выходные параметры: ExtractBlindWatermarkTask
ProcessImage
Новые входные параметры: Definition, ResourceId

Новые структуры данных:

BlindWatermarkInput
BlindWatermarkTemplate
LiveAiAnalysisDescriptionItem
LiveAiParagraphInfo
ProcessImageTemplate

Измененные структуры данных:

AdaptiveDynamicStreamingTaskInput
Новые члены: BlindWatermark
ImageAreaBoxInfo
Новые члены: BoundingBoxUnitType
LiveStreamAiAnalysisResultInfo
Измененные члены: ResultSet
LiveStreamAiAnalysisResultItem
Новые члены: DescriptionResult
TranscodeTaskInput
Новые члены: BlindWatermark

## Релиз 54

Время релиза: 2025-11-13 11:59:51

Обновления релиза:

Улучшение существующей документации.

Измененные API:

CreateSmartSubtitleTemplate
Новые входные параметры: ProcessType
DescribeImageTaskDetail
Новые выходные параметры: ErrCode, ErrMsg, Message
DescribeSmartSubtitleTemplates
Новые входные параметры: ProcessType
DescribeTranscodeTemplates
Новые входные параметры: EnhanceSceneType, EnhanceTranscodeType, EnhanceType
ModifySmartSubtitleTemplate
Новые входные параметры: ProcessType

Новые структуры данных:

AdvancedSuperResolutionConfig
AiAnalysisTaskVideoComprehensionInput
AiAnalysisTaskVideoComprehensionOutput
AiAnalysisTaskVideoComprehensionResult
DiffusionEnhanceConfig
FrameRateWithDenConfig
OverrideEraseParameter
PureSubtitleTransResult
PureSubtitleTransResultOutput
SubtitleTransResultItem
UpdateSmartErasePrivacyConfig
UpdateSmartEraseSubtitleConfig
UpdateSmartEraseWatermarkConfig

Измененные структуры данных:

AiAnalysisResult
Новые члены: VideoComprehensionTask
ImageEnhanceConfig
Новые члены: AdvancedSuperResolutionConfig
ImageProcessTaskResult
Новые члены: ErrMsg
RawSmartSubtitleParameter
Новые члены: ProcessType
SmartEraseTaskInput
Новые члены: OverrideParameter
SmartSubtitleTaskAsrFullTextResultOutput
Новые члены: Path
SmartSubtitleTaskTransTextResultOutput
Новые члены: Path, SubtitleResults
SmartSubtitleTemplateItem
Новые члены: ProcessType
SmartSubtitlesResult
Новые члены: PureSubtitleTransTask
VideoEnhanceConfig
Новые члены: EnhanceSceneType, DiffusionEnhance, FrameRateWithDen

## Релиз 53

Время релиза: 2025-11-12 16:04:25

Обновления релиза:

Улучшение существующей документации.

Измененные структуры данных:

AdaptiveDynamicStreamingTaskInput
Новые члены: KeyPTSList
VideoEnhanceConfig
Удаленные члены: SharpEnhance, FaceEnhance

## Релиз 52

Время релиза: 2025-10-13 10:32:30

Обновления релиза:

Улучшение существующей документации.

Измененные API:

DescribeTasks
Новые входные параметры: SubTaskHasFailed
ParseNotification
Новые выходные параметры: BatchTaskEvent

Новые структуры данных:

AiAnalysisTaskVideoRemakeInput
AiAnalysisTaskVideoRemakeOutput
AiAnalysisTaskVideoRemakeResult

Измененные структуры данных:

AddOnSubtitle
Новые члены: OutputFormat, DefaultTrack
AiAnalysisResult
Новые члены: VideoRemakeTask

## Релиз 51

Время релиза: 2025-09-29 11:47:20

Обновления релиза:

Улучшение существующей документации.

Новые API:

CreateSmartEraseTemplate
DeleteSmartEraseTemplate
DescribeSmartEraseTemplates
ModifySmartEraseTemplate

Новые структуры данных:

SmartEraseTemplateItem

## Релиз 50

Время релиза: 2025-09-24 14:57:53

Обновления релиза:

Улучшение существующей документации.

Измененные API:

ProcessImage
Новые входные параметры: OutputPath

## Релиз 49

Время релиза: 2025-09-19 15:38:37

Обновления релиза:

Улучшение существующей документации.

Измененные API:

DescribeTaskDetail
Новые выходные параметры: ExtractBlindWatermarkTask
ProcessMedia
Новые входные параметры: SmartEraseTask

Новые структуры данных:

AiAnalysisTaskDubbingInput
AiAnalysisTaskDubbingOutput
AiAnalysisTaskDubbingResult
EraseArea
EraseTimeArea
ExtractBlindWatermarkTask
ExtractBlindWatermarkTaskConfig
RawSmartEraseParameter
SmartErasePrivacyConfig
SmartEraseSubtitleConfig
SmartEraseTaskInput
SmartEraseTaskResult
SmartEraseWatermarkConfig
VODInputInfo
VODOutputStorage

Измененные структуры данных:

ActivityPara
Новые члены: SmartEraseTask
ActivityResItem
Новые члены: SmartEraseTask
AiAnalysisResult
Новые члены: DubbingTask
AiAnalysisTaskDelLogoOutput
Новые члены: VoiceClonedVideo, VoiceClonedMarkFile
MediaInputInfo
Новые члены: VODInputInfo
SmartSubtitleTaskAsrFullTextResultOutput
Новые члены: OutputStorage
SmartSubtitleTaskTransTextResultOutput
Новые члены: OutputStorage
TaskOutputStorage
Новые члены: VODOutputStorage
WorkflowTask
Новые члены: SmartEraseTaskResult

## Релиз 48

Время релиза: 2025-08-26 19:44:12

Обновления релиза:

Улучшение существующей документации.

Измененные API:

CreateLiveRecordTemplate
Новые входные параметры: RecordType
ModifyLiveRecordTemplate
Новые входные параметры: RecordType

Измененные структуры данных:

HighlightSegmentItem
Новые члены: Title, Summary
LiveRecordTemplate
Новые члены: RecordType
LiveStreamAiAnalysisResultItem
Новые члены: HighlightResultSet
MediaAiAnalysisHighlightItem
Новые члены: HighlightUrl, CovImgUrl
RawTranscodeParameter
Новые члены: SubtitleTemplate
SubtitleTemplate
Новые члены: SubtitleFileInput, OutlineWidth, OutlineColor, OutlineAlpha, ShadowWidth, ShadowColor, ShadowAlpha, LineSpacing, Alignment

## Релиз 47

Время релиза: 2025-08-04 17:36:22

Обновления релиза:

Улучшение существующей документации.

Измененные API:

CreateQualityControlTemplate
Новые входные параметры: Strategy
DescribeTasks
Новые входные параметры: StartTime, EndTime
ModifyQualityControlTemplate
Новые входные параметры: Strategy

Новые структуры данных:

ExecRuleTaskData
ExecRulesTask
QualityControlStrategy
RuleConditionItem
Rules
ScheduleExecRuleTaskResult
SubtitlePosition
TimeSpotCheck

Измененные структуры данных:

ActivityPara
Новые члены: ExecRulesTask
ActivityResItem
Новые члены: ExecRuleTask
AiAnalysisTaskDelLogoOutput
Новые члены: SubtitlePos
MediaAiAnalysisTagItem
Новые члены: SpecialInfo
QualityControlTemplate
Новые члены: Strategy
ScheduleAnalysisTaskResult
Новые члены: BeginProcessTime, FinishTime
SmartSubtitlesTaskInput
Новые члены: OutputStorage, OutputObjectPath

## Релиз 46

Время релиза: 2025-07-30 16:07:32

Обновления релиза:

Улучшение существующей документации.

Измененные структуры данных:

AdaptiveDynamicStreamingTaskInput
Новые члены: StdExtInfo
ScheduleTask
Измененные члены: ErrCode, Message

## Релиз 45

Время релиза: 2025-07-23 14:31:19

Обновления релиза:

Улучшение существующей документации.

Измененные структуры данных:

AdaptiveDynamicStreamingTaskInput
Измененные члены: SubtitleTemplate

## Релиз 44

Время релиза: 2025-07-22 14:47:39

Обновления релиза:

Улучшение существующей документации.

Измененные структуры данных:

AdaptiveDynamicStreamingTaskInput
Новые члены: SubtitleTemplate

## Релиз 43

Время релиза: 2025-07-22 14:39:50

Обновления релиза:

Улучшение существующей документации.

Измененные API:

CreateQualityControlTemplate
Новые входные параметры: RecordFormat
ModifyQualityControlTemplate
Новые входные параметры: RecordFormat

Измененные структуры данных:

LiveStreamAsrFullTextRecognitionResult
Новые члены: StartTime, EndTime, SteadyState, UserId
LiveStreamTransTextRecognitionResult
Новые члены: StartTime, EndTime, SteadyState, UserId
MediaAiAnalysisDescriptionItem
Новые члены: MindMapUrl
MediaProcessTaskImageSpriteResult
Новые члены: BeginProcessTime, FinishTime
ScheduleRecognitionTaskResult
Новые члены: BeginProcessTime, FinishTime
SubtitleTemplate
Новые члены: YPos, BoardY, BoardWidth, BoardHeight, BoardColor, BoardAlpha

## Релиз 42

Время релиза: 2025-06-23 15:42:21

Обновления релиза:

Улучшение существующей документации.

Измененные структуры данных:

MediaProcessTaskSampleSnapshotResult
Новые члены: BeginProcessTime, FinishTime
MediaProcessTaskSnapshotByTimeOffsetResult
Новые члены: BeginProcessTime, FinishTime

## Релиз 41

Время релиза: 2025-06-12 19:42:40

Обновления релиза:

Улучшение существующей документации.

Новые API:

BatchProcessMedia
DescribeBatchTaskDetail
DescribeImageTaskDetail

Новые структуры данных:

BatchSmartSubtitlesResult
BatchSubTaskResult
ImageDenoiseConfig
ImageProcessTaskOutput
ImageProcessTaskResult
SmartSubtitleTaskBatchOutput

Измененные структуры данных:

ImageEnhanceConfig
Новые члены: Denoise, ImageQualityEnhance, LowLightEnhance
RawTranscodeParameter
Новые члены: StdExtInfo, EnhanceConfig

## Релиз 40

Время релиза: 2025-05-24 19:19:43

Обновления релиза:

Улучшение существующей документации.

Измененные API:

CreateLiveRecordTemplate
Новые входные параметры: MP4Configure
Измененные входные параметры: HLSConfigure
CreateTranscodeTemplate
Новые входные параметры: StdExtInfo
ModifyLiveRecordTemplate
Новые входные параметры: MP4Configure

Новые структуры данных:

ImageAreaBoxInfo
ImageEraseConfig
ImageEraseLogoConfig
MP4ConfigureInfo

Измененные структуры данных:

ImageTaskInput
Новые члены: EraseConfig
LiveRecordTemplate
Новые члены: MP4Configure
QualityControlData
Новые члены: QualityEvaluationMeanOpinionScore
WordResult
Новые члены: Trans

## Релиз 39

Время релиза: 2025-04-14 17:49:13

Обновления релиза:

Улучшение существующей документации.

Измененные структуры данных:

AiAnalysisTaskHeadTailOutput
Измененные члены: TailTimeOffset

## Релиз 38

Время релиза: 2025-04-02 19:39:18

Обновления релиза:

Улучшение существующей документации.

Новые API:

CreateAIAnalysisTemplate
CreateAIRecognitionTemplate
CreateAdaptiveDynamicStreamingTemplate
CreateAnimatedGraphicsTemplate
CreateAsrHotwords
CreateContentReviewTemplate
CreateImageSpriteTemplate
CreateLiveRecordTemplate
CreatePersonSample
CreateQualityControlTemplate
CreateSampleSnapshotTemplate
CreateSchedule
CreateSmartSubtitleTemplate
CreateSnapshotByTimeOffsetTemplate
CreateTranscodeTemplate
CreateWatermarkTemplate
CreateWordSamples
CreateWorkflow
DeleteAIAnalysisTemplate
DeleteAIRecognitionTemplate
DeleteAdaptiveDynamicStreamingTemplate
DeleteAnimatedGraphicsTemplate
DeleteAsrHotwords
DeleteContentReviewTemplate
DeleteImageSpriteTemplate
DeleteLiveRecordTemplate
DeletePersonSample
DeleteQualityControlTemplate
DeleteSampleSnapshotTemplate
DeleteSchedule
DeleteSmartSubtitleTemplate
DeleteSnapshotByTimeOffsetTemplate
DeleteTranscodeTemplate
DeleteWatermarkTemplate
DeleteWordSamples
DeleteWorkflow
DescribeAIAnalysisTemplates
DescribeAIRecognitionTemplates
DescribeAdaptiveDynamicStreamingTemplates
DescribeAnimatedGraphicsTemplates
DescribeAsrHotwords
DescribeAsrHotwordsList
DescribeContentReviewTemplates
DescribeImageSpriteTemplates
DescribeLiveRecordTemplates
DescribeMediaMetaData
DescribePersonSamples
DescribeQualityControlTemplates
DescribeSampleSnapshotTemplates
DescribeSchedules
DescribeSmartSubtitleTemplates
DescribeSnapshotByTimeOffsetTemplates
DescribeStreamLinkSecurityGroup
DescribeTaskDetail
DescribeTasks
DescribeTranscodeTemplates
DescribeWatermarkTemplates
DescribeWordSamples
DescribeWorkflows
DisableSchedule
DisableWorkflow
EditMedia
EnableSchedule
EnableWorkflow
ExecuteFunction
ManageTask
ModifyAIAnalysisTemplate
ModifyAIRecognitionTemplate
ModifyAdaptiveDynamicStreamingTemplate
ModifyAnimatedGraphicsTemplate
ModifyAsrHotwords
ModifyContentReviewTemplate
ModifyImageSpriteTemplate
ModifyLiveRecordTemplate
ModifyPersonSample
ModifyQualityControlTemplate
ModifySampleSnapshotTemplate
ModifySchedule
ModifySmartSubtitleTemplate
ModifySnapshotByTimeOffsetTemplate
ModifyTranscodeTemplate
ModifyWatermarkTemplate
ModifyWordSample
ParseLiveStreamProcessNotification
ParseNotification
ProcessImage
ProcessLiveStream
ResetWorkflow

Новые структуры данных:

AIAnalysisTemplateItem
AIRecognitionTemplateItem
Activity
ActivityPara
ActivityResItem
ActivityResult
AdaptiveDynamicStreamingInfoItem
AdaptiveDynamicStreamingTemplate
AdaptiveStreamTemplate
AiAnalysisResult
AiAnalysisTaskClassificationInput
AiAnalysisTaskClassificationOutput
AiAnalysisTaskClassificationResult
AiAnalysisTaskCoverInput
AiAnalysisTaskCoverOutput
AiAnalysisTaskCoverResult
AiAnalysisTaskDelLogoInput
AiAnalysisTaskDelLogoOutput
AiAnalysisTaskDelLogoResult
AiAnalysisTaskDescriptionInput
AiAnalysisTaskDescriptionOutput
AiAnalysisTaskDescriptionResult
AiAnalysisTaskFrameTagInput
AiAnalysisTaskFrameTagOutput
AiAnalysisTaskFrameTagResult
AiAnalysisTaskHeadTailInput
AiAnalysisTaskHeadTailOutput
AiAnalysisTaskHeadTailResult
AiAnalysisTaskHighlightInput
AiAnalysisTaskHighlightOutput
AiAnalysisTaskHighlightResult
AiAnalysisTaskHorizontalToVerticalInput
AiAnalysisTaskHorizontalToVerticalOutput
AiAnalysisTaskHorizontalToVerticalResult
AiAnalysisTaskSegmentInput
AiAnalysisTaskSegmentOutput
AiAnalysisTaskSegmentResult
AiAnalysisTaskTagInput
AiAnalysisTaskTagOutput
AiAnalysisTaskTagResult
AiContentReviewResult
AiParagraphInfo
AiRecognitionResult
AiRecognitionTaskAsrFullTextResult
AiRecognitionTaskAsrFullTextResultInput
AiRecognitionTaskAsrFullTextResultOutput
AiRecognitionTaskAsrFullTextSegmentItem
AiRecognitionTaskAsrWordsResult
AiRecognitionTaskAsrWordsResultInput
AiRecognitionTaskAsrWordsResultItem
AiRecognitionTaskAsrWordsResultOutput
AiRecognitionTaskAsrWordsSegmentItem
AiRecognitionTaskFaceResult
AiRecognitionTaskFaceResultInput
AiRecognitionTaskFaceResultItem
AiRecognitionTaskFaceResultOutput
AiRecognitionTaskFaceSegmentItem
AiRecognitionTaskObjectResult
AiRecognitionTaskObjectResultInput
AiRecognitionTaskObjectResultItem
AiRecognitionTaskObjectResultOutput
AiRecognitionTaskObjectSeqmentItem
AiRecognitionTaskOcrFullTextResult
AiRecognitionTaskOcrFullTextResultInput
AiRecognitionTaskOcrFullTextResultOutput
AiRecognitionTaskOcrFullTextSegmentItem
AiRecognitionTaskOcrFullTextSegmentTextItem
AiRecognitionTaskOcrWordsResult
AiRecognitionTaskOcrWordsResultInput
AiRecognitionTaskOcrWordsResultItem
AiRecognitionTaskOcrWordsResultOutput
AiRecognitionTaskOcrWordsSegmentItem
AiRecognitionTaskTransTextResult
AiRecognitionTaskTransTextResultInput
AiRecognitionTaskTransTextResultOutput
AiRecognitionTaskTransTextSegmentItem
AiReviewPoliticalAsrTaskInput
AiReviewPoliticalAsrTaskOutput
AiReviewPoliticalOcrTaskInput
AiReviewPoliticalOcrTaskOutput
AiReviewPoliticalTaskInput
AiReviewPoliticalTaskOutput
AiReviewPornAsrTaskInput
AiReviewPornAsrTaskOutput
AiReviewPornOcrTaskInput
AiReviewPornOcrTaskOutput
AiReviewPornTaskInput
AiReviewPornTaskOutput
AiReviewProhibitedAsrTaskInput
AiReviewProhibitedAsrTaskOutput
AiReviewProhibitedOcrTaskInput
AiReviewProhibitedOcrTaskOutput
AiReviewTaskPoliticalAsrResult
AiReviewTaskPoliticalOcrResult
AiReviewTaskPoliticalResult
AiReviewTaskPornAsrResult
AiReviewTaskPornOcrResult
AiReviewTaskPornResult
AiReviewTaskProhibitedAsrResult
AiReviewTaskProhibitedOcrResult
AiReviewTaskTerrorismOcrResult
AiReviewTaskTerrorismResult
AiReviewTerrorismOcrTaskInput
AiReviewTerrorismOcrTaskOutput
AiReviewTerrorismTaskInput
AiReviewTerrorismTaskOutput
AiSampleFaceInfo
AiSampleFaceOperation
AiSampleFailFaceInfo
AiSamplePerson
AiSampleTagOperation
AiSampleWord
AiSampleWordInfo
AnimatedGraphicsTemplate
ArtifactRepairConfig
AsrFullTextConfigureInfo
AsrFullTextConfigureInfoForUpdate
AsrHotwordsSet
AsrHotwordsSetItem
AsrWordsConfigureInfo
AsrWordsConfigureInfoForUpdate
AudioBeautifyConfig
AudioDenoiseConfig
AudioEnhanceConfig
AudioSeparateConfig
AwsS3FileUploadTrigger
ClassificationConfigureInfo
ClassificationConfigureInfoForUpdate
ColorEnhanceConfig
ComposeAudioItem
ComposeAudioOperation
ComposeAudioStream
ComposeCanvas
ComposeEmptyItem
ComposeImageItem
ComposeImageOperation
ComposeMediaConfig
ComposeMediaItem
ComposeMediaTrack
ComposeSourceMedia
ComposeStyles
ComposeSubtitleItem
ComposeSubtitleStyle
ComposeTargetInfo
ComposeTrackTime
ComposeTransitionItem
ComposeTransitionOperation
ComposeVideoItem
ComposeVideoStream
ContainerDiagnoseResultItem
ContentReviewTemplateItem
CosFileUploadTrigger
CoverConfigureInfo
CoverConfigureInfoForUpdate
DiagnoseResult
EditMediaFileInfo
EditMediaOutputConfig
EditMediaTask
EditMediaTaskInput
EditMediaTaskOutput
EnhanceConfig
FaceConfigureInfo
FaceConfigureInfoForUpdate
FaceEnhanceConfig
FrameRateConfig
FrameTagConfigureInfo
FrameTagConfigureInfoForUpdate
HLSConfigureInfo
HdrConfig
HighlightSegmentItem
ImageEncodeConfig
ImageEnhanceConfig
ImageQualityEnhanceConfig
ImageSpriteTemplate
ImageTaskInput
ImageWatermarkInput
ImageWatermarkInputForUpdate
ImageWatermarkTemplate
LiveActivityResItem
LiveActivityResult
LiveRecordFile
LiveRecordResult
LiveRecordTaskInput
LiveRecordTemplate
LiveScheduleLiveRecordTaskResult
LiveScheduleTask
LiveStreamAiAnalysisResultInfo
LiveStreamAiAnalysisResultItem
LiveStreamAiQualityControlResultInfo
LiveStreamAiRecognitionResultInfo
LiveStreamAiRecognitionResultItem
LiveStreamAiReviewImagePoliticalResult
LiveStreamAiReviewImagePornResult
LiveStreamAiReviewImageTerrorismResult
LiveStreamAiReviewResultInfo
LiveStreamAiReviewResultItem
LiveStreamAiReviewVoicePornResult
LiveStreamAsrFullTextRecognitionResult
LiveStreamAsrWordsRecognitionResult
LiveStreamFaceRecognitionResult
LiveStreamObjectRecognitionResult
LiveStreamOcrFullTextRecognitionResult
LiveStreamOcrWordsRecognitionResult
LiveStreamProcessErrorInfo
LiveStreamProcessTask
LiveStreamRecordResultInfo
LiveStreamTagRecognitionResult
LiveStreamTaskNotifyConfig
LiveStreamTransTextRecognitionResult
LowLightEnhanceConfig
MediaAiAnalysisClassificationItem
MediaAiAnalysisCoverItem
MediaAiAnalysisDescriptionItem
MediaAiAnalysisFrameTagItem
MediaAiAnalysisFrameTagSegmentItem
MediaAiAnalysisHighlightItem
MediaAiAnalysisTagItem
MediaAnimatedGraphicsItem
MediaAudioStreamItem
MediaContentReviewAsrTextSegmentItem
MediaContentReviewOcrTextSegmentItem
MediaContentReviewPoliticalSegmentItem
MediaContentReviewSegmentItem
MediaImageSpriteItem
MediaMetaData
MediaProcessTaskAdaptiveDynamicStreamingResult
MediaProcessTaskAnimatedGraphicResult
MediaProcessTaskImageSpriteResult
MediaProcessTaskResult
MediaProcessTaskSampleSnapshotResult
MediaProcessTaskSnapshotByTimeOffsetResult
MediaProcessTaskTranscodeResult
MediaSampleSnapshotItem
MediaSnapshotByTimeOffsetItem
MediaSnapshotByTimePicInfoItem
MediaTranscodeItem
MediaVideoStreamItem
OcrFullTextConfigureInfo
OcrFullTextConfigureInfoForUpdate
OcrWordsConfigureInfo
OcrWordsConfigureInfoForUpdate
PoliticalAsrReviewTemplateInfo
PoliticalAsrReviewTemplateInfoForUpdate
PoliticalConfigureInfo
PoliticalConfigureInfoForUpdate
PoliticalImgReviewTemplateInfo
PoliticalImgReviewTemplateInfoForUpdate
PoliticalOcrReviewTemplateInfo
PoliticalOcrReviewTemplateInfoForUpdate
PornAsrReviewTemplateInfo
PornAsrReviewTemplateInfoForUpdate
PornConfigureInfo
PornConfigureInfoForUpdate
PornImgReviewTemplateInfo
PornImgReviewTemplateInfoForUpdate
PornOcrReviewTemplateInfo
PornOcrReviewTemplateInfoForUpdate
ProhibitedAsrReviewTemplateInfo
ProhibitedAsrReviewTemplateInfoForUpdate
ProhibitedConfigureInfo
ProhibitedConfigureInfoForUpdate
ProhibitedOcrReviewTemplateInfo
ProhibitedOcrReviewTemplateInfoForUpdate
QualityControlData
QualityControlItem
QualityControlItemConfig
QualityControlResult
QualityControlTemplate
SampleSnapshotTemplate
ScheduleAnalysisTaskResult
ScheduleQualityControlTaskResult
ScheduleRecognitionTaskResult
ScheduleReviewTaskResult
ScheduleSmartSubtitleTaskResult
ScheduleTask
SchedulesInfo
ScratchRepairConfig
SecurityGroupInfo
SegmentRecognitionItem
SharpEnhanceConfig
SmartSubtitleTaskAsrFullTextResult
SmartSubtitleTaskAsrFullTextResultOutput
SmartSubtitleTaskAsrFullTextSegmentItem
SmartSubtitleTaskResultInput
SmartSubtitleTaskTransTextResult
SmartSubtitleTaskTransTextResultOutput
SmartSubtitleTaskTransTextSegmentItem
SmartSubtitleTemplateItem
SmartSubtitlesResult
SnapshotByTimeOffsetTemplate
SuperResolutionConfig
SvgWatermarkInput
SvgWatermarkInputForUpdate
TagConfigureInfo
TagConfigureInfoForUpdate
TaskSimpleInfo

## Release 36

Время выпуска: 2025-03-28 15:36:43

Обновления выпуска:

Улучшение существующей документации.

Новые API:

CreateAsrHotwords
CreateSmartSubtitleTemplate
DeleteAsrHotwords
DeleteSmartSubtitleTemplate
DescribeAsrHotwords
DescribeAsrHotwordsList
DescribeSmartSubtitleTemplates
ModifyAsrHotwords
ModifySmartSubtitleTemplate

Измененные API:

ProcessMedia
Новые входные параметры: ResourceId, SmartSubtitlesTask, SkipMateData

Новые структуры данных:

AsrHotWordsConfigure
AsrHotwordsSet
AsrHotwordsSetItem
AudioTrackChannelInfo
RawSmartSubtitleParameter
ScheduleSmartSubtitleTaskResult
SmartSubtitleTaskAsrFullTextResult
SmartSubtitleTaskAsrFullTextResultOutput
SmartSubtitleTaskAsrFullTextSegmentItem
SmartSubtitleTaskResultInput
SmartSubtitleTaskTransTextResult
SmartSubtitleTaskTransTextResultOutput
SmartSubtitleTaskTransTextSegmentItem
SmartSubtitleTemplateItem
SmartSubtitlesResult
SmartSubtitlesTaskInput
SpekeDrm
TrackInfo

Измененные структуры данных:

ActivityPara
Новые члены: SmartSubtitlesTask
ActivityResItem
Новые члены: SmartSubtitlesTask
AdaptiveStreamTemplate
Новые члены: AudioList
AudioTemplateInfo
Новые члены: TrackChannelInfo
DrmInfo
Новые члены: SpekeDrm
HighlightSegmentItem
Новые члены: BeginTime, EndTime
MediaTranscodeItem
Новые члены: CallBackExtInfo
SegmentRecognitionItem
Новые члены: PersonId
WorkflowTask
Новые члены: SmartSubtitlesTaskResult

## Release 35

Время выпуска: 2025-02-19 14:54:41

Обновления выпуска:

Улучшение существующей документации.

Измененные структуры данных:

AiParagraphInfo
Новые члены: Title, Keywords
MediaAiAnalysisDescriptionItem
Новые члены: Title, Keywords

## Release 34

Время выпуска: 2025-02-05 10:32:43

Обновления выпуска:

Улучшение существующей документации.

Новые API:

DescribeStreamLinkSecurityGroup

Новые структуры данных:

SecurityGroupInfo

## Release 33

Время выпуска: 2024-12-25 18:11:12

Обновления выпуска:

Улучшение существующей документации.

Новые API:

CreateLiveRecordTemplate
DeleteLiveRecordTemplate
DescribeLiveRecordTemplates
ModifyLiveRecordTemplate

Новые структуры данных:

HLSConfigureInfo
LiveRecordTemplate

## Release 32

Время выпуска: 2024-12-17 12:08:06

Обновления выпуска:

Улучшение существующей документации.

Измененные API:

ParseLiveStreamProcessNotification
Новые выходные параметры: Timestamp, Sign

Измененные структуры данных:

AddOnSubtitle
Новые члены: SubtitleName

## Release 31

Время выпуска: 2024-12-11 16:07:01

Обновления выпуска:

Улучшение существующей документации.

Новые API:

ProcessImage

Измененные API:

DescribeTranscodeTemplates
Новые входные параметры: SceneType, CompressType

Новые структуры данных:

ImageEncodeConfig
ImageEnhanceConfig
ImageTaskInput
WordResult

Измененные структуры данных:

AiAnalysisTaskSegmentOutput
Новые члены: Abstract
AiRecognitionTaskAsrFullTextSegmentItem
Новые члены: Wordlist
AiRecognitionTaskInput
Новые члены: UserExtPara
AiRecognitionTaskTransTextSegmentItem
Новые члены: Wordlist
SegmentRecognitionItem
Новые члены: CovImgUrl, Keywords, BeginTime, EndTime
TranscodeTemplate
Новые члены: AliasName
VideoTemplateInfo
Новые члены: ScenarioBased, SceneType, CompressType
VideoTemplateInfoForUpdate
Новые члены: ScenarioBased, SceneType, CompressType

## Release 30

Время выпуска: 2024-11-07 11:23:14

Обновления выпуска:

Улучшение существующей документации.

Новые структуры данных:

SegmentSpecificInfo

Измененные структуры данных:

AdaptiveStreamTemplate
Измененные члены:
Video
AiRecognitionTaskAsrFullTextResultOutput
Устаревшие члены:
OutputStorage
AiRecognitionTaskTransTextResultOutput
Удаленные члены:
OutputStorage
TEHDConfig
Измененные члены:
MaxVideoBitrate
TEHDConfigForUpdate
Измененные члены:
MaxVideoBitrate
TerrorismConfigureInfo
Измененные члены:
OcrReviewInfo
UserDefineOcrTextReviewTemplateInfoForUpdate
Измененные члены:
LabelSet
VideoTemplateInfo
Новые члены: GopUnit, HlsTime, VideoProfile, VideoLevel, Bframes, Mode, Sar, NoScenecut, BitDepth, RawPts, Compress, SegmentSpecificInfo
VideoTemplateInfoForUpdate
Новые члены: GopUnit, HlsTime, VideoProfile, VideoLevel, Bframes, Mode, Sar, NoScenecut, BitDepth, RawPts, Compress, SegmentSpecificInfo

## Release 29

Время выпуска: 2024-09-30 14:46:08

Обновления выпуска:

Улучшение существующей документации.

Новые API:

CreateQualityControlTemplate
DeleteQualityControlTemplate
DescribeQualityControlTemplates
ModifyQualityControlTemplate

Измененные API:

CreateAdaptiveDynamicStreamingTemplate
Новые входные параметры: PureAudio, SegmentType
CreateSchedule
Новые входные параметры: ResourceId
DescribeAIAnalysisTemplates
Новые входные параметры: Name
DescribeAIRecognitionTemplates
Новые входные параметры: Name
DescribeAdaptiveDynamicStreamingTemplates
Новые входные параметры: PureAudio, Name
DescribeAnimatedGraphicsTemplates
Новые входные параметры: Name
DescribeContentReviewTemplates
Новые входные параметры: Name
DescribeImageSpriteTemplates
Новые входные параметры: Name
DescribeSampleSnapshotTemplates
Новые входные параметры: Name
DescribeSnapshotByTimeOffsetTemplates
Новые входные параметры: Name
DescribeTranscodeTemplates
Новые входные параметры: Name
DescribeWatermarkTemplates
Новые входные параметры: Name
ModifyAdaptiveDynamicStreamingTemplate
Новые входные параметры: PureAudio, SegmentType
ModifySchedule
Новые входные параметры: ResourceId
ParseLiveStreamProcessNotification
Новые выходные параметры: AiAnalysisResultInfo, AiQualityControlResultInfo, LiveRecordResultInfo

Новые структуры данных:

AiAnalysisTaskDelLogoInput
AiAnalysisTaskDelLogoOutput
AiAnalysisTaskDelLogoResult
AiAnalysisTaskDescriptionInput
AiAnalysisTaskDescriptionOutput
AiAnalysisTaskDescriptionResult
AiAnalysisTaskHeadTailInput
AiAnalysisTaskHeadTailOutput
AiAnalysisTaskHeadTailResult
AiAnalysisTaskHorizontalToVerticalInput
AiAnalysisTaskHorizontalToVerticalOutput
AiAnalysisTaskHorizontalToVerticalResult
AiAnalysisTaskSegmentInput
AiAnalysisTaskSegmentOutput
AiAnalysisTaskSegmentResult
AiParagraphInfo
AiRecognitionTaskObjectResult
AiRecognitionTaskObjectResultInput
AiRecognitionTaskObjectResultItem
AiRecognitionTaskObjectResultOutput
AiRecognitionTaskObjectSeqmentItem
ContainerDiagnoseResultItem
DiagnoseResult
LiveStreamAiAnalysisResultInfo
LiveStreamAiAnalysisResultItem
LiveStreamAiQualityControlResultInfo
LiveStreamObjectRecognitionResult
LiveStreamRecordResultInfo
LiveStreamTagRecognitionResult
MediaAiAnalysisDescriptionItem
QualityControlItemConfig
QualityControlTemplate
SegmentRecognitionItem
TranslateConfigureInfo

Измененные структуры данных:

AIRecognitionTemplateItem
Новые члены: TranslateConfigure
ActivityPara
Новые члены: QualityControlTask
ActivityResItem
Новые члены: QualityControlTask
Измененные члены:
SnapshotByTimeOffsetTask
AdaptiveDynamicStreamingTaskInput
Новые члены: DefinitionType
AdaptiveDynamicStreamingTemplate
Новые члены: PureAudio, SegmentType
AiAnalysisResult
Новые члены: DeLogoTask, SegmentTask, HeadTailTask, DescriptionTask, HorizontalToVerticalTask
AiRecognitionResult
Новые члены: ObjectTask
AiRecognitionTaskAsrFullTextResult
Новые члены: Progress
AiRecognitionTaskTransTextResult
Новые члены: Progress
AudioTemplateInfo
Измененные члены:
Bitrate
AudioTemplateInfoForUpdate
Измененные члены:
Bitrate
ComposeAudioStream
Новые члены: Bitrate
ComposeVideoStream
Новые члены: Bitrate
HighlightSegmentItem
Новые члены: SegmentTags
LiveActivityResItem
Новые члены: LiveQualityControlTask
LiveStreamAiRecognitionResultItem
Новые члены: ObjectRecognitionResultSet, TagRecognitionResultSet
LiveStreamTaskNotifyConfig
Новые члены: NotifyKey
MediaVideoStreamItem
Новые члены: Codecs, FpsNumerator, FpsDenominator
QualityControlData
Новые члены: ContainerDiagnoseResultSet
SchedulesInfo
Новые члены: ResourceId
TextWatermarkTemplateInput
Новые члены: TextContent
TextWatermarkTemplateInputForUpdate
Новые члены: TextContent
VideoTemplateInfo
Новые члены: SegmentType, FpsDenominator, Stereo3dType
Измененные члены:
Fps, Bitrate
VideoTemplateInfoForUpdate
Новые члены: SegmentType, FpsDenominator, Stereo3dType
Измененные члены:
Fps, Bitrate

## Release 28

Время выпуска: 2023-10-12 16:40:08

Обновления выпуска:

Улучшение существующей документации.

Измененные API:

DescribeTaskDetail
Новые выходные параметры: LiveScheduleTask
EditMedia
Новые входные параметры: ComposeConfig
ParseNotification
Новые выходные параметры: Timestamp, Sign
ProcessLiveStream
Новые входные параметры: AiAnalysisTask, AiQualityControlTask, ScheduleId

Новые структуры данных:

AudioBeautifyConfig
AudioDenoiseConfig
AudioEnhanceConfig
AudioSeparateConfig
ComposeAudioItem
ComposeAudioOperation
ComposeAudioStream
ComposeCanvas
ComposeEmptyItem
ComposeImageItem
ComposeImageOperation
ComposeMediaConfig
ComposeMediaItem
ComposeMediaTrack
ComposeSourceMedia
ComposeStyles
ComposeSubtitleItem
ComposeSubtitleStyle
ComposeTargetInfo
ComposeTrackTime
ComposeTransitionItem
ComposeTransitionOperation
ComposeVideoItem
ComposeVideoStream
LiveActivityResItem
LiveActivityResult
LiveRecordFile
LiveRecordResult
LiveRecordTaskInput
LiveScheduleLiveRecordTaskResult
LiveScheduleTask
VolumeBalanceConfig

Измененные структуры данных:

EditMediaFileInfo
Новые члены: Id
EnhanceConfig
Новые члены: AudioEnhance
SchedulesInfo
Новые члены: Type
Измененные члены:
Status
TaskNotifyConfig
Новые члены: NotifyKey

## Release 27

Время выпуска: 2023-09-05 17:58:35

Обновления выпуска:

Улучшение существующей документации.

Новые структуры данных:

DrmInfo
SimpleAesDrm

Измененные структуры данных:

AdaptiveDynamicStreamingTaskInput
Новые члены: DrmInfo

## Release 26

Время выпуска: 2023-08-23 18:03:26

Обновления выпуска:

Улучшение существующей документации.

Новые структуры данных:

AddOnSubtitle

Измененные структуры данных:

AdaptiveDynamicStreamingTaskInput
Новые члены: AddOnSubtitles
OverrideTranscodeParameter
Новые члены: StdExtInfo, AddOnSubtitles

## Release 25

Время выпуска: 2023-04-23 16:54:15

Обновления выпуска:

Улучшение существующей документации.

Измененные API:

DescribeSchedules
Новые входные параметры: TriggerType
ProcessMedia
Новые входные параметры: AiQualityControlTask

Новые структуры данных:

AiAnalysisTaskHighlightInput
AiAnalysisTaskHighlightOutput
AiAnalysisTaskHighlightResult
AiQualityControlTaskInput
HighlightSegmentItem
MediaAiAnalysisHighlightItem
QualityControlData
QualityControlItem
QualityControlResult
ScheduleQualityControlTaskResult

Измененные структуры данных:

AiAnalysisResult
Новые члены: HighlightTask
ScheduleTask
Новые члены: ErrCode, Message
WorkflowTask
Новые члены: AiQualityControlTaskResult

## Release 24

Время выпуска: 2023-04-23 14:35:29

Обновления выпуска:

Улучшение существующей документации.

Измененные структуры данных:

OverrideTranscodeParameter
Новые члены: AddonAudioStream

## Release 23

Время выпуска: 2023-03-13 12:10:59

Обновления выпуска:

Улучшение существующей документации.

Новые API:

CreateSchedule
DeleteSchedule
DescribeSchedules
DisableSchedule
EnableSchedule
ModifySchedule

Новые структуры данных:

Activity
ActivityPara
AwsS3FileUploadTrigger
AwsSQS
S3InputInfo
S3OutputStorage
SchedulesInfo

Измененные структуры данных:

MediaInputInfo
Новые члены: S3InputInfo
TaskNotifyConfig
Новые члены: AwsSQS
TaskOutputStorage
Новые члены: S3OutputStorage
WorkflowTrigger
Новые члены: AwsS3FileUploadTrigger

## Release 22

Время выпуска: 2023-02-15 11:30:19

Обновления выпуска:

Улучшение существующей документации.

Измененные структуры данных:

AiAnalysisTaskInput
Новые члены: ExtendedParameter

## Release 21

Время выпуска: 2022-12-29 15:38:52

Обновления выпуска:

Улучшение существующей документации.

Измененные API:

ProcessMedia
Новые входные параметры: TaskType

Измененные структуры данных:

LiveStreamTaskNotifyConfig
Измененные члены:
CmqModel, CmqRegion
TaskNotifyConfig
Измененные члены:
CmqModel, CmqRegion

## Release 20

Время выпуска: 2022-11-18 14:58:38

Обновления выпуска:

Улучшение существующей документации.

Измененные API:

CreateImageSpriteTemplate
Новые входные параметры: Format
ModifyImageSpriteTemplate
Новые входные параметры: Format

Новые структуры данных:

AiRecognitionTaskTransTextResult
AiRecognitionTaskTransTextResultInput
AiRecognitionTaskTransTextResultOutput
AiRecognitionTaskTransTextSegmentItem
LiveStreamTransTextRecognitionResult
SubtitleTemplate

Измененные структуры данных:

AiRecognitionResult
Новые члены: TransTextTask
AudioTemplateInfoForUpdate
Новые члены: StreamSelects
ImageSpriteTemplate
Новые члены: Format
LiveStreamAiRecognitionResultItem
Новые члены: TransTextRecognitionResultSet
OverrideTranscodeParameter
Новые члены: SubtitleTemplate

## Release 19

Время выпуска: 2022-10-08 10:52:22

Обновления выпуска:

Улучшение существующей документации.

Измененные структуры данных:

EditMediaOutputConfig
Новые члены: Type
TaskSimpleInfo
Новые члены: SubTaskTypes

## Release 18

Время выпуска: 2022-08-01 17:24:03

Обновления выпуска:

Улучшение существующей документации.

Измененные API:

CreateTranscodeTemplate
Новые входные параметры: EnhanceConfig
DescribeTaskDetail
Новые выходные параметры: ScheduleTask
DescribeTasks
Новые выходные параметры: TotalCount
DescribeTranscodeTemplates
Новые входные параметры: TranscodeType
ModifyTranscodeTemplate
Новые входные параметры: EnhanceConfig
ParseNotification
Новые выходные параметры: ScheduleTaskEvent
ProcessMedia
Новые входные параметры: ScheduleId

Новые структуры данных:

ActivityResItem
ActivityResult
ArtifactRepairConfig
ColorEnhanceConfig
EnhanceConfig
FaceEnhanceConfig
FrameRateConfig
HdrConfig
ImageQualityEnhanceConfig
LowLightEnhanceConfig
ScheduleAnalysisTaskResult
ScheduleRecognitionTaskResult
ScheduleReviewTaskResult
ScheduleTask
ScratchRepairConfig
SharpEnhanceConfig
SuperResolutionConfig
VideoDenoiseConfig
VideoEnhanceConfig

Измененные структуры данных:

TranscodeTemplate
Новые члены: EnhanceConfig

## Release 17

Время выпуска: 2022-06-20 10:20:43

Обновления выпуска:

Улучшение существующей документации.

Измененные структуры данных:

AiRecognitionTaskFaceResultItem
Новые члены: Gender, Birthday, Profession, SchoolOfGraduation, Abstract, PlaceOfBirth, PersonType, Remark, Url

## Release 16

Время выпуска: 2022-05-19 16:44:18

Обновления выпуска:

Улучшение существующей документации.

Измененные API:

DescribeAIAnalysisTemplates
Новые входные параметры: Type
DescribeAIRecognitionTemplates
Новые входные параметры: Type
DescribeContentReviewTemplates
Новые входные параметры: Type

Измененные структуры данных:

AIAnalysisTemplateItem
Новые члены: Type
AIRecognitionTemplateItem
Новые члены: Type

## Release 15

Время выпуска: 2022-05-11 16:12:35

Обновления выпуска:

Улучшение существующей документации.

Измененные структуры данных:

ContentReviewTemplateItem
Новые члены: Type

## Release 14

Время выпуска: 2022-05-09 11:28:21

Обновления выпуска:

Улучшение существующей документации.

Измененные структуры данных:

VideoTemplateInfoForUpdate
Новые члены: ContentAdaptStream

## Release 13

Время выпуска: 2021-12-03 10:13:05

Обновления выпуска:

Улучшение существующей документации.

Измененные структуры данных:

MediaProcessTaskTranscodeResult
Новые члены: Progress

## Release 12

Время выпуска: 2021-10-21 11:00:14

Обновления выпуска:

Улучшение существующей документации.

Измененные структуры данных:

MediaVideoStreamItem
Новые члены: HdrType

## Release 11

Время выпуска: 2021-10-13 15:53:24

Обновления выпуска:

Улучшение существующей документации.

Измененные структуры данных:

LiveStreamTaskNotifyConfig
Новые члены: NotifyType, NotifyUrl

## Release 10

Время выпуска: 2021-08-24 15:51:49

Обновления выпуска:

Улучшение существующей документации.

Измененные структуры данных:

MediaAudioStreamItem
Новые члены: Channel
MediaVideoStreamItem
Новые члены: ColorPrimaries, ColorSpace, ColorTransfer

## Release 9

Время выпуска: 2021-08-06 14:45:15

Обновления выпуска:

Улучшение существующей документации.

Новые структуры данных:

HeadTailParameter

Измененные структуры данных:

TaskNotifyConfig
Новые члены: NotifyType, NotifyUrl
TranscodeTaskInput
Новые члены: HeadTailParameter

## Release 8

Время выпуска: 2021-07-28 17:01:34

Обновления выпуска:

Улучшение существующей документации.

Измененные API:

EditMedia
Новые входные параметры: OutputConfig

Новые структуры данных:

EditMediaOutputConfig

## Release 7

Время выпуска: 2021-06-04 10:40:17

Обновления выпуска:

Улучшение существующей документации.

Измененные структуры данных:

RawImageWatermarkInput
Новые члены: RepeatType

## Release 6

Время выпуска: 2021-01-21 17:53:03

Обновления выпуска:

Улучшение существующей документации.

Измененные структуры данных:

ImageWatermarkInput
Новые члены: RepeatType
ImageWatermarkInputForUpdate
Новые члены: RepeatType
ImageWatermarkTemplate
Новые члены: RepeatType
TranscodeTaskInput
Новые члены: StartTimeOffset, EndTimeOffset

## Release 5

Время выпуска: 2020-12-24 11:17:16

Обновления выпуска:

Улучшение существующей документации.

Новые структуры данных:

OverrideTranscodeParameter
UrlInputInfo

Измененные структуры данных:

AiAnalysisTaskClassificationResult
Новые члены: ErrCodeExt
AiAnalysisTaskCoverResult
Новые члены: ErrCodeExt
AiAnalysisTaskFrameTagResult
Новые члены: ErrCodeExt
AiAnalysisTaskTagResult
Новые члены: ErrCodeExt
AiRecognitionTaskAsrFullTextResult
Новые члены: ErrCodeExt
AiRecognitionTaskAsrWordsResult
Новые члены: ErrCodeExt
AiRecognitionTaskFaceResult
Новые члены: ErrCodeExt
AiRecognitionTaskOcrFullTextResult
Новые члены: ErrCodeExt
AiRecognitionTaskOcrWordsResult
Новые члены: ErrCodeExt
AiReviewTaskPoliticalAsrResult
Новые члены: ErrCodeExt
AiReviewTaskPoliticalOcrResult
Новые члены: ErrCodeExt
AiReviewTaskPoliticalResult
Новые члены: ErrCodeExt
AiReviewTaskPornAsrResult
Новые члены: ErrCodeExt
AiReviewTaskPornOcrResult
Новые члены: ErrCodeExt
AiReviewTaskPornResult
Новые члены: ErrCodeExt
AiReviewTaskProhibitedAsrResult
Новые члены: ErrCodeExt
AiReviewTaskProhibitedOcrResult
Новые члены: ErrCodeExt
AiReviewTaskTerrorismOcrResult
Новые члены: ErrCodeExt
AiReviewTaskTerrorismResult
Новые члены: ErrCodeExt
MediaInputInfo
Новые члены: UrlInputInfo
MediaProcessTaskAdaptiveDynamicStreamingResult
Новые члены: ErrCodeExt
MediaProcessTaskAnimatedGraphicResult
Новые члены: ErrCodeExt
MediaProcessTaskImageSpriteResult
Новые члены: ErrCodeExt
MediaProcessTaskSampleSnapshotResult
Новые члены: ErrCodeExt
MediaProcessTaskSnapshotByTimeOffsetResult
Новые члены: ErrCodeExt
MediaProcessTaskTranscodeResult
Новые члены: ErrCodeExt
TranscodeTaskInput
Новые члены: OverrideParameter
VideoTemplateInfo
Новые члены: Vcrf
VideoTemplateInfoForUpdate
Новые члены: Vcrf

## Release 4

Время выпуска: 2020-10-16 18:33:05

Обновления выпуска:

Улучшение существующей документации.

Новые API:

ExecuteFunction

## Release 3

Время выпуска: 2020-09-17 17:24:46

Обновления выпуска:

Улучшение существующей документации.

Измененные структуры данных:

MediaAiAnalysisFrameTagItem
Новые члены: CategorySet

## Release 2

Время выпуска: 2020-08-13 20:08:53

Обновления выпуска:

Улучшение существующей документации.

Измененные API:

DescribeTaskDetail
Новые выходные параметры: ExtInfo

## Существующий выпуск

Время выпуска: 2020-07-24 14:21:20

Существующие API и структуры данных следующие:

Улучшение существующей документации.

Существующие API:

CreateAIAnalysisTemplate
CreateAIRecognitionTemplate
CreateAdaptiveDynamicStreamingTemplate
CreateAnimatedGraphicsTemplate
CreateContentReviewTemplate
CreateImageSpriteTemplate
CreatePersonSample
CreateSampleSnapshotTemplate
CreateSnapshotByTimeOffsetTemplate
CreateTranscodeTemplate
CreateWatermarkTemplate
CreateWordSamples
CreateWorkflow
DeleteAIAnalysisTemplate
DeleteAIRecognitionTemplate
DeleteAdaptiveDynamicStreamingTemplate
DeleteAnimatedGraphicsTemplate
DeleteContentReviewTemplate
DeleteImageSpriteTemplate
DeletePersonSample
DeleteSampleSnapshotTemplate
DeleteSnapshotByTimeOffsetTemplate
DeleteTranscodeTemplate
DeleteWatermarkTemplate
DeleteWordSamples
DeleteWorkflow
DescribeAIAnalysisTemplates
DescribeAIRecognitionTemplates
DescribeAdaptiveDynamicStreamingTemplates
DescribeAnimatedGraphicsTemplates
DescribeContentReviewTemplates
DescribeImageSpriteTemplates
DescribeMediaMetaData
DescribePersonSamples
DescribeSampleSnapshotTemplates
DescribeSnapshotByTimeOffsetTemplates
DescribeTaskDetail
DescribeTasks
DescribeTranscodeTemplates
DescribeWatermarkTemplates
DescribeWordSamples
DescribeWorkflows
DisableWorkflow
EditMedia
EnableWorkflow
ManageTask
ModifyAIAnalysisTemplate
ModifyAIRecognitionTemplate
ModifyAdaptiveDynamicStreamingTemplate
ModifyAnimatedGraphicsTemplate
ModifyContentReviewTemplate
ModifyImageSpriteTemplate
ModifyPersonSample
ModifySampleSnapshotTemplate
ModifySnapshotByTimeOffsetTemplate
ModifyTranscodeTemplate
ModifyWatermarkTemplate
ModifyWordSample
ParseLiveStreamProcessNotification
ParseNotification
ProcessLiveStream
ProcessMedia
ResetWorkflow

Существующие структуры данных:

AIAnalysisTemplateItem
AIRecognitionTemplateItem
AdaptiveDynamicStreamingInfoItem
AdaptiveDynamicStreamingTaskInput
AdaptiveDynamicStreamingTemplate
AdaptiveStreamTemplate
AiAnalysisResult
AiAnalysisTaskClassificationInput
AiAnalysisTaskClassificationOutput
AiAnalysisTaskClassificationResult
AiAnalysisTaskCoverInput
AiAnalysisTaskCoverOutput
AiAnalysisTaskCoverResult
AiAnalysisTaskFrameTagInput
AiAnalysisTaskFrameTagOutput
AiAnalysisTaskFrameTagResult
AiAnalysisTaskInput
AiAnalysisTaskTagInput
AiAnalysisTaskTagOutput
AiAnalysisTaskTagResult
AiContentReviewResult
AiContentReviewTaskInput
AiRecognitionResult
AiRecognitionTaskAsrFullTextResult
AiRecognitionTaskAsrFullTextResultInput
AiRecognitionTaskAsrFullTextResultOutput
AiRecognitionTaskAsrFullTextSegmentItem
AiRecognitionTaskAsrWordsResult
AiRecognitionTaskAsrWordsResultInput
AiRecognitionTaskAsrWordsResultItem
AiRecognitionTaskAsrWordsResultOutput
AiRecognitionTaskAsrWordsSegmentItem
AiRecognitionTaskFaceResult
AiRecognitionTaskFaceResultInput
AiRecognitionTaskFaceResultItem
AiRecognitionTaskFaceResultOutput
AiRecognitionTaskFaceSegmentItem
AiRecognitionTaskInput
AiRecognitionTaskOcrFullTextResult
AiRecognitionTaskOcrFullTextResultInput
AiRecognitionTaskOcrFullTextResultOutput
AiRecognitionTaskOcrFullTextSegmentItem
AiRecognitionTaskOcrFullTextSegmentTextItem
AiRecognitionTaskOcrWordsResult
AiRecognitionTaskOcrWordsResultInput
AiRecognitionTaskOcrWordsResultItem
AiRecognitionTaskOcrWordsResultOutput
AiRecognitionTaskOcrWords

---
*Источник (EN): [history.md](./history.md)*
