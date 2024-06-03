<template>
    <h1>Search Results for "{{ card_name }}"</h1>
    <table>
      <!-- <thead>
        <tr>
          <th></th>
        </tr>
      </thead> -->
      <tbody>
        <tr v-for="data in search_data">
          <td>{{ data['name'] }}</td>
        </tr>
      </tbody>
    </table>
</template>

<script>
export default {
  name: 'App',
  components: {},
  data: function () {
    return {
      search_data: ext_search_data,
      card_name: window.ext_card_name,
    }
  },
  methods: {
    
  },
  computed: {},
}
</script>
