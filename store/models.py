from django.db import models

# The requirements are a bit unclear and confusing
# Assuming second field is CIDR so it also includes net mask defining the net.
# 1.2.3.0/24 or 1.2.3.0/255.255.255.0 or 1.2.3.0/0.0.0.255
# Those are three equivalents.
# If network definition is already given then first field may be just canonical name.
# Then 'netmask' may also be duplicate of CIDR's definition.
# If so then there should be the validator netmask to check if it is equivalent of CIDR


class Network(models.Model):
    LOCATIONS = (
        (1, 'New York'),
        (2, 'Tampa'),
        (3, 'Portland')
    )
    ENVS = (
        (1, 'development'),
        (2, 'test'),
        (3, 'production')
    )
    network = models.CharField(max_length=255, null=False, unique=True)  # This field must be canonical name
    cidr = models.CharField(max_length=255, null=False)  # This field is already shows netmask: 1.2.3.0/24
    net_mask = models.CharField(max_length=255, null=True)  # This field may be another representation o
    # f '/24': 255.255.255.0 Thus it is not needed or requirements are misunderstood
    # Anyway, serializer has appropriate validator for this
    location = models.IntegerField(choices=LOCATIONS, null=False)
    environment = models.IntegerField(choices=ENVS, null=False)
