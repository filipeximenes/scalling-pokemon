from django.db import models


class PokemonKind(models.Model):
    name = models.TextField(blank=True, null=True)
    type1 = models.IntegerField(blank=True, null=True)
    type2 = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'PokemonKind'

    def __str__(self):
        return f'<PokemonKind {self.name}>'


class Trainer(models.Model):
    name = models.TextField(blank=True, null=True)
    pokedex = models.ManyToManyField(PokemonKind, through='Pokemon')

    favorite_pokemon = models.ForeignKey(
        PokemonKind, models.SET_NULL, null=True, related_name='+')

    class Meta:
        db_table = 'Trainer'

    def __str__(self):
        return f'<Trainer {self.name}>'


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

    def __str__(self):
        return f'<Pokemon {self.pokemon_kind.name} {self.trainer.name}>'
