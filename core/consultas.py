from django.db.models import Q
from core.models import Job, Pool, Jobmedia, Status


def filtro_rangedate(start_date=None, end_date=None):

    jobid = []
    name = []
    job = []
    starttime = []
    type = []
    level = []
    poolid = []
    jobfiles = []
    jobbytes = []

    qs_filter = list(Job.objects.values('jobid', 'name', 'job', 'starttime', 'type', 'level', 'poolid', 'jobfiles',
                                        'jobbytes').filter(endtime__range=(start_date, end_date)))

    for obj in qs_filter:
        qs_pool = list(Pool.objects.values('name').filter(poolid=obj['poolid']))
        jobid.append(obj['jobid'])
        name.append(obj['name'].decode('utf8'))
        job.append(obj['job'].decode('utf8'))
        starttime.append(obj['starttime'])
        type.append(obj['type'].decode('utf8'))
        level.append(obj['level'].decode('utf8'))
        for pool in qs_pool:
            poolid.append(pool['name'].decode('utf8'))
        jobfiles.append(obj['jobfiles'])
        jobbytes.append(obj['jobbytes'])

    qs_lista = zip(jobid, name, job, starttime, type, level, poolid, jobfiles, jobbytes)

    return qs_lista


def filtro_status(status=None, start_date=None, end_date=None):

    jobid = []
    name = []
    job = []
    starttime = []
    type = []
    level = []
    poolid = []
    jobfiles = []
    jobbytes = []

    qs_filter = list(Job.objects.values('jobid', 'name', 'job', 'starttime', 'type', 'level', 'poolid', 'jobfiles',
                                        'jobbytes').filter(Q(poolid=status), Q(endtime__range=(start_date, end_date))))

    for obj in qs_filter:
        qs_pool = list(Pool.objects.values('name').filter(poolid=obj['poolid']))
        jobid.append(obj['jobid'])
        name.append(obj['name'].decode('utf8'))
        job.append(obj['job'].decode('utf8'))
        starttime.append(obj['starttime'])
        type.append(obj['type'].decode('utf8'))
        level.append(obj['level'].decode('utf8'))
        for pool in qs_pool:
            poolid.append(pool['name'].decode('utf8'))
        jobfiles.append(obj['jobfiles'])
        jobbytes.append(obj['jobbytes'])

    qs_lista = zip(jobid, name, job, starttime, type, level, poolid, jobfiles, jobbytes)

    return qs_lista


def filtro_clientid(clientid=None, start_date=None, end_date=None):

    jobid = []
    name = []
    job = []
    starttime = []
    type = []
    level = []
    poolid = []
    jobfiles = []
    jobbytes = []

    qs_filter = list(Job.objects.values('jobid', 'name', 'job', 'starttime', 'type', 'level', 'poolid', 'jobfiles',
                                        'jobbytes').filter(Q(clientid=clientid),
                                                           Q(endtime__range=(start_date, end_date))))

    for obj in qs_filter:
        qs_pool = list(Pool.objects.values('name').filter(poolid=obj['poolid']))
        jobid.append(obj['jobid'])
        name.append(obj['name'].decode('utf8'))
        job.append(obj['job'].decode('utf8'))
        starttime.append(obj['starttime'])
        type.append(obj['type'].decode('utf8'))
        level.append(obj['level'].decode('utf8'))
        for pool in qs_pool:
            poolid.append(pool['name'].decode('utf8'))
        jobfiles.append(obj['jobfiles'])
        jobbytes.append(obj['jobbytes'])

    qs_lista = zip(jobid, name, job, starttime, type, level, poolid, jobfiles, jobbytes)

    return qs_lista


def filtro_mediaid(mediaid=None, start_date=None, end_date=None):

    jobid = []
    name = []
    job = []
    starttime = []
    type = []
    level = []
    poolid = []
    jobfiles = []
    jobbytes = []

    qs_jobmediaid = list(Jobmedia.objects.values('jobid').filter(mediaid=mediaid).distinct())

    for obj in qs_jobmediaid:

        qs_filter = list(Job.objects.values('jobid', 'name', 'job', 'starttime', 'type', 'level', 'poolid', 'jobfiles',
                           'jobbytes').filter(Q(jobid=obj['jobid']),
                                              Q(endtime__range=(start_date, end_date))))

        for items in qs_filter:
            qs_pool = list(Pool.objects.values('name').filter(poolid=items['poolid']))
            jobid.append(items['jobid'])
            name.append(items['name'].decode('utf8'))
            job.append(items['job'].decode('utf8'))
            starttime.append(items['starttime'])
            type.append(items['type'].decode('utf8'))
            level.append(items['level'].decode('utf8'))
            for pool in qs_pool:
                poolid.append(pool['name'].decode('utf8'))
            jobfiles.append(items['jobfiles'])
            jobbytes.append(items['jobbytes'])

    qs_lista = zip(jobid, name, job, starttime, type, level, poolid, jobfiles, jobbytes)
    return qs_lista


def filtro_statusjobs(start_date=None, end_date=None):

    statusjobs = []
    tiposstatusjobs = []
    qtdstatusjobs = []

    qs_filter = list(Job.objects.values('jobstatus').filter(endtime__range=(start_date, end_date)))
    qs_tipos = list(Job.objects.values('jobstatus').filter(endtime__range=(start_date, end_date)).distinct())

    for items in qs_filter:
       statusjobs.append(items['jobstatus'])

    qtdstatusjobs.append(len(statusjobs))

    for items in qs_tipos:
        if items['jobstatus'].decode('utf8') == 'T':
            tiposstatusjobs.append('Completed successfully')

    qs_lista = zip(tiposstatusjobs, qtdstatusjobs)
    return qs_lista