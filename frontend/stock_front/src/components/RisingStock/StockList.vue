<template>
  <div>
    <v-navigation-drawer app clipped permanent>
      <v-list>
        <v-list-item-group mandatory color="secondary">
          <v-list-item v-for="stock in stocks" :key="stock.code">
            <v-list-item-content @click="goToNews(stock)">
              <v-list-item-title>
                  {{ stock.name }}
              </v-list-item-title>
              <v-list-item-subtitle class="pt-1 black--text">
                {{ stock.curprice }}원 &nbsp;▴ {{ stock.diff }}원 &nbsp;▴ {{ stock.ratio }}%
              </v-list-item-subtitle>
            </v-list-item-content>
          </v-list-item>
        </v-list-item-group>
      </v-list>
    </v-navigation-drawer>

    <v-main>
      <router-view />
    </v-main>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  data: () => ({
    stocks: []
  }),

  created () {
    this.fetchStockList()
  },

  methods: {
    fetchStockList () {
      axios
        .get('/api/risingstock/')
        .then(res => {
          this.stocks = res.data
        })
        .catch(err => {
          console.log('fetchStockList GET Err', err.response)
          alert(err.response.status + ' ' + err.response.statusText)
        })
    },
    goToNews (stock) {
      this.$router.push({
        name: 'NewsList',
        params: {code: stock.code, stock: stock}
      })
    }
  }
}
</script>
