from django.contrib.auth.models import User, Group
from .models import Listings
from rest_framework import serializers

# TODO: Create your serializers here.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']

class ListingsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Listings
        fields = ['area_unit', 'bathrooms', 'bedrooms', 'home_size', 'home_type', 'last_sold_date', 'last_sold_price', 'link', 'price', 'property_size', 'rent_price', 'rentzestimate_amount', 'rentzestimate_last_updated', 'tax_value', 'tax_year', 'year_built', 'zestimate_amount', 'zestimate_last_updated', 'zillow_id', 'address', 'city', 'state', 'zipcode']