from rest_framework import serializers
from .models import Employee


def multiple_of_1000(value):
    if value % 1000 != 0:
        raise serializers.ValidationError(
            "Emp sal should be multiples of 1000")


class EmployeeSerializers(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = "__all__"

    def validate_esal(self, value):
        if value < 5000:
            raise serializers.ValidationError(
                "Employee salary should be minimum 5000.")
        return value

    def validate(self, data):
        ename = data.get("ename")
        esal = data.get("esal")
        if ename.lower() == "sunny":
            if esal < 50000:
                raise serializers.ValidationError(
                    "Employee name with sunny should have salary upto 50000")

        return data
