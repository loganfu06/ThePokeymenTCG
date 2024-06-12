<template>
  <div>
    <h2><a :href="this.trainer_delete_url">Delete this card</a></h2>
    <h1>Name: {{ this.trainer.name }}</h1>
    <img :src="this.trainer.image" width="50%" />
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
      id: ext_id,
      trainer_list_url: ext_trainer_list_url,
      trainer_delete_url: ext_trainer_delete_url,
    }
  },
  methods: {
    get_trainer_info() {
      fetch(this.trainer_detail_js_url, {
        method: 'get',
        credentials: 'same-origin'
      })
        .then(function (response) {
          // console.log('response', response)
          return response.json()
        })
        .then(this.assign_trainer)
        .catch((error) => {
          // console.log('error', error)
          this.trainer_error = ['error when loading trainer information']
        })
    },
    assign_trainer(trainer_json) {
      // console.log('json', trainer_json)
      this.trainer = trainer_json['trainer']
    }
  }
}
</script>
