from django.contrib import admin
from django.urls import path
from en_doc import views

urlpatterns = [
    path('', views.index, name='en_index'),
    # main pages urls
    path('information/', views.information, name='en_information'),
    path('graph/', views.graph, name='en_graph'),
    path('comparison/', views.comparison, name='en_comparison'),
    path('search/', views.search, name='en_search'),
    path('es_search/', views.es_search, name='en_es_search'),
    path('subject/', views.subject, name='en_subject'),
    path('subject_statistics/', views.subject_statistics, name='en_subject_statistics'),
    path('compare_document/', views.compare_document, name='en_compare_document'),
    path('adaptation/', views.adaptation, name='en_adaptation'),
    path('votes_analysis/', views.votes_analysis, name='en_votes_analysis'),
    path('subject_graph/', views.subject_graph, name='en_subject_graph'),
    path('named_entities/', views.named_entities, name='en_named_entities'),
    path('leadership_slogan/', views.leadership_slogan, name='en_leadership_slogan'),
    path('portal_analysis/', views.portal_analysis, name='en_portal_analysis'),
    path('definition/', views.definition, name='en_definition'),
    path("legal_literature_adaptation/", views.legal_literature_adaptation, name="en_legal_literature_adaptation"),
    path("search_actors/", views.search_actors, name='en_search_actors'),
    path("show_actors/", views.show_actors, name='en_show_actors'),
    path("collective_actors/", views.collective_actors, name='en_collective_actors'),
    path("executive_regulations_analysis/", views.executive_regulations_analysis,
         name='en_executive_regulations_analysis'),
    path("executive_regulations_analysis/", views.executive_regulations_supervision,
         name='en_executive_regulations_supervision'),
    path("principles_analysis/", views.principles_analysis, name='en_principles_analysis'),
    path("regularity/", views.regularity, name="en_regularity"),
    path("window_unit/", views.window_unit, name='en_window_unit'),
    path("business_advisor/", views.business_advisor, name='en_business_advisor'),
    path("official_references/", views.official_references, name='en_official_references'),
    path("regularity_life_cycle/", views.regularity_life_cycle, name="en_regularity_life_cycle"),
    path("AI_topics/", views.AI_topics, name='en_AI_topics'),
    path('recommendation/', views.recommendation, name='en_recommendation'),
    path('GetLevelByCountryId/<int:country_id>/', views.GetLevelByCountryId, name='GetLevelByCountryId'),
    path('GetTypeByCountryId/<int:country_id>/', views.GetTypeByCountryId, name='GetTypeByCountryId'),
    path('GetApprovalReferencesByCountryId/<int:country_id>/', views.GetApprovalReferencesByCountryId, name='GetApprovalReferencesByCountryId'),
    path('GetYearsBoundByCountryId/<int:country_id>/', views.GetYearsBoundByCountryId, name='GetYearsBoundByCountryId'),
    path('GetDocumentsWithoutSubject/<int:country_id>/<int:measure_id>/', views.GetDocumentsWithoutSubject, name='GetDocumentsWithoutSubject'),
    path('GetSubjectKeywords/<int:subject_id>/', views.GetSubjectKeywords, name='GetSubjectKeywords'),


    # urls inside main pages
    path('GetDocumentById/<int:id>/', views.GetDocumentById, name='GetDocumentById'),
    path('GetDocumentsByCountryId_Modal/<int:country_id>/<int:start_index>/<int:end_index>/', views.GetDocumentsByCountryId_Modal,name='GetDocumentsByCountryId_Modal'),
    path('GetTFIDFByDocumentId/<int:document_id>/', views.GetTFIDFByDocumentId, name='GetTFIDFByDocumentId'),
    path('GetNGramByDocumentId/<int:document_id>/<int:gram>/', views.GetNGramByDocumentId, name='GetNGramByDocumentId'),
    path('GetReferencesByDocumentId/<int:document_id>/<int:type>/', views.GetReferencesByDocumentId, name='GetReferencesByDocumentId'),
    path('GetSubjectByDocumentId/<int:document_id>/<int:measure_id>/', views.GetSubjectByDocumentId, name='GetSubjectByDocumentId'),
    path('get_subject_detail/<int:document_id>/<int:subject_id>/',views.get_subject_detail, name='get_subject_detail'),
    path('GetReferences2Doc/<int:document1_id>/<int:document2_id>/', views.GetReferences2Doc, name='GetReferences2Doc'),
    path('UpdateNgramScore/<int:document_id>/<int:gram>/<str:gram_ids>/', views.UpdateNgramScore,name='UpdateNgramScore'),
    path('InsertNgram/<int:document_id>/<int:gram>/<str:texts>/', views.InsertNgram, name='InsertNgram'),
    path('DeleteNgram/<int:gram_id>/', views.DeleteNgram, name='DeleteNgram'),
    path('GetCountryById/<int:id>/', views.GetCountryById, name='GetCountryById'),
    path('GetGraphSimilarityMeasureByCountry/<int:country_id>/', views.GetGraphSimilarityMeasureByCountry,name='GetGraphSimilarityMeasureByCountry'),
    path('GetGraphDistribution/<int:country_id>/<int:measure_id>/', views.GetGraphDistribution,name='GetGraphDistribution'),
    path('GetDocumentByCountryTypeSubject_Modal/<int:country_id>/<int:type_id>/<int:subject_id>/<str:tag>/', views.GetDocumentByCountryTypeSubject_Modal, name='GetDocumentByCountryTypeSubject_Modal'),
    path('GetDocumentByCountryTypeSubject/<int:country_id>/<int:type_id>/<int:subject_id>/<str:tag>/', views.GetDocumentByCountryTypeSubject, name='GetDocumentByCountryTypeSubject'),
    path('GetGraphEdgesByDocumentIdMeasure/<int:country_id>/<int:src_type_id>/<int:src_subject_id>/<int:dest_type_id>/<int:dest_subject_id>/<int:measure_id>/<str:weight>/',views.GetGraphEdgesByDocumentIdMeasure, name='GetGraphEdgesByDocumentIdMeasure'),
    path('SearchDocumentOR/<int:country_id>/<int:level_id>/<int:subject_id>/<int:type_id>/<int:approval_reference_id>/<int:from_year>/<int:to_year>/<str:place>/<str:text>/', views.SearchDocumentOR, name='SearchDocumentOR'),
    path('SearchDocumentAnd/<int:country_id>/<int:level_id>/<int:subject_id>/<int:type_id>/<int:approval_reference_id>/<int:from_year>/<int:to_year>/<str:place>/<str:text>/', views.SearchDocumentAnd, name='SearchDocumentAnd'),
    path('SearchDocumentExact/<int:country_id>/<int:level_id>/<int:subject_id>/<int:type_id>/<int:approval_reference_id>/<int:from_year>/<int:to_year>/<str:place>/<str:text>/', views.SearchDocumentExact, name='SearchDocumentExact'),
    path('SearchDocumentWithoutText/<int:country_id>/<int:level_id>/<int:subject_id>/<int:type_id>/<int:approval_reference_id>/<int:from_year>/<int:to_year>/',views.SearchDocumentWithoutText, name='SearchDocumentWithoutText'),
    path('GetSearchDetailsAndOR/<int:document_id>/<str:text>/<str:where>/<str:mode>/', views.GetSearchDetailsAndOR, name='GetSearchDetailsAndOR'),
    path('GetSearchDetailsExact/<int:document_id>/<str:text>/<str:where>/', views.GetSearchDetailsExact, name='GetSearchDetailsExact'),
    path('GetGraphEdgesByDocumentsList/<int:measure_id>/', views.GetGraphEdgesByDocumentsList, name='GetGraphEdgesByDocumentsList'),
    path('GetDefinitionByDocumentId/<int:document_id>/', views.GetDefinitionByDocumentId, name='GetDefinitionByDocumentId'),
    path('GetAbbreviationsByDocumentId/<int:document_id>/', views.GetAbbreviationsByDocumentId, name='GetAbbreviationsByDocumentId'),
    path('GetDocumentsByCountrySubject/<int:country_id>/<str:subjects_id>/', views.GetDocumentsByCountrySubject,name='GetDocumentsByCountrySubject'),
    path('GetDocumentEntities/<int:document_id>/', views.GetDocumentEntities, name='GetDocumentEntities'),
    path('GetDocumentsWithEntitiesByCountry/<int:country_id>/', views.GetDocumentsWithEntitiesByCountry, name='GetDocumentsWithEntitiesByCountry'),
    path('GetDocumentContent/<int:document_id>/', views.GetDocumentContent, name='GetDocumentContent'),
    path('SearchDocumentByname/<int:country_id>/<str:text>/', views.SearchDocumentByname, name='SearchDocumentByname'),
    path('GetActorsList/', views.GetActorsList, name='GetActorsList'),
    path('GetDocumentActorsList/<int:country_id>/<str:actors_list>/', views.GetDocumentActorsList, name='GetDocumentActorsList'),
    path('GetActorsChartData/<int:document_id>/', views.GetActorsChartData, name='GetActorsChartData'),
    path('GetActorsParagraphs/<int:document_id>/<str:actor_name>/', views.GetActorsParagraphs, name='GetActorsParagraphs'),
    path('GetDocumentActorsParagraphs/<int:document_id>/<str:actors_list>/', views.GetDocumentActorsParagraphs, name='GetDocumentActorsParagraphs'),
    path('GetActorsListById/<str:actors_list>/', views.GetActorsListById, name='GetActorsListById'),

    # Cube urls
    path('document_json_list/<int:id>/', views.document_json_list, name='document_json_list'),

    # ES
    path('SearchDocument_ES/<int:country_id>/<int:level_id>/<int:approval_reference_id>/<int:from_year>/<int:to_year>/<str:place>/<str:text>/<str:search_type>/', views.SearchDocument_ES, name='SearchDocument_ES'),
    path('GetSearchDetails_ES/<int:document_id>/<str:search_type>/<str:text>/', views.GetSearchDetails_ES, name='GetSearchDetails_ES'),

]