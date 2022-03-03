<template>
  <div>
    <v-navigation-drawer app clipped>
      <v-list>
        <v-list-item-group v-model="code" mandatory color="secondary">
          <v-list-item v-for="stock in stocks" :key="stock.code">
            <v-list-item-content>
              <v-list-item-title>
                <router-link :to="`/risingstock/${stock.code}`">
                  {{ stock.name }}
                </router-link>
              </v-list-item-title>
              <v-list-item-subtitle>
                {{ stock.curprice }} ▴{{ stock.diff }} ▴{{ stock.ratio }}%
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
        ratio: 2
      }
    ],
    code: 0
  })
}
</script>
