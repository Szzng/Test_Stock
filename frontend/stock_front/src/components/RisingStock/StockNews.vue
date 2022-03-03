<template>
  <div>
      {{NewsOfRisingStock[0].keyword}}
      {{NewsOfRisingStock[0].created_at}}
    <v-row v-for="news in NewsOfRisingStock" :key="news.id">
      <v-col cols="9">
          <span style="font-size:20px;">
          <a :href="news.url">{{ news.title }}</a>
          </span>
          </v-col>
      <v-col cols="3"> {{news.written_at}} </v-col>
    </v-row>
  </div>
</template>

<script>
export default {
  data: () => ({
    NewsOfRisingStock: [
      {
        id: 1,
        code: '121212',
        keyword: '삼성전자',
        title:
          '삼성전자뉴스삼성전자뉴스삼성전자뉴스삼성전자뉴스삼성전자뉴스삼성전자뉴스',
        url: 'www.naver.com',
        written_at: '2시간 전',
        created_at: '2022.03.02. 11:00'
      }
    ],
    code: 0
  })
}
</script>
