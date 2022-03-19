<template>
  <div>
    <v-dialog v-model="dialog.register" width="553" height="600">
      <v-card class="pa-6" color="#FFFFFF">
        <v-toolbar cards flat class="my-6">
          <!-- <img class="mx-auto" src="@/assets/tm_img/tm_shy.png" width="200" /> -->
        </v-toolbar>
        <v-form id="register-form" ref="registerForm" class="pa-3 pt-6">
          <v-text-field
            name="username"
            label="아이디"
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
            name="password1"
            label="비밀번호"
            outlined
            color="primary"
            type="password"
          ></v-text-field>
                    <v-text-field
            name="password2"
            label="비밀번호 확인"
            outlined
            color="primary"
            type="password"
          ></v-text-field>

        <!-- social login insert -->

        </v-form>
        <v-card-actions>
          <v-btn block large color="primary" depressed @click="save">
            회원가입
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
    ...mapState('accountsStore', ['dialog'])
  },
  methods: {
    ...mapActions('accountsStore', ['register']),
    save () {
      console.log('save()...')
      const postData = new FormData(document.getElementById('register-form'))
      this.register(postData)
      this.$refs.registerForm.reset()
    }
  }
}
</script>
