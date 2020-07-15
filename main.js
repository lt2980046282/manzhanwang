import Vue from 'vue'
import App from './App'
//引入vuex
import store from './store'
import '@/static/js/pc.js'

import request from '@/common/request.js'
import api from '@/api/index.js'
import url from '@/common/config.js'
import { myRequest } from '@/api/index.js'
Vue.prototype.$myRequest=myRequest
//把vuex定义成全局组件
Vue.prototype.$store = store
Vue.config.productionTip = false
if(process.env.NODE_ENV === "development") {
	Vue.prototype.$weburl = 'http://api.baititong.top:8000/';  
}else{
	Vue.prototype.$weburl = 'http://api.baititong.top:8000/';  
}
Vue.prototype.$request = request
Vue.prototype.$api = api
Vue.prototype.$url = url

App.mpType = 'app'

const app = new Vue({
    ...App,
	store
})
app.$mount()




 



