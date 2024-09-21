import os.path

from django.http import JsonResponse
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.utils import json
from scrapy.utils.project import get_project_settings
from scrapy.crawler import CrawlerProcess

from crawler.crawler.spiders.courses import YorkuCourseSpider
from uni_scrapper_api.permissions import IsStaffUser, IsAdmin

list_of_universities = {
    "Yorku": YorkuCourseSpider,
}


def read_file(path):
    with open(path, 'r') as json_file:
        data = json.load(json_file)
        return data


@api_view(['GET'])
@permission_classes([IsAdmin])
def run_course_spider(request, university_name):
    spider = list_of_universities.get(university_name.capitalize())

    if spider is None:
        return Response({'error ': 'The given university name is invalid'}, status=400)

    json_file_path = 'outputs/yorku_courses.json'
    if not os.path.exists(json_file_path):
        settings = get_project_settings()
        process = CrawlerProcess(settings)
        process.crawl(spider)
        process.start()
        # process.join()

    return JsonResponse(read_file(json_file_path), safe=False)


@api_view(['GET'])
@permission_classes([IsStaffUser])
def get_universities(request):
    return Response(list_of_universities.keys(), status=200)


@api_view(['GET'])
def hello(request):
    return Response('Hello', status=200)
