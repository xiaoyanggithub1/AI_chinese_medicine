const getters = {

	token: (state) => state.user.token,

	// //获取用户信息
	// userInfo: (state) => state.user.info,

	// //用户权限
	// userRoles: (state) => {
	// 	let roles = ['tourist']

	// 	if (state.user.token) {
	// 		roles.push('user')
	// 	}

	// 	// if (state.user.id == 1) {
	// 	// 	roles.push('admin')
	// 	// }
	// 	// console.log(state)
	// 	return roles
	// }
}

export default getters
