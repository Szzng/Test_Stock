<template>
  <div class="mx-4 my-6">
    <v-row
      justify="center"
      align="center"
      class="py-4"
      style="font-size: 25px; font-weight: bold"
    >
      {{ stock.name }}
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
      <v-col cols="2" style="font-size: 15px">{{ stock.created_at }}</v-col>
    </v-row>

    <v-card class="mx-3 my-5" color="#FAF9F5" flat>
      <v-row
        align="center"
        class="ma-0"
        v-for="news in NewsOfRisingStock"
        :key="news.id"
      >
        <v-col cols="10">
          <v-card-title class="py-0" style="font-size: 19px">
            <a :href="news.url"> · {{ news.title }}</a>
          </v-card-title>
        </v-col>
        <v-col cols="2">
          <v-card-actions class="py-0">{{ news.written_at }}</v-card-actions>
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
    code: 0
  }),

  methods: {
    getNewsOfRisingStock (code) {
      axios
        .get('', code)
        .then((res) => {
          let NewsOfRisingStock = res.data
        })
        .catch((err) => {
          console.log('getNewsOfRisingStock GET Err', err.response)
          alert('ERROR')
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
