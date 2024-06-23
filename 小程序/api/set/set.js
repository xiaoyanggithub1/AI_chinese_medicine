import request from '@/utils/https';

export function updateManagers(data) {
	return request({
		url: '/admin/manager/updateManagers',
		method: 'post',
		data
	})
}
export function managerYj(data) {
	return request({
		url: '/admin/manager/yj',
		method: 'post',
		data
	})
}
