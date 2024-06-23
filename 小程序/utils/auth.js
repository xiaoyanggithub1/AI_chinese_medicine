const TokenKey = 'APPLET-TOKEN'


// 获取本地token
export function getToken() {
	const value = uni.getStorageSync(TokenKey);
	return value
}

// 设置本地token
export function setToken(token) {
	try {
		return uni.setStorageSync(TokenKey, token);
	} catch (e) {
		console.log(e, '设置本地token错误')
	}
}

// 移除本地token
export function removeToken() {
	try {
		uni.removeStorageSync(TokenKey);
	} catch (e) {
		// error
	}
}
