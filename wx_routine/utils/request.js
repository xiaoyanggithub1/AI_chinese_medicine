import axios from 'axios'


import settle from "axios/lib/core/settle";
import buildURL from "axios/lib/helpers/buildURL";
import buildFullPath from "axios/lib/core/buildFullPath";

import store from '@/store/index.js'

import {
	baseURL
} from '@/config/index.js'

//解决uniapp 适配axios请求，避免报adapter is not a function错误
axios.defaults.adapter = function(config) {
	return new Promise((resolve, reject) => {
		const fullurl = buildFullPath(config.baseURL, config.url);

		let header = config.headers
		header.token = 'xxxxxx'
		// console.log(config.headers, 'header')
		uni.request({
			method: config.method.toUpperCase(),
			url: buildURL(fullurl, config.params, config.paramsSerializer),
			header,
			data: config.data,
			dataType: config.dataType,
			responseType: config.responseType,
			sslVerify: config.sslVerify,
			complete: function complete(response) {

				response = {
					data: response.data,
					status: response.statusCode,
					errMsg: response.errMsg,
					header: response.header,
					config,
				};

				settle(resolve, reject, response);
			},
		});
	});
};




// 创建axios实例
const request = axios.create({
	baseURL: baseURL, // api 的 base_url
	timeout: 60000 // 请求超时时间
})



// request拦截器
request.interceptors.request.use(
	config => {


		if (store.getters.token) {
			// 给请求头添加Authorization
			// console.log(store.getters.token)

			// config.headers["token"] = 'xxx';
			// console.log(config.headers)
		}
		config.headers["token"] = 'xxx';
		console.log(config.headers,'headers')
		return config;
	},
	error => {

		return Promise.reject(error);
	}
);
// response 拦截器
request.interceptors.response.use(
	(response) => {
		return new Promise((resolve, reject) => {
			const res = response.data
			// 正常数据返回
			resolve(response.data)
		})
	},
	(error) => {
		console.log(error)
		uni.hideToast();
		uni.showToast({
			title: '网络繁忙,请稍后再试',
			duration: 2000,
			icon: 'none'
		});
		Promise.reject(error)
		return '错误'
	}
)





export default request