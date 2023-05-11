import Vue from 'vue'
import Router from 'vue-router'
import Index from '@/components/Index'
import Person from '@/components/Person'

Vue.use(Router)
let router  = new Router({
  routes: [
    {
      path: '/',
      name: 'Index',
      component: Index
    },
    {
      path: '/Person',
      name: 'Person',
      component: Person,
      meta:{'title':'个人信息','requireAuth':false}
    }
  ]
})

router.beforeEach(function(to,from,next){
  if(to.meta.requireAuth){
    let token = window.localStorage.getItem('token') || ""
    if(token == "" || token == null){
      alert('请登录后访问');
      next('/');
    }
  }
  next();
})

export default router

