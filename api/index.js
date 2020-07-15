const BASE_URL = 'http://api.baititong.top:8000/'
export const myRequest = (options) => {
	return new Promise((reslove, reject) => {
		uni.request({
			url: BASE_URL + options.url,
			method: options.method || 'GET',
			data: options.data || {},
			success: (res) => {
				if (!res.data) {
					return uni.showToast({
						title: "数据获取失败",
						icon:'none',
						mask:true
					})
				}
				reslove(res)
			},
			fail:(err)=> {
				uni.showToast({
					title: "请求接口失败",
					icon:'none',
					mask:true
				})
				reject(err)
			}
		})
	})
}
