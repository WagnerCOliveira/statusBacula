# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Basefiles(models.Model):
    baseid = models.AutoField(db_column='BaseId', primary_key=True)  # Field name made lowercase.
    basejobid = models.PositiveIntegerField(db_column='BaseJobId')  # Field name made lowercase.
    jobid = models.PositiveIntegerField(db_column='JobId')  # Field name made lowercase.
    fileid = models.PositiveBigIntegerField(db_column='FileId')  # Field name made lowercase.
    fileindex = models.PositiveIntegerField(db_column='FileIndex', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'BaseFiles'


class Cdimages(models.Model):
    mediaid = models.PositiveIntegerField(db_column='MediaId', primary_key=True)  # Field name made lowercase.
    lastburn = models.DateTimeField(db_column='LastBurn')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CDImages'


class Client(models.Model):
    clientid = models.AutoField(db_column='ClientId', primary_key=True)  # Field name made lowercase.
    name = models.TextField(db_column='Name', unique=True)  # Field name made lowercase.
    uname = models.TextField(db_column='Uname')  # Field name made lowercase.
    autoprune = models.IntegerField(db_column='AutoPrune', blank=True, null=True)  # Field name made lowercase.
    fileretention = models.PositiveBigIntegerField(db_column='FileRetention', blank=True, null=True)  # Field name made lowercase.
    jobretention = models.PositiveBigIntegerField(db_column='JobRetention', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Client'


class Counters(models.Model):
    counter = models.TextField(db_column='Counter', primary_key=True)  # Field name made lowercase.
    minvalue = models.IntegerField(db_column='MinValue', blank=True, null=True)  # Field name made lowercase.
    maxvalue = models.IntegerField(db_column='MaxValue', blank=True, null=True)  # Field name made lowercase.
    currentvalue = models.IntegerField(db_column='CurrentValue', blank=True, null=True)  # Field name made lowercase.
    wrapcounter = models.TextField(db_column='WrapCounter')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Counters'


class Device(models.Model):
    deviceid = models.AutoField(db_column='DeviceId', primary_key=True)  # Field name made lowercase.
    name = models.TextField(db_column='Name')  # Field name made lowercase.
    mediatypeid = models.PositiveIntegerField(db_column='MediaTypeId', blank=True, null=True)  # Field name made lowercase.
    storageid = models.PositiveIntegerField(db_column='StorageId', blank=True, null=True)  # Field name made lowercase.
    devmounts = models.PositiveIntegerField(db_column='DevMounts', blank=True, null=True)  # Field name made lowercase.
    devreadbytes = models.PositiveBigIntegerField(db_column='DevReadBytes', blank=True, null=True)  # Field name made lowercase.
    devwritebytes = models.PositiveBigIntegerField(db_column='DevWriteBytes', blank=True, null=True)  # Field name made lowercase.
    devreadbytessincecleaning = models.PositiveBigIntegerField(db_column='DevReadBytesSinceCleaning', blank=True, null=True)  # Field name made lowercase.
    devwritebytessincecleaning = models.PositiveBigIntegerField(db_column='DevWriteBytesSinceCleaning', blank=True, null=True)  # Field name made lowercase.
    devreadtime = models.PositiveBigIntegerField(db_column='DevReadTime', blank=True, null=True)  # Field name made lowercase.
    devwritetime = models.PositiveBigIntegerField(db_column='DevWriteTime', blank=True, null=True)  # Field name made lowercase.
    devreadtimesincecleaning = models.PositiveBigIntegerField(db_column='DevReadTimeSinceCleaning', blank=True, null=True)  # Field name made lowercase.
    devwritetimesincecleaning = models.PositiveBigIntegerField(db_column='DevWriteTimeSinceCleaning', blank=True, null=True)  # Field name made lowercase.
    cleaningdate = models.DateTimeField(db_column='CleaningDate', blank=True, null=True)  # Field name made lowercase.
    cleaningperiod = models.PositiveBigIntegerField(db_column='CleaningPeriod', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Device'


class File(models.Model):
    fileid = models.BigAutoField(db_column='FileId', primary_key=True)  # Field name made lowercase.
    fileindex = models.PositiveIntegerField(db_column='FileIndex', blank=True, null=True)  # Field name made lowercase.
    jobid = models.PositiveIntegerField(db_column='JobId')  # Field name made lowercase.
    pathid = models.PositiveIntegerField(db_column='PathId')  # Field name made lowercase.
    filenameid = models.PositiveIntegerField(db_column='FilenameId')  # Field name made lowercase.
    deltaseq = models.PositiveSmallIntegerField(db_column='DeltaSeq', blank=True, null=True)  # Field name made lowercase.
    markid = models.PositiveIntegerField(db_column='MarkId', blank=True, null=True)  # Field name made lowercase.
    lstat = models.TextField(db_column='LStat')  # Field name made lowercase.
    md5 = models.TextField(db_column='MD5', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'File'


class Fileset(models.Model):
    filesetid = models.AutoField(db_column='FileSetId', primary_key=True)  # Field name made lowercase.
    fileset = models.TextField(db_column='FileSet')  # Field name made lowercase.
    md5 = models.TextField(db_column='MD5', blank=True, null=True)  # Field name made lowercase.
    createtime = models.DateTimeField(db_column='CreateTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'FileSet'


class Filename(models.Model):
    filenameid = models.AutoField(db_column='FilenameId', primary_key=True)  # Field name made lowercase.
    name = models.TextField(db_column='Name')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Filename'


class Job(models.Model):
    jobid = models.AutoField(db_column='JobId', primary_key=True)  # Field name made lowercase.
    job = models.TextField(db_column='Job')  # Field name made lowercase.
    name = models.TextField(db_column='Name')  # Field name made lowercase.
    type = models.CharField(db_column='Type', max_length=1)  # Field name made lowercase.
    level = models.CharField(db_column='Level', max_length=1)  # Field name made lowercase.
    clientid = models.IntegerField(db_column='ClientId', blank=True, null=True)  # Field name made lowercase.
    jobstatus = models.CharField(db_column='JobStatus', max_length=1)  # Field name made lowercase.
    schedtime = models.DateTimeField(db_column='SchedTime', blank=True, null=True)  # Field name made lowercase.
    starttime = models.DateTimeField(db_column='StartTime', blank=True, null=True)  # Field name made lowercase.
    endtime = models.DateTimeField(db_column='EndTime', blank=True, null=True)  # Field name made lowercase.
    realendtime = models.DateTimeField(db_column='RealEndTime', blank=True, null=True)  # Field name made lowercase.
    jobtdate = models.PositiveBigIntegerField(db_column='JobTDate', blank=True, null=True)  # Field name made lowercase.
    volsessionid = models.PositiveIntegerField(db_column='VolSessionId', blank=True, null=True)  # Field name made lowercase.
    volsessiontime = models.PositiveIntegerField(db_column='VolSessionTime', blank=True, null=True)  # Field name made lowercase.
    jobfiles = models.PositiveIntegerField(db_column='JobFiles', blank=True, null=True)  # Field name made lowercase.
    jobbytes = models.PositiveBigIntegerField(db_column='JobBytes', blank=True, null=True)  # Field name made lowercase.
    readbytes = models.PositiveBigIntegerField(db_column='ReadBytes', blank=True, null=True)  # Field name made lowercase.
    joberrors = models.PositiveIntegerField(db_column='JobErrors', blank=True, null=True)  # Field name made lowercase.
    jobmissingfiles = models.PositiveIntegerField(db_column='JobMissingFiles', blank=True, null=True)  # Field name made lowercase.
    poolid = models.PositiveIntegerField(db_column='PoolId', blank=True, null=True)  # Field name made lowercase.
    filesetid = models.PositiveIntegerField(db_column='FileSetId', blank=True, null=True)  # Field name made lowercase.
    priorjobid = models.PositiveIntegerField(db_column='PriorJobId', blank=True, null=True)  # Field name made lowercase.
    purgedfiles = models.IntegerField(db_column='PurgedFiles', blank=True, null=True)  # Field name made lowercase.
    hasbase = models.IntegerField(db_column='HasBase', blank=True, null=True)  # Field name made lowercase.
    hascache = models.IntegerField(db_column='HasCache', blank=True, null=True)  # Field name made lowercase.
    reviewed = models.IntegerField(db_column='Reviewed', blank=True, null=True)  # Field name made lowercase.
    comment = models.TextField(db_column='Comment', blank=True, null=True)  # Field name made lowercase.

    def __str__(self):
        return self.name

    class Meta:
        managed = False
        db_table = 'Job'
        verbose_name = 'Job'
        verbose_name_plural = 'Jobs'


class Jobhisto(models.Model):
    jobid = models.PositiveIntegerField(db_column='JobId')  # Field name made lowercase.
    job = models.TextField(db_column='Job')  # Field name made lowercase.
    name = models.TextField(db_column='Name')  # Field name made lowercase.
    type = models.CharField(db_column='Type', max_length=1)  # Field name made lowercase.
    level = models.CharField(db_column='Level', max_length=1)  # Field name made lowercase.
    clientid = models.IntegerField(db_column='ClientId', blank=True, null=True)  # Field name made lowercase.
    jobstatus = models.CharField(db_column='JobStatus', max_length=1)  # Field name made lowercase.
    schedtime = models.DateTimeField(db_column='SchedTime', blank=True, null=True)  # Field name made lowercase.
    starttime = models.DateTimeField(db_column='StartTime', blank=True, null=True)  # Field name made lowercase.
    endtime = models.DateTimeField(db_column='EndTime', blank=True, null=True)  # Field name made lowercase.
    realendtime = models.DateTimeField(db_column='RealEndTime', blank=True, null=True)  # Field name made lowercase.
    jobtdate = models.PositiveBigIntegerField(db_column='JobTDate', blank=True, null=True)  # Field name made lowercase.
    volsessionid = models.PositiveIntegerField(db_column='VolSessionId', blank=True, null=True)  # Field name made lowercase.
    volsessiontime = models.PositiveIntegerField(db_column='VolSessionTime', blank=True, null=True)  # Field name made lowercase.
    jobfiles = models.PositiveIntegerField(db_column='JobFiles', blank=True, null=True)  # Field name made lowercase.
    jobbytes = models.PositiveBigIntegerField(db_column='JobBytes', blank=True, null=True)  # Field name made lowercase.
    readbytes = models.PositiveBigIntegerField(db_column='ReadBytes', blank=True, null=True)  # Field name made lowercase.
    joberrors = models.PositiveIntegerField(db_column='JobErrors', blank=True, null=True)  # Field name made lowercase.
    jobmissingfiles = models.PositiveIntegerField(db_column='JobMissingFiles', blank=True, null=True)  # Field name made lowercase.
    poolid = models.PositiveIntegerField(db_column='PoolId', blank=True, null=True)  # Field name made lowercase.
    filesetid = models.PositiveIntegerField(db_column='FileSetId', blank=True, null=True)  # Field name made lowercase.
    priorjobid = models.PositiveIntegerField(db_column='PriorJobId', blank=True, null=True)  # Field name made lowercase.
    purgedfiles = models.IntegerField(db_column='PurgedFiles', blank=True, null=True)  # Field name made lowercase.
    hasbase = models.IntegerField(db_column='HasBase', blank=True, null=True)  # Field name made lowercase.
    hascache = models.IntegerField(db_column='HasCache', blank=True, null=True)  # Field name made lowercase.
    reviewed = models.IntegerField(db_column='Reviewed', blank=True, null=True)  # Field name made lowercase.
    comment = models.TextField(db_column='Comment', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'JobHisto'


class Jobmedia(models.Model):
    jobmediaid = models.AutoField(db_column='JobMediaId', primary_key=True)  # Field name made lowercase.
    jobid = models.PositiveIntegerField(db_column='JobId')  # Field name made lowercase.
    mediaid = models.PositiveIntegerField(db_column='MediaId')  # Field name made lowercase.
    firstindex = models.PositiveIntegerField(db_column='FirstIndex', blank=True, null=True)  # Field name made lowercase.
    lastindex = models.PositiveIntegerField(db_column='LastIndex', blank=True, null=True)  # Field name made lowercase.
    startfile = models.PositiveIntegerField(db_column='StartFile', blank=True, null=True)  # Field name made lowercase.
    endfile = models.PositiveIntegerField(db_column='EndFile', blank=True, null=True)  # Field name made lowercase.
    startblock = models.PositiveIntegerField(db_column='StartBlock', blank=True, null=True)  # Field name made lowercase.
    endblock = models.PositiveIntegerField(db_column='EndBlock', blank=True, null=True)  # Field name made lowercase.
    volindex = models.PositiveIntegerField(db_column='VolIndex', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'JobMedia'


class Location(models.Model):
    locationid = models.AutoField(db_column='LocationId', primary_key=True)  # Field name made lowercase.
    location = models.TextField(db_column='Location')  # Field name made lowercase.
    cost = models.IntegerField(db_column='Cost', blank=True, null=True)  # Field name made lowercase.
    enabled = models.IntegerField(db_column='Enabled', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Location'


class Locationlog(models.Model):
    loclogid = models.AutoField(db_column='LocLogId', primary_key=True)  # Field name made lowercase.
    date = models.DateTimeField(db_column='Date', blank=True, null=True)  # Field name made lowercase.
    comment = models.TextField(db_column='Comment')  # Field name made lowercase.
    mediaid = models.PositiveIntegerField(db_column='MediaId', blank=True, null=True)  # Field name made lowercase.
    locationid = models.PositiveIntegerField(db_column='LocationId', blank=True, null=True)  # Field name made lowercase.
    newvolstatus = models.CharField(db_column='NewVolStatus', max_length=9)  # Field name made lowercase.
    newenabled = models.IntegerField(db_column='NewEnabled', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'LocationLog'


class Log(models.Model):
    logid = models.AutoField(db_column='LogId', primary_key=True)  # Field name made lowercase.
    jobid = models.PositiveIntegerField(db_column='JobId', blank=True, null=True)  # Field name made lowercase.
    time = models.DateTimeField(db_column='Time', blank=True, null=True)  # Field name made lowercase.
    logtext = models.TextField(db_column='LogText')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Log'


class Media(models.Model):
    mediaid = models.AutoField(db_column='MediaId', primary_key=True)  # Field name made lowercase.
    volumename = models.TextField(db_column='VolumeName', unique=True)  # Field name made lowercase.
    slot = models.IntegerField(db_column='Slot', blank=True, null=True)  # Field name made lowercase.
    poolid = models.PositiveIntegerField(db_column='PoolId', blank=True, null=True)  # Field name made lowercase.
    mediatype = models.TextField(db_column='MediaType')  # Field name made lowercase.
    mediatypeid = models.PositiveIntegerField(db_column='MediaTypeId', blank=True, null=True)  # Field name made lowercase.
    labeltype = models.IntegerField(db_column='LabelType', blank=True, null=True)  # Field name made lowercase.
    firstwritten = models.DateTimeField(db_column='FirstWritten', blank=True, null=True)  # Field name made lowercase.
    lastwritten = models.DateTimeField(db_column='LastWritten', blank=True, null=True)  # Field name made lowercase.
    labeldate = models.DateTimeField(db_column='LabelDate', blank=True, null=True)  # Field name made lowercase.
    voljobs = models.PositiveIntegerField(db_column='VolJobs', blank=True, null=True)  # Field name made lowercase.
    volfiles = models.PositiveIntegerField(db_column='VolFiles', blank=True, null=True)  # Field name made lowercase.
    volblocks = models.PositiveIntegerField(db_column='VolBlocks', blank=True, null=True)  # Field name made lowercase.
    volmounts = models.PositiveIntegerField(db_column='VolMounts', blank=True, null=True)  # Field name made lowercase.
    volbytes = models.PositiveBigIntegerField(db_column='VolBytes', blank=True, null=True)  # Field name made lowercase.
    volparts = models.PositiveIntegerField(db_column='VolParts', blank=True, null=True)  # Field name made lowercase.
    volerrors = models.PositiveIntegerField(db_column='VolErrors', blank=True, null=True)  # Field name made lowercase.
    volwrites = models.PositiveIntegerField(db_column='VolWrites', blank=True, null=True)  # Field name made lowercase.
    volcapacitybytes = models.PositiveBigIntegerField(db_column='VolCapacityBytes', blank=True, null=True)  # Field name made lowercase.
    volstatus = models.CharField(db_column='VolStatus', max_length=9)  # Field name made lowercase.
    enabled = models.IntegerField(db_column='Enabled', blank=True, null=True)  # Field name made lowercase.
    recycle = models.IntegerField(db_column='Recycle', blank=True, null=True)  # Field name made lowercase.
    actiononpurge = models.IntegerField(db_column='ActionOnPurge', blank=True, null=True)  # Field name made lowercase.
    volretention = models.PositiveBigIntegerField(db_column='VolRetention', blank=True, null=True)  # Field name made lowercase.
    voluseduration = models.PositiveBigIntegerField(db_column='VolUseDuration', blank=True, null=True)  # Field name made lowercase.
    maxvoljobs = models.PositiveIntegerField(db_column='MaxVolJobs', blank=True, null=True)  # Field name made lowercase.
    maxvolfiles = models.PositiveIntegerField(db_column='MaxVolFiles', blank=True, null=True)  # Field name made lowercase.
    maxvolbytes = models.PositiveBigIntegerField(db_column='MaxVolBytes', blank=True, null=True)  # Field name made lowercase.
    inchanger = models.IntegerField(db_column='InChanger', blank=True, null=True)  # Field name made lowercase.
    storageid = models.PositiveIntegerField(db_column='StorageId', blank=True, null=True)  # Field name made lowercase.
    deviceid = models.PositiveIntegerField(db_column='DeviceId', blank=True, null=True)  # Field name made lowercase.
    mediaaddressing = models.IntegerField(db_column='MediaAddressing', blank=True, null=True)  # Field name made lowercase.
    volreadtime = models.PositiveBigIntegerField(db_column='VolReadTime', blank=True, null=True)  # Field name made lowercase.
    volwritetime = models.PositiveBigIntegerField(db_column='VolWriteTime', blank=True, null=True)  # Field name made lowercase.
    endfile = models.PositiveIntegerField(db_column='EndFile', blank=True, null=True)  # Field name made lowercase.
    endblock = models.PositiveIntegerField(db_column='EndBlock', blank=True, null=True)  # Field name made lowercase.
    locationid = models.PositiveIntegerField(db_column='LocationId', blank=True, null=True)  # Field name made lowercase.
    recyclecount = models.PositiveIntegerField(db_column='RecycleCount', blank=True, null=True)  # Field name made lowercase.
    initialwrite = models.DateTimeField(db_column='InitialWrite', blank=True, null=True)  # Field name made lowercase.
    scratchpoolid = models.PositiveIntegerField(db_column='ScratchPoolId', blank=True, null=True)  # Field name made lowercase.
    recyclepoolid = models.PositiveIntegerField(db_column='RecyclePoolId', blank=True, null=True)  # Field name made lowercase.
    comment = models.TextField(db_column='Comment', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Media'


class Mediatype(models.Model):
    mediatypeid = models.AutoField(db_column='MediaTypeId', primary_key=True)  # Field name made lowercase.
    mediatype = models.TextField(db_column='MediaType')  # Field name made lowercase.
    readonly = models.IntegerField(db_column='ReadOnly', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MediaType'


class Path(models.Model):
    pathid = models.AutoField(db_column='PathId', primary_key=True)  # Field name made lowercase.
    path = models.TextField(db_column='Path')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Path'


class Pathhierarchy(models.Model):
    pathid = models.IntegerField(db_column='PathId', primary_key=True)  # Field name made lowercase.
    ppathid = models.IntegerField(db_column='PPathId')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PathHierarchy'


class Pathvisibility(models.Model):
    pathid = models.IntegerField(db_column='PathId')  # Field name made lowercase.
    jobid = models.IntegerField(db_column='JobId', primary_key=True)  # Field name made lowercase.
    size = models.BigIntegerField(db_column='Size', blank=True, null=True)  # Field name made lowercase.
    files = models.IntegerField(db_column='Files', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PathVisibility'
        unique_together = (('jobid', 'pathid'),)


class Pool(models.Model):
    poolid = models.AutoField(db_column='PoolId', primary_key=True)  # Field name made lowercase.
    name = models.TextField(db_column='Name', unique=True)  # Field name made lowercase.
    numvols = models.PositiveIntegerField(db_column='NumVols', blank=True, null=True)  # Field name made lowercase.
    maxvols = models.PositiveIntegerField(db_column='MaxVols', blank=True, null=True)  # Field name made lowercase.
    useonce = models.IntegerField(db_column='UseOnce', blank=True, null=True)  # Field name made lowercase.
    usecatalog = models.IntegerField(db_column='UseCatalog', blank=True, null=True)  # Field name made lowercase.
    acceptanyvolume = models.IntegerField(db_column='AcceptAnyVolume', blank=True, null=True)  # Field name made lowercase.
    volretention = models.PositiveBigIntegerField(db_column='VolRetention', blank=True, null=True)  # Field name made lowercase.
    voluseduration = models.PositiveBigIntegerField(db_column='VolUseDuration', blank=True, null=True)  # Field name made lowercase.
    maxvoljobs = models.PositiveIntegerField(db_column='MaxVolJobs', blank=True, null=True)  # Field name made lowercase.
    maxvolfiles = models.PositiveIntegerField(db_column='MaxVolFiles', blank=True, null=True)  # Field name made lowercase.
    maxvolbytes = models.PositiveBigIntegerField(db_column='MaxVolBytes', blank=True, null=True)  # Field name made lowercase.
    autoprune = models.IntegerField(db_column='AutoPrune', blank=True, null=True)  # Field name made lowercase.
    recycle = models.IntegerField(db_column='Recycle', blank=True, null=True)  # Field name made lowercase.
    actiononpurge = models.IntegerField(db_column='ActionOnPurge', blank=True, null=True)  # Field name made lowercase.
    pooltype = models.CharField(db_column='PoolType', max_length=9)  # Field name made lowercase.
    labeltype = models.IntegerField(db_column='LabelType', blank=True, null=True)  # Field name made lowercase.
    labelformat = models.TextField(db_column='LabelFormat', blank=True, null=True)  # Field name made lowercase.
    enabled = models.IntegerField(db_column='Enabled', blank=True, null=True)  # Field name made lowercase.
    scratchpoolid = models.PositiveIntegerField(db_column='ScratchPoolId', blank=True, null=True)  # Field name made lowercase.
    recyclepoolid = models.PositiveIntegerField(db_column='RecyclePoolId', blank=True, null=True)  # Field name made lowercase.
    nextpoolid = models.PositiveIntegerField(db_column='NextPoolId', blank=True, null=True)  # Field name made lowercase.
    migrationhighbytes = models.PositiveBigIntegerField(db_column='MigrationHighBytes', blank=True, null=True)  # Field name made lowercase.
    migrationlowbytes = models.PositiveBigIntegerField(db_column='MigrationLowBytes', blank=True, null=True)  # Field name made lowercase.
    migrationtime = models.PositiveBigIntegerField(db_column='MigrationTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Pool'


class Restoreobject(models.Model):
    restoreobjectid = models.AutoField(db_column='RestoreObjectId', primary_key=True)  # Field name made lowercase.
    objectname = models.TextField(db_column='ObjectName')  # Field name made lowercase.
    restoreobject = models.TextField(db_column='RestoreObject')  # Field name made lowercase.
    pluginname = models.TextField(db_column='PluginName')  # Field name made lowercase.
    objectlength = models.IntegerField(db_column='ObjectLength', blank=True, null=True)  # Field name made lowercase.
    objectfulllength = models.IntegerField(db_column='ObjectFullLength', blank=True, null=True)  # Field name made lowercase.
    objectindex = models.IntegerField(db_column='ObjectIndex', blank=True, null=True)  # Field name made lowercase.
    objecttype = models.IntegerField(db_column='ObjectType', blank=True, null=True)  # Field name made lowercase.
    fileindex = models.PositiveIntegerField(db_column='FileIndex', blank=True, null=True)  # Field name made lowercase.
    jobid = models.PositiveIntegerField(db_column='JobId')  # Field name made lowercase.
    objectcompression = models.IntegerField(db_column='ObjectCompression', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'RestoreObject'


class Status(models.Model):
    jobstatus = models.CharField(db_column='JobStatus', primary_key=True, max_length=1)  # Field name made lowercase.
    jobstatuslong = models.TextField(db_column='JobStatusLong', blank=True, null=True)  # Field name made lowercase.
    severity = models.IntegerField(db_column='Severity', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Status'


class Storage(models.Model):
    storageid = models.AutoField(db_column='StorageId', primary_key=True)  # Field name made lowercase.
    name = models.TextField(db_column='Name')  # Field name made lowercase.
    autochanger = models.IntegerField(db_column='AutoChanger', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Storage'


class Unsavedfiles(models.Model):
    unsavedid = models.AutoField(db_column='UnsavedId', primary_key=True)  # Field name made lowercase.
    jobid = models.PositiveIntegerField(db_column='JobId')  # Field name made lowercase.
    pathid = models.PositiveIntegerField(db_column='PathId')  # Field name made lowercase.
    filenameid = models.PositiveIntegerField(db_column='FilenameId')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'UnsavedFiles'


class Version(models.Model):
    versionid = models.PositiveIntegerField(db_column='VersionId')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Version'
