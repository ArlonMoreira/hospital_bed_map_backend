from rest_framework import serializers
from ..models import Hospital
from pycpfcnpj import cpfcnpj

class HospitalSerializer(serializers.ModelSerializer):

    is_active = serializers.BooleanField(
        required=False, #Não é obrigatório, por padrão será atribuído o valor True  
        error_messages={
            'invalid': 'Esse campo precisa ser do tipo boolean.'
        }
    )    

    class Meta:
        model = Hospital
        fields = ('id', 'cnes', 'cnpj', 'name', 'acronym', 'is_active')

    def validate_cnes(self, value):
        if not(value.isdigit()):
            raise serializers.ValidationError('Apenas valores numéricos são aceitos.')
        return value

    def validate_cnpj(self, value):
        if not(cpfcnpj.validate(value)):
            raise serializers.ValidationError('CNPJ inválido.')
        return value
    
    def save(self, **kwargs):
        hospital = self.instance

        if(hospital): #if the data is updated
            hospital.cnes = self.validated_data.get('cnes', hospital.cnes)
            hospital.cnpj = self.validated_data.get('cnpj', hospital.cnpj)
            hospital.name = self.validated_data.get('name', hospital.name)
            hospital.acronym = self.validated_data.get('acronym', hospital.acronym)
            hospital.is_active = self.validated_data.get('is_active', hospital.is_active)
            hospital.author = self.context['user']
            hospital.save()
        else:
            hospital = Hospital(
                cnes=self.validated_data.get('cnes'),
                cnpj=self.validated_data.get('cnpj'),
                name=self.validated_data.get('name'),
                acronym=self.validated_data.get('acronym'),
                is_active=self.validated_data.get('is_active', True),
                author=self.context['user']
            )
            hospital.save()

        return hospital
        