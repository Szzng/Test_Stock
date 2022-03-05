import Vue from 'vue'
import Router from 'vue-router'
import MainHome from '@/components/MainHome.vue'
import StocksDrawer from '@/components/RisingStock/StocksDrawer.vue'
// import StockNews from '@/components/RisingStock/StockNews.vue'

Vue.use(Router)

export default new Router({
  mode: 'history',
  routes: [
    { path: '/', component: MainHome },
    {
      path: '/risingstock',
      component: StocksDrawer,
      props: true,
      children: [
        {
          path: ':code',
          name: 'StockNews',
          props: true,
          component: () => import('@/components/RisingStock/StockNews.vue')
        }
      ]
    }
  ]
})
