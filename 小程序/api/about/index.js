
/**
 * 用户登录模块需要的api
 */

import request from '@/utils/https.js';

export function managerSc(data) {
	return request({
		url: '/admin/manager/sc',
		method: 'post',
		data
	})
}
