import io

from rest_framework import serializers
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer

from .models import Women, Category


# class WomenModel:
#
#     def __init__(self, title, content):
#         self.title = title
#         self.content = content

# ModelSerializer класс сериализации для работы с моделями
class WomenSerializer(serializers.ModelSerializer):
    # Делаем поле user скрытым и по умолчанию принимающее актитвного пользователя.
    user = serializers.HiddenField(default=serializers.CurrentUserDefault)

    # B Meta  определяем модель и какие поля будем использовать.
    class Meta:
        model = Women
        fields = '__all__'

# # Serializer базовыый класс сериализации
# class WomenSerializer(serializers.Serializer):
#     # Атрибуты сериализатора должны быть такие же, как и у модели.
#     title = serializers.CharField(max_length=250)
#     content = serializers.CharField()
#     # read_only=True  для того чтобы не выходило исключение.
#     time_create = serializers.DateTimeField(read_only=True)
#     time_update = serializers.DateTimeField(read_only=True)
#     is_published = serializers.BooleanField(default=True)
#     cat_id = serializers.IntegerField()
#
#     # Создание объекта модели, делается внутри сериализатора, а не в представлении.
#     # Коллекцию validated_data берем после вызова метода is_valid()
#     def create(self, validated_data):
#         # Распаковываем коллекцию validated_data
#         return Women.objects.create(**validated_data)
#
#     # метод срабатывает когда при создании объекта сериализатора передается 2 параметра: request.data, instance.
#     def update(self, instance, validated_data):
#         instance.title = validated_data.get('title', instance.title)
#         instance.content = validated_data.get('content', instance.content)
#         instance.time_create = validated_data.get('time_create', instance.time_create)
#         instance.time_update = validated_data.get('time_update', instance.time_update)
#         instance.is_published = validated_data.get('is_published', instance.is_published)
#         instance.cat_id = validated_data.get('cat_id', instance.cat_id)
#         instance.save()
#         return instance





# функция кодирования
# def encode():
#     # Создаем экземпляр класса WomenModel
#     model = WomenModel('Анджелина Джоли', 'Content: Биография Анджелины Джоли')
#     # Пропускаем через сериализатор
#     model_sr = WomenSerializer(model)
#     # У сериализатора есть коллекция data, это словарь.
#     print(model_sr.data, type(model_sr.data), sep='\n')
#     # Переводим словарь в JSON
#     json = JSONRenderer().render(model_sr.data)
#     print(json)
#
#
# def decode():
#     # Имитируем json-строку
#     # ОЧЕНЬ ВАЖНО! Если используем кириллицу(русский язык), то надо добавлять encode  или использовать bytes.
#     # stream = io.BytesIO('{"title":"Анджелина Джоли","content":"Биография Анджелины Джоли"}'.encode('utf-8'))
#     string = bytes('{"title":"Анджелина Джоли","content":"Биография Анджелины Джоли"}', "utf-8")
#     stream = io.BytesIO(string)
#
#     # Парсим данные
#     data = JSONParser().parse(stream)
#     # Пропускаем через сериализатор, используем параметр data
#     serializer = WomenSerializer(data=data)
#     # Валидируем даныые
#     serializer.is_valid()
#     # Данные храняться в коллекции validated_data
#     print(serializer.validated_data)
