

import request from '@/utils/https';

// export function managerScs(data) {
// 	return request({
// 		url: '/admin/manager/scs',
// 		method: 'post',
// 		data
// 	})
// }

export function managerScs(data) {
	return request({
		url: '/admin/manager/scs',
		method: 'post',
		data
	})
}
