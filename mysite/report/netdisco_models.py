# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Admin(models.Model):
    job = models.AutoField(primary_key=True)
    entered = models.DateTimeField(blank=True, null=True)
    started = models.DateTimeField(blank=True, null=True)
    finished = models.DateTimeField(blank=True, null=True)
    device = models.GenericIPAddressField(blank=True, null=True)
    port = models.TextField(blank=True, null=True)
    action = models.TextField(blank=True, null=True)
    subaction = models.TextField(blank=True, null=True)
    status = models.TextField(blank=True, null=True)
    username = models.TextField(blank=True, null=True)
    userip = models.GenericIPAddressField(blank=True, null=True)
    log = models.TextField(blank=True, null=True)
    debug = models.NullBooleanField()
    device_key = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'admin'


class Community(models.Model):
    ip = models.GenericIPAddressField(primary_key=True)
    snmp_comm_rw = models.TextField(blank=True, null=True)
    snmp_auth_tag_read = models.TextField(blank=True, null=True)
    snmp_auth_tag_write = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'community'


class DbixClassSchemaVersions(models.Model):
    version = models.CharField(primary_key=True, max_length=10)
    installed = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'dbix_class_schema_versions'


class Device(models.Model):
    ip = models.GenericIPAddressField(primary_key=True)
    creation = models.DateTimeField(blank=True, null=True)
    dns = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    uptime = models.BigIntegerField(blank=True, null=True)
    contact = models.TextField(blank=True, null=True)
    name = models.TextField(blank=True, null=True)
    location = models.TextField(blank=True, null=True)
    layers = models.CharField(max_length=8, blank=True, null=True)
    ports = models.IntegerField(blank=True, null=True)
    mac = models.TextField(blank=True, null=True)  # This field type is a guess.
    serial = models.TextField(blank=True, null=True)
    model = models.TextField(blank=True, null=True)
    ps1_type = models.TextField(blank=True, null=True)
    ps2_type = models.TextField(blank=True, null=True)
    ps1_status = models.TextField(blank=True, null=True)
    ps2_status = models.TextField(blank=True, null=True)
    fan = models.TextField(blank=True, null=True)
    slots = models.IntegerField(blank=True, null=True)
    vendor = models.TextField(blank=True, null=True)
    os = models.TextField(blank=True, null=True)
    os_ver = models.TextField(blank=True, null=True)
    log = models.TextField(blank=True, null=True)
    snmp_ver = models.IntegerField(blank=True, null=True)
    snmp_comm = models.TextField(blank=True, null=True)
    snmp_class = models.TextField(blank=True, null=True)
    vtp_domain = models.TextField(blank=True, null=True)
    last_discover = models.DateTimeField(blank=True, null=True)
    last_macsuck = models.DateTimeField(blank=True, null=True)
    last_arpnip = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'device'


class DeviceIp(models.Model):
    ip = models.GenericIPAddressField(primary_key=True)
    alias = models.GenericIPAddressField()
    subnet = models.TextField(blank=True, null=True)  # This field type is a guess.
    port = models.TextField(blank=True, null=True)
    dns = models.TextField(blank=True, null=True)
    creation = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'device_ip'
        unique_together = (('ip', 'alias'),)


class DeviceModule(models.Model):
    ip = models.GenericIPAddressField(primary_key=True)
    index = models.IntegerField()
    description = models.TextField(blank=True, null=True)
    type = models.TextField(blank=True, null=True)
    parent = models.IntegerField(blank=True, null=True)
    name = models.TextField(blank=True, null=True)
    class_field = models.TextField(db_column='class', blank=True, null=True)  # Field renamed because it was a Python reserved word.
    pos = models.IntegerField(blank=True, null=True)
    hw_ver = models.TextField(blank=True, null=True)
    fw_ver = models.TextField(blank=True, null=True)
    sw_ver = models.TextField(blank=True, null=True)
    serial = models.TextField(blank=True, null=True)
    model = models.TextField(blank=True, null=True)
    fru = models.NullBooleanField()
    creation = models.DateTimeField(blank=True, null=True)
    last_discover = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'device_module'
        unique_together = (('ip', 'index'),)


class DevicePort(models.Model):
    ip = models.GenericIPAddressField()
    port = models.TextField(primary_key=True)
    creation = models.DateTimeField(blank=True, null=True)
    descr = models.TextField(blank=True, null=True)
    up = models.TextField(blank=True, null=True)
    up_admin = models.TextField(blank=True, null=True)
    type = models.TextField(blank=True, null=True)
    duplex = models.TextField(blank=True, null=True)
    duplex_admin = models.TextField(blank=True, null=True)
    speed = models.TextField(blank=True, null=True)
    name = models.TextField(blank=True, null=True)
    mac = models.TextField(blank=True, null=True)  # This field type is a guess.
    mtu = models.IntegerField(blank=True, null=True)
    stp = models.TextField(blank=True, null=True)
    remote_ip = models.GenericIPAddressField(blank=True, null=True)
    remote_port = models.TextField(blank=True, null=True)
    remote_type = models.TextField(blank=True, null=True)
    remote_id = models.TextField(blank=True, null=True)
    vlan = models.TextField(blank=True, null=True)
    pvid = models.IntegerField(blank=True, null=True)
    lastchange = models.BigIntegerField(blank=True, null=True)
    manual_topo = models.BooleanField()
    is_uplink = models.NullBooleanField()
    slave_of = models.TextField(blank=True, null=True)
    is_master = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'device_port'
        unique_together = (('port', 'ip'),)


