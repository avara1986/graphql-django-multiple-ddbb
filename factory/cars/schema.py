from graphene_django import DjangoObjectType
import graphene
from cars.models import Car as CarModel, Model as ModelModel, Brand as BrandModel


class Car(DjangoObjectType):
    id = graphene.Int()
    color = graphene.String()

    class Meta:
        model = CarModel


class CreateCar(graphene.Mutation):

    class Arguments:
        color = graphene.String()
        model = graphene.Int()

    ok = graphene.Boolean()
    car = graphene.Field(lambda: Car)

    def mutate(self, info, color, model):
        car = CarModel.objects.create(color=color, model=ModelModel.objects.get(pk=model))
        ok = True
        return CreateCar(car=car, ok=ok)


class Model(DjangoObjectType):

    class Meta:
        model = ModelModel


class Brand(DjangoObjectType):

    class Meta:
        model = BrandModel


class MyMutations(graphene.ObjectType):
    create_car = CreateCar.Field()


class Query(graphene.ObjectType):
    cars = graphene.List(Car)
    models = graphene.List(Model)

    def resolve_cars(self, info, **kwargs):
        return CarModel.objects.all().prefetch_related('model', 'model__brand')

    car = graphene.Field(Car,
                         id=graphene.Int(),
                         color=graphene.String())

    def resolve_models(self, info, **kwargs):
        # We can easily optimize query count in the resolve method
        return ModelModel.objects.all()

    def resolve_car(self, info, **kwargs):
        id = kwargs.get('id')
        color = kwargs.get('color')
        if id is not None:
            return CarModel.objects.get(pk=id)

        if color is not None:
            return CarModel.objects.get(color=color)

        return None

schema = graphene.Schema(query=Query, mutation=MyMutations)
