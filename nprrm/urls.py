from django.contrib import admin
from django.urls import include, path
from django.views.generic import TemplateView
from django.shortcuts import render
from django.contrib.sitemaps.views import sitemap
from django.contrib.auth import views as auth_views
from django.conf import settings
from pages.sitemaps import (
    CompensationFundSitemap, ContactSitemap, DecisionMeetingSitemap, FederalLawSitemap, 
    IndexSitemap, InspectionSitemap, JoinUsSitemap, LocalRegulationSitemap, MemberSitemap,
    NewsSitemap, PriorityDirectionSitemap, RegulatoryLegalSitemap, ReportingSitemap,
    TechnicalRegulationSitemap)
from pages.views import (
    CompensationFundPageList, ContactPageDetail, DecisionMeetingPageList, FederalLawPageList,
    IndexPageDetail, InspectionPageList, JoinUsPageDetail, LocalRegulationPageList,
    MemberExcludedPageList, MemberPageList, NewsPageList, PriorityDirectionPageDetail,
    RegulatoryLegalPageList, ReportingPageList, TechnicalRegulationPageList)


admin.site.site_header = admin.site.site_title = 'Ассоциация «РегионРемМонтаж ПБ»'

#--

sitemaps = {
    'index': IndexSitemap,
    'p-d': PriorityDirectionSitemap,
    'members': MemberSitemap,
    'c-f': CompensationFundSitemap,
    'inspection': InspectionSitemap,
    'd-m': DecisionMeetingSitemap,
    'reporting': ReportingSitemap,
    'news': NewsSitemap,
    'j-u': JoinUsSitemap,
    't-r': TechnicalRegulationSitemap,
    'f-l': FederalLawSitemap,
    'r-l': RegulatoryLegalSitemap,
    'l-r': LocalRegulationSitemap,
    'contacts': ContactSitemap,
}

#--

urlpatterns = [
    path('admin/logout/', auth_views.LogoutView.as_view(next_page='/admin/login'), name='logout'),
    path('admin/', admin.site.urls),
    
    path('', IndexPageDetail.as_view(), name='index'),

    path('priority-directions/', PriorityDirectionPageDetail.as_view(), name='p-d_detail'),
    path('members/', MemberPageList.as_view(), name='members_list'),
    path('members/excluded/', MemberExcludedPageList.as_view(), name='members_excluded_list'),
    path('compensation-fund/', CompensationFundPageList.as_view(), name='c-f_list'),
    path('inspection/', InspectionPageList.as_view(), name='inspection_list'),
    path('decision-meetings/', DecisionMeetingPageList.as_view(), name='d-m_list'),
    path('reporting/', ReportingPageList.as_view(), name='reporting_list'),
    path('news/', NewsPageList.as_view(), name='news_list'),
    path('join-us/', JoinUsPageDetail.as_view(), name='j-u_detail'),

    path('technical-regulations/', TechnicalRegulationPageList.as_view(), name='t-r_list'),
    path('federal-laws/', FederalLawPageList.as_view(), name='f-l_list'),
    path('regulatory-legal/', RegulatoryLegalPageList.as_view(), name='r-l_list'),
    path('local-regulation/', LocalRegulationPageList.as_view(), name='l-r_list'),

    path('contacts/', ContactPageDetail.as_view(), name='contact_detail'),
    
    path('privacy-policy/', TemplateView.as_view(
        template_name="privacy-policy/index.html"), name="p-p_template"),
    
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps},
         name='django.contrib.sitemaps.views.sitemap'),
]


#--

def handler400(request, exception, template_name='errors/400.html'):
    response = render(request, template_name)
    response.status_code = 400
    return response


def handler403(request, exception, template_name='errors/403.html'):
    response = render(request, template_name)
    response.status_code = 403
    return response


def handler404(request, exception, template_name='errors/404.html'):
    response = render(request, template_name)
    response.status_code = 404
    return response

def handler500(request, template_name='errors/500.html'):
    response = render(request, template_name)
    response.status_code = 500
    return response

#--

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include('debug_toolbar.urls')),
    ] + urlpatterns

    urlpatterns += [
        path('400/', TemplateView.as_view(template_name="errors/400.html")),
        path('403/', TemplateView.as_view(template_name="errors/403.html")),
        path('404/', TemplateView.as_view(template_name="errors/404.html")),
        path('500/', TemplateView.as_view(template_name="errors/500.html")),
    ]

    from django.conf.urls.static import static
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
    urlpatterns += static(r'/favicon.ico', document_root='static/favicon.ico')
    # urlpatterns += static(r'/site.webmanifest', document_root='static/site.webmanifest')