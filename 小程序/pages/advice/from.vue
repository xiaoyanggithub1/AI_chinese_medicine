<template>
	<view class="app-container">
		<view class="from-container">
			<textarea placeholder="请输入你要反馈的问题(5-100字)" v-model="from.yj" />
		</view>
		<view class="from-container">
			<input type="text" placeholder="电话号码" v-model="from.phone" />
		</view>
		<view class="from-container">
			<text>感谢你的意见反馈，我们会再接再厉的！</text>
		</view>
		<view class="from-container">
			<button @click="saveData()">提交</button>
		</view>
	</view>
</template>

<script>
	import {
		managerYj
	} from '@/api/set/set.js'
	export default {
		data() {
			return {
				from: {
					yj: '',
					phone: ""
				}

			}
		},
		methods: {
			saveData() {
				if (this.from.yj == '') {
					uni.$u.toast('反馈内容不能为空')
					return
				}
				if (this.from.yj.length < 5 || this.from.yj.length > 100) {
					uni.$u.toast('长度控制在5到100内')
					return
				}

				if (this.from.phone == '') {
					uni.$u.toast('电话不能为空')
					return
				}
				if (!this.from.phone.match(
						/^(?:(?:\+|00)86)?1(?:(?:3[\d])|(?:4[5-79])|(?:5[0-35-9])|(?:6[5-7])|(?:7[0-8])|(?:8[\d])|(?:9[1589]))\d{8}$/
					)) {
					uni.$u.toast('手机格式不对')
					return

				}
				// 掉接口
				managerYj(this.from).then(res => {
					uni.$u.toast('提交成功，感谢你的意见反馈！')
					setTimeout(() => {
					uni.redirectTo({
						url: '/pages/advice/advice',
						
					});
					}, 1000)
				}).catch(err=>{
					console.log(err)
				})

			}

		}
	}
</script>

<style lang="scss" scoped>
	.app-container {
		width: 100%;

		.from-container {
			padding: 20rpx;
			width: calc(100% - 40rpx);

			textarea {
				background: #E9E9EB;
				padding: 10rpx;
				width: calc(100% - 20rpx);
				border-radius: 20rpx;
			}

			input {
				background: #E9E9EB;
				padding: 10rpx;
				width: calc(100% - 20rpx);
				border-radius: 20rpx;
				height: 80rpx;
			}

			button {
				width: 200rpx;
			}

			text {
				color: #767676;
			}
		}


	}
</style>