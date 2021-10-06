from aiogram.dispatcher.filters.state import StatesGroup, State


class RecruitingQuery(StatesGroup):
    StartRecruit = State()
    Email = State()
    Research = State()
    OtherResearchType = State()
    BasicRequirements = State()
    CountRespondents = State()
    DataRespondent = State()
    StockRespondents = State()
    CompanyInfo = State()
    Name = State()
    Gender = State()
    GetArticles = State()
    WhatSources = State()
    CheckInfo = State()
    FinishRecruit = State()


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
