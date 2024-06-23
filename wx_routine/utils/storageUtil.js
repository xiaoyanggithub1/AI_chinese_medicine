function get(key) {
	return uni.getStorageSync(key);
}


function set(key, value, success, error) {
	uni.setStorage({
		'key': key,
		'data': value,
		success: function(res) {
			if (success) {
				success(res)
			}

		},
		fail: function(err) {
			if (error) {
				error(err)
			}
		}
	})
}

export default {
	get,
	set
}