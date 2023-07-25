from rest_framework import serializers
from hospital_bed_map_backend.beds.models import Beds, Sectors, TypeOccupation, Type

class BedsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Beds
        fields = ('sector',
                  'name',
                  'type_occupation',
                  'type',
                  'is_active',
                  'is_extra',
                  'author')
        
    def save(self):

        beds = Beds(
            sector=self.validated_data.get('sector'),
            name=self.validated_data.get('name'),
            type_occupation=self.validated_data.get('type_occupation'),
            type=self.validated_data.get('type'),
            is_active=self.validated_data.get('is_active', True),
            is_extra=self.validated_data.get('is_extra', False),
            author=self.context['user']
        )
        beds.save()
        
        return beds
        
    