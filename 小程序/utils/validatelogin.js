function AccountVerification(data) {
	if (!(/^1[3456789]\d{9}$/.test(data))) {
		uni.showToast({
			title: "手机号码不正确",
			icon: 'none'
		});
		return false;
	}
	return true
}

function PasswordVerification(data) {
	var reg = /^(?![0-9]+$)(?![a-zA-Z]+$)[0-9A-Za-z]{6,100}$/;
	if (!reg.test(data)) {
		uni.showToast({
			title: "密码长度不能小于6位,且必须包含数字和英文字符!",
			icon: 'none',
			duration: 3000
		});
		return false;
	}
	return true
}

export default {
	AccountVerification,
	PasswordVerification
}