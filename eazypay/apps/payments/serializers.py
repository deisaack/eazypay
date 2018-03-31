from rest_framework import serializers
from .models import Payment

class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = '__all__'


"""
{
    "tillNumber": 254766999904,
    "mobileNumber": 254765555012,
    "amount": 100,
    "timeStamp": "2016-11-28T11:42:30",
    "transactionRefNo": 123456,
    "servedBy": 1234,
    "additionalInfo": "test trxn"
}
"""
class PaymentXmlSerializer(serializers.Serializer):
    tillNumber = serializers.IntegerField()
    mobileNumber = serializers.CharField(max_length=50)
    transactionRefNo = serializers.CharField(max_length=50)
    servedBy = serializers.CharField(max_length=50)
    additionalInfo = serializers.CharField(max_length=50)
    amount = serializers.DecimalField(decimal_places=4, max_digits=20)
    timeStamp = serializers.DateTimeField()

