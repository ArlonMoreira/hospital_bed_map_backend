from rest_framework import serializers
from hospital_bed_map_backend.beds.models import Beds, TypeOccupation, Type

class TypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Type
        fields = ('id', 'description')

class TypeOccupationSerializer(serializers.ModelSerializer):

    class Meta:
        model = TypeOccupation
        fields = ('id', 'status', 'description')

class BedsActiveUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Beds
        fields = ('id', 'is_active')

    def save(self):
        bed = self.instance.first()

        bed.is_active = self.validated_data.get('is_active', bed.is_active)
        bed.author = self.context['user']
        bed.save()

        return bed

class BedsStatusUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Beds
        fields = ('id', 'type_occupation')

    def save(self):
        bed = self.instance.first()

        bed.type_occupation = self.validated_data.get('type_occupation', bed.type_occupation)
        bed.author = self.context['user']
        bed.save()

        return bed
    
class BedsListPublicSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()
    sector = serializers.SerializerMethodField()
    type_occupation_id = serializers.IntegerField()
    type_occupation_status = serializers.CharField()
    type_occupation_description = serializers.CharField()
    type = serializers.CharField()
    is_extra = serializers.BooleanField()    

    class Meta:
        fields = ('id', 'name', 'sector', 'type_occupation_id', 'type_occupation_status', 'type_occupation_description', 'type', 'is_extra')

    def get_sector(self, obj):
        sector_data = {
            'id': obj['sector__id'],
            'name': obj['sector__name'],
            'tip_acc': obj['sector__tip_acc__description']
        }
        return sector_data      
        
class BedsListSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    hospital_id = serializers.IntegerField()
    sector_id = serializers.IntegerField()
    name = serializers.CharField()
    type_occupation_id = serializers.IntegerField()
    type_occupation_status = serializers.CharField()
    type_occupation_description = serializers.CharField()
    type = serializers.CharField()
    is_active = serializers.BooleanField()
    is_extra = serializers.BooleanField()

    class Meta:
        fields = ('id', 'hospital_id', 'sector_id', 'name', 'type_occupation_id',
                  'type_occupation_status', 'type_occupation_description', 'type',
                  'is_active', 'is_extra')
    
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

    def save(self, **kwargs):
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