class DevicePortLog(models.Model):
    id = models.AutoField()
    ip = models.GenericIPAddressField(blank=True, null=True)
    port = models.TextField(blank=True, null=True)
    reason = models.TextField(blank=True, null=True)
    log = models.TextField(blank=True, null=True)
    username = models.TextField(blank=True, null=True)
    userip = models.GenericIPAddressField(blank=True, null=True)
    action = models.TextField(blank=True, null=True)
    creation = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'device_port_log'


class DevicePortPower(models.Model):
    ip = models.GenericIPAddressField()
    port = models.TextField(primary_key=True)
    module = models.IntegerField(blank=True, null=True)
    admin = models.TextField(blank=True, null=True)
    status = models.TextField(blank=True, null=True)
    class_field = models.TextField(db_column='class', blank=True, null=True)  # Field renamed because it was a Python reserved word.
    power = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'device_port_power'
        unique_together = (('port', 'ip'),)


class DevicePortProperties(models.Model):
    ip = models.GenericIPAddressField()
    port = models.TextField(primary_key=True)
    error_disable_cause = models.TextField(blank=True, null=True)
    remote_is_wap = models.NullBooleanField()
    remote_is_phone = models.NullBooleanField()
    remote_vendor = models.TextField(blank=True, null=True)
    remote_model = models.TextField(blank=True, null=True)
    remote_os_ver = models.TextField(blank=True, null=True)
    remote_serial = models.TextField(blank=True, null=True)
    raw_speed = models.BigIntegerField(blank=True, null=True)
    faststart = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'device_port_properties'
        unique_together = (('port', 'ip'),)


class DevicePortSsid(models.Model):
    ip = models.GenericIPAddressField(blank=True, null=True)
    port = models.TextField(blank=True, null=True)
    ssid = models.TextField(blank=True, null=True)
    broadcast = models.NullBooleanField()
    bssid = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'device_port_ssid'


class DevicePortVlan(models.Model):
    ip = models.GenericIPAddressField(primary_key=True)
    port = models.TextField()
    vlan = models.IntegerField()
    native = models.BooleanField()
    creation = models.DateTimeField(blank=True, null=True)
    last_discover = models.DateTimeField(blank=True, null=True)
    vlantype = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'device_port_vlan'
        unique_together = (('ip', 'port', 'vlan', 'native'),)


class DevicePortWireless(models.Model):
    ip = models.GenericIPAddressField(blank=True, null=True)
    port = models.TextField(blank=True, null=True)
    channel = models.IntegerField(blank=True, null=True)
    power = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'device_port_wireless'


class DevicePower(models.Model):
    ip = models.GenericIPAddressField(primary_key=True)
    module = models.IntegerField()
    power = models.IntegerField(blank=True, null=True)
    status = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'device_power'
        unique_together = (('ip', 'module'),)


class DeviceSkip(models.Model):
    backend = models.TextField(primary_key=True)
    device = models.GenericIPAddressField()
    actionset = models.TextField(blank=True, null=True)  # This field type is a guess.
    deferrals = models.IntegerField(blank=True, null=True)
    last_defer = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'device_skip'
        unique_together = (('backend', 'device'),)


class DeviceVlan(models.Model):
    ip = models.GenericIPAddressField(primary_key=True)
    vlan = models.IntegerField()
    description = models.TextField(blank=True, null=True)
    creation = models.DateTimeField(blank=True, null=True)
    last_discover = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'device_vlan'
        unique_together = (('ip', 'vlan'),)


class Log(models.Model):
    id = models.AutoField()
    creation = models.DateTimeField(blank=True, null=True)
    class_field = models.TextField(db_column='class', blank=True, null=True)  # Field renamed because it was a Python reserved word.
    entry = models.TextField(blank=True, null=True)
    logfile = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'log'


class NetmapPositions(models.Model):
    host_groups = models.TextField()  # This field type is a guess.
    vlan = models.IntegerField()
    positions = models.TextField()
    device = models.GenericIPAddressField(blank=True, null=True)
    locations = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'netmap_positions'


class Node(models.Model):
    mac = models.TextField(primary_key=True)  # This field type is a guess.
    switch = models.GenericIPAddressField()
    port = models.TextField()
    vlan = models.TextField()
    active = models.NullBooleanField()
    oui = models.CharField(max_length=8, blank=True, null=True)
    time_first = models.DateTimeField(blank=True, null=True)
    time_recent = models.DateTimeField(blank=True, null=True)
    time_last = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'node'
        unique_together = (('mac', 'switch', 'port', 'vlan'),)


