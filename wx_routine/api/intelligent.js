import Request from '@/utils/request.js'
import promiss from '@/utils/request_2.js'

//Ai问诊
export function query(data) {
	return Request({
		url: 'http://10.16.11.65:5009/query',
		method: 'post',
		data
	})
}

// 中药查询
export function cxzhongyao(data) {
	return promiss({
		url: '/admin/cxzhongyao',
		method: 'post',
		data
	})
}

// 方剂查询
export function cxfangji(data) {
	return promiss({
		url: '/admin/cxfangji',
		method: 'post',
		data
	})
}

// export function cxzhongyao(data) {
// 	return promiss({
// 		url: '/admin/cxzhongyao',
// 		method: 'post',
// 		data
// 	})
// }

// // 方剂查询
// export function cxfangji(data) {
// 	return promiss({
// 		url: '/admin/cxfangji',
// 		method: 'post',
// 		data
// 	})
// }