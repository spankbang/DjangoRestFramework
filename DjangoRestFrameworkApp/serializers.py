from rest_framework import serializers
from .models import Employee


def multiple_of_1000(value):
    if value % 1000 != 0:
        raise serializers.ValidationError("Emp sal should be multiples of 1000")

class EmployeeSerializers(serializers.Serializer):
    eno = serializers.IntegerField()
    ename = serializers.CharField(max_length=4)
    esal = serializers.FloatField(validators =[multiple_of_1000])
    eaddr = serializers.CharField(max_length=120)

    def create(self, validated_data):
        return Employee.objects.create(**validated_data)


    def update(self, instance, validated_data):
        instance.eno = validated_data.get("eno", instance.eno)
        instance.ename = validated_data.get("ename",instance.ename)
        instance.esal = validated_data.get("esal",instance.esal)
        instance.eaddr = validated_data.get("eaddr", instance.eaddr)
        instance.save()
        return instance

    def validate_esal(self, value):
        if value < 5000:
            raise serializers.ValidationError("Employee salary should be minimum 5000.")
        return value


    def validate(self, data):
        ename = data.get("ename")
        esal = data.get("esal")
        if ename.lower() == "sunny":
            if esal < 50000:
                raise serializers.ValidationError("Employee name with sunny should have salary upto 50000")

        return data