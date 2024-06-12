<template>
    <div>
      <h1>{{this.energy.name}}</h1>
      <table class="table table-condensed">
        <tr>
        <td><img :src="this.energy.image" width="80%"></td>
        <td>
          <h1>Prices:</h1>
          <ul v-for="foil, key in prices.prices" v-bind:key="foil">
            <li>
            <h2>{{ key }}</h2>
            <ul v-for="price, key in foil" v-bind:key="price"><li v-if="price != null">{{ key }}: ${{ price }}</li><li v-if="price == null">{{ key }}: N/A</li></ul>
            </li>
          </ul>
          <h1>Highest Market Price: ${{ this.energy.highest_market_price }}</h1>
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
        energy: ext_energy_dico,
        types: ext_energy_dico.types,
        prices: ext_energy_dico.prices,
        id: ext_id,
        energy_list_url: ext_energy_list_url,
        // energy_delete_url: ext_energy_delete_url,
      }
    },
    methods: {
      get_energy_info() {
        fetch(this.energy_detail_js_url, {
          method: 'get',
          credentials: 'same-origin'
        })
          .then(function (response) {
            console.log('response', response)
            return response.json()
          })
          .then(this.assign_energy)
          .catch((error) => {
            console.log('error', error)
            this.energy_error = ['error when loading energy information']
          })
      },
      assign_energy(energy_json) {
        console.log('json', energy_json)
        this.energy = energy_json['energy']
      }
    },
    computed: {},
    beforeMount() {
      this.get_energy_info()
    }
  }
  </script>