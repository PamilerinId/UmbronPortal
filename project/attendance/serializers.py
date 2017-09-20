from rest_framework import serializers
from .models import Attendance



class AttendanceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Attendance
        fields = ('url', 'student', 'date_taken', 'is_present', 'class_teacher')