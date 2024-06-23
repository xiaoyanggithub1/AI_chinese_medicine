
/**
 * 用户登录模块需要的api
 */

import request from '@/utils/https';

export function loginManager(data) {
	return request({
		url: '/admin/loginManager',
		method: 'post',
		data
	})
}

export function managers(data) {
	return request({
		url: '/admin/managers',
		method: 'post',
		data
	})
}



