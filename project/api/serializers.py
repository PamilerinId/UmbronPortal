from rest_framework import serializers
from .models import *  # CustomUser, Class, School, Session, Subject, Principal, ClassTeacher, Teacher, Parent, Student


class CustomUserSerializer(serializers.HyperlinkedModelSerializer):
    """Not sure should be included since users are already categorized(profiled)
    Ps. If eventual removal, remove all 'user = CustomUserSerializer()' instances
     and use depth option in Meta class"""
    class Meta:
        model = CustomUser
        fields = ('url', 'first_name', 'last_name', 'username',
                  'email', 'type', 'sex', 'd_o_b', 'address',
                  'tel', 'nationality', 'lga', 'religion',
                  )


class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True)
    confirm_password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = CustomUser
        fields = ('url', 'first_name', 'last_name', 'username', 'password',
                  'confirm_password', 'email', 'type', 'sex', 'd_o_b',
                  'address', 'tel', 'nationality', 'lga', 'religion',
                  'school', 'class_room', 'subject'
                  )

    def create(self, validated_data):
        return CustomUser.objects.create_user(**validated_data)

    def update(self, instance, validated_data):
        instance.email = validated_data.get('email', instance.email)
        instance.username = validated_data.get('username',
                                               instance.username)
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)

        password = validated_data.get('password', None)
        confirm_password = validated_data.get('confirm_password', None)

        if password and password == confirm_password:
            instance.set_password(password)

        instance.save()
        return instance

    def validate(self, data):
        '''
        Ensure the passwords are the same
        '''
        if data['password']:
            print "Here"
            if data['password'] != data['confirm_password']:
                raise serializers.ValidationError(
                    "The passwords have to be the same"
                )
        return data


class SessionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Session
        fields = ('url', 'school_session')


class TermSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Term
        fields = ('url', 'term')


class SchoolSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = School
        fields = ('url', 'name')


class ClassSerializer(serializers.HyperlinkedModelSerializer):
    school = SchoolSerializer()

    class Meta:
        model = Class
        fields = ('url', 'name', 'school')


class SubjectSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Subject
        fields = ('url', 'name', 'ca_score', 'exam_score')
