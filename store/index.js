import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

const store = new Vuex.Store({
	state: {
		isLogin :uni.getStorageSync('isLogin')?true:false,
	},
	mutations: {
		update(state,[key,value]){
			state[key]=value;
		},
	}
})

export default store