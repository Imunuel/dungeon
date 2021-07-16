from django.utils.translation import gettext_lazy as _

EU_SERVER = "EU"
AS_SERVER = "AS"
AF_SERVER = "AF"
NA_SERVER = "NA"
SA_SERVER = "SA"
OC_SERVER = "OC"


SERVERS_DICT = {
    EU_SERVER: _("Europe"),
    AS_SERVER: _("Asia"),
    AF_SERVER: _("Africa"),
    NA_SERVER: _("North America"),
    SA_SERVER: _("South and Central America"),
    OC_SERVER: _("Oceania")
}


SERVER_TYPES = ((k, v) for k, v in SERVERS_DICT.items())

MAXIMUM_DAY = 7
