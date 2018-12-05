import ipaddress
from rest_framework import serializers
from .models import Network


class NetmaskValidator(object):
    """
    Checks if CIDR netmask matches net_mask field.
    """
    def __call__(self, attrs):
        cidr = ipaddress.IPv4Network(attrs['cidr'])
        net_mask = attrs['net_mask']
        if str(cidr.netmask) != net_mask:
            raise serializers.ValidationError('Net mask does not fit CIDR mask')


class OverlapValidator(object):
    """
    Tests if new object's CIDR overlaps with existing networks
    """
    def __init__(self, queryset):
        self.queryset = queryset

    def __call__(self, value):
        for net_obj in self.queryset:
            net = ipaddress.IPv4Network(net_obj.cidr)
            self_net = ipaddress.IPv4Network(value)
            if net.overlaps(self_net):
                raise serializers.ValidationError('Overlaps with existing network ' + net_obj.network)


class NetworkSerializer(serializers.ModelSerializer):
    cidr = serializers.CharField(validators=[OverlapValidator(queryset=Network.objects.all())])

    class Meta:
        model = Network
        fields = '__all__'
        validators = [NetmaskValidator()]

    def validate_cidr(self, obj):
        """
        This is basic validation of appropriate CIDR format defined in 'ipaddress' module
        """
        try:
            ipaddress.IPv4Network(obj)
        except ValueError as e:
            raise serializers.ValidationError(e)
        return obj
