from rest_framework.response import Response
from .models import Ads
from rest_framework.views import APIView
from datetime import datetime
from django.db.models import Sum
from django.db.models.functions import Coalesce
from advertisers.models import Client


class AdsAPIView(APIView):
    # media 기준 합계 도출
    def get(self, request):
        """
        Assignee : 홍은비
        Reviewer : 장우경, 진병수
        """
        client_number = request.GET.get('advertiser', None)

        try:
            start_date = datetime.strptime(request.GET.get('start_date', None), '%Y.%m.%d').date()
            end_date = datetime.strptime(request.GET.get('end_date', None), '%Y.%m.%d').date()
        except ValueError:
            return Response('[날짜 형식 오류] 날짜를 yyyy.mm.dd 형식으로 요청해주십시오.', status=404)


        advertiser = Client.objects.filter(client_number=client_number)

        if not advertiser:
            return Response('해당 광고주 uid는 존재하지 않습니다.', status=404)


        objects = Ads.objects.filter(client__client_number=client_number, date__gte=start_date, date__lte=end_date).values(\
            'platform'
            ).annotate(
                sum_cost=Coalesce(Sum('cost'), 0),
                sum_impression=Coalesce(Sum('impression'), 0),
                sum_click=Coalesce(Sum('click'), 0),
                sum_conversion=Coalesce(Sum('conversion'), 0),
                sum_cv=Coalesce(Sum('cv'), 0)
            )

        final_report = {}

        for obj in objects:
            final_report[obj['platform']] = {
                'CTR': round((obj['sum_click'] * 100) / obj['sum_impression'], 2),
                'ROAS': round((obj['sum_cv'] * 100) / obj['sum_cost'], 2),
                'CPC': round(obj['sum_cost'] / obj['sum_click'], 2),
                'CVR': round((obj['sum_conversion'] * 100) / obj['sum_click'], 2),
                'CPA': round(obj['sum_cost']  / obj['sum_conversion'], 2),
            }


        return Response(final_report, status=200)





