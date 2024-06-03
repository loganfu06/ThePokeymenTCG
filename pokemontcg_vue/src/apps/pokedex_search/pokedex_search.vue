<template>
  <h1>{{ search_data.length }} search results for "{{ card_name }}".</h1>
  Sort by rarity:
  <select v-model="current_rarity">
    <option>None</option>
    <option v-for="rarity in rarities">{{ rarity }}</option>
  </select>


  <table border="1px solid black">
    <div style="width: 1000px; display: block;">
      <thead>
        <tr>
          <th>Card name</th>
          <th>Image</th>
          <th>Rarity</th>
          <th>Add to Database</th>
        </tr>
      </thead>
    </div>
    <div style="height:700px; overflow-y: scroll; display: block; width: 1000px;">
      <tbody>
        <tr v-for="data in search_data" v-show="filterData(data)">
          <td>{{ data['name'] }}</td>
          <td><img :src="getImgUrl(data)"></td>
          <td>{{ data['rarity'] }}</td>
          <td><button v-on:click="createRedirect(data)">Add card</button></td>
        </tr>
      </tbody>
    </div>
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
      rarities: ext_rarities,
      current_rarity: "None",
      createUrlBase: ext_create_url.slice(0,-1),
    }
  },
  methods: {
    getImgUrl(data) {
      var stringUrl = data['images']['small']
      return new URL(stringUrl)
    },
    filterData(data) {
      if (this.current_rarity == 'None') {
        return true
      }
      else {
        return this.current_rarity == data['rarity']
      }
    },
    createRedirect(data) {
      var createUrl = this.createUrlBase + data['id']
      window.location.href = createUrl
    },
    computed: {},
  }
}
</script>
