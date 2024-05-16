from django.forms import model_to_dict
from django.shortcuts import render
from rest_framework import generics, viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import action
from rest_framework import generics
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Women, Category
from .serializers import WomenSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser, IsAuthenticated
from .permissions import IsAdminOrReadOnly, IsOwnerOrReadOnly


# Определяем класс пагинации
class WomenAPIListPagination(PageNumberPagination):
    # кол-во записей на странице
    page_size = 2
    # параметр который позволяет вручную регулировать кол-во записей на странице, но не больше max_page_size
    page_size_query_param = 'page_size'
    # максимальное кол-во записей на странице
    max_page_size = 10000


class WomenAPIList(generics.ListCreateAPIView):
    queryset = Women.objects.all()
    serializer_class = WomenSerializer
    # permission_classes  ограничитель доступа
    # IsAuthenticatedOrReadOnly только для авторизованных или всем, но для чтения.
    permission_classes = (IsAuthenticatedOrReadOnly,)
    # Определяем класс котоырй будет использоваться для пагинации.
    pagination_class = WomenAPIListPagination


class WomenAPIUpdate(generics.RetrieveUpdateAPIView):
    queryset = Women.objects.all()
    serializer_class = WomenSerializer
    permission_classes = (IsAuthenticated,)
    # authentication_classes = (TokenAuthentication, )


class WomenAPIDestroy(generics.RetrieveDestroyAPIView):
    queryset = Women.objects.all()
    serializer_class = WomenSerializer
    # IsAdminUser  удалять посты может только администратор.
    permission_classes = (IsAdminOrReadOnly,)

# ModelViewSet для GET, POST, PUT, DELETE запросов.
# class WomenViewSet(viewsets.ModelViewSet):
#     # queryset = Women.objects.all()
#     serializer_class = WomenSerializer
#
#     # Переопределяем метод queryset
#     # Если переопределяем queyset, т ов  routers надо добавить параметр basename
#     def get_queryset(self):
#         pk = self.kwargs.get('pk')
#         if not pk:
#             return Women.objects.all()[:3]
#         return Women.objects.filter(pk=pk)
#
#     # cation декоратор для новых маршрутов.
#     # В methods прописываем какие методы будут для маршрута, detail если False то возвращаем нескольк озаписей, и наоборот если True.
#     @action(methods=['get'], detail=True)
#     def category(self, request, pk=None):
#         cats = Category.objects.get(pk=pk)
#         return Response({'cats': cats.name})

# class WomenAPIView(generics.ListAPIView):
#     queryset = Women.objects.all()
#     serializer_class = WomenSerializer


# ListCreateAPIView для GET и POST-запросов.
# class WomenAPIList(generics.ListCreateAPIView):
#     queryset = Women.objects.all()
#     serializer_class = WomenSerializer
#
#
# # UpdateAPIView для  PUT и PATCH запросы.
# class WomenAPIUpdate(generics.UpdateAPIView):
#     queryset = Women.objects.all()
#     serializer_class = WomenSerializer
#
#
# # RetrieveUpdateDestroyAPIView позволяет работать с одной записью. GET, PUT, PATCH< DELETE запросы.
# class WomenAPIDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Women.objects.all()
#     serializer_class = WomenSerializer

# # Класс ApiView является базовым класом представлений в DjangoRestFramework.
# # Он проводит проверку методов.
# # Если метод не разрешен возвращает JSON-сообщение.
# class WomenAPIView(APIView):
#
#     # Определяем метод GET
#     def get(self, request):
#         w = Women.objects.all()
#         # Класс Response переводит данные в JSON-строку
#         # many=True так как передаем несколько объектов, обращаемся к коллекции data
#         return Response({'posts': WomenSerializer(w, many=True).data})
#
#     # Определяем метод POST
#     def post(self, request):
#         # Проводим валидацию данных. если вдруг поля отсутствуют или некорректны.
#         # Берем данные и коллекции request.data
#         serializer = WomenSerializer(data=request.data)
#         # raise_exception=True, для того чтобы вызывать исключение, а не ошибку.
#         serializer.is_valid(raise_exception=True)
#         # При вызове метода save()  при POST-запросе срабатывает метод create сериализатора.
#         serializer.save()
#         return Response({'new_post': serializer.data})
#
#         # new_post = Women.objects.create(
#         #     # Берем данные из коллекции request.data
#         #     title=request.data['title'],
#         #     content=request.data['content'],
#         #     cat_id=request.data['cat_id']
#         # )
#         # model_to_dict преобразовывает объект в словарь.
#         # return Response({'new_post': WomenSerializer(new_post).data})
#
#
#     def put(self, request, *args, **kwargs):
#         # Берем ключ.
#         pk = kwargs.get('pk', None)
#         # Если ключа нет, то возвращаем ответ с ошибкой
#         if not pk:
#             return Response({'error': 'Method not allowed.'})
#
#         # Пытаемся извлечь запись по ключу.
#         try:
#             instance = Women.objects.get(pk=pk)
#         except:
#             return Response({'error': 'Object not found.'})
#
#         #Создаем объект сериализатора c двумя параметрами, чтобы сработал метод update()
#         serializer = WomenSerializer(data=request.data, instance=instance)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#
#         return Response({'post': serializer.data})
#
#     def delete(self, request, *args, **kwargs):
#         # Берем ключ.
#         pk = kwargs.get('pk', None)
#         # Если ключа нет, то возвращаем ответ с ошибкой
#         if not pk:
#             return Response({'error': 'Method not allowed.'})
#
#         # Пытаемся извлечь запись по ключу.
#         try:
#             instance = Women.objects.get(pk=pk)
#         except:
#             return Response({'error': 'Object not found.'})
#
#         instance.delete()
#
#         return Response({'post': 'post delete' + str(pk)})
