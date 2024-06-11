<template>
    <div>
      <!-- <a :href="this.pokemon_update_url">Update Food</a><br />
      <a :href="this.pokemon_delete_url">Delete Food</a><br /> -->
      <!-- card_id = models.CharField()
          name = models.CharField()
          types = models.ManyToManyField(Type)
          rarity = models.CharField()
          image = models.CharField()
          prices = models.JSONField(default=list)
          highest_market_price = models.FloatField() -->
      <h1>Name: {{this.pokemon.name}}</h1>
      <table class="table table-condensed">
        <tr>
        <td><img :src="this.pokemon.image" width="80%"></td>
        <td>
          <h1>Types:</h1>
          <ul v-for="t in types" v-bind:key="t" class="list-group"><li><h3>{{ t.name }}</h3></li></ul>
          <h1>Rarity: {{ this.pokemon.rarity }}</h1>
          <h1>Prices:</h1>
          <ul v-for="foil, key in prices.prices" v-bind:key="foil" class="list-group">
            <li class="list-group-item">
            <h2>{{ key }}</h2>
            <ul v-for="price, key in foil" v-bind:key="price"><li v-if="price != null">{{ key }}: {{ price }}</li><li v-if="price == null">{{ key }}: N/A</li></ul>
            </li>
          </ul>
          <h1>Highest Market Price: {{ this.pokemon.highest_market_price }}</h1>
        </td>
        </tr>
      </table>
    </div>
  </template>
  <script>
  export default {
    name: 'App',
    components: {},
    data: function () {
      return {
        pokemon: ext_pokemon_dico,
        types: ext_pokemon_dico.types,
        prices: ext_pokemon_dico.prices,
        id: ext_id,
        pokemon_list_url: ext_pokemon_list_url,
      }
    },
    methods: {
      get_pokemon_info() {
        fetch(this.pokemon_detail_js_url, {
          method: 'get',
          credentials: 'same-origin'
        })
          .then(function (response) {
            console.log('response', response)
            return response.json()
          })
          .then(this.assign_pokemon)
          .catch((error) => {
            console.log('error', error)
            this.pokemon_error = ['error when loading pokemon information']
          })
      },
      assign_pokemon(pokemon_json) {
        console.log('json', pokemon_json)
        this.pokemon = pokemon_json['pokemon']
      }
    },
    computed: {},
    beforeMount() {
      this.get_pokemon_info()
    }
  }
  </script>