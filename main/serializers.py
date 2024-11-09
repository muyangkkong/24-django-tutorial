from rest_framework import serializers
from main.models import Student

class StudentSerializer(serializers.ModelSerializer):
    """
    학생 모델에 대한 Serializer
    """

    ### assignment2: 이곳에 과제를 작성해주세요
    class Meta:
        model=Student
        fields=["name","student_number","primary_major"]
    def save(self,**kwargs):
        validated_data={**self.validated_data,**kwargs}
        if (self.instance is not None):
            self.instance=self.update(self.instance,validated_data)
        else:
            self.instance=self.create(validated_data)
        return self.instance
    ### end assignment2
