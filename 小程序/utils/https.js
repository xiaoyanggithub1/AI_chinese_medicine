/**
 *  @description 此处请求封装适用于普通request请求需要携带token的应用场景
 *  @param config config 是全局的配置文件对象(包含url/appid等一些其他你项目需要用到的配置信息)
 *  @param getToken getToken 是获取本地存储token的方法
 *  @param setToken setToken 是设置本地存储token的方法
 *  @param tool tool 是封装的一些公共API适用方法(toast/confirm...)
 *  @param timeout timeout 设置请求超时时间 
 *  @author Coding by Akai,Dear user,if you think this a litte uncertain,please add my WeChat to contact me;
 *  @description WeChat Akaibiu (添加时请备注来意,谢谢~!!!)
 *  @version 1.0.0 
 */
// import config from '@/config/config.js';
// import {getToken,setToken} from '@/utils/auth';
// import errorCode from '@/utils/errorCode';
// import tool from '@/utils/common.js';
import {
	baseURL
} from '@/config/index.js'
import {
	getToken,
	removeToken
} from '@/utils/auth.js'

import store from '@/store/index.js'

let timeout = 10000;
const baseUrl = baseURL;
const request = config => {
	/**
	 * @description  如果isToken为true的时候需要token(一般会在登录的时候存储token和token_type)  为false不需要token
	 * @description  config.header['Authorization'] = 'Bearer ' + uni.getStorageSync('token'); // token_type 一般情况下为'Bearer ' 切记有空格哦
	 * @description  config.header['Content-Type'] = 'application/x-www-form-urlencoded'; // 常规请求头配置
	 */
	// const isToken = config.headers.isToken; 
	config.header = config.header || {};

	let token = ""
	if (store.getters.token) {
		token = store.getters.token
	} else if (getToken()) {
		store.commit('SET_TOKEN', token)
		token = store.getters.token
	}


	if (token) {
		// 给请求头添加Authorization
		// console.log(store.getters.token)

		config.header["token"] = store.getters.token;
		// console.log(config.headers)
	}
	/**
	 * @description  get请求映射params参数
	 */
	if (config.params) {
		let url = config.url + '?' + tool.tansParams(config.params)
		url = url.slice(0, -1)
		config.url = url

	}
	return new Promise((resolve, reject) => {
		uni.request({
			method: config.method || 'get',
			timeout: config.timeout || timeout,
			url: config.baseUrl || baseUrl + config.url,
			data: config.data,
			header: config.header,
			dataType: 'json',
			success(res) {
				if (res.data.code == 201) {

					removeToken()
					store.commit('SET_TOKEN', undefined)
					uni.$u.toast('登录过期，请重新登录！')
					setTimeout(() => {
						uni.reLaunch({
							url: '/pages/login/index'
						});
					}, 1000)

					reject(res.data)
				}

			
				if (res.data.code == 1) {
					uni.$u.toast(res.data.data)
					reject(res.data)
				}

				// switch (res.data.code) {
				// 	case 401:
				// 		tool.toastTip(res.data.msg, 'none', 1500);
				// 		break;
				// 	case 500:
				// 		tool.toastTip(res.data.msg, 'none', 1500);
				// 		break;
				// 	default:
				// 		/* 默认执行操作 */
				// 		break;
				// }
				/**
				 * @description 请求成功返回的数据
				 */
				resolve(res.data)
			},
			fail: (error) => {
				console.log(error, 'xxx')
				// let {errMsg} = error
				// if (errMsg === 'Network Error') {
				// 	errMsg = '后端接口连接异常'
				// } else if (errMsg.includes('timeout')) {
				// 	errMsg = '系统接口请求超时'
				// } else if (errMsg.includes('Request failed with status code')) {
				// 	errMsg = '系统接口' + errMsg.substr(errMsg.length - 3) + '异常'
				// }
				// tool.toastTip(errMsg, 'none', 1500)
				/**
				 * @description 请求失败返回的消息
				 */
				reject(error)
			},
			complete() {
				/**
				 * @description 请求完做的事
				 */
				// uni.hideLoading() 
			}
		})
	})
}

/**
 *  @description 暴露出request请求供其他业务使用
 */

export default request