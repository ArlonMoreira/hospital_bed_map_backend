from rest_framework import serializers
from ..models import Sectors, Hospital, TypeAccommodation
from datetime import datetime

class TypeAccommodationSerializer(serializers.ModelSerializer):
    class Meta:
        model = TypeAccommodation
        fields = ('id', 'description')

class SectorSerializerUpdate(serializers.ModelSerializer):
    is_active = serializers.BooleanField(
        required=False,
        error_messages={
            'invalid': 'Esse campo precisa ser do tipo boolean.'
        }
    )
    tip_acc = serializers.CharField(required=False)
    name = serializers.CharField(required=False)
    description = serializers.CharField(required=False)

    class Meta:
        model = Sectors
        fields = ('id', 'name', 'description', 'tip_acc', 'activation_date', 'deactivation_date', 'is_active')

    def save(self):
        sector = self.instance.first()

        if(sector):
            sector.name = self.validated_data.get('name', sector.name)
            sector.description = self.validated_data.get('description', sector.description)
            sector.tip_acc = TypeAccommodation.objects.filter(description=self.validated_data.get('tip_acc', sector.tip_acc)).first()
            sector.is_active = self.validated_data.get('is_active', sector.is_active)
            sector.author = self.context['user']

            if not self.validated_data.get('is_active'):
                sector.deactivation_date = datetime.today()
            else:
                sector.activation_date = datetime.today()

            sector.save()

        return sector

class SectorsSerializer(serializers.ModelSerializer):

    is_active = serializers.BooleanField(
        required=True,
        error_messages={
            'invalid': 'Esse campo precisa ser do tipo boolean.'
        }
    )
    tip_acc = serializers.CharField(
        required=True,
        allow_null=False,
        allow_blank=False
    )

    class Meta:
        model = Sectors
        fields = ('id', 'name', 'description', 'tip_acc', 'activation_date', 'deactivation_date', 'is_active')

    def validate_name(self, value):
        hospital = Hospital.objects.filter(id=self.context['hospital']).first()
        if Sectors.objects.filter(name=value, hospital=hospital).exists():
            raise serializers.ValidationError('Setor com este Nome já existe.')
        return value
        
    def validate_description(self, value):
        hospital = Hospital.objects.filter(id=self.context['hospital']).first()
        if Sectors.objects.filter(description=value, hospital=hospital).exists():
            raise serializers.ValidationError('Setor com esta Descrição já existe.')
        return value

    def validate_tip_acc(self, value):
        if not(TypeAccommodation.objects.filter(description=value).exists()):
            raise serializers.ValidationError('Tipo de acomodação inválido.')
        return value

    def save(self):
        sector = Sectors(
            hospital=Hospital.objects.filter(id=self.context['hospital']).first(),
            name=self.validated_data.get('name'),
            description=self.validated_data.get('description'),
            tip_acc=TypeAccommodation.objects.filter(description=self.validated_data.get('tip_acc')).first(),
            is_active=self.validated_data.get('is_active'),
            author=self.validated_data.get('user')
        )

        if not self.validated_data.get('is_active'):
            sector.deactivation_date = datetime.today()
        else:
            sector.activation_date = datetime.today()

        sector.save()

        return sector