class NodeIp(models.Model):
    mac = models.TextField(primary_key=True)  # This field type is a guess.
    ip = models.GenericIPAddressField()
    active = models.NullBooleanField()
    time_first = models.DateTimeField(blank=True, null=True)
    time_last = models.DateTimeField(blank=True, null=True)
    dns = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'node_ip'
        unique_together = (('mac', 'ip'),)


class NodeMonitor(models.Model):
    mac = models.TextField(primary_key=True)  # This field type is a guess.
    active = models.NullBooleanField()
    why = models.TextField(blank=True, null=True)
    cc = models.TextField(blank=True, null=True)
    date = models.DateTimeField(blank=True, null=True)
    matchoui = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'node_monitor'


class NodeNbt(models.Model):
    mac = models.TextField(primary_key=True)  # This field type is a guess.
    ip = models.GenericIPAddressField(blank=True, null=True)
    nbname = models.TextField(blank=True, null=True)
    domain = models.TextField(blank=True, null=True)
    server = models.NullBooleanField()
    nbuser = models.TextField(blank=True, null=True)
    active = models.NullBooleanField()
    time_first = models.DateTimeField(blank=True, null=True)
    time_last = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'node_nbt'


class NodeWireless(models.Model):
    mac = models.TextField(primary_key=True)  # This field type is a guess.
    ssid = models.TextField()
    uptime = models.IntegerField(blank=True, null=True)
    maxrate = models.IntegerField(blank=True, null=True)
    txrate = models.IntegerField(blank=True, null=True)
    sigstrength = models.IntegerField(blank=True, null=True)
    sigqual = models.IntegerField(blank=True, null=True)
    rxpkt = models.BigIntegerField(blank=True, null=True)
    txpkt = models.BigIntegerField(blank=True, null=True)
    rxbyte = models.BigIntegerField(blank=True, null=True)
    txbyte = models.BigIntegerField(blank=True, null=True)
    time_last = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'node_wireless'
        unique_together = (('mac', 'ssid'),)


class Oui(models.Model):
    oui = models.CharField(primary_key=True, max_length=8)
    company = models.TextField(blank=True, null=True)
    abbrev = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'oui'


class Process(models.Model):
    controller = models.IntegerField()
    device = models.GenericIPAddressField()
    action = models.TextField()
    status = models.TextField(blank=True, null=True)
    count = models.IntegerField(blank=True, null=True)
    creation = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'process'


class Sessions(models.Model):
    id = models.CharField(primary_key=True, max_length=32)
    creation = models.DateTimeField(blank=True, null=True)
    a_session = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sessions'


class SnNode(models.Model):
    mac = models.TextField(primary_key=True)  # This field type is a guess.
    sys_id = models.TextField()
    time_last = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sn_node'


class SnVuln(models.Model):
    vuln_id = models.TextField(primary_key=True)
    vuln_name = models.TextField()
    internal_ip = models.GenericIPAddressField()
    time_last_scan = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sn_vuln'


class Statistics(models.Model):
    day = models.DateField(primary_key=True)
    device_count = models.IntegerField()
    device_ip_count = models.IntegerField()
    device_link_count = models.IntegerField()
    device_port_count = models.IntegerField()
    device_port_up_count = models.IntegerField()
    ip_table_count = models.IntegerField()
    ip_active_count = models.IntegerField()
    node_table_count = models.IntegerField()
    node_active_count = models.IntegerField()
    netdisco_ver = models.TextField(blank=True, null=True)
    snmpinfo_ver = models.TextField(blank=True, null=True)
    schema_ver = models.TextField(blank=True, null=True)
    perl_ver = models.TextField(blank=True, null=True)
    pg_ver = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'statistics'


class Subnets(models.Model):
    net = models.TextField(primary_key=True)  # This field type is a guess.
    creation = models.DateTimeField(blank=True, null=True)
    last_discover = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'subnets'


class Topology(models.Model):
    dev1 = models.GenericIPAddressField()
    port1 = models.TextField()
    dev2 = models.GenericIPAddressField()
    port2 = models.TextField()

    class Meta:
        managed = False
        db_table = 'topology'
        unique_together = (('dev1', 'port1'), ('dev2', 'port2'),)


class UserLog(models.Model):
    entry = models.AutoField()
    username = models.CharField(max_length=50, blank=True, null=True)
    userip = models.GenericIPAddressField(blank=True, null=True)
    event = models.TextField(blank=True, null=True)
    details = models.TextField(blank=True, null=True)
    creation = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_log'


class Users(models.Model):
    username = models.CharField(primary_key=True, max_length=50)
    password = models.TextField(blank=True, null=True)
    creation = models.DateTimeField(blank=True, null=True)
    last_on = models.DateTimeField(blank=True, null=True)
    port_control = models.NullBooleanField()
    ldap = models.NullBooleanField()
    admin = models.NullBooleanField()
    fullname = models.TextField(blank=True, null=True)
    note = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'users'
