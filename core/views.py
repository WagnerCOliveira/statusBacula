from django.shortcuts import render
from django.views.generic import TemplateView, View
from .models import Client, Job, Status, Pool, Media
from django.views.generic.dates import YearArchiveView, MonthArchiveView, WeekArchiveView, DayArchiveView
from django.db.models import Count, Sum
from chartjs.views.lines import BaseLineChartView
from .consultas import filtro_rangedate, filtro_status, filtro_clientid, filtro_mediaid, filtro_statusjobs


class IndexView(TemplateView):
    template_name = 'index.html'


class JobsView(TemplateView):
    template_name = 'painelchart.html'


class JobsChartPanelView(View):

    def get(self, request, *args, **kargs):
        # Arquivos/Cliente
        labelsjf = []
        datajf = []
        labelsjc = []
        datajc = []
        labelsja = []
        dataja = []

        qs_ja = list(Job.objects.values('name').annotate(name_jobbytes=Sum('jobbytes')).order_by('-name_jobbytes'))
        qs_jc = list(Job.objects.values('name').annotate(name_count=Count('name')).order_by('-name_count'))
        qs_jf = list(Job.objects.values('name').annotate(name_jobfiles=Sum('jobfiles')).order_by('-name_jobfiles'))

        for objja in qs_ja:
            labelsja.append(objja['name'].decode('utf8'))
            dataja.append(objja['name_jobbytes'])

        for objjc in qs_jc:
            labelsjc.append(objjc['name'].decode('utf8'))
            datajc.append(objjc['name_count'])

        for obj in qs_jf:
            labelsjf.append(obj['name'].decode('utf8'))
            datajf.append(obj['name_jobfiles'])

        lsjf_table = zip(labelsjf, datajf)
        lsjf_graph = zip(labelsjf, datajf)

        lsjc_table = zip(labelsjc, datajc)
        lsjc_graph = zip(labelsjc, datajc)

        lsja_table = zip(labelsja, dataja)
        lsja_graph = zip(labelsja, dataja)

        context = {
            'lsjf_table': lsjf_table,
            'lsjf_graph': lsjf_graph,
            'lsjc_table': lsjc_table,
            'lsjc_graph': lsjc_graph,
            'lsja_table': lsja_table,
            'lsja_graph': lsja_graph
        }

        start_date = request.GET.get('start_date', None)
        end_date = request.GET.get('end_date', None)

        if start_date and end_date:
            labelsjf = []
            datajf = []
            labelsjc = []
            datajc = []
            labelsja = []
            dataja = []

            qs_jc = list(Job.objects.values('name').filter(endtime__range=(start_date, end_date)).annotate(
                name_count=Count('name')).order_by('-name_count'))

            qs_jf = list(Job.objects.values('name').filter(endtime__range=(start_date, end_date)).annotate(
                name_jobfiles=Sum('jobfiles')).order_by('-name_jobfiles'))

            qs_ja = list(Job.objects.values('name').filter(endtime__range=(start_date, end_date)).annotate(
                name_jobbytes=Sum('jobbytes')).order_by('-name_jobbytes'))

            for objja in qs_ja:
                labelsja.append(objja['name'].decode('utf8'))
                dataja.append(objja['name_jobbytes'])

            for obj in qs_jf:
                labelsjf.append(obj['name'].decode('utf8'))
                datajf.append(obj['name_jobfiles'])

            for objjc in qs_jc:
                labelsjc.append(objjc['name'].decode('utf8'))
                datajc.append(objjc['name_count'])

            lsjf_table = zip(labelsjf, datajf)
            lsjf_graph = zip(labelsjf, datajf)
            lsjc_table = zip(labelsjc, datajc)
            lsjc_graph = zip(labelsjc, datajc)
            lsja_table = zip(labelsja, dataja)
            lsja_graph = zip(labelsja, dataja)

            context = {
                'lsjf_table': lsjf_table,
                'lsjf_graph': lsjf_graph,
                'lsjc_table': lsjc_table,
                'lsjc_graph': lsjc_graph,
                'lsja_table': lsja_table,
                'lsja_graph': lsja_graph,
                'start_date': start_date,
                'end_date': end_date
                }

        return render(request, 'painel.html', context)

