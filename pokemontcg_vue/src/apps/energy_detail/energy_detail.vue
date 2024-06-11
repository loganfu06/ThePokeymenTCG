<template>
  <div>
    <h1>Name: {{ this.energy.name }}</h1>
    <img :src="this.energy.image" width="50%" />
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
      id: ext_id,
      energy_list_url: ext_energy_list_url
    }
  },
  methods: {
    get_energy_info() {
      fetch(this.energy_detail_js_url, {
        method: 'get',
        credentials: 'same-origin'
      })
        .then(function (response) {
          // console.log('response', response)
          return response.json()
        })
        .then(this.assign_energy)
        .catch((error) => {
          // console.log('error', error)
          this.energy_error = ['error when loading energy information']
        })
    },
    assign_energy(energy_json) {
      // console.log('json', energy_json)
      this.energy = energy_json['energy']
    }
  }
}
</script>
