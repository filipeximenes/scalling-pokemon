from django.db import models


class PokemonKind(models.Model):
    name = models.TextField(blank=True, null=True)
    type1 = models.IntegerField(blank=True, null=True)
    type2 = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'PokemonKind'


class Trainer(models.Model):
    name = models.TextField(blank=True, null=True)
    pokedex = models.ManyToManyField(PokemonKind, through='Pokemon')

    class Meta:
        db_table = 'Trainer'


class Pokemon(models.Model):
    trainer = models.ForeignKey(
        Trainer, models.CASCADE, related_name='pokemons')
    pokemon_kind = models.ForeignKey(PokemonKind, models.CASCADE)

    place = models.IntegerField(blank=True, null=True)
    pokelevel = models.IntegerField(blank=True, null=True)
    hp = models.IntegerField(blank=True, null=True)
    maxhp = models.IntegerField(blank=True, null=True)
    attack = models.IntegerField(blank=True, null=True)
    defense = models.IntegerField(blank=True, null=True)
    spatk = models.IntegerField(blank=True, null=True)
    spdef = models.IntegerField(blank=True, null=True)
    speed = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'Pokemon'
