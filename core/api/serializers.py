from rest_framework.serializers import ModelSerializer
from core.models import Documents, AppliedCompanies, Processes, Interviews
from core.models import User


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'password')
        read_only_fields = ('full_name',)
        extra_kwargs = {'password': {'write_only': True}, 
                        'first_name': {'write_only': True},
                        'last_name': {'write_only': True}}


    def create(self, validated_data):
        user = User.objects.create(
            username = validated_data['username'],
            email = validated_data['email'],
            first_name = validated_data['first_name'],
            last_name = validated_data['last_name']
            )

        if 'profile_pic' in validated_data:
            user.profile_pic = validated_data['profile_pic']

        user.set_password(validated_data['password'])
        user.save()

        return user


class DocumentSerializer(ModelSerializer):
    user = UserSerializer(read_only=True)
    class Meta:
        model = Documents
        fields = '__all__'


class AppliedCompanieSerializer(ModelSerializer):
    user = UserSerializer(read_only=True)
    class Meta:
        model = AppliedCompanies
        fields = '__all__'


class ProcessesCompanieSerializer(ModelSerializer):
    class Meta:
        model = Processes
        fields = '__all__'


class InterviewsCompanieSerializer(ModelSerializer):
    class Meta:
        model = Interviews
        fields = '__all__'