class PainelJobsView(View):

    def get(self, request, *args, **kargs):
        qs_statusjobs = []
        start_date = request.GET.get('start_date', None)
        end_date = request.GET.get('end_date', None)

        if start_date and end_date:

            qs_statusjobs = filtro_statusjobs(start_date=start_date, end_date=end_date)

        context = {
            'qs_statusjobs': qs_statusjobs
        }

        return render(request, 'paineljobs.html', context)


class ListarJobsPanelView(View):

    def get(self, request, *args, **kargs):

        lista_jobs = []

        qs_status = list(Status.objects.values('jobstatus', 'jobstatuslong'))
        qs_name = list(Client.objects.values('clientid', 'name'))
        qs_pool = list(Pool.objects.values('poolid', 'name'))
        qs_media = list(Media.objects.values('mediaid', 'volumename'))

        context = {
            'qs_status': qs_status,
            'qs_name': qs_name,
            'qs_pool': qs_pool,
            'qs_media': qs_media
        }

        start_date = request.GET.get('start_date', None)
        end_date = request.GET.get('end_date', None)
        status = request.GET.get('status', None)
        clientId = request.GET.get('clientId', None)
        poolId = request.GET.get('poolId', None)
        mediaId = request.GET.get('mediaId', None)

        if start_date and end_date:

            lista_jobs = filtro_rangedate(start_date=start_date, end_date=end_date)

        if status or clientId or mediaId:

            if poolId == 'any' and clientId == 'any' and mediaId == 'any':

                lista_jobs = filtro_rangedate(start_date=start_date, end_date=end_date)

            elif poolId != 'any':

                lista_jobs = filtro_status(status=poolId, start_date=start_date, end_date=end_date)

            elif clientId != 'any':

                lista_jobs = filtro_clientid(clientid=clientId, start_date=start_date, end_date=end_date)

            elif mediaId != 'any':

                lista_jobs = filtro_mediaid(mediaid=mediaId, start_date=start_date, end_date=end_date)

        context = {
            'qs_status': qs_status,
            'qs_name': qs_name,
            'qs_pool': qs_pool,
            'qs_media': qs_media,
            'lista_jobs': lista_jobs
        }

        return render(request, 'listarjobs.html', context)


class DadosJSONView(BaseLineChartView):

    def get_labels(self):
        labels = []
        queryset = list(Job.objects.values('name').annotate(name_jobfiles=Sum('jobfiles')).order_by('-name_jobfiles'))
        for obj in queryset:
            labels.append(obj['name'].decode('utf-8'))
        return labels

    def get_providers(self):
        datasets = [
            "Total armazenado (Todas as mídias)",
        ]
        return datasets

    def get_data(self):
        dados = []
        temp = []
        queryset = list(Job.objects.values('name').annotate(name_jobfiles=Sum('jobfiles')).order_by('-name_jobfiles'))
        for i in range(1):
            for obj in queryset:
                temp.append(obj['name_jobfiles'])
            dados.append(temp)
        return dados


class ClientesView(TemplateView):
    template_name = 'listclientes.html'

    def get_context_data(self, **kwargs):
        context = super(ClientesView, self).get_context_data(**kwargs)
        context['Client'] = Client.objects.all()
        return context


"""
class PainelClientesView(TemplateView):
    template_name = 'painel.html'

    def get_context_data(self, **kwargs):
        context = super(PainelClientesView, self).get_context_data(**kwargs)
        start_date = self.request.GET.get('start_date')
        end_date = self.request.GET.get('end_date')

        if start_date and end_date:
            context['Jobcount'] = Job.objects.values('name').filter(endtime__range=(start_date, end_date)).annotate(
            Count('name'))

        return context
"""


class JobYearArchiveView(YearArchiveView):
    template_name = 'job_archive_year.html'
    queryset = Job.objects.all()
    date_field = "endtime"
    make_object_list = True
    allow_future = True


class JobMonthArchiveView(MonthArchiveView):
    template_name = 'job_archive_month.html'
    queryset = Job.objects.all()
    date_field = 'endtime'
    allow_future = True


class JobWeekArchiveView(WeekArchiveView):
    template_name = 'job_archive_week.html'
    queryset = Job.objects.all()
    date_field = 'endtime'
    week_format = '%W'
    allow_future = True


class JobDayArchiveView(DayArchiveView):
    template_name = 'job_archive_day.html'
    queryset = Job.objects.all()
    date_field = 'endtime'
    day_format = '%d'
    allow_future = True
