from rest_framework.decorators import api_view, permission_classes, renderer_classes, parser_classes
from django.shortcuts import render
from . import serializers as sz
from rest_framework import viewsets
from .models import Payment
from rest_framework_xml.renderers import XMLRenderer
from rest_framework_xml.parsers import XMLParser
from rest_framework.response import Response
from bs4 import BeautifulSoup
from django.db import IntegrityError
from django.http import HttpResponse

import json
from datetime import date, datetime
from rest_framework import status
from rest_framework import viewsets


def json_serial(obj):
    """JSON serializer for objects not serializable by default json code"""

    if isinstance(obj, (datetime, date)):
        return obj.isoformat()
    raise TypeError ("Type %s not serializable" % type(obj))

# from rest_framework.parsers import
class PaymentViewset(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = sz.PaymentSerializer
    # filter_backends =

responce_template ="""
<?xml version="1.0" encoding="UTF-8"?>
<S:Envelope xmlns:S="http://schemas.xmlsoap.org/soap/envelope/">
   <S:Body>
      <ns2:paymentconfirmationResponse xmlns:ns2="http://fortified.integration.mb.modefinserver.com/">
         <ns2:paymentConfirmation>
            <resultCode>{code}</resultCode>
            <transactionRefNo>{reff_no}</transactionRefNo>
         </ns2:paymentConfirmation>
      </ns2:paymentconfirmationResponse>
   </S:Body>
</S:Envelope>"""

@api_view(('POST',))
@parser_classes((XMLParser,))
@renderer_classes((XMLRenderer,))
def receive_paument(request):
    try:
        data = json.dumps(request.data, default=json_serial)
    except Exception:
        resp = responce_template.format(code='555', reff_no='error reading your data')
        return HttpResponse(resp, status=status.HTTP_400_BAD_REQUEST)
    try:
        payload = json.loads(data)
        payload = payload['{http://schemas.xmlsoap.org/soap/envelope/}Body']['{http://fortified.integration.mb.modefinserver.com/}paymentconfirmation']
    except Exception as e:
        resp = responce_template.format(code='555', reff_no='error reading your data')
        return HttpResponse(resp, status=status.HTTP_400_BAD_REQUEST)
    serializer = sz.PaymentXmlSerializer(data=payload)
    if not serializer.is_valid():
        resp = responce_template.format(code='555', reff_no='Invalid data provided')
        return HttpResponse(resp, status=status.HTTP_400_BAD_REQUEST)
        # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    valid_data=serializer.data
    try:
        payment = Payment.objects.create(
            amount= valid_data['amount'],
            timestamp= valid_data['timeStamp'],
            till_number = valid_data['tillNumber'],
            mobile_number = valid_data['mobileNumber'],
            transaction_ref_no = valid_data['transactionRefNo'],
            served_by=valid_data['servedBy'],
            additional_info=valid_data['additionalInfo']
        )
    except IntegrityError as e:
        resp = responce_template.format(code='555', reff_no='A similar transaction already exists')
        return HttpResponse(resp, status=status.HTTP_400_BAD_REQUEST)
    resp = responce_template.format(code='000', reff_no=payment.transaction_ref_no)
    return HttpResponse(resp)
