	import {
		loginManager
	} from '@/api/login/index.js'

	import {
		setToken,
		removeToken
	} from '@/utils/auth.js'
	const user = {
		state: {
			//token
			token: undefined,

			//用户信息
			info: undefined,


		},

		mutations: {
			//设置token
			SET_TOKEN: (state, token) => {
				state.token = token
			},

			//设置用户信息
			SET_USER_INFO: (state, info) => {
				state.info = info
			}

		},
		actions: {
			//用户登录
			Login({
				commit,
				dispatch
			}, loginData) {

				return new Promise((resolve, reject) => {
					loginManager(loginData).then(res => {
						if (res.code != 0) {
							uni.$u.toast(res.data)
							reject(res)
							return
						}
					
						const token = res.data.access_token

						commit('SET_TOKEN', token)
						setToken(token)
						resolve(token)
					})
				})
			},

			// 用户退出
			Logout({
				commit
			}) {
				return new Promise((resolve, reject) => {
					// 这里再调一个退出接口
					commit('SET_TOKEN', '')
					removeToken()
					resolve()
				})
			},

			GetUserInfo({
				commit
			}) {
				return new Promise((resolve, reject) => {
					getUserInfo().then(res => {
						commit('SET_USER_INFO', res?.data)
						resolve(res)
					})
				})
			}

		}

	}

	export default user