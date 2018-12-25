# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = True` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class ApkInfo(models.Model):
    did = models.CharField(max_length=60)
    up_date = models.DateTimeField()
    on = models.CharField(max_length=30, blank=True, null=True)
    action = models.CharField(max_length=30, blank=True, null=True)
    appname = models.CharField(db_column='appName', max_length=60, blank=True, null=True)  # Field name made lowercase.
    packagename = models.CharField(db_column='packageName', max_length=100, blank=True, null=True)  # Field name made lowercase.
    versioncode = models.CharField(db_column='versionCode', max_length=30, blank=True, null=True)  # Field name made lowercase.
    versionname = models.CharField(db_column='versionName', max_length=100, blank=True, null=True)  # Field name made lowercase.
    firstinstalltime = models.CharField(db_column='firstInstallTime', max_length=30, blank=True, null=True)  # Field name made lowercase.
    lastupdatetime = models.CharField(db_column='lastUpdateTime', max_length=30, blank=True, null=True)  # Field name made lowercase.
    sourcedir = models.CharField(db_column='sourceDir', max_length=200, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'apk_info'
        unique_together = (('id', 'up_date'),)


class ApklogSubmit(models.Model):
    did = models.CharField(max_length=60)
    up_date = models.DateTimeField()
    on = models.CharField(max_length=30, blank=True, null=True)
    dn = models.CharField(max_length=30, blank=True, null=True)
    dm = models.CharField(max_length=30, blank=True, null=True)
    session = models.CharField(max_length=10, blank=True, null=True)
    mac = models.CharField(max_length=30, blank=True, null=True)
    verc = models.CharField(max_length=30, blank=True, null=True)
    vern = models.CharField(max_length=30, blank=True, null=True)
    gzid = models.CharField(max_length=60, blank=True, null=True)
    fn = models.CharField(max_length=30, blank=True, null=True)
    jt = models.CharField(max_length=30, blank=True, null=True)
    file = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'apklog_submit'
        unique_together = (('id', 'up_date'),)


class AppUsage(models.Model):
    did = models.CharField(max_length=60)
    up_date = models.DateTimeField()
    on = models.CharField(max_length=30, blank=True, null=True)
    packagename = models.CharField(db_column='packageName', max_length=30, blank=True, null=True)  # Field name made lowercase.
    starttime = models.CharField(db_column='startTime', max_length=30, blank=True, null=True)  # Field name made lowercase.
    endtime = models.CharField(db_column='endTime', max_length=30, blank=True, null=True)  # Field name made lowercase.
    flag = models.CharField(max_length=30, blank=True, null=True)
    duration = models.CharField(max_length=30, blank=True, null=True)
    count = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'app_usage'


class DeviceInfo(models.Model):
    did = models.CharField(max_length=60)
    up_date = models.DateTimeField()
    on = models.CharField(max_length=30, blank=True, null=True)
    devicename = models.CharField(db_column='deviceName', max_length=30, blank=True, null=True)  # Field name made lowercase.
    devicemodel = models.CharField(db_column='deviceModel', max_length=30, blank=True, null=True)  # Field name made lowercase.
    mac = models.CharField(max_length=30, blank=True, null=True)
    oemname = models.CharField(db_column='oemName', max_length=30, blank=True, null=True)  # Field name made lowercase.
    screenwidth = models.CharField(db_column='screenWidth', max_length=30, blank=True, null=True)  # Field name made lowercase.
    screenheight = models.CharField(db_column='screenHeight', max_length=30, blank=True, null=True)  # Field name made lowercase.
    screensize = models.CharField(db_column='screenSize', max_length=30, blank=True, null=True)  # Field name made lowercase.
    platform = models.CharField(max_length=30, blank=True, null=True)
    wifimac = models.CharField(db_column='wifiMac', max_length=30, blank=True, null=True)  # Field name made lowercase.
    uniqueid = models.CharField(db_column='uniqueID', max_length=30, blank=True, null=True)  # Field name made lowercase.
    deviceid = models.CharField(db_column='deviceID', max_length=30, blank=True, null=True)  # Field name made lowercase.
    androidid = models.CharField(db_column='androidID', max_length=30, blank=True, null=True)  # Field name made lowercase.
    signalsource = models.CharField(db_column='signalSource', max_length=30, blank=True, null=True)  # Field name made lowercase.
    availmem = models.CharField(db_column='availMem', max_length=30, blank=True, null=True)  # Field name made lowercase.
    threshold = models.CharField(max_length=30, blank=True, null=True)
    totalmem = models.CharField(db_column='totalMem', max_length=30, blank=True, null=True)  # Field name made lowercase.
    lowmemory = models.CharField(db_column='lowMemory', max_length=30, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'device_info'
        unique_together = (('id', 'up_date'),)


class LocationInfo(models.Model):
    did = models.CharField(max_length=60)
    up_date = models.DateTimeField()
    on = models.CharField(max_length=30, blank=True, null=True)
    addr = models.CharField(max_length=60, blank=True, null=True)
    city = models.CharField(max_length=30, blank=True, null=True)
    coortype = models.CharField(db_column='coorType', max_length=30, blank=True, null=True)  # Field name made lowercase.
    country = models.CharField(max_length=30, blank=True, null=True)
    district = models.CharField(max_length=30, blank=True, null=True)
    errorcode = models.CharField(db_column='errorCode', max_length=30, blank=True, null=True)  # Field name made lowercase.
    latitude = models.CharField(max_length=30, blank=True, null=True)
    longitude = models.CharField(max_length=30, blank=True, null=True)
    province = models.CharField(max_length=30, blank=True, null=True)
    radius = models.CharField(max_length=30, blank=True, null=True)
    street = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'location_info'


class LogHeartbeat(models.Model):
    did = models.CharField(max_length=60)
    up_date = models.DateTimeField()
    on = models.CharField(max_length=30, blank=True, null=True)
    dn = models.CharField(max_length=30, blank=True, null=True)
    dm = models.CharField(max_length=30, blank=True, null=True)
    mac = models.CharField(max_length=30, blank=True, null=True)
    vern = models.CharField(max_length=30, blank=True, null=True)
    gzid = models.CharField(max_length=60, blank=True, null=True)
    app = models.CharField(max_length=60, blank=True, null=True)
    session = models.CharField(max_length=10, blank=True, null=True)
    verc = models.CharField(max_length=30, blank=True, null=True)
    local_ts = models.CharField(max_length=30, blank=True, null=True)
    interval = models.CharField(max_length=10, blank=True, null=True)
    pid = models.CharField(max_length=10, blank=True, null=True)
    jt = models.CharField(max_length=30, blank=True, null=True)
    cid = models.CharField(max_length=30, blank=True, null=True)
    description = models.CharField(max_length=30, blank=True, null=True)
    cn = models.CharField(max_length=30, blank=True, null=True)
    recognizer = models.CharField(max_length=30, blank=True, null=True)
    fid = models.CharField(max_length=60, blank=True, null=True)
    chuid = models.CharField(max_length=60, blank=True, null=True)
    match_time = models.CharField(max_length=30, blank=True, null=True)
    success_count = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'log_heartbeat'
        unique_together = (('id', 'up_date'),)


class OsInfo(models.Model):
    did = models.CharField(max_length=60)
    up_date = models.DateTimeField()
    on = models.CharField(max_length=30, blank=True, null=True)
    sdkversion = models.CharField(db_column='sdkVersion', max_length=30, blank=True, null=True)  # Field name made lowercase.
    androidversion = models.CharField(db_column='androidVersion', max_length=30, blank=True, null=True)  # Field name made lowercase.
    cpuabi = models.CharField(db_column='cpuAbi', max_length=30, blank=True, null=True)  # Field name made lowercase.
    board = models.CharField(max_length=30, blank=True, null=True)
    manufacturer = models.CharField(max_length=100, blank=True, null=True)
    syslanguage = models.CharField(db_column='sysLanguage', max_length=30, blank=True, null=True)  # Field name made lowercase.
    syscountry = models.CharField(db_column='sysCountry', max_length=30, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'os_info'


class OtherDevice(models.Model):
    did = models.CharField(max_length=60)
    up_date = models.DateTimeField()
    on = models.CharField(max_length=30, blank=True, null=True)
    hostname = models.CharField(db_column='hostName', max_length=30, blank=True, null=True)  # Field name made lowercase.
    gzmac = models.CharField(db_column='gzMac', max_length=30, blank=True, null=True)  # Field name made lowercase.
    scancount = models.CharField(db_column='scanCount', max_length=10, blank=True, null=True)  # Field name made lowercase.
    reachablecount = models.CharField(db_column='reachableCount', max_length=10, blank=True, null=True)  # Field name made lowercase.
    ip = models.CharField(max_length=30, blank=True, null=True)
    latestreachable = models.CharField(db_column='latestReachable', max_length=30, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'other_device'


class OtherMessage(models.Model):
    did = models.CharField(max_length=60)
    up_date = models.DateTimeField()
    on = models.CharField(max_length=30, blank=True, null=True)
    bd_push_id = models.CharField(max_length=60, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'other_message'


class ProcessInfo(models.Model):
    did = models.CharField(max_length=60)
    up_date = models.DateTimeField()
    on = models.CharField(max_length=30, blank=True, null=True)
    processname = models.CharField(db_column='processName', max_length=30, blank=True, null=True)  # Field name made lowercase.
    pid = models.CharField(max_length=30, blank=True, null=True)
    uid = models.CharField(max_length=30, blank=True, null=True)
    pkglist = models.CharField(db_column='pkgList', max_length=200, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'process_info'


class SnapshotSubmit(models.Model):
    did = models.CharField(max_length=60)
    up_date = models.DateTimeField()
    on = models.CharField(max_length=30, blank=True, null=True)
    dn = models.CharField(max_length=30, blank=True, null=True)
    dm = models.CharField(max_length=30, blank=True, null=True)
    ts = models.CharField(max_length=30, blank=True, null=True)
    session = models.CharField(max_length=30, blank=True, null=True)
    gzid = models.CharField(max_length=60, blank=True, null=True)
    fid = models.CharField(max_length=60, blank=True, null=True)
    type = models.CharField(max_length=10, blank=True, null=True)
    o = models.CharField(max_length=10, blank=True, null=True)
    w = models.CharField(max_length=10, blank=True, null=True)
    h = models.CharField(max_length=10, blank=True, null=True)
    cv = models.CharField(max_length=30, blank=True, null=True)
    ci = models.CharField(max_length=30, blank=True, null=True)
    dummy = models.CharField(max_length=60, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'snapshot_submit'


class UbUpdata(models.Model):
    did = models.CharField(max_length=60)
    up_date = models.DateTimeField()
    on = models.CharField(max_length=30, blank=True, null=True)
    dn = models.CharField(max_length=30, blank=True, null=True)
    dm = models.CharField(max_length=30, blank=True, null=True)
    mac = models.CharField(max_length=30, blank=True, null=True)
    vern = models.CharField(max_length=30, blank=True, null=True)
    jt = models.CharField(max_length=30, blank=True, null=True)
    session = models.CharField(max_length=30, blank=True, null=True)
    gzid = models.CharField(max_length=60, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'ub_updata'
