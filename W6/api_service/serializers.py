from rest_framework import serializers


from cinema.models import Movie, Salon, Cinema


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'


class CinemaSerializer(serializers.ModelSerializer):
    salon = serializers.HyperlinkedRelatedField(view_name='salon-detail',
                                                many=True, queryset=Salon.objects.all())

    class Meta:
        model = Cinema
        fields = ['name', 'salon']


class SalonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Salon
        fields = '__all__'


class TempSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=200)
    age = serializers.IntegerField()
    address = serializers.CharField(max_length=255, required=False)

    def validate_name(self, value):
        if 'america' in value:
            raise serializers.ValidationError("Marg Bar Nang to!")
        return value

    def create(self, validated_data, address='tehran'):
        if 'address' not in validated_data.keys():
            return TempUser(**validated_data, address=address)
        return TempUser(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data['name']
        instance.age = validated_data['age']
        return instance


class TempSalonSerializer(serializers.ModelSerializer):
    # name = serializers.CharField(max_length=50)
    # capacity = serializers.IntegerField()
    # cinema = TempCinemaSerializer()

    class Meta:
        model = Salon
        fields = ['name', 'cinema']

    # def create(self, validated_data):
    #     return Cinema.objects.create(**validated_data)


class TempCinemaSerializer(serializers.ModelSerializer):
    # name = serializers.CharField(max_length=255)
    # salon_number = serializers.IntegerField()
    # address = serializers.CharField(max_length=255)
    salon = TempSalonSerializer(many=True)

    class Meta:
        model = Cinema
        fields = ['name', 'address', 'salon']
    # def create(self, validated_data):
    #     return Cinema.objects.create(**validated_data)

    # def update(self, instance, validated_data):
    #     instance.name = validated_data['name']
    #     instance.salon_number = validated_data['salon_number']
    #     instance.address = validated_data['address']
    #     instance.save()
    #     return instance


class TempUser:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address
