<template>
  <div>
    <v-navigation-drawer app clipped>
      <v-list>
        <v-list-item-group v-model="code" mandatory color="secondary">
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
export default {
  data: () => ({
    stocks: [
      {
        code: '121212',
        name: '삼성전자',
        curprice: 70000,
        diff: 200,
        ratio: 2,
        volume: 100000,
        per: 3,
        roe: 4,
        created_at: '2022.03.02. 11:00'

      },
      {
        code: '144444',
        name: 'NAVER',
        curprice: 70000,
        diff: 200,
        ratio: 2,
        volume: 100000,
        per: 3,
        roe: 4,
        created_at: '2022.03.02. 11:00'
      },
      {
        code: '77777',
        name: '코리아써키트',
        curprice: 70000,
        diff: 200,
        ratio: 2,
        volume: 100000,
        per: 3,
        roe: 4,
        created_at: '2022.03.02. 11:00'

      }
    ],
    code: 0
  }),
  methods: {
    goToNews (stock) {
      this.$router.push({
        name: 'StockNews',
        params: {code: stock.code, stock: stock}
      })
    }
  }
}
</script>
