<template>
    <div>
      <a :href="this.pokemon_list_url">Pokemon list</a><br /><br />
      <!-- <a :href="this.pokemon_update_url">Update Food</a><br />
      <a :href="this.pokemon_delete_url">Delete Food</a><br /> -->
      <h1>Name: {{this.pokemon.name}}</h1>
      <img :src="this.pokemon.image" width="50%">
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