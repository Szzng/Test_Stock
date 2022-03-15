<template>
  <div>
    <v-app-bar
      app
      color="#FFFFFF"
      clipped-left

      style="border-bottom: 1px solid #d2d2d2 !important"
    >
      <a href="/"><v-toolbar-title>SZ Stock</v-toolbar-title></a>

      <v-tabs centered class="pl-n12 black--text" color="primary">
        <v-tabs-slider></v-tabs-slider>
        <v-tab
          class="black--text"
          v-for="menu in menus"
          :key="menu.name"
          :to="menu.url"
          >{{ menu.name }}</v-tab
        >
      </v-tabs>

      <v-spacer></v-spacer>

      <v-responsive max-width="240">
        <v-text-field
          class="search_box"
          hide-details
          dense
          filled
          rounded
          color="#F5F6F8"
          placeholder="검색어를 입력하세요"
        >
          <v-icon slot="append" color="primary">mdi-magnify</v-icon>
        </v-text-field>
      </v-responsive>

      <v-badge
        :content="notifications"
        :value="notifications"
        color="secondary"
        overlap
      >
        <v-icon color="black" class="pl-5">mdi-bell</v-icon>
      </v-badge>

      <v-menu offset-y left bottom>
        <template v-slot:activator="{ on, attrs }">
          <v-btn text class="pl-3" v-bind="attrs" v-on="on">
            <v-icon color="black"> mdi-account</v-icon>
            <span style="color: black; font-weight: bold">
              {{ me.username }}
            </span>
          </v-btn>
        </template>

        <v-list style="text-align: center">
          <template v-if="!loginState.isLogin">
            <v-list-item>
              <v-list-item-title>회원가입</v-list-item-title>
            </v-list-item>
            <v-list-item @click="dialogOpen('login')">
              <v-list-item-title>로그인</v-list-item-title>
            </v-list-item>
          </template>

          <template v-else>
            <v-list-item>
              <v-list-item-title @click="logout">로그아웃</v-list-item-title>
            </v-list-item>
            <v-list-item>
              <router-link to="/mypage/profile">My Page</router-link>
            </v-list-item>
          </template>
        </v-list>
      </v-menu>
    </v-app-bar>
    <LogIn />
  </div>
</template>

<script>
import LogIn from '@/components/LogIn.vue'
import { mapState, mapMutations, mapActions } from 'vuex'

export default {
  components: { LogIn },

  data: () => ({
    menus: [
      { name: 'Home', url: '/' },
      { name: '상승종목', url: '/risingstock' },
      { name: '키워드 뉴스', url: '/mynews' }
    ],
    notifications: 1
  }),

  computed: {
    ...mapState('accountsStore', ['loginState', 'me'])
  },

  methods: {
    ...mapMutations('accountsStore', ['dialogOpen']),
    ...mapActions('accountsStore', ['logout'])
  }
}
</script>

<style scoped>
.v-dialog .v-text-field--outlined >>> fieldset {
  border-color: #b4b4b4;
  border-width: 1px;
}

.v-tab,
.v-dialog .v-btn {
  font-weight: bold;
  font-size: 1em;
}

.search_box input::placeholder {
  color: red !important;
  opacity: 1;
}
</style>
