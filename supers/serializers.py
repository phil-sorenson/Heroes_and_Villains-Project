from uuid import _FieldsType
from rest_framework import serializers

import super_types
from super_types.models import SuperType
from .models import Super

class SuperSerializer(serializers.ModelSerializer):
    class Meta:
        model = Super
        fields = ['id', 'name', 'alter_ego', 'primary_ability', 'secondary_ability', 'catchphrase', 'super_type','super_type_id']
        depth=1
    super_type_id = serializers.IntegerField(SuperType.type)

    