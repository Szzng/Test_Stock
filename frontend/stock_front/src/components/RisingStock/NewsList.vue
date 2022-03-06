<template>
  <div class="mx-4 my-6">
    <v-row
      justify="center"
      align="center"
      class="py-4"
      style="font-size: 25px; font-weight: bold"
    >
     <a :href="`https://finance.naver.com/item/main.nhn?code=${stock.code}`" target="_blank">
      {{ stock.name }}
     </a>
    </v-row>
    <v-row justify="center" align="center" class="mb-2 font-weight-bold">
      <v-col cols="9" class="text-center">
        <v-chip outlined label color="black">
          <v-icon left> mdi-cash </v-icon>
          {{ stock.curprice }}원
        </v-chip>
        <v-chip outlined label color="pink" class="ml-2">
          <v-icon left> mdi-trending-up</v-icon>
          {{ stock.diff }}원
        </v-chip>
        <v-chip outlined label color="red" class="ml-2">
          <v-icon left> mdi-trending-up</v-icon>
          {{ stock.ratio }}%
        </v-chip>
        <v-chip outlined label color="green darken-3" class="ml-5">
          <v-icon left> mdi-account-group-outline </v-icon>
          거래량 {{ stock.volume }}
        </v-chip>
        <v-chip outlined label color="indigo darken-4" class="ml-5">
          PER {{ stock.per }}
        </v-chip>
        <v-chip outlined label color="indigo darken-4" class="ml-2">
          ROE {{ stock.roe }}
        </v-chip>
      </v-col>
      <v-col cols="2" style="font-size: 15px" class="text-right">{{ stock.created_at }}</v-col>
    </v-row>

    <v-card class="mx-4 my-6">
      <v-row
        align="center"
        class="ma-0"
        v-for="news in NewsList"
        :key="news.id"
      >
        <v-col cols="10">
          <v-card-title class="py-0" style="font-size: 18px;">
            <a :href="news.url" target="_blank"> · {{ news.title.substr(0,60) }}</a>
          </v-card-title>
        </v-col>
        <v-col cols="2">
          <v-card-actions class="py-0 justify-end">{{ news.written_at }}</v-card-actions>
        </v-col>
        <v-row><v-divider class="mx-11"></v-divider> </v-row>
      </v-row>
    </v-card>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  props: ['stock'],

  data: () => ({
    NewsList: []
  }),

  created () {
    this.fetchNewsList(this.$route.params.code)
    this.$watch(
      () => this.$route.params.code,
      (toParams, fromParams) => {
        this.fetchNewsList(toParams)
      }
    )
  },

  methods: {
    fetchNewsList (code) {
      axios
        .get(`/api/risingstock/${code}/`)
        .then(res => {
          this.NewsList = res.data
        })
        .catch(err => {
          console.log('fetchNewsList GET Err', err.response)
          alert(err.response.status + ' ' + err.response.statusText)
        })
    }
  }
}
</script>

<style scoped>
a {
  text-decoration: none;
  color: black;
}

a:hover {
  color: #d4525d;
}
</style>
