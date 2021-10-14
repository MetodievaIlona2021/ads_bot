from aiogram.dispatcher.filters.state import StatesGroup, State


class RecruitingQuery(StatesGroup):
    StartRecruit = State()
    BasicRequirements = State()
    ScreeningQuestionnaire = State()
    ImportantCriteria = State()
    ProjectTimeline = State()
    OtherCriteria = State()
    RequirementsRespondent = State()
    DataRespondent = State()
    StockRespondents = State()
    ResearchTopic = State()
    BasicCriteria = State()
    PreliminaryCommunication = State()
    CompanyInfo = State()
    EmailInfo = State()
    ProjectScreeningQuestionnaire = State()
    FieldActivity = State()
    Education = State()
    ProductService = State()
    ConsumptionFrequency = State()
    RespondentIncome = State()
    Research = State()
    OtherResearchType = State()
    CountRespondents = State()
    SurveyTime = State()
    PaymentsType = State()
    WhatSources = State()
    GetArticles = State()
    Name = State()
    Gender = State()
    Username = State()
    CheckInfo = State()
    FinishRecruit = State()
    TargetAudience = State()
    Budget = State()


class OnlineMeeting(StatesGroup):
    DateMeeting = State()
    TimeMeeting = State()


class PaymentService(StatesGroup):
    Payment = State()
    PaymentQIWI = State()
    PaymentQIWIAmount = State()
    PaymentYOUKASSA = State()
    PaymentYOUKASSAAmount = State()


class NewItem(StatesGroup):
    NewInterview = State()
    NewInterviewDesc = State()
    NewInterviewThumb = State()
    NewInterviewLink = State()
    NewInterviewConfirm = State()

    NewReview = State()
    NewReviewDesc = State()
    NewReviewThumb = State()
    NewReviewLink = State()
    NewReviewConfirm = State()

    NewNews = State()
    NewNewsDesc = State()
    NewNewsThumb = State()
    NewNewsLink = State()
    NewNewsConfirm = State()

    NewSignificant = State()
    NewSignificantDesc = State()
    NewSignificantThumb = State()
    NewSignificantConfirm = State()

    NewArticle = State()
    NewArticleDesc = State()
    NewArticleThumb = State()
    NewArticleLink = State()
    NewArticleConfirm = State()

    NewCase = State()
    NewCaseDesc = State()
    NewCaseThumb = State()
    NewCaseConfirm = State()
