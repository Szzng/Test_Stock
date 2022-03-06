import Vue from 'vue'
import Router from 'vue-router'
import MainHome from '@/components/MainHome.vue'
import StockList from '@/components/RisingStock/StockList.vue'

Vue.use(Router)

export default new Router({
  mode: 'history',
  routes: [
    { path: '/', component: MainHome },
    {
      path: '/risingstock',
      component: StockList,
      props: true,
      children: [
        {
          path: ':code',
          name: 'NewsList',
          props: true,
          component: () => import('@/components/RisingStock/NewsList.vue')
        }
      ]
    }
  ]
})
