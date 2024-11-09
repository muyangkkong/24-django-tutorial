from rest_framework import serializers


class StudentSerializer(serializers.ModelSerializer):
    """
    학생 모델에 대한 Serializer
    """

    ### assignment2: 이곳에 과제를 작성해주세요
    class Meta:
        model=Student
        fields=["name","student_number","primary_major"]
    ### end assignment2
