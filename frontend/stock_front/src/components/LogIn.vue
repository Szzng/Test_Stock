<template>
  <div>
    <v-dialog v-model="dialog.login" width="553" height="600">
      <v-card class="pa-6" color="#FFFFFF">
        <v-toolbar cards flat class="my-6">
          <!-- <img class="mx-auto" src="@/assets/tm_img/tm_shy.png" width="200" /> -->
        </v-toolbar>
        <v-form id="login-form" ref="loginForm" class="pa-3 pt-6">
          <v-text-field
            name="username"
            label="username"
            outlined
            color="primary"
          ></v-text-field>
          <v-text-field
            name="email"
            label="이메일"
            outlined
            color="primary"
          ></v-text-field>
          <v-text-field
            name="password"
            label="비밀번호"
            outlined
            color="primary"
            type="password"
          ></v-text-field>
          <v-row align="center" justify="center">
            <v-col>
              <v-checkbox color="secondary">
                <template v-slot:label>로그인을 유지합니다.</template>
              </v-checkbox>
            </v-col>
            <v-col class="text-right">
              <a href="#">이메일, 비밀번호를 잊으셨나요? </a>
            </v-col>
          </v-row>
        </v-form>
        <v-card-actions>
          <v-btn block large color="primary" depressed @click="save">
            로그인
          </v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </div>
</template>

<script>
import { mapActions, mapState } from 'vuex'

export default {
  computed: {
    ...mapState('accountsStore', ['dialog', 'loginState', 'me'])
  },
  methods: {
    ...mapActions('accountsStore', ['login']),
    save () {
      console.log('save()...')
      const postData = new FormData(document.getElementById('login-form'))
      this.login(postData)
      this.$refs.loginForm.reset()
    }
  }
}
</script>
