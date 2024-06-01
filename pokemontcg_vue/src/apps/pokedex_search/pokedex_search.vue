<template>
    <h1>This is a test (from Vue!!!)</h1>
    <li v-for="data in search_data"><h2>{{ data['name'] }} - {{ data['id'] }}</h2></li>
</template>

<script>
export default {
  name: 'App',
  components: {},
  data: function () {
    return {
      search_data: ext_search_data,
    }
  },
  methods: {
    
  },
  computed: {},
}
</script>
