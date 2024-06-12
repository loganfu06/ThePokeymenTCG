<template>
    <div>
      <h1>{{this.trainer.name}}</h1>
      <table class="table table-condensed">
        <tr>
        <td><img :src="this.trainer.image" width="80%"></td>
        <td>
          <h1>Rarity: {{ this.trainer.rarity }}</h1>
          <h1>Prices:</h1>
          <ul v-for="foil, key in prices.prices" v-bind:key="foil">
            <li>
            <h2>{{ key }}</h2>
            <ul v-for="price, key in foil" v-bind:key="price"><li v-if="price != null">{{ key }}: ${{ price }}</li><li v-if="price == null">{{ key }}: N/A</li></ul>
            </li>
          </ul>
          <h1>Highest Market Price: ${{ this.trainer.highest_market_price }}</h1>
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
        trainer: ext_trainer_dico,
        types: ext_trainer_dico.types,
        prices: ext_trainer_dico.prices,
        id: ext_id,
        trainer_list_url: ext_trainer_list_url,
        // trainer_delete_url: ext_trainer_delete_url,
      }
    },
    methods: {
      get_trainer_info() {
        fetch(this.trainer_detail_js_url, {
          method: 'get',
          credentials: 'same-origin'
        })
          .then(function (response) {
            console.log('response', response)
            return response.json()
          })
          .then(this.assign_trainer)
          .catch((error) => {
            console.log('error', error)
            this.trainer_error = ['error when loading trainer information']
          })
      },
      assign_trainer(trainer_json) {
        console.log('json', trainer_json)
        this.trainer = trainer_json['trainer']
      }
    },
    computed: {},
    beforeMount() {
      this.get_trainer_info()
    }
  }
  </script>