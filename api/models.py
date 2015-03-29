from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=50)


class Commodity(models.Model):
    category = models.ForeignKey(Category)
    name = models.CharField(max_length=50)
    average_price = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.name


class Economy(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Faction(models.Model):
    name = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.name


class Government(models.Model):
    name = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.name


class Allegiance(models.Model):
    name = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.name


class State(models.Model):
    name = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.name


class Security(models.Model):
    name = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.name


class System(models.Model):
    name = models.CharField(max_length=255)
    x = models.FloatField()
    y = models.FloatField()
    z = models.FloatField()
    faction = models.ForeignKey(Faction, null=True)
    population = models.CharField(max_length=255, null=True)
    government = models.ForeignKey(Government, null=True)
    allegiance = models.ForeignKey(Allegiance, null=True)
    state = models.ForeignKey(State, null=True)
    security = models.ForeignKey(Security, null=True)
    primary_economy = models.ForeignKey(Economy, null=True)
    needs_permit = models.BooleanField(default=False)
    updated_at = models.DateTimeField()

    def __str__(self):
        return self.name


class StationType(models.Model):
    name = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.name


class Station(models.Model):
    system = models.ForeignKey(System)
    name = models.CharField(max_length=50)
    max_landing_pad_size = models.CharField(max_length=1, null=True)
    distance_to_star = models.IntegerField(null=True)
    faction = models.ForeignKey(Faction, null=True)
    government = models.ForeignKey(Government, null=True)
    allegiance = models.ForeignKey(Allegiance, null=True)
    state = models.ForeignKey(State, null=True)
    type = models.ForeignKey(StationType, null=True)
    has_blackmarket = models.IntegerField()
    has_commodities = models.IntegerField()
    has_refuel = models.IntegerField()
    has_repair = models.IntegerField()
    has_rearm = models.IntegerField()
    has_outfitting = models.IntegerField()
    has_shipyard = models.IntegerField()
    economies = models.ManyToManyField(Economy)
    prohibited_commodities = models.ManyToManyField(Commodity)
    updated_at = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.name


class Listing(models.Model):
    station = models.ForeignKey(Station)
    commodity = models.ForeignKey(Commodity)
    supply = models.IntegerField()
    demand = models.IntegerField()
    buy_price = models.IntegerField()
    sell_price = models.IntegerField()
    collected_at = models.DateTimeField()
    update_count = models.IntegerField()


class AllegianceRank(models.Model):
    name = models.CharField(max_length=25)
    allegiance = models.ForeignKey(Allegiance)

    def __str__(self):
        return self.name


class ModuleType(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class ModuleParameterType(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class ModuleParameter(models.Model):
    type = models.ForeignKey(ModuleParameterType)
    value = models.CharField(max_length=75)

    def __str__(self):
        return self.value


class Module(models.Model):
    name = models.CharField(max_length=50)
    type = models.ForeignKey(ModuleType)
    parameters = models.ManyToManyField(ModuleParameter)

    def __str__(self):
        return self.name


class ShipSlot(models.Model):
    size = models.ForeignKey(ModuleParameter, null=True)
    module = models.ForeignKey(Module, null=True)
    type = models.ForeignKey(ModuleType)


class ShipParameterType(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class ShipParameter(models.Model):
    type = models.ForeignKey(ShipParameterType)
    value = models.CharField(max_length=75)

    def __str__(self):
        return self.value


class ShipType(models.Model):
    type = models.CharField(max_length=25)

    def __str__(self):
        return self.type


class Ship(models.Model):
    name = models.CharField(max_length=25)
    type = models.ForeignKey(ShipType)
    required_rank = models.ForeignKey(AllegianceRank, null=True)
    parameters = models.ManyToManyField(ShipParameter)
    slots = models.ManyToManyField(ShipSlot)

    def __str__(self):
        return self.name
