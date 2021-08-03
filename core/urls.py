from django.urls import path
from .views import IndexView, ClientesView, JobYearArchiveView, JobMonthArchiveView, \
    JobWeekArchiveView, JobDayArchiveView, DadosJSONView, JobsChartPanelView, \
    ListarJobsPanelView, PainelJobsView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('clientes/', ClientesView.as_view(), name='clientes'),
    path('painel/clientes/', JobsChartPanelView.as_view(), name='painelclientes'),
    path('listar/jobs/', ListarJobsPanelView.as_view(), name='listarjobs'),
    path('painel/jobs/', PainelJobsView.as_view(), name='paineljobs'),
    path('job/<int:year>/', JobYearArchiveView.as_view(), name='job_year_archive'),
    # Example: /2012/08/
    path('job/<int:year>/<int:month>/', JobMonthArchiveView.as_view(month_format='%m'), name="archive_month_numeric"),
    # Example: /2012/aug/
    path('job/<int:year>/<str:month>/', JobMonthArchiveView.as_view(), name="archive_month"),
    # Example: /2012/week/23/
    path('job/<int:year>/week/<int:week>/', JobWeekArchiveView.as_view(), name="archive_week"),
    # Example: /2012/05/10/
    path('job/<int:year>/<int:month>/<int:day>/', JobDayArchiveView.as_view(), name="archive_day"),
    # Graficos
    path('dados/', DadosJSONView.as_view(), name='dados'),
    #path('painelchart/', JobsView.as_view(), name='painelchart'),
    path('chartpanel/', JobsChartPanelView.as_view(), name='chartpanel'),
]
