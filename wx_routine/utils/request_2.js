const base = 'http://101.43.174.240:8003'
const promiss = (options) => {
	// 获取本地存储token 
	let token = uni.getStorageSync('token')

	if (token != '') {
		options.header = {
			'content-type': 'application/json',
			'token': `${token}` // 这里是token(可自行修改)
		};
	}
	return new Promise((resolve, reject) => {
		uni.request({
			url: base + options.url,
			method: options.method || 'GET',
			data: options.data || {},
			header: options.header,
			success: (res) => {
				if (res.data.code !== 0) {
					// return uni.showToast({
					// 	title: res.data.data
					// })
				}
				resolve(res)
			},
			fail: (err) => {
				uni.showToast({
					title: "请求接口失败"
				})
				reject(err)
			}

		})
	})
}
export default